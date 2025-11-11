from django.urls import path
from . import views

app_name = "main"



urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("impact/", views.economeyimpact_view, name="economeyimpact_view"),
    path("culture-impact/", views.cultureImpact_view, name="cultureImpact_view"),
    path("fields/", views.fields_view, name="fields_view"),
    path("future/", views.future_view, name="future_view"),
    path("initiatives/", views.initiatives_view, name="initiatives_view"),
    path("innovation/", views.innovation_view, name="innovation_view"),
    path("tech-in-saudi/", views.techInSaudi_view, name="techInSaudi_view")
]