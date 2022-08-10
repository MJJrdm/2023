from django.conf import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 50

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'page_size': self.page.paginator.per_page,
            'results': data
        })
