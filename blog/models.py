from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:400] + "..."
