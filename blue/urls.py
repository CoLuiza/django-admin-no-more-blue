from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

themes_urlpatterns = [
    path('', login_required(views.ThemeSelectorView.as_view())),
    path('set-theme/', login_required(views.SelectThemeView.as_view())),
]
