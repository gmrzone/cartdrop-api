from rest_framework.pagination import CursorPagination


class SubcategoryPagination(CursorPagination):

    page_size = 8
    ordering = 'id'
    max_page_size = 12

class BrandPagination(CursorPagination):

    page_size = 10
    ordering = 'id'
    max_page_size = 12

