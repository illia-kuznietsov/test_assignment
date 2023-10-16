from django.test import TestCase

from django.test import TestCase
from .models import Restaurant, Dish, Menu, Employee, Vote
from django.contrib.auth.models import User
from .serializers import RestaurantSerializer
from rest_framework.test import APIClient, APITestCase


class RestaurantModelTest(TestCase):
    def test_create_and_retrieve_restaurant(self):
        Restaurant.objects.create(name="Test Restaurant", address="Test Address")
        restaurant = Restaurant.objects.get(name="Test Restaurant")
        self.assertEqual(restaurant.address, "Test Address")


class DishModelTest(TestCase):
    def test_create_and_retrieve_dish(self):
        Dish.objects.create(name="Test Dish", recipe="Test Recipe", ingredients="Test Ingredients")
        dish = Dish.objects.get(name="Test Dish")
        self.assertEqual(dish.recipe, "Test Recipe")


class DishModelTest(TestCase):

    def setUp(self):
        self.dish = Dish.objects.create(name="Pizza", recipe="Some recipe", ingredients="Some ingredients")

    def test_string_representation(self):
        self.assertEqual(str(self.dish), self.dish.name)

    def test_dish_creation(self):
        self.assertIsInstance(self.dish, Dish)


class RestaurantSerializerTest(TestCase):

    def test_serialize_restaurant(self):
        restaurant = Restaurant.objects.create(name="Test Restaurant", address="Test Address")
        serializer = RestaurantSerializer(restaurant)
        self.assertEqual(serializer.data, {'id': restaurant.id, 'name': 'Test Restaurant', 'address': 'Test Address'})


class RestaurantViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_restaurant(self):
        response = self.client.post('/restaurants/', {'name': 'Test Restaurant', 'address': 'Test Address'},
                                    format='json')
        self.assertEqual(response.status_code, 201)  # 201 Created


class DishViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.dish = Dish.objects.create(name="Pizza", recipe="Some recipe", ingredients="Some ingredients")
        self.url = '/dishes/'

    def test_retrieve_dish_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)  # OK
        self.assertEqual(len(response.data), 1)

    def test_retrieve_single_dish(self):
        response = self.client.get(f'{self.url}{self.dish.id}/')
        self.assertEqual(response.status_code, 200)  # OK
        self.assertEqual(response.data['name'], "Pizza")


class VoteIntegrationTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.restaurant = Restaurant.objects.create(name="Test Restaurant", address="Test Address")
        self.employee_user = User.objects.create_user(username='testuser', password='testpass')
        self.employee = Employee.objects.create(user=self.employee_user, name="Test Employee",
                                                restaurant=self.restaurant)
        self.dish = Dish.objects.create(name="Pizza", recipe="Some recipe", ingredients="Some ingredients")
        self.menu = Menu.objects.create(restaurant=self.restaurant, date="2023-10-01")
        self.menu.dishes.add(self.dish)

    def test_employee_voting(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post('/votes/', {'employee': self.employee.id, 'menu': self.menu.id}, format='json')
        self.assertEqual(response.status_code, 201)  # Created
