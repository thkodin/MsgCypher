"""msgcypher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# For include patterns (to access potentially multiple app view URLs), we need
# to include the namespace argument and the app name if we want to use these
# URLs in HTML templates (e.g., to jump between apps or general navigation).
# This is done by setting app_name = "appname" in the corresponding app's
# urls.py, or passing a tuple of list of app urls and the appname to include.
# Otherwise, Django has no idea how to reverse the URLs.
urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("encoder/", include(("encoder.urls", "encoder"), namespace="encoder")),
    path("decoder/", include(("decoder.urls", "decoder"), namespace="decoder")),
    path("admin/", admin.site.urls),
]
