from django.db import models

# Create your models here.
class post (models.Model):
    Title = models.CharField (max_length=200)
    Text = models.TextField(_(""))
    Author = auth.get_user_model()
    created_date = models.DateTimeField()
    Published_date= models.DateField