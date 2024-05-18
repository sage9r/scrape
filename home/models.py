from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=50)
    publish = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self) -> str:
        return self.name