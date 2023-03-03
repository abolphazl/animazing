from django.db import models


# class Episode(models.Modle):
#     no = models.CharField(max_length=256)
#     title = models.CharField(max_length=256)
#     image = models.CharField(max_length=256)
#     image_large = models.CharField(max_length=256)
#     plot = models.TextField()
#     published_date = models.CharField(max_length=256)
#     rating_count = models.IntegerField()
#     rating_star = models.FloatField()
#     session = models.ForeignKey('Season', on_delete=models.CASCADE, related_name='episodes')

# class Season(models.Model):
#     name = models.CharField(max_length=256)
#     anime = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='seasons')

# class Anime(models.Model):
#     imdb_id = models.CharField(max_length=256)
#     title = models.CharField(max_length=256)
#     image = models.CharField(max_length=512)
#     plot = models.TextField()
#     rating_count = models.IntegerField()
#     rating_star = models.FloatField()
#     genres = models.CharField(max_length=256)
#     last_update = models.DateTimeField(auto_now_add=True)