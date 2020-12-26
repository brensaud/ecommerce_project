from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view()),
    # path('fbv/', views.product_list_view),
    path('<slug>/', views.ProductDetailSlugView.as_view()),
    # path('<int:pk>/', views.ProductDetailView.as_view()),
    # path('fbv/<int:pk>/', views.product_detail_view),
    # path('featured', views.ProductFeaturedView.as_view()),
    # path('featured/<int:pk>/', views.ProductFeaturedDetailView.as_view()),
]