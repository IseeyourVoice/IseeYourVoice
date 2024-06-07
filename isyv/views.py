from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# views.py

from django.shortcuts import render, redirect

from .forms import CommentForm
from .models import Post, Comment
from django.contrib.auth.decorators import login_required


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        Post.objects.create(title=title, content=content, author=author)
        return redirect('isyv:board')
    return render(request, 'common/create_post.html')


@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 댓글을 작성한 사용자
            comment.save()
    return redirect('isyv:view_post', post_id=post_id)


def view_post(request, post_id):
    # 게시글 ID를 사용하여 해당 게시글을 가져옵니다. 없을 경우 404 에러를 반환합니다.
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)

    return render(request, 'common/post.html', {'post': post, 'comments': comments})


def index(request):
    return render(request, 'index.html')


def soundedit(request):
    return render(request, 'common/soundedit.html')


def soundedit_download(request):
    f = request.POST.get('file')
    return render(request, 'common/soundedit_download.html', {'filename': f})


def board(request):  # 게시판 뷰 추가
    posts = Post.objects.all()
    return render(request, 'common/board.html', {'posts': posts})
