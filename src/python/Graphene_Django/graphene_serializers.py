'''
This example shows how to use Graphene Serializers to create a GraphQL schema, 
which includes a Query object with a resolve_all_my_models method 
that will return a list of all MyModel objects. Additionally, 
the example shows how to use the login_required decorator 
to ensure that the method is only accessible to authenticated users.
'''

import graphene
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    all_my_models = graphene.List(MyModelType)

    @login_required
    def resolve_all_my_models(self, info, **kwargs):
        return MyModel.objects.all()

schema = graphene.Schema(query=Query)


