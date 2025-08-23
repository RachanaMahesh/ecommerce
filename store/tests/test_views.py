from unittest import skip
from django.http import HttpRequest
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from ..models import Category, Product
from django.contrib.auth.models import User
from ..views import all_products, product_detail

# @skip("example for skipping")
# class TestSkip(TestCase):
#     def test_skip_example():
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug = 'django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id = 1, title='django beginners', created_by_id=1, slug ='django-beginners', price = '20.00', image='django')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product Response status
        """
        response = self.c.get(reverse("store:product_detail", args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category Response Status
        """
        response = self.c.get(reverse("store:category_list", kwargs= {'category_slug': 'django'}))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        htmlcontent = response.content.decode('utf8')
        # print(htmlcontent)
        self.assertInHTML("<title>Home</title>",htmlcontent)
        self.assertTrue(htmlcontent.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code,200)
        
    def test_view_function(self):
        request = self.factory.get(reverse("store:product_detail",args=["django-beginners"]))
        response = product_detail(request, slug = self.data1.slug )
        htmlcontent = response.content.decode('utf8')
        # self.assertIn("<title> </title>",htmlcontent)
        self.assertTrue(htmlcontent.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code,200)

    def test_view_home_function(self):
        request = self.factory.get("item/django-beginners")
        response = all_products(request)
        htmlcontent = response.content.decode('utf8')
        self.assertIn("<title>Home</title>",htmlcontent)
        self.assertTrue(htmlcontent.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code,200)

