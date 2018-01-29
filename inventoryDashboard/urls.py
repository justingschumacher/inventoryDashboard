from django.urls import path
from inventoryDashboard import views

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailClassView.as_view(), name='item_detail'),
]
