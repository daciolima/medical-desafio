from django.db import models


class AppointmentTodayManager(models.Manager):
    def get_queryset(self):
        return (
            super(AppointmentTodayManager, self)
            .get_queryset()
            .filter(status="confirmed")
        )
