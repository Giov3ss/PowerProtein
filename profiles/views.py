from django.shortcuts import render


def profile(request):
    """
    Show user's profile views
    """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)