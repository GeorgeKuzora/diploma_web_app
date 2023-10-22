from django.urls import path
from . import views


app_name = "jobs"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.JobSearch.as_view(), name="search"),
    path("job/<int:job_id>/", views.job_detail, name="job_detail"),
]
