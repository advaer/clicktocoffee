__author__ = 'advaer'

from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="main/index.html")),
    url(r'^sendmail$', views.SendMail.as_view()),
]