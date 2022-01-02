from django.http import response
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ProductVariationPagination(PageNumberPagination):
    def get_page_size(self, request):
        size = request.query_params.get("size")
        if size:
            return size
        return super().get_page_size(request)

    def get_paginated_response(self, data):
        page_size = int(self.get_page_size(self.request))
        product_count = int(self.page.paginator.count)
        page_count = (
            1
            if product_count < page_size
            else product_count // page_size
            if product_count % page_size <= 0
            else (product_count // page_size) + 1
        )
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "product_count": product_count,
                "page_count": page_count,
                "products": data,
            }
        )
