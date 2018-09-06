from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200, default=None, blank=True, null=True)
    details = models.TextField(default=None, null=True)

    def __str__(self):
        return self.summary
