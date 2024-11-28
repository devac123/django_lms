from django.db import models
class ContactUs(models.Model):
    name = models.CharField(max_length=100, help_text="Your name")
    email = models.EmailField(max_length=254, help_text="Your email address")
    subject = models.CharField(max_length=255, help_text="Subject of your message")
    message = models.TextField(help_text="Your message")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Time of submission")

    def __str__(self):
        return f"Message from {self.name} ({self.email})"