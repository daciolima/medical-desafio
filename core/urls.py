from django.urls import path

from .views import IndexView, UmlView, \
    LoginView, LogoutView, \
    patients_list, patient_create, patient_detail, patient_update, patient_delete


app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('uml', UmlView.as_view(), name="uml"),


]


urlpatterns += [
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
]


urlpatterns += [
    path('list/', patients_list, name="patients"),
    path('create', patient_create, name="patient_create"),
    path('detail/<int:id>', patient_detail, name="patient_detail"),
    path('update/<int:id>', patient_update, name="patient_update"),
    path('delete/<int:id>', patient_delete, name="patient_delete"),
]
