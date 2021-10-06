from django.db import models
from datetime import datetime

# class AppointmentTodayManager(models.Manager):
#     def get_queryset(self):
#         return (
#             super(AppointmentTodayManager, self)
#             .get_queryset()
#             .filter(status="confirmed")
#         )


class AppointmentTodayManager(models.Manager):
    def get_queryset(self):
        today = datetime.today()
        date_today = datetime(
            today.year,
            today.month,
            today.day,
        )

        return (
            super(AppointmentTodayManager, self).get_queryset().filter(date=date_today)
        )
