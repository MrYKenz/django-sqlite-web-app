from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name + ": " + self.description


class Image(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=5)
    url = models.CharField(max_length=800)
    description = models.CharField(max_length=100)
    is_fave = models.BooleanField(default=False)

    def __str__(self):
        return self.description
