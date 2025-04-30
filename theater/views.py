from datetime import datetime
from django.db.models import F, Count
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from theater.models import Genre, Actor, TheaterHall

from theater.serializers import (
    GenreSerializer,
    ActorSerializer,
    TheaterHallSerializer,
)

class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TheaterHallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = TheaterHall.objects.all()
    serializer_class = TheaterHallSerializer
    # permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

