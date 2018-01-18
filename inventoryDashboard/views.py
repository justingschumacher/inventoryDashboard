from django.shortcuts import render
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic import DeleteView, DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .models import vmwareGuest
from .forms import VmwareGuestForm


# Create your views here.

class IndexDetailView(DetailView):

    model = vmwareGuest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class IndexListView(ListView):

    model = vmwareGuest

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context