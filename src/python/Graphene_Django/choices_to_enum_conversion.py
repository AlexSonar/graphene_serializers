from django.db import models
from graphene_django import DjangoObjectType

class PetModel(models.Model):
    kind = models.CharField(
        max_length=100,
        choices=(("cat", "Cat"), ("dog", "Dog"))
    )

class Pet(DjangoObjectType):
    class Meta:
        model = PetModel
        fields = ("id", "kind",)
        