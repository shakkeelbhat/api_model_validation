from django.db import models

class Company(models.Model):

    id = models.BigAutoField(primary_key=True)
    