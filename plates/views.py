from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Review, Comment
from .forms import PostForm, ReviewForm, CommentForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'plates/index.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    review_form = ReviewForm()
    reviews = post.review_set.all()
    comments = Comment.objects.filter(post=post, review__in=reviews) # 확인필요
    comment_form = CommentForm()
    context = {
        'post': post,
        'review_form': review_form,
        'reviews': reviews,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'plates/detail.html', context)



# @login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('plates:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
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


# @login_required
def review_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post_form = PostForm(request.POST)
    if post_form.is_valid():
        review = post_form.save(commit=False)
        review.post = post
        review.user = request.user
        review.save()
        return redirect('plates:detail', post.pk)
    context = {
        'post': post,
        'post_form': post_form,
    }
    return render(request, 'plates/detail.html', context)

# @login_required
def review_update(request, post_pk, review_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(pk=review_pk)
    if request.user == review:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('plates:detail', post.pk)
        else:
            form = ReviewForm(instance=review)

# @login_required
def review_delete(request, post_pk, review_pk):
    review = review.objects.get(pk=review_pk)

    if request.user == review.user:
        review.delete()
    return redirect('plates:detail', post_pk)


def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
    return redirect('plates:index')

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