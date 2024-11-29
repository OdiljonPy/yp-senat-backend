from django.core.paginator import Paginator
from django.db.models import Count
from services.serializers import CommissionMemberSerializer


def get_commissions(commissions, context: dict, page: int, page_size: int):
    total_projects = commissions.aggregate(count=Count('id'))['count']
    paginator = Paginator(commissions, page_size)
    page_obj = paginator.get_page(page)

    responses = {
        "totalElements": total_projects,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(page_obj),
        "first": not page_obj.has_previous(),
        "last": not page_obj.has_next(),
        "empty": total_projects == 0,
        "content": CommissionMemberSerializer(page_obj, many=True, context=context).data,
    }
    return responses
