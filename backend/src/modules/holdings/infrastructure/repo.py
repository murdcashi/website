from typing import Optional
from ..application.ports import PageRepo
from ..domain.entities import PageEntity
from .models import Page

class DjangoPageRepo(PageRepo):
    def get_published_by_slug(self, slug: str) -> Optional[PageEntity]:
        obj = Page.objects.filter(slug=slug, is_published=True).first()
        if not obj:
            return None
        return PageEntity(
            slug=obj.slug,
            title=obj.title,
            body=obj.body,
            is_published=obj.is_published,
            updated_at=obj.updated_at,
        )
