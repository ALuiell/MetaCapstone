from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated

def say_hello(request):
    return render(request, 'index.html')
class MenuItemsView(generics.ListCreateAPIView):
   permission_classes = [IsAuthenticated]
   queryset = MenuItem.objects.all()
   serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]