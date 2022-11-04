from .models import Post , Coment
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm, EmailPostForm
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def post_list(request):
    #posts = Post.published.all()
    object_list=Post.published.all()
    pagnitor=Paginator(object_list,3)
    page=request.GET.get('page')

    try:
        posts=pagnitor.page(page)
    except PageNotAnInteger:
        posts=pagnitor.page(1)
    except EmptyPage:
        posts=pagnitor.page(pagnitor.num_pages)
    return render(request, 'newblog/index.html', {'page':page , 'posts': posts})


def share(request):
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = EmailPostForm()
        return render(request, 'newblog/form.html', {'form': form})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,slug=post,status='published', publish__year=year, publish__month=month, publish__day=day)
    comments=post.comments.filter(active=True)
    new_comment=None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
    else:
        comment_form=CommentForm()
    return render(request,'newblog/detail.html',{'post':post,'comments':comments,'new_comment':new_comment,'comment_form':comment_form})
