from django.shortcuts import render
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy
from .models import vmwareGuest
from .forms import VmwareGuestForm


# Create your views here.

class IndexView():
    pass