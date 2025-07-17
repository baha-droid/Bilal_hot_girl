from django.db import models


class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='tours/, blank=True')


    def __str__(self):
        return self.title
