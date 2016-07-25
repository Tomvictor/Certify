from django.db import models
from django.utils import timezone
# Create your models here.

class Candidate(models.Model):
    FirstName = models.CharField(max_length=60)
    LastName  = models.CharField(max_length=60)
    GenderChoice = (
        ('M','Male'),('F','Female'),('O','Other')
    )
    Gender = models.CharField(max_length=10,choices=GenderChoice)
    DateOfBirth = models.DateField(default=timezone.now())
    Mail = models.EmailField(null=True)
    Phone = models.CharField(max_length=20)
    Organisation = models.CharField(max_length=500)
    Address = models.TextField()
    FromDate = models.DateField()
    ToDate = models.DateField()
    VerificationCode = models.CharField(max_length=180)
    ProfilePicture = models.FileField(upload_to="profile/%Y/%m/")
    Certificate = models.FileField(upload_to="certificate/%Y/%m/")
    def __str__(self):
        return self.FirstName