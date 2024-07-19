# menu/urls.py

from django.urls import path
from .views import MenuItemList, MenuItemDetail
from .views import ReservationListCreate

urlpatterns = [
    path('menu-items/', MenuItemList.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemDetail.as_view(), name='menuitem-detail'),
    path('reservations/', ReservationListCreate.as_view(), name='reservation-list-create'),
]
