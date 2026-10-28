"""Checks webhook requests' X-DocSpring-Signature header (https://docspring.com/docs/webhooks/verifying-signatures/)."""

import hashlib
import hmac
import re
import time
from typing import Optional, Union

# The number of seconds a webhook request's signature stays valid (verify_webhook_signature)
WEBHOOK_SIGNATURE_TOLERANCE = 300

# At most 15 digits: int() raises for a string of more than 4,300 (sys.get_int_max_str_digits), and a timestamp that
# long is never within the tolerance anyway
_TIMESTAMP = re.compile(r"\A[0-9]{1,15}\Z")


def verify_webhook_signature(
    payload: Union[str, bytes],
    signature_header: str,
    secret: str,
    tolerance: int = WEBHOOK_SIGNATURE_TOLERANCE,
    now: Optional[int] = None,
) -> bool:
    """Checks a webhook request's X-DocSpring-Signature header.

    Returns True when one of its v1 signatures is the HMAC-SHA256 of "{t}.{payload}" with the webhook's secret, and its
    timestamp t is at most `tolerance` seconds from `now`. Returns False for anything else, including a missing or
    malformed header.

    :param payload: the request body exactly as it was received (Flask: request.get_data()), not parsed JSON.
    :param signature_header: the X-DocSpring-Signature header.
    :param secret: the webhook's signing secret.
    :param tolerance: how many seconds old (or early) the timestamp can be. 5 minutes by default.
    :param now: the current Unix time in seconds, for tests. The system clock by default.
    """
    if isinstance(payload, str):
        payload = payload.encode("utf-8")
    if not isinstance(payload, (bytes, bytearray)) or not isinstance(signature_header, str):
        return False
    if not isinstance(secret, str) or not secret:
        return False

    parts = [part.strip().split("=", 1) for part in signature_header.split(",")]
    timestamp = next((part[1] if len(part) == 2 else "" for part in parts if part[0] == "t"), None)
    signatures = [part[1] for part in parts if part[0] == "v1" and len(part) == 2 and part[1]]
    if timestamp is None or not _TIMESTAMP.match(timestamp) or not signatures:
        return False

    current = int(time.time()) if now is None else int(now)
    if abs(current - int(timestamp)) > tolerance:
        return False

    expected = hmac.new(
        secret.encode("utf-8"), timestamp.encode("ascii") + b"." + bytes(payload), hashlib.sha256
    ).hexdigest()
    return any(hmac.compare_digest(expected.encode("ascii"), signature.encode("utf-8")) for signature in signatures)
