from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from wagtail.search import index
from wagtail.admin.edit_handlers import StreamFieldPanel

from ..fields import BodyStreamBlock


class StaticPage(Page):
    body = StreamField(BodyStreamBlock())

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
