from django.shortcuts import get_object_or_404
from django.urls import path
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant, Dish, Menu, Employee, Vote
from .serializers import RestaurantSerializer, DishSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


class TodaysMenuResultsView(APIView):
    def get(self, request, address):
        tomorrow = timezone.now().date() + timezone.timedelta(days=1)
        restaurant = get_object_or_404(Restaurant, address=address)

        # Getting menus of the restaurant for today
        menus = Menu.objects.filter(restaurant=restaurant, date=tomorrow)

        results = ["Results of today's vote are here. It will affect choice for tomorrow"]
        for menu in menus:
            votes = Vote.objects.filter(menu=menu).count()
            # You might use a serializer here to format the menu and its dishes
            results.append({
                "menu": "Serialized menu here",
                "votes": votes
            })

        return Response(results)


class CurrentDayMenuView(APIView):
    def get(self, request, address):
        today = timezone.now().date()
        print(today)
        restaurant = get_object_or_404(Restaurant, address=address)
        # Get the menu of the restaurant for today
        menus = Menu.objects.filter(restaurant=restaurant, date=today)

        # Get the menu with the most votes
        most_voted_menu = None
        max_votes = -1
        for menu in menus:
            print(menu.date)
            votes = Vote.objects.filter(menu=menu).count()
            print(votes)
            if votes > max_votes:
                max_votes = votes
                most_voted_menu = menu

        if most_voted_menu:
            # You might use a serializer here to return menu details
            return Response({"menu": MenuSerializer.get_dishes(most_voted_menu)})
        else:
            return Response({"error": "No menu available for today"}, status=404)


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

