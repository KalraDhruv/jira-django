from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Bug(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    
    content = models.TextField()

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Open'
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        # Orders bugs by date_posted in descending order (newest first)
        ordering = ['-date_posted']
        # Sets the plural name for the model in the Django admin
        verbose_name_plural = "Bugs"

    def __str__(self):
        # Human-readable representation of the object
        return f'Bug {self.pk}: {self.title} ({self.status})'