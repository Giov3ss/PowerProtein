from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ExpertAdviceForm

def expert_advice(request):
    if request.method == 'POST':
        form = ExpertAdviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your form was sent!')
            return redirect('expert_advice:success.html')
        else:
            messages.erro(request, 'Please correct the errors!')
    else:
        form = ExpertAdviceForm()

    return render(request, 'expert_advice/expert_advice_form.html', {'form': form})

def success(request):
    return render(request, 'expert_advice/success.html')
