from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from .models import Reviews
from .forms import ReviewsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def reviews(request):
    reviews_list = (Reviews.objects.filter(approved=True).order_by('-created_on'))
    return render(request, 'reviews/reviews.html', {
        'reviews_list': reviews_list,
        'edit_review_url': reverse('reviews:edit_review', kwargs={'pk': 0}),
    })


@login_required
def add_review(request):
    
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.name = request.user
            form.save()
            messages.success(request, 'Your review was sent successfully and is awaiting approval! ')
            return redirect('reviews:reviews')
    else: 
        form = ReviewsForm()
    return render(request, 'reviews/add_edit_review.html', {'form': form})


@login_required
def edit_review(request, pk):
    review = get_object_or_404(Reviews, id=pk)
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review was updated successfully!')
            return redirect('reviews:reviews')
    else:
        form = ReviewsForm(instance=review)
    return render(request, 'reviews/add_edit_review.html', {'form': form, 'review': review})


@login_required
def delete_review(request, review_id):

    reviews = get_object_or_404(Reviews, id=review_id)
    reviews.delete()
    messages.success(request, 'Your review was deleted successfully')
    return redirect('reviews:reviews')
