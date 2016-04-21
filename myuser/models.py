from django.db import models

# class MyModel(models.Model):
    # name = models.CharField

MyModel = type("MyModel", (models.Model,), {"name": models.CharField("名前", max_length=128),
                                            "__module__": "myuser.models"})
