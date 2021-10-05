from rest_framework import serializers

from core.models import Appointment, DoctorUser, Patient


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorUser
        fields = ("first_name",)


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("name",)


class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()
    status = serializers.CharField(source="get_status_display")

    date = serializers.DateField(format="%d/%m/%Y", required=False, read_only=True)
    created_at = serializers.DateTimeField(
        format="%d-%m-%YT%H:%M:%S", required=False, read_only=True
    )

    class Meta:
        model = Appointment
        fields = (
            "title",
            "date",
            "time",
            "description",
            "status",
            "doctor",
            "patient",
            "created_at",
        )
