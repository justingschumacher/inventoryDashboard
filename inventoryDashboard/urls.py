from django.urls import path
from inventoryDashboard import views

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailClassView.as_view(), name='item_detail'),
    path('highCPU/', views.HighCPUCountClassView.as_view(), name='high_cpu_count'),
]
