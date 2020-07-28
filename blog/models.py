from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #date = models.DateField(default='')

    def __str__(self):
        return self.title

# insted of showing 'blog object 1' or 'blog object 2' we can see the title of the projects in the admin site
