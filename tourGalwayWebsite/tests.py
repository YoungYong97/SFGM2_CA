from django.urls import reverse, resolve
from django.test import TestCase
from .views import forum ,board_topics ,home
from .models import Board

#Tests for forum
class ForumTests(TestCase):
    def test_forum_view_status_code(self):
        url = reverse('forum')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_forum_url_resolves_forum_view(self):
        view = resolve('/')
        self.assertEquals(view.func, forum)
    def setUp(self):
        self.board = Board.objects.create(name='GSD', description='GSD board.')
        url = reverse('forum')
        self.response = self.client.get(url)


#Tests for home
class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)



#Board Topic tests
class BoardTopicsTests(TestCase):
#Setup an object to represant one of the boards
    def setUp(self):
        Board.objects.create(name='Other Stuff', description='A discussion about unrelated things')
#Testing if Django returns a status code 200 for an existing Board
    def test_forum_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
#testing if Django is returning a status code 404 (page not found) for a Board that doesn’t exist in the database.
    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code,404)
#testing if Django is using the correct view function to render the topics.
    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/forum/2/')
        self.assertEquals(view.func, board_topics)

