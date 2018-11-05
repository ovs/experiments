# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
#from market.models import MarketShop
from tg.models import Post, Activity


# models test
class OnetTest(TestCase):
    def create(self):
        print "CREATE"

    def test_one_1(self):
        print "test_one_1"
        # Get the post object
        a = Post.objects.create()
        print "a.pk", a.pk,type(a)
        post = Post.objects.get(pk=1)
        print "post.pk", post.pk
            # # Add a like activity
            # post.likes.create(activity_type=Activity.LIKE, user=request.user)

            # # Or in a similar way using the Activity model to add the like
            # Activity.objects.create(content_object=post, activity_type=Activity.LIKE, user=request.user)

            # # Get all Activity instances related to Post
            # post.likes.all()

            # # Count the number of likes
            # post.likes.count()

            # # Get the users who liked the post
            # post.likes.values_list('user__first_name', flat=True)

    # def create_marketshop(self, title="only a test", body="yes, this is only a test"):
    #     return MarketShop.objects.create(title=title)

    # def test_marketshop_creation(self):
    #     w = self.create_marketshop()
    #     self.assertTrue(isinstance(w, MarketShop))
    #     self.assertEqual(w.__unicode__(), w.title)

    # def test_marketshop_list_view(self):
    #     w = self.create_marketshop()
    #     url = reverse("market")
    #     # url = reverse("market.views.MarketPageView")
    #     print "url=", url
    #     return
    #     resp = self.client.get(url)

    #     self.assertEqual(resp.status_code, 200)
    #     print resp.content
    #     self.assertIn(w.title, resp.content)


