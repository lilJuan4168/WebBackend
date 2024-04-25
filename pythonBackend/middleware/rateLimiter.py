from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from limits.storage import RedisStorage
from limits.strategies import MovingWindowRateLimiter

# Create redis conection
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379")

rate_limit_exceeded_handler_status_code = _rate_limit_exceeded_handler
