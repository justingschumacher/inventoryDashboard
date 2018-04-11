from django.urls import path
from inventoryDashboard import views

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('detail/<int:pk>', views.DetailClassView.as_view(), name='item_detail'),
    path('highCPU/', views.HighCPUCountClassView.as_view(), name='high_cpu_count'),
    path('getSBShighCPU/', views.HighCPUCountClassView.getsbs, name='high_cpu_countSBS'),
    path('highMEM/', views.HighMemoryCountClassView.as_view(), name='high_memory_count'),
    path('guestsDirectors/', views.GuestsbyDirectorClassView.as_view(), name='guestsDirector'),
    path('getSBSguestsDirector/', views.GuestsbyDirectorClassView.getsbs, name='guestsDirectorSBS'),
    path('guestsSupportGroup/', views.GuestsbySupportGroupClassView.as_view(), name='guestsSupportGroup'),
    path('getSBSguestsSupportGroup/', views.GuestsbySupportGroupClassView.getsbs, name='guestsSupportGroupSBS'),
    path('osDistribution/', views.OSDistributionClassView.as_view(), name='osDistribution'),
    path('DirectorResourceSum/', views.DirectorResourceSum.as_view(), name='DirectorResourceSum'),
    path('SupportGroupResourceSum/', views.SupportGroupResourceSum.as_view(), name='SupportGroupResourceSum'),
]
