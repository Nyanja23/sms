from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False, db_index=True)

    is_staff_member = models.BooleanField(default=False, db_index=True)

    def __str__(self) -> str:
        return self.username
    
