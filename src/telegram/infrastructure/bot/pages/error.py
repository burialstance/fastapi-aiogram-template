from typing import Optional

from .base import Page
from ..misc import icons


class WarningPage(Page):
    title: Optional[str] = 'WarningPage'
    icon: Optional[str] = icons.warning
    content: Optional[str] = 'Warning'


class ForbiddenPage(Page):
    title: Optional[str] = 'ForbiddenPage'
    icon: Optional[str] = icons.forbidden
    content: Optional[str] = 'Forbidden'
