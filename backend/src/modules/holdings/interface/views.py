from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..application.services import GetPublishedPage
from ..infrastructure.repo import DjangoPageRepo
from .serializers import PageOut

@api_view(["GET"])
def page_detail(request, slug: str):
    svc = GetPublishedPage(DjangoPageRepo())
    page = svc.execute(slug)

    if not page:
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    data = PageOut({
        "slug": page.slug,
        "title": page.title,
        "body": page.body,
        "updated_at": page.updated_at,
    }).data
    return Response(data, status=status.HTTP_200_OK)
