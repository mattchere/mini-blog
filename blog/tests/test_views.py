from django.test import TestCase

from django.contrib.auth.models import User
from blog.models import Blogger, BlogPost, Comment

from django.core.urlresolvers import reverse

class BloggerListViewTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        number_of_blog_posts = 13
        for blog_num in range(number_of_blog_posts):
            user = User.objects.create_user(username=str(blog_num), password='12345')
            Blogger.objects.create(user=user, bio='A')

    def test_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/bloggers/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('bloggers'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('bloggers'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'blog/blogger_list.html')

    def test_lists_all_bloggers(self):
        resp = self.client.get(reverse('bloggers'))
        self.assertEqual(resp.status_code, 200)

        self.assertTrue(len(resp.context['blogger_list']) == 13)