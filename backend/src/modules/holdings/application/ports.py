from abc import ABC, abstractmethod
from typing import Optional
from ..domain.entities import PageEntity

class PageRepo(ABC):
    @abstractmethod
    def get_published_by_slug(self, slug: str) -> Optional[PageEntity]:
        raise NotImplementedError
