from django.db import models
from django.contrib.auth.models import User


class VerificationUserCode(models.Model):
    verify_code = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.verify_code} - {self.is_active}'