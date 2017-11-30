from django.contrib import admin
from .models import directors,actors,movie_cast,movies,rating,comments

# Register your models here.
admin.site.register(directors)
admin.site.register(rating)
admin.site.register(movies)
admin.site.register(movie_cast)
admin.site.register(actors)
admin.site.register(comments)