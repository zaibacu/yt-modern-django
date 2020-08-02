from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

COUNTRIES = (
    ("LT", _("Lithuania")),
    ("UK", _("United Kingdom")),
    ("PL", _("Poland"))
)


class Category(models.Model):
    name = models.CharField(max_length=256)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "<Category {}>".format(self.name)


class Customer(models.Model):
    name = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return "<Customer name={}, country={}>".format(self.name, self.country)


class Event(models.Model):
    comment = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "<Event by: {} customer: {} time: {}>".format(self.user, self.customer, self.created)

