from django.urls import path, include
from rest_framework import routers

from theater.views import (
    GenreViewSet,
    ActorViewSet,
    TheaterHallViewSet, PlayViewSet, PerformanceViewSet, ReservationViewSet,
)

router = routers.DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theater_halls", TheaterHallViewSet)
router.register("play", PlayViewSet)
router.register("performance", PerformanceViewSet)
router.register("Reservation", ReservationViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "theater"