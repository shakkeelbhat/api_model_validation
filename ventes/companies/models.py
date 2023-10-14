from django.db import models
from django.core.validators import MinLengthValidator,RegexValidator, MinValueValidator
class Company(models.Model):

    id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=False, null=False, validators=[MinLengthValidator(5)])
    email_id  = models.EmailField(max_length=100)
    company_code = models.CharField(unique=True, blank=True, max_length=5,validators=[RegexValidator(r'^[A-Z]{2}\d{2}[EN]$')])
    strength = models.IntegerField(blank=True, validators=[MinValueValidator(0)])
    website = models.URLField(blank=True,null=True)
    created_time = models.DateTimeField(auto_now_add=True)



    class Meta:
        constraints = [models.CheckConstraint(
            check = models.Q(strength__gte=0),
            name="strength_gte_0"
        ),]