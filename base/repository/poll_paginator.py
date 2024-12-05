from django.core.paginator import Paginator
from django.db.models import Count
from base.serializers import PollSerializer


def get_poll_list(context: dict, request_data, page, page_size):
    poll_query = request_data
    total_count = poll_query.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(poll_query, page_size)
    polls = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(polls),
        "first": not polls.has_previous(),
        "last": not polls.has_next(),
        "empty": total_count == 0,
        "content": PollSerializer(polls, many=True, context=context).data,
    }

    return responses
