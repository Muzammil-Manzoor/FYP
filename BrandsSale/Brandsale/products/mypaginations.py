from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagiation(PageNumberPagination):
    page_size=5
