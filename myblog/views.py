from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import PageNotAnInteger , Paginator, EmptyPage
from .forms import CommentForm
from taggit.models import Tag
from django.db.models import Q


# Create your views here.

def post_list(request, tag_slug=None):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 6)  # You can adjust this number
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myblog/post/list.html', {
        'posts': page_obj,
        'tag': tag,
        'tags': Tag.objects.all(),
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    })




def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug, status=Post.Status.PUBLISHED)

    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don’t save yet
            new_comment = comment_form.save(commit=False)
            # Assign the post to the comment
            new_comment.post = post
            new_comment.save()

            # clear the comment form after saving .
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()

    return render(
        request,
        'myblog/post/detail.html',
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form
        }
    )

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'myblog/tag_list.html', {'tags': tags})


def post_search(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query),
            status=Post.Status.PUBLISHED
        )

    return render(request, 'myblog/post/search_results.html', {
        'query': query,
        'results': results
    })