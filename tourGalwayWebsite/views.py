from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .forms import NewTopicForm, PostForm
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
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    return render(request, 'topics.html', {'board': board, 'topics': topics})


@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = request.user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter =  user.username
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by= request.user
            )
            return redirect('topic_message', board_pk=board.pk, topic_pk=topic.pk) 
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})

def topic_message(request, board_pk, topic_pk):
    topic = get_object_or_404(Topic, pk=topic_pk, board_id=board_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_message.html' , {'topic': topic} )

@login_required
def reply_topic(request, board_pk, topic_pk):
    topic = get_object_or_404(Topic, board__id=board_pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()  # <- here
            topic.save()                         # <- and here

            return redirect('topic_message.html', board_pk=board_pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})


def testlang(request):
    return HttpResponse(_('Welcome to the discussion board!'))
