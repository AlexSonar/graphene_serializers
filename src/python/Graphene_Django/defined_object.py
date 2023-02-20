import graphene
from graphene_django import DjangoObjectType

from .models import Question

class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("id", "question_text")

class Query(graphene.ObjectType):
    questions = graphene.List(QuestionType)
    question_by_id = graphene.Field(QuestionType, id=graphene.String())

    def resolve_questions(root, info, **kwargs):
        # Querying a list
        return Question.objects.all()

    def resolve_question_by_id(root, info, id):
        # Querying a single question
        return Question.objects.get(pk=id)
