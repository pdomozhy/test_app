from django.urls import path


from . import views


urlpatterns = [
    path('shops/', views.ShopList.as_view()),
    path('shops/<int:pk>', views.ShopDetail.as_view()),
]
