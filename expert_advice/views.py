from .forms import ExpertAdviceAddFrom
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # noqa
from .models import ExpertAdvice
from django.urls import reverse_lazy


class ExpertAdviceView(CreateView):
    """
    A view to handle the creation of expert advice requests.
    """
    model = ExpertAdvice
    form_class = ExpertAdviceAddFrom
    template_name = 'expert_advice/expert_advice_form.html'
    success_url = reverse_lazy('expert_advice:success')

    def form_valid(self, form):
        return super().form_valid(form)
        messages.success = "Expert Advice request sent!"


def success(request):
    """
    A view function to render the success page
    """
    return render(request, 'expert_advice/success.html')
