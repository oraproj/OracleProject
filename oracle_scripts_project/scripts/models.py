from django.db import models
from django import forms
from django.contrib.auth.models import User

string_connection = models.CharField(max_length=1000)
string_connection.contribute_to_class(User, 'string_connection')
