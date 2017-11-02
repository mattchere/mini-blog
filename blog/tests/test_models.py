from django.test import TestCase

from blog.models import Blogger, BlogPost, Comment
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class BloggerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser1', password='12345')
        test_user.save()

        Blogger.objects.create(user=test_user, bio='This is a test bio.')

    def test_user_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('user').verbose_name
        self.assertEquals(field_label, 'user')

    def test_bio_label(self):
        blogger = Blogger.objects.get(id=1)
        field_label = blogger._meta.get_field('bio').verbose_name
        self.assertEquals(field_label, 'bio')

    def test_object_name_is_username(self):
        blogger = Blogger.objects.get(id=1)
        expected_object_name = blogger.user.username
        self.assertEquals(expected_object_name, str(blogger))

    def test_get_absolute_url(self):
        blogger = Blogger.objects.get(id=1)
        self.assertEquals(blogger.get_absolute_url(), '/blog/blogger/1')

        
class BlogPostModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser1', password='12345')
        test_user.save()

        blogger = Blogger.objects.create(user=test_user, bio='This is a test bio.')
        post_date1 = datetime.today()
        post_date2 = datetime.today() + timedelta(days=1)
        BlogPost.objects.create(title='Title', post_date=post_date1, author=blogger, description='Testing')
        BlogPost.objects.create(title='Title2', post_date=post_date2, author=blogger, description='Testing2')

    def test_title_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_post_date_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label, 'post date')

    def test_author_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('author').verbose_name
        self.assertEquals(field_label, 'author')
        
    def test_description_label(self):
        blogpost = BlogPost.objects.get(id=1)
        field_label = blogpost._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_object_name_is_title(self):
        blogpost = BlogPost.objects.get(id=1)
        expected_object_name = blogpost.title
        self.assertEquals(expected_object_name, str(blogpost))

    def test_get_absolute_url(self):
        blogpost = BlogPost.objects.get(id=1)
        self.assertEquals(blogpost.get_absolute_url(), '/blog/1')

    def test_ordering(self):
        # Order all blog posts in reverse chronological order for testing
        blogposts = list(BlogPost.objects.all())
        blogposts.sort(key=lambda x: x.post_date, reverse=True)

        # Check that each blogpost is in reverse chronological order as expected
        for post1, post2 in zip(blogposts, BlogPost.objects.all()):
            self.assertEquals(post1, post2)
        
