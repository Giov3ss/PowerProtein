from django.shortcuts import render, redirect
from .forms import ExpertAdviceForm

def expert_advice(request):
    if request.method == 'POST':
        form = ExpertAdviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ExpertAdviceForm()

    return render(request, 'expert_advice/expert_advice_form.html', {'form': form})

def success(request):
    return render(request, 'success.html')
