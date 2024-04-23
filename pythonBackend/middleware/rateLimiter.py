from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from limits.storage import RedisStorage
from limits.strategies import MovingWindowRateLimiter

# Create redis conection
limiter = Limiter(
    key_func=get_remote_address,
    storage_uri="redis://default:aJe2KI3AThz2dSTqVqzX6YDaSYDo31op@redis-16858.c329.us-east4-1.gce.redns.redis-cloud.com:16858")

# Configure error handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)