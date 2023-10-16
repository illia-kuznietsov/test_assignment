from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'restaurants', views.RestaurantViewSet)
router.register(r'dishes', views.DishViewSet)
router.register(r'menus', views.MenuViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'votes', views.VoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('current_menu/<str:address>/', views.CurrentDayMenuView.as_view()),
    path('today_results/<str:address>/', views.TodaysMenuResultsView.as_view()),
]