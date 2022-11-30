from django.db import models

# Create your models here.
class Lead (models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  email = models.EmailField(unique=True, primary_key=True)
  date_time = models.DateTimeField(auto_now_add=True)


class Scan (models.Model):
  url = models.URLField(max_length=150, db_index=True, blank=True)
  ip = models.GenericIPAddressField()
  date_time = models.DateTimeField(auto_now_add=True, primary_key=True)
  is_private = models.BooleanField(default=False)
  client_details = models.ForeignKey(Lead, on_delete=models.DO_NOTHING, null=True)