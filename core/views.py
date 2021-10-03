from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Patient, Appointment
from .forms import LoginForm, PatientForm, AppointmentForm
from django.contrib.auth import authenticate, login, logout


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "core/index.html")


class UmlView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "core/uml.html")


# ############# View Login/Logout ###############
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("core:index")
        form = LoginForm()
        return render(request, "core/login.html", {"form": form})

    def post(self, request):
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(
                    request, username=cd["username"], password=cd["password"]
                )
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect("core:index")
                    else:
                        messages.success(request, "Usuário ou senha invalidos!")
                else:
                    messages.success(request, "Usuário ou senha invalidos!")
        else:
            form = LoginForm()
        return render(request, "core/login.html", {"form": form})


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("login")


# ############# View Patient ###############
@login_required
def patients_list(request):
    patients = Patient.objects.all()
    page = request.GET.get("page", 1)
    paginator = Paginator(patients, 5)
    try:
        object_patients = paginator.page(page)
    except PageNotAnInteger:
        object_patients = paginator.page(1)
    except EmptyPage:
        object_patients = paginator.page(paginator.num_pages)
    return render(request, "core/patients_list.html", {"patients": object_patients})


@login_required
def patient_create(request):
    print(request.POST)
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:patients")
    else:
        form = PatientForm()
    return render(request, "core/patient_create.html", {"form": form})


@login_required
def patient_detail(request, id):
    patient = get_object_or_404(Patient, pk=id)
    return render(request, "core/patient_detail.html", {"patient": patient})


@login_required
def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return render(request, "core/patient_detail.html", {"patient": patient})
    return render(request, "core/patient_edit.html", {"patient": patient})


@login_required
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, "Cliente excluído com sucesso")
    return redirect("core:patients")


# ############# View Appointment ###############
class AppointmentView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = "core/appointments_list.html"
    queryset = Appointment.objects.all()
    context_object_name = "appointments"
    paginate_by = 5


@login_required
def appointment_create(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:appointments")
        else:
            messages.success(request, "Existe campos inválidos. Corrigir.")
    else:
        form = AppointmentForm()
    return render(request, "core/appointment_create.html", {"form": form})


@login_required
def appointment_update(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    form = AppointmentForm(request.POST or None, instance=appointment)
    print(request.POST)
    if form.is_valid():
        form.save()
        return redirect("core:appointments")
    return render(request, "core/appointment_edit.html", {"form": form})


@login_required
def appointment_detail(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    return render(request, "core/appointment_detail.html", {"appointment": appointment})


@login_required
def appointment_delete(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    appointment.delete()
    messages.success(request, "Consulta excluida com sucesso.")
    return redirect("core:appointments")
