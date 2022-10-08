from rest_framework.pagination import PageNumberPagination

class DefaultPageNoPagination(PageNumberPagination):
    page_size_query_param='pageSize'
    max_page_size = 15
    page_query_param = 'pageNo'

