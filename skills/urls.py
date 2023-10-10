from django.urls import path
from . import views


app_name = "skills"
urlpatterns = [
    path("", views.index, name="skill_list"),
    path("skill/<int:skill_id>/", views.detail, name="detail"),
]
