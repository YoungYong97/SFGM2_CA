from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
from .models import Board
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
    return render(request, 'new_topic.html', {'board' : board})