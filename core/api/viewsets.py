from rest_framework.viewsets import ModelViewSet
from core.models import Appointment
from .serializers import AppointmentSerializer


class AppointmentViewSet(ModelViewSet):

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
