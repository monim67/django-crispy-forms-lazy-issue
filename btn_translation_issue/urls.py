from django.urls import path

from .views import (
    DemoView,
)


app_name = 'btn_translation_issue'

urlpatterns = [
    path('', DemoView.as_view(), name='index'),
]
