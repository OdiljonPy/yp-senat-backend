from .models import VisitorActivity
from services.models import Post
from datetime import date


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip_address = request.META.get('REMOTE_ADDR')
        session_key = request.session.session_key
        if not session_key:
            request.session.create()

        if not VisitorActivity.objects.filter(ip_address=ip_address).exists():
            VisitorActivity.objects.create(ip_address=ip_address)

        if 'post_id' in request.GET:
            post = Post.objects.get(id=request.GET['post_id'])
            if not VisitorActivity.objects.filter(ip_address=ip_address, created_at__date=date.today(), post=post).exists():
                VisitorActivity.objects.create(ip_address=ip_address, post=post)
        return response
