from django.db import models

STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]

# Choices for task label
LABEL_CHOICES = [
    ('WORK', 'Work'),
    ('GROCERY', 'Grocery'),
    ('STUDY', 'Study'),
    ('OTHER', 'Other'),
]

class Task(models.Model):
    task_text = models.CharField(max_length=255)
    task_description = models.TextField(null=True, blank=True)
    task_status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='PENDING'
    )
    task_label = models.CharField(
        max_length=10,
        choices=LABEL_CHOICES,
        default='WORK'
    )
    due_date = models.DateField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task_text} [{self.get_task_status_display()} - {self.get_task_label_display()}]"
# Create your models here.
