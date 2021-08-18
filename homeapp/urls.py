from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:c_slug>/', views.home, name='prdct_cat'),
    path('<slug:c_slug>/<slug:prdct_slug>/',views.prdct_details, name='prdct_details'),
    path('search', views.search, name='search')
]