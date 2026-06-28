from django.db import models
from django.contrib.auth.models import User
import uuid


class Event(models.Model):

    title = models.CharField(max_length=200)

    venue = models.CharField(max_length=200)

    date = models.DateField()

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="events/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    profile_pic = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username


class Registration(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE
    )

    registered_at = models.DateTimeField(
        auto_now_add=True
    )

    # Personal Details

    full_name = models.CharField(max_length=100)

    student_id = models.CharField(max_length=30)

    email = models.EmailField()

    mobile = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    semester = models.CharField(max_length=50)

    # Ticket

    ticket_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )

    ticket_number = models.CharField(
        max_length=20,
        blank=True
    )

    def save(self, *args, **kwargs):

        if not self.ticket_number:
            self.ticket_number = (
                f"TKT-{self.user.id:03d}-{self.event.id:03d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.event.title}"
