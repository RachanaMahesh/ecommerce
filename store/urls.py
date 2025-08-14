from django.urls import path
from . import views

app_name = "shop"  # ✅ This is required when using namespaceSS

urlpatterns = [path("", views.all_products, name="all_products")]
