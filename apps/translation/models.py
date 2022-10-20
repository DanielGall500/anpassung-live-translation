from django.db import models

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_admin = models.BooleanField(default=False)

    def get_id(self):
        return self.id

    def get_full_name(self):
        return f"{self.f_name} {self.l_name}"

    def __str__(self):
        return f"{self.get_id()}: {self.get_full_name()}"