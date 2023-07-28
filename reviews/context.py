from .models import Reviews

def service_reviews(request):
    """
    A view that retrieves a queryset of approved service reviews
    with 'carousel_review', meaning they're suitable to be displayed 
    in a carousel on the website.
    """
    service_reviews =  Reviews.objects.filter(
        approved=True, carousel_review=True
    ).order_by('-created_on')

    context = {
        'service_reviews': service_reviews,
    }

    return context