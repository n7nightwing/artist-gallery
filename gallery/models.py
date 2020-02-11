from django.db import models

class Artist(models.Model):
    avatar = models.TextField()
    name = models.CharField(max_length=100)
    year_born = models.CharField(max_length=100)
    year_died = models.CharField(max_length=100)
    bio_url = models.TextField()

    def __str__(self):
            return self.name

class Creation(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='creations')
    title = models.CharField(max_length=100, default='no creation title')
    year_completed = models.CharField(max_length=100, default='no year_completed')
    medium = models.CharField(max_length=100, default='no medium') 
    image = models.TextField(null=True)

    def __str__(self):
        return self.title
