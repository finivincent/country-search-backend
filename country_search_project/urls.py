from django.contrib import admin
from django.urls import path
from country_search_app.views import search_countries

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/search/', search_countries, name='search_countries'),
]