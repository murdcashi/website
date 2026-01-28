from typing import Optional
from .ports import PageRepo
from ..domain.entities import PageEntity

class GetPublishedPage:
    def __init__(self, repo: PageRepo):
        self.repo = repo

    def execute(self, slug: str) -> Optional[PageEntity]:
        slug = slug.strip().lower()
        if not slug:
            return None
        return self.repo.get_published_by_slug(slug)
