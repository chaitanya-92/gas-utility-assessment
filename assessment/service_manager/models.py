from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class ServiceTicket(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Under Review', 'Under Review'),
        ('Completed', 'Completed'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.CharField(max_length=150)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='New', max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ticket {self.id}: {self.category} ({self.status})"
