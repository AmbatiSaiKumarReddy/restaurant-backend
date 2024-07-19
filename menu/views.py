# menu/views.py

from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from .models import Reservation
from .serializers import ReservationSerializer


class MenuItemList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
