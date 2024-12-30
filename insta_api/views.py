from django.http import JsonResponse
from .services.insta_service import get_instagram_feed

def instagram_feed(request):
    feed = get_instagram_feed()
    return JsonResponse(feed, safe=False)
