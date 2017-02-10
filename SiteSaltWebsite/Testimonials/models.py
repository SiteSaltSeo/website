from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField("Job Title", max_length=140)
    company = models.CharField("Company", max_length=140)
    avatar = models.ImageField("Profile Picture", blank=True, null=True)
    testimonial = models.TextField()

    def __str__(self):
        return self.name

