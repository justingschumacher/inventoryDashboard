from django.db.models import Q
from django.utils import timezone
from django.views.generic import View, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Vmguest

# Create your views here.


class IndexClassView(View):
    model = Vmguest

    template_name = 'inventoryDashboard/index_new.html'

    success_url = reverse_lazy('index')

    fields = ('vmguestid', 'vm_name', 'vmhostid', 'vmhostname', 'clid', 'clustername', 'dcid',
              'dcname', 'vcid', 'vchostname', 'fid', 'mem_gb', 'disk_gb', 'cpu', 'overall_cpu_usage',
              'guest_memory_usage', 'ostype', 'state', 'annotation', 'vlan', 'ip', 'prefix',
              'connected', 'timestamp', )

    def get(self, request):
        vmguests = Vmguest.objects.all()
        vm_count = Vmguest.objects.filter(Q(vmguestid__gte=0)).count()
        redhat_count = Vmguest.objects.filter(Q(ostype__icontains='Red Hat')).count()
        windows_count = Vmguest.objects.filter(Q(ostype__icontains='Windows')).count()
        ubuntu_count = Vmguest.objects.filter(Q(ostype__icontains='Ubuntu')).count()
        suse_count = Vmguest.objects.filter(Q(ostype__icontains='SUSE')).count()
        other_count = Vmguest.objects.filter(Q(vmguestid__gte=0)).exclude(Q(ostype__icontains='Windows') |
                                                                          Q(ostype__icontains='Red Hat') |
                                                                          Q(ostype__icontains='Ubuntu') |
                                                                          Q(ostype__icontains='SUSE')
                                                                          ).count()
        high_cpu_count = Vmguest.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = Vmguest.objects.filter(Q(cpu__gt=4))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'vm_count': vm_count,
                       'redhat_count': redhat_count,
                       'windows_count': windows_count,
                       'ubuntu_count': ubuntu_count,
                       'suse_count': suse_count,
                       'other_count': other_count,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests})

    def post(self, request):
        vmguests = Vmguest.objects.order_by('clustername')
        searchterm = ''
        oracle_count = Vmguest.objects.filter(Q(ostype__icontains='Ora')).count()
        if request.POST and request.POST.get('search'):
            searchterm = request.POST.get('search').lower()
            vmguests = vmguests.filter(Q(vm_name__icontains=searchterm) |
                                       Q(vmhostname__icontains=searchterm) |
                                       Q(clustername__icontains=searchterm) |
                                       Q(dcname__icontains=searchterm) |
                                       Q(vchostname__icontains=searchterm) |
                                       Q(cpu__icontains=searchterm) |
                                       Q(ostype__icontains=searchterm) |
                                       Q(state__icontains=searchterm) |
                                       Q(connected__icontains=searchterm)
                                       )
        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'searchterm': searchterm,
                       'oracle_count': oracle_count})


class DetailClassView(DetailView):
    model = Vmguest

    template_name = 'inventoryDashboard/item_detail.html'

    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class HighCPUCountClassView(View):
    model = Vmguest

    template_name = 'inventoryDashboard/high_cpu_count.html'

    success_url = reverse_lazy('high_cpu_count')

    fields = ('vmguestid', 'vm_name', 'vmhostid', 'vmhostname', 'clid', 'clustername', 'dcid',
              'dcname', 'vcid', 'vchostname', 'fid', 'mem_gb', 'disk_gb', 'cpu', 'overall_cpu_usage',
              'guest_memory_usage', 'ostype', 'state', 'annotation', 'vlan', 'ip', 'prefix',
              'connected', 'timestamp', )

    def get(self, request):
        vmguests = Vmguest.objects.all()
        high_cpu_count = Vmguest.objects.filter(Q(cpu__gt=4)).count()
        high_cpu_guests = Vmguest.objects.filter(Q(cpu__gt=4))

        return render(request,
                      self.template_name,
                      {'Vmguests': vmguests,
                       'high_cpu_count': high_cpu_count,
                       'high_cpu_guests': high_cpu_guests})
