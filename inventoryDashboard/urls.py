from django.urls import path
from inventoryDashboard.views import IndexDetailView
from inventoryDashboard.views import IndexListView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    # path('<slug:slug>/', IndexDetailView.as_view(), name='index'),
    # path('project/detail/<int:pk>', views.DetailView.as_view(), name='project_detail'),
]