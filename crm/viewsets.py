from rest_framework import viewsets, authentication, permissions

from .serializers import CustomerSerializer, EventSerializer
from .models import Customer, Event
from .permissions import IsOwnerOrReadOnly


class CustomerList(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]

    permission_classes = [
        permissions.DjangoModelPermissions
    ]

    def get_queryset(self):
        return Customer.objects.all()


class EventList(viewsets.ModelViewSet):
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]

    permission_classes = [
        IsOwnerOrReadOnly
    ]

    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()
