from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='Low')
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField()

    def __str__(self):
        return self.title

