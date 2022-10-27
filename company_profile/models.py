from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=35)
    description = models.CharField(max_length=250)
    title_bottom_left = models.CharField(max_length=85)
    info_bottom_left = models.CharField(max_length=250)
    info_bottom_right = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class Service(models.Model):
    service_name = models.CharField(max_length=35)
    title = models.CharField(max_length=35)
    short_info = models.CharField(max_length=35)
    description = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.service_name}'


class Advantage(models.Model):
    advantage1 = models.CharField(max_length=250)
    advantage2 = models.CharField(max_length=250)
    advantage3 = models.CharField(max_length=250)

    def __str__(self):
        return 'Преимущества'


class Message(models.Model):
    # source https://stackoverflow.com/questions/47564905/multiple-validators-for-django-1-11-model-charfield
    def regex_validators(value):
        phone_validators = [MinLengthValidator(12),
                            RegexValidator(regex='^\+7[\d]{10}$')]

        for validator in phone_validators:
            try:
                validator(value)
                continue
            except ValidationError as exc:
                raise exc
        return value

    name = models.CharField(max_length=35, validators=[RegexValidator(regex='^[a-zA-Zа-яА-ЯёЁ]+$')])
    mail = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=12,
                             validators=[regex_validators])
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'
