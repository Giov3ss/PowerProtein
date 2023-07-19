from .models import Reviews

def service_reviews(request):
    
    service_reviews =  Reviews.objects.filter(
        approved=True, carousel_review=True
    ).order_by('-created_on')

    context = {
        'service_reviews': service_reviews,
    }

    return context