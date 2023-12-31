# Generated by Django 4.1.4 on 2023-10-14 17:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)])),
                ('email_id', models.EmailField(max_length=100)),
                ('company_code', models.CharField(blank=True, max_length=5, unique=True, validators=[django.core.validators.RegexValidator('^[A-Z]{2}\\d{2}[EN]$')])),
                ('strength', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('website', models.URLField(blank=True, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='company',
            constraint=models.CheckConstraint(check=models.Q(('strength__gte', 0)), name='strength_gte_0'),
        ),
    ]
