from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    STATUS_CHOICES = [
        ("cold", "Cold"),
        ("warm", "Warm"),
        ("hot", "Hot"),
    ]
    lead = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="cold", null=True, blank=True
    )
    related_name = models.CharField(max_length=40, null=True, blank=True)
    linkedin_connection = models.CharField(max_length=50, null=True, blank=True)
    comments = models.TextField(max_length=300, null=True, blank=True)
    first_contact = models.DateTimeField("date of first contact", null=True, blank=True)
    description_contact = models.TextField(max_length=200, null=True, blank=True)
    date_of_last_contact = models.DateTimeField(
        "date of last contact", null=True, blank=True
    )
    description_contact_more = models.TextField(max_length=300, null=True, blank=True)
    follow_up_action = models.CharField(max_length=100, null=True, blank=True)
    date_of_next_contact = models.DateTimeField(
        "date of next contact", null=True, blank=True
    )
    new_business = models.TextField(max_length=500, null=True, blank=True)
    recommendation = models.TextField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Client list"

    def __str__(self):
        return f"{self.company_name}, {self.website}, {self.lead}, {self.email}"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
