from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from .models import Reviews
from .forms import ReviewsForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def reviews(request):
    reviews_list = (Reviews.objects.filter(approved=True).order_by('-created_on'))
    return render(request, 'reviews/reviews.html', {'reviews_list': reviews_list})


@login_required
def add_review(request):

    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.name = request.user
            review.save()
            messages.success(request, 'Your review was sent successfully!')
            return redirect('reviews:reviews')
    else:
        form.ReviewsForm()
    return render(request, 'reviews/add_edit_review.html', {'form': form})


@login_required
def edit_review(request, pk):
    
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review was updated successfully!')
            return redirect('reviews:reviews')
    else:
        form = ReviewsForm(instance=review)
    return render(request, 'reviews/add_edit_review.html', {'form': form})


@login_required
def delete_review(request, review_id):

    reviews = get_object_or_404(Reviews, id=review_id)
    reviews.delete()
    messages.success(request, 'Your review was deleted successfully')
    return redirect('reviews:reviews')
