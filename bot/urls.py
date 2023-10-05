from django.urls import path, include
from .views import link_input, links_template_view

app_name = "bot"

urlpatterns = [
    path("api/v1/", include("bot.api.v1.urls")),
    path('link-input/', link_input, name='link_input'),
    path('links_available/',links_template_view, name='links-template')
]

