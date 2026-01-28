from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class PageEntity:
    slug: str
    title: str
    body: str
    is_published: bool
    updated_at: datetime
