from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from app.models import CustomUser, Post
from .serializers import CustomUserSerializers, PostSerializers


class UserPostAPITestCase(APITestCase):
    def setUp(self):
        self.user1 = CustomUser.objects.create(username='test_username', email='test@d.com')
        self.user2 = CustomUser.objects.create(username='test_username1', email='test@d.com1')
        self.post1 = Post.objects.create(user=self.user1, title='test_title', body='test_body')
        self.post2 = Post.objects.create(user=self.user1, title='test_title1', body='test_body1')

    def test_get_user(self):
        url = reverse('users_list')
        response = self.client.get(url)
        serializers_data = CustomUserSerializers([self.user1, self.user2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializers_data, response.data)

    def test_get_post_list(self):
        url = reverse('posts_list', kwargs={'user_id': self.user1.id})
        response = self.client.get(url)
        serializer_data = PostSerializers([self.post1, self.post2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_get_user_post_list(self):
        url = reverse('posts_list', kwargs={'user_id': self.user1.id})
        response = self.client.get(url)
        serializer_data = PostSerializers([self.post1, self.post2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer_data)

    def test_create_post(self):
        url = reverse('create_post')
        data = {'user': self.user1.id, 'title': 'new_post_title', 'body': 'new_post_body'}
        response = self.client.post(url, data)
        created_post = Post.objects.latest('id')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['id'], created_post.id)
        self.assertEqual(created_post.user, self.user1)
        self.assertEqual(created_post.title, 'new_post_title')
        self.assertEqual(created_post.body, 'new_post_body')

    def test_delete_post(self):
        url = reverse('destroy_post', kwargs={'pk': self.post1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

# class UserPostAPITestCase(APITestCase):
#     def setUp(self):
#         self.user1 = CustomUser.objects.create(username='test_username', email='test@d.com')
#         self.user2 = CustomUser.objects.create(username='test_username1', email='test@d.com1')
#         self.post1 = Post.objects.create(user=self.user1, title='test_title', body='test_body')
#         self.post2 = Post.objects.create(user=self.user1, title='test_title1', body='test_body1')
#
#     def test_get_user(self):
#         url = reverse('users_list')
#         response = self.client.get(url)
#         serializers_data = CustomUserSerializers([self.user1, self.user2], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializers_data, response.data)
#
#     def test_get_post(self):
#         url = reverse('posts_list')
#         response = self.client.get(url)
#         serializers_data = PostSerializers([self.post1, self.post1], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializers_data, response.data)








#
# class CustomUserAPIListTest(APITestCase):
#     def test_get_custom_users(self):
#         url = reverse('custom_users_list')
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#
# class PostAPIListTest(APITestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create(username='testuser')
#         self.post = Post.objects.create(user=self.user, title='Test Post')
#
#     def test_get_posts_for_user(self):
#         url = reverse('posts_list', args=[self.user.id])
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, 200)
#
#
# class PostCreateAPIListTest(APITestCase):
#     def test_create_post(self):
#         data = {'user': 1, 'title': 'New Post'}
#         url = reverse('create_post')
#         response = self.client.post(url, data)
#         print(response.data)  # Распечатайте содержимое ответа сервера
#         self.assertEqual(response.status_code, 201)
#         self.assertEqual(Post.objects.count(), 1)
#
#
# class PostDestroyAPILIstTest(APITestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create(username='testuser')
#         self.post = Post.objects.create(user=self.user, title='Test Post')
#
#     def test_delete_post(self):
#         url = reverse('destroy_post', args=[self.post.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, 204)
#         self.assertEqual(Post.objects.count(), 0)