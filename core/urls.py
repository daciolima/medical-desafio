from django.urls import path

from .views import (
    IndexView,
    LoginView,
    LogoutView,
    patients_list,
    patient_create,
    patient_detail,
    patient_update,
    patient_delete,
    AppointmentView,
    appointment_create,
    appointment_update,
    appointment_detail,
    appointment_delete,
)


app_name = "core"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]


urlpatterns += [
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]


urlpatterns += [
    path("list/", patients_list, name="patients"),
    path("create", patient_create, name="patient_create"),
    path("detail/<int:id>", patient_detail, name="patient_detail"),
    path("update/<int:id>", patient_update, name="patient_update"),
    path("delete/<int:id>", patient_delete, name="patient_delete"),
]


urlpatterns += [
    path("appointment-list/", AppointmentView.as_view(), name="appointments"),
    path("appointment-create", appointment_create, name="appointment_create"),
    path("appointment-detail/<int:id>", appointment_detail, name="appointment_detail"),
    path("appointment-update/<int:id>", appointment_update, name="appointment_update"),
    path("appointment-delete/<int:id>", appointment_delete, name="appointment_delete"),
]
