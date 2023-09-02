from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from .models import Reviews
from .forms import ReviewsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test


def reviews(request):
    """
    A view of approved reviews from the database
    """
    reviews_list = (Reviews.objects.filter(approved=True).order_by('-created_on'))  # noqa
    return render(request, 'reviews/reviews.html', {
        'reviews_list': reviews_list,
        'edit_review_url': reverse('reviews:edit_review', kwargs={'pk': 0}),  # noqa
    })


@login_required
def add_review(request):
    """
    A view to add new reviews
    """
    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.name = request.user
            form.save()
            messages.success(request, 'Your review was sent successfully and is now awaiting approval.')  # noqa
            return redirect('reviews:reviews')
    else:
        form = ReviewsForm()
    return render(request, 'reviews/add_edit_review.html', {'form': form})


@login_required
def edit_review(request, pk):
    """
    A view that allow users to edit their own reviews.
    """
    review = get_object_or_404(Reviews, id=pk)
    if not request.user.is_superuser and review.name != request.user.username:
        messages.warning(request, 'You can only edit your own reviews!')
        return render(request, "errors/403.html")

    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review was updated successfully!')
            return redirect('reviews:reviews')
    else:
        form = ReviewsForm(instance=review)
        messages.info(request, f"You are editing {review.name} review's")
    return render(request, 'reviews/add_edit_review.html', {'form': form, 'review': review})  # noqa


@login_required
def delete_review(request, review_id):
    """
    A view that allow users to delete their own review.
    """
    reviews = get_object_or_404(Reviews, id=review_id)
    reviews.delete()
    messages.success(request, 'Your review was deleted successfully')
    return redirect('reviews:reviews')
