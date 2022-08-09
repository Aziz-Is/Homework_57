from django.urls import path
from webapp.views import login_view
# app_name = "accounts"

urlpatterns = [
    path('login/', login_view, name="login"),
]