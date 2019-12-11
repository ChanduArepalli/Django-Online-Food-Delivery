import unittest
from django.urls import reverse
from django.test import Client
from .models import Product, Order
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_product(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["description"] = "description"
    defaults["stock"] = "stock"
    defaults["price"] = "price"
    defaults.update(**kwargs)
    return Product.objects.create(**defaults)


def create_order(**kwargs):
    defaults = {}
    defaults["address"] = "address"
    defaults["deliveried"] = "deliveried"
    defaults["deliveried_at"] = "deliveried_at"
    defaults.update(**kwargs)
    if "product" not in defaults:
        defaults["product"] = create_django_contrib_auth_models_user()
    return Order.objects.create(**defaults)


class ProductViewTest(unittest.TestCase):
    '''
    Tests for Product
    '''
    def setUp(self):
        self.client = Client()

    def test_list_product(self):
        url = reverse('Product_product_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_product(self):
        url = reverse('Product_product_create')
        data = {
            "name": "name",
            "description": "description",
            "stock": "stock",
            "price": "price",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_product(self):
        product = create_product()
        url = reverse('Product_product_detail', args=[product.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_product(self):
        product = create_product()
        data = {
            "name": "name",
            "description": "description",
            "stock": "stock",
            "price": "price",
        }
        url = reverse('Product_product_update', args=[product.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class OrderViewTest(unittest.TestCase):
    '''
    Tests for Order
    '''
    def setUp(self):
        self.client = Client()

    def test_list_order(self):
        url = reverse('Product_order_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_order(self):
        url = reverse('Product_order_create')
        data = {
            "address": "address",
            "deliveried": "deliveried",
            "deliveried_at": "deliveried_at",
            "product": create_django_contrib_auth_models_user().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_order(self):
        order = create_order()
        url = reverse('Product_order_detail', args=[order.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_order(self):
        order = create_order()
        data = {
            "address": "address",
            "deliveried": "deliveried",
            "deliveried_at": "deliveried_at",
            "product": create_django_contrib_auth_models_user().pk,
        }
        url = reverse('Product_order_update', args=[order.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


