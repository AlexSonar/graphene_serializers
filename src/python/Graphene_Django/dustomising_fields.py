from graphene_django import DjangoObjectType
from .models import Question

class QuestionType(DjangoObjectType):

    class Meta:
        model = Question
        fields = ("id", "question_text")

    extra_field = graphene.String()

    def resolve_extra_field(self, info):
        return "hello!"
