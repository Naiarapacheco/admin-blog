from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:category_slug>/<slug:slug>', views.detail, name='post_detail'), # slug - identificador (first the category-SLUG will show on the url and then the post-SLUG)
    path('<slug:slug>/', views.category, name='category_detail'), # slug - identificador
] 
