from django.db import models

from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin
)
import secrets


class VotersManager(BaseUserManager):
    def create_voter(self, email, firstname, lastname, phone, password=None, **extra_data):
        if not email:
            raise ValueError("A valid email-address is required.")
        elif not password:
            raise ValueError("Account cannot be created without a password.")

        new_voters_email = self.normalize_email(email)
        new_voter = self.model(email=new_voters_email, firstname=firstname, lastname=lastname, phone=phone, **extra_data)
        new_voter.set_password(password)

        new_voter.save(using=self._db)
        return new_voter

    def create_superuser(self, email, firstname, lastname, phone, **extra_data):
        extra_data.setdefault("is_active", True)
        extra_data.setdefault("is_staff", True)
        extra_data.setdefault("is_superuser", True)
        extra_data.setdefault("user_type", "AGENT")

        new_superuser = self.create_voter(email, firstname, lastname, phone, **extra_data)
        return new_superuser



class Voters(AbstractBaseUser, PermissionsMixin):
    USER_MODE = [
        ("AGENT", "AGENT"),
        ("VOTER", "VOTER")
    ]
    firstname = models.CharField(max_length=50, help_text="Agent's firstname")
    lastname = models.CharField(max_length=50, help_text="Agent's lastname (Surname)")
    address = models.CharField(max_length=150, help_text="Agent's address (Optional).", null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    user_type = models.CharField(max_length=10, choices=USER_MODE, default="VOTER")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=11)
    polliing_unit_unique_id = models.CharField(max_length=10, unique=True, verbose_name="Polliing-Unit Unique Id")

    password = models.CharField(max_length=180)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["firstname", "lastname", "phone"]
    USERNAME_FIELD = "email"

    objects = VotersManager()

    def __str__(self) -> str:
        return f"{self.firstname} {self.lastname}"
    
    def save(self, *args, **kwargs) -> None:
        if not self.polliing_unit_unique_id:
            polliing_unit_unique_id = secrets.token_hex(3)
            self.polliing_unit_unique_id = polliing_unit_unique_id
        super().save(*args, **kwargs)
        return self.__str__()

    def has_module_perms(self, app_label: str) -> bool:
        return True

    def has_perm(self, obj=None) -> bool:
        return True

    class Meta:
        verbose_name = "Agents (Voters)"
        verbose_name_plural = "Agents (Voters)"
        unique_together = ["firstname", "lastname"]

