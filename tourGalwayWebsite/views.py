from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from .forms import NewTopicForm
from .models import Board, Topic, Post
# Create your views here.

#Default page
def home(request):
    return render(request,'home.html')

#Forum
def forum(request):
    boards = Board.objects.all()
    return render(request,'forum.html', {'boards': boards})

#Webpages
def contact(request):
    return render(request,'contact.html')
def food(request):
    return render(request,'food.html')
def ptv(request):
    return render(request,'ptv.html')
def transport(request):
    return render(request,'transport.html')

#Each of the board topics
def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter =  user.get_username()
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('topic_message', board_pk=board.pk, topic_pk=topic.pk, post_pk=post.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_message(request, board_pk, topic_pk):
    board = get_object_or_404(Board, pk=board_pk)
    topic = get_object_or_404(Topic, pk=topic_pk)
    subject = topic.subject
   # post = get_object_or_404(Post, post_pk=post_pk)
    user = User.objects.first()

    return render(request, 'topic_message.html', {'board': board} , subject )

def testlang(request):
    return HttpResponse(_('Welcome to the discussion board!'))
