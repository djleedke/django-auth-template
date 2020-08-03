from django.test import TestCase
from django.urls import reverse, resolve
from .models import User

#Creates a test user
def create_user():
    user = User()
    user.email = 'test@test.com'
    user.set_password('testtest')
    user.first_name = 'Test'
    user.last_name = 'Dummy'
    user.save()
    return user

class UserModelTest(TestCase):

    #Testing creation of a user
    def test_user_creation(self):
        user = create_user()
        record = User.objects.get(pk=1)
        self.assertEqual(record, user)

class LoginViewTest(TestCase):

    def test_view_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class SignUpViewTest(TestCase):

    def test_view_url(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

class PasswordResetViewTest(TestCase):

    def test_view_url(self):
        response = self.client.get('/password_reset/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_name(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)

class IndexViewTest(TestCase):
    
    def test_view_url_logged_in(self):
        user = create_user()
        self.client.login(email=user.email, password='testtest')
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_view_url_logged_out(self):
        response = self.client.get('/', follow=True)
        self.assertRedirects(response, '/login/')
