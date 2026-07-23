from django.db import models

class JobApplication(models.Model):
    # Status choices definition
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    # Required fields
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255, blank=True, null=True)
    
    # Optional salary field
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Dropdown status choice with default 'Applied'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Applied')
    
    # Application dates
    application_date = models.DateField()
    deadline = models.DateField(null=True, blank=True)
    
    # Additional notes
    notes = models.TextField(blank=True, null=True)
    
    # Auto timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.position} at {self.company_name}"