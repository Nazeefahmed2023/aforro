
# rate_limit.py
# Simple rate limiting decorator for Django views.

from django.core.cache import cache
from django.http import JsonResponse
import time

# Maximum number of requests allowed per window (per IP)
RATE_LIMIT = 20
# Time window in seconds
WINDOW = 60

def rate_limit(view_func):
    """
    Decorator to rate limit a view by IP address.
    If the user exceeds the allowed number of requests in the time window,
    a 429 response is returned.
    """
    def _wrapped_view(request, *args, **kwargs):
        ip = request.META.get('REMOTE_ADDR')
        key = f"rl:{ip}"
        data = cache.get(key, {'count': 0, 'start': time.time()})
        now = time.time()
        if now - data['start'] > WINDOW:
            # Reset the window
            data = {'count': 1, 'start': now}
        else:
            data['count'] += 1
        cache.set(key, data, timeout=WINDOW)
        if data['count'] > RATE_LIMIT:
            return JsonResponse({'detail': 'Rate limit exceeded'}, status=429)
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# TODO: Enhance to use user ID for rate limiting if authenticated
