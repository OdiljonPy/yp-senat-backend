from django.core.paginator import Paginator
from django.db.models import Count

from services.serializers import VideoSerializer

def get_video_list(context: dict, response_data, page, page_size):
    video_query = response_data
    total_count = video_query.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(video_query, page_size)
    video = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(video),
        "first": not video.has_previous(),
        "last": not video.has_next(),
        "empty": total_count == 0,
        "content": VideoSerializer(video, many=True, context=context).data,
    }

    return responses