from django.core.paginator import Paginator
from django.db.models import Count
from services.serializers import NormativeDocumentsSerializer


def get_document_list(context: dict, request_data, page, page_size):
    documents_query = request_data
    total_count = documents_query.aggregate(total_count=Count('id'))['total_count']

    paginator = Paginator(documents_query, page_size)
    documents = paginator.get_page(page)

    responses = {
        "totalElements": total_count,
        "totalPages": paginator.num_pages,
        "size": page_size,
        "number": page,
        "numberOfElements": len(documents),
        "first": not documents.has_previous(),
        "last": not documents.has_next(),
        "empty": total_count == 0,
        "content": NormativeDocumentsSerializer(documents, many=True, context=context).data,
    }

    return responses
