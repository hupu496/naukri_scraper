from django.db import models

class Candidate(models.Model):
    source = models.CharField(max_length=50, choices=[('naukri', 'Naukri'), ('linkedin', 'LinkedIn')])
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)  # JSON or comma-separated
    skills = models.TextField(blank=True, null=True)
    raw_data = models.JSONField(blank=True, null=True)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name