from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class CustomUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='newuser',
            email='newuser@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'newuser')
        self.assertEqual(user.email, 'newuser@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(str(user), user.username)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@email.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignUpViewTests(TestCase):
    def test_signup_page_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration\signup.html')

    def test_signup_form(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='newuser',
            email='newuser@email.com',
            password='testpass123',
            first_name='new',
            last_name='user',
        )
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.all()[0].username, 'newuser')
        self.assertEqual(User.objects.all()[0].email, 'newuser@email.com')
        self.assertEqual(User.objects.all()[0].first_name, 'new')
        self.assertEqual(User.objects.all()[0].last_name, 'user')


# class ProfileViewTests(SimpleTestCase):
#     def test_profile_page_status_code(self):
#         response = self.client.get('/accounts/profile/', follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('profile'), follow=True)
#         self.assertEqual(response.status_code, 200)

#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('profile'), follow=True)
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'registration\profile.html')
