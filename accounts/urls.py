from django.urls import path
from webapp.views import  import IndexView
app_name = "accounts"

urlpatterns = [
    path('', IndexView.as_view(), name ="index"),
]