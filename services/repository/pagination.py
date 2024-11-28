from django.core.paginator import Paginator
from django.db.models import Count
from services.serializers import PostSerializer, MandatCategorySerializer


def get_post_list(context: dict, request_data, page, page_size):
    season_query = request_data
    total_count = season_query.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(season_query, page_size)
    season = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(season),
        "first": not season.has_previous(),
        "last": not season.has_next(),
        "empty": total_count == 0,
        "content": PostSerializer(season, many=True, context=context).data,
    }

    return responses
