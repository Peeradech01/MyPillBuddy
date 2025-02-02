from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"



class Patient(models.Model):
    GENDER_CHOICES = [
        ('ชาย', 'ชาย'),
        ('หญิง', 'หญิง'),
        ('ไม่ระบุ', 'ไม่ระบุ'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField(null=True)
    health_detail = models.TextField()
    chronic_disease = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='patients')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"



class Medication(models.Model):

    TYPE_CHOICES = [
        ('ยาเม็ด', 'ยาเม็ด'),
        ('ยาน้ำ', 'ยาน้ำ'),

    ]

    name = models.CharField(max_length=255)
    drugtype = models.CharField(max_length=100, choices=TYPE_CHOICES, default=None)

    def __str__(self):
        return self.name

class Prescription(models.Model):

    TIME_CHOICES = [
        ('ก่อนอาหาร', 'ก่อนอาหาร'),
        ('หลังอาหาร', 'หลังอาหาร'),
    ]

    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=155)  # ความถี่ในการกิน เช้า เย็น
    duration  = models.CharField(max_length=100, choices=TIME_CHOICES, default=None)
    notes = models.TextField(blank=True)
    start_date = models.DateField(default=None)
    end_date = models.DateField(null=True, blank=True,default=None)


    def __str__(self):
        return f"{self.medication.name} - {self.patient.id}"


class MedicationReminder(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    reminder_time = models.TimeField()
    taken = models.BooleanField(default=False) # กินยายัง

    def __str__(self):
        return f"Reminder for {self.prescription.medication.name} at {self.reminder_time}"

    def is_past_due(self):
        return timezone.now() > self.reminder_time
