from graphene_django import DjangoObjectType
from .models import Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question_text")
      #   You can also set the fields attribute to the special value "__all__" to indicate that all fields in the model should be used.
      #   fields = "__all__"
      # Show all fields except those in exclude:
      # exclude = ("question_text",)
