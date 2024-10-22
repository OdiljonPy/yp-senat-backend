from datetime import date

from django.utils.deprecation import MiddlewareMixin

from .models import Visitors
from .utils import get_ip


class VisitorsMiddlewares(MiddlewareMixin):
    def process_request(self, request):
        ip = get_ip(request)
        current_date = date.today()
        name = request.META.get('HTTP_USER_AGENT', '')

        is_admin_or_swagger = request.path.startswith('/admin/') or request.path.startswith('/swagger/')
        visitors = Visitors.objects.filter(ip=ip, created_at__day=current_date.day,
                                           created_at__month=current_date.month,
                                           created_at__year=current_date.year)

        if not visitors.exists() and not is_admin_or_swagger:
            Visitors.objects.create(ip=ip, name=name)
        return None
