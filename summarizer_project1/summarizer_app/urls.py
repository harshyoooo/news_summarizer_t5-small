from django.urls import path
from .views import SummarizeAPIView, index

urlpatterns = [
    path("", index, name="index"),  # for HTML form
    path("api/summarize/", SummarizeAPIView.as_view(), name="summarize-api"),
]
