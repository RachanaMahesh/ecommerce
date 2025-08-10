from django.test import TestCase
from store.models import Category,Product
from django.contrib.auth.models import User


class TestCategoryModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug = 'django')

    def test_category_model_instance(self):
        """
        Test Category model for data insertion/types/fields atrribute"""
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_string(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')

class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug = 'django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id = 1, title='django beginners', created_by_id=1, slug ='django-beginners', price = '20.00', image='django')

    def test_product_model_entry(self):
        """
        Test Category model for data insertion/types/fields atrribute
        """
        data = self.data1
        self.assertTrue(isinstance(data,Product))
        self.assertEqual(str(data), 'django beginners')