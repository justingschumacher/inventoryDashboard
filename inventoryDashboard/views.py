from django.db.models import Q, Count
from django.utils import timezone
from django.views.generic import View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import DjangoReportCore

# Create your views here.


class IndexClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/index.html'

    success_url = reverse_lazy('index')

    fields = ('__all__')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        high_cpu_count = DjangoReportCore.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = DjangoReportCore.objects.filter(Q(cpu__gt=4))
        high_memory_count = DjangoReportCore.objects.filter(Q(mem_gb__gte=8)).count()
        high_memory_guests = DjangoReportCore.objects.filter(Q(mem_gb__gte=8))
        guests_by_director_count = DjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
        guests_by_support_group_count = DjangoReportCore.objects.values('support_group').annotate(VMs=Count('support_group'))
        vm_count_by_os = DjangoReportCore.objects.values('ostype').annotate(VMs=Count('ostype'))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests,
                       'high_memory_count': high_memory_count,
                       'high_memory_guests': high_memory_guests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       })

    def post(self, request):
        vmguests = DjangoReportCore.objects.order_by('clustername')
        searchterm = ''
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            vmguests = vmguests.filter(Q(vmname__icontains=searchterm) |
                                       Q(vmhostname__icontains=searchterm) |
                                       Q(clustername__icontains=searchterm) |
                                       Q(dcname__icontains=searchterm) |
                                       Q(vchostname__icontains=searchterm) |
                                       Q(cpu__icontains=searchterm) |
                                       Q(ostype__icontains=searchterm) |
                                       Q(state__icontains=searchterm) |
                                       Q(connected__icontains=searchterm) |
                                       Q(director__icontains=searchterm) |
                                       Q(support_group__icontains=searchterm)
                                       )
        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'searchterm': searchterm,
                       })


class DetailClassView(DetailView):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/item_detail.html'

    success_url = reverse_lazy('index')

    guests_by_director_count = DjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
    guests_by_support_group_count = DjangoReportCore.objects.values('support_group').annotate(VMs=Count('support_group'))


class GuestsbyDirectorClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/guests_by_director.html'

    success_url = reverse_lazy('index')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        guests_by_director_count = DjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
        guests_by_support_group_count = DjangoReportCore.objects.values('support_group').annotate(VMs=Count('support_group'))
        vm_count_by_os = DjangoReportCore.objects.values('ostype').annotate(VMs=Count('ostype'))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       })


class GuestsbySupportGroupClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/guests_by_support_group.html'

    success_url = reverse_lazy('index')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        guests_by_director_count = DjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
        guests_by_support_group_count = DjangoReportCore.objects.values('support_group').annotate(VMs=Count('support_group'))
        vm_count_by_os = DjangoReportCore.objects.values('ostype').annotate(VMs=Count('ostype'))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       })


class OSDistributionClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/os_distribution.html'

    success_url = reverse_lazy('index')

    fields = ('__all__')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        guests_by_director_count = DjangoReportCore.objects.values('director').annotate(VMs=Count('director'))
        guests_by_support_group_count = DjangoReportCore.objects.values('support_group').annotate(VMs=Count('support_group'))
        vm_count_by_os = DjangoReportCore.objects.values('ostype').annotate(VMs=Count('ostype'))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'guests_by_director_count': guests_by_director_count,
                       'guests_by_support_group_count': guests_by_support_group_count,
                       'vm_count_by_os': vm_count_by_os,
                       })


class HighCPUCountClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/high_cpu_count.html'

    success_url = reverse_lazy('high_cpu_count')

    fields = ('__all__')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        high_cpu_count = DjangoReportCore.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = DjangoReportCore.objects.filter(Q(cpu__gt=4))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests})


class HighMemoryCountClassView(View):
    model = DjangoReportCore

    template_name = 'inventoryDashboard/high_mem_count.html'

    success_url = reverse_lazy('high_mem_count')

    fields = ('__all__')

    def get(self, request):
        vmguests = DjangoReportCore.objects.all()
        high_mem_count = DjangoReportCore.objects.filter(Q(mem_gb__gt=8)).count()
        high_mem_guests = DjangoReportCore.objects.filter(Q(mem_gb__gt=8))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_mem_count': high_mem_count,
                       'high_mem_guests': high_mem_guests})
