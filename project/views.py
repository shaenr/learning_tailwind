from django.shortcuts import render
from django.views.generic import TemplateView as BaseTemplateView
from typing import Any, Dict
from django.conf import settings as conf
from django.http import HttpRequest, HttpResponse


class PageView(BaseTemplateView):
    """
    Only for subclassing. See IndexPage.
    """
    page_title: str = ""
    page_name: str = ""
    title_sep: str = " | "
    pages_dir: str = "pages/"
    suffix: str = ".html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        ctx = super().get_context_data(**kwargs)
        ctx['page_title'] = self.page_title
        return ctx

class IndexPage(PageView):
    """
    Just define the page_name and the page_title. The page_title will be used in title strings.
    The page_name will use `pages/{name}.html` template to render.
    """
    page_name: str = "index"
    page_title: str = "The Index Page"
    template_name: str = f"{PageView.pages_dir}{page_name}{PageView.suffix}"