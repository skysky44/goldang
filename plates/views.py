from django.shortcuts import render, redirect
from django.db.models import F
from django.contrib.auth.decorators import login_required
from .models import Post, Review, Comment, PostImage, ReviewImage
from .forms import PostForm, ReviewForm, CommentForm, PostImageForm, ReviewImageForm
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.all()
    지역별_맛집 = Post.objects.filter(address_city__in=["서울시 마포구", "서울특별시 마포구"])[:8]
    조회수_맛집 = Post.objects.order_by("-visited")[:8]

    context = {
        'posts': posts,
        '지역별_맛집': 지역별_맛집,
        '조회수_맛집': 조회수_맛집,
    }
    return render(request, 'plates/index.html', context)

# 수정
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    posts = Post.objects.all()
    review_form = ReviewForm()
    comment_form = CommentForm()
    reviews = post.review_set.all()

    review_images = []
    post_images = PostImage.objects.filter(post=post)
    for review in reviews:
        for review_image in review.review_images.all():
            review_images.append(review_image)

    review_images_reversed = list(reversed(review_images))
    

    nearby_restaurants = posts.filter(address_city=post.address_city).exclude(pk=post_pk)[:5]
    post.visited = F('visited') + 1
    # post.visited += 1
    post.save()
    '''다음 호출이 일어날 때 위 연산이 수행되는 것 같다.'''
    # To access the new value saved this way, the object must be reloaded (3.2 Doc)
    # post = Post.objects.get(pk=post_pk)
    post.refresh_from_db()

    context = {
        'post': post,
        'post_images': post_images,
        'review_form': review_form,
        'reviews': reviews,
        'comment_form': comment_form,
        '맛있다': post.review_set.filter(taste_evaluation=5),
        '괜찮다': post.review_set.filter(taste_evaluation=3),
        '별로': post.review_set.filter(taste_evaluation=1),
        'review_images': review_images,
        'review_images_reversed': review_images_reversed,

        'nearby_restaurants': nearby_restaurants,
    }

    return render(request, 'plates/detail.html', context)




# @login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        imageForm = PostImageForm(request.POST, request.FILES)
        if form.is_valid() and imageForm.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            for image in request.FILES.getlist('image'): # s 없나
                PostImage.objects.create(post=post, image=image)
            return redirect('plates:detail', post.pk)
    else:
        form = PostForm()
        imageForm = PostImageForm()
    context = {
        'form': form,
        'imageForm': imageForm,
    }
    return render(request, 'plates/create.html', context)


# @login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('plates:index')


# @login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('plates:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('plates:index')
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'plates/update.html', context)



def review_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post_form = PostForm(request.POST)
    
    
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        imageForm = ReviewImageForm(request.POST, request.FILES)
        if review_form.is_valid() and imageForm.is_valid():
            review = review_form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()

            for image in request.FILES.getlist('image'):
                ReviewImage.objects.create(review=review, image=image)

            return redirect('plates:detail', post.pk)
    else:
        review_form = ReviewForm()
        imageForm = ReviewImageForm()
    context = {
        'post': post,
        # 'post_form': post_form,
        'review_form': review_form,
        'imageForm': imageForm,
    }
    return render(request, 'plates/review.html', context)


# @login_required

# 수정
def review_update(request, post_pk, review_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(pk=review_pk, post=post)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, instance=review)
            imageForm = ReviewImageForm(request.POST, request.FILES, instance=review.review_images.first())
            if review_form.is_valid() and imageForm.is_valid():
                review_form.save()

                ReviewImage.objects.filter(review=review).delete()
                for image in request.FILES.getlist('image'):
                    ReviewImage.objects.create(review=review, image=image)

                return redirect('plates:detail', post.pk)
        else:
            review_form = ReviewForm(instance=review)
            imageForm = ReviewImageForm(instance=review.review_images.first())

    else:
        return redirect('plates:detail', post.pk)

    context = {
        'review_form': review_form,
        'post': post,
        'review': review,
        'imageForm': imageForm,
    }

    return render(request, 'plates/review_update.html', context)


# @login_required
def review_delete(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if request.user == review.user:
        review.delete()
    return redirect('plates:detail', post_pk)


def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('plates:detail', post_pk)

def comment_create(request, post_pk, review_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.review = review
            comment.user = request.user
            comment.save()
            return redirect('plates:detail', post.pk)

def comment_update(request, post_pk, review_pk, comment_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(pk=review_pk)
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('plates:detail', post.pk)
        else:
            form = CommentForm(instance=comment)

def comment_delete(request, post_pk, review_pk, comment_pk):
    comment = comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('plates:detail', post_pk)













def review_detail(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review_images = ReviewImage.objects.filter(review=review)
    context = {
        'review': review,
        'review_images': review_images,
    }
    return render(request, 'plates/review_detail.html', context)