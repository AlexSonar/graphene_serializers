import graphene
from your.schemas import Query as YourQuery
from your.serializers import ReservationComponentMutation

# notice its an objecttype, and i've also added some debug
class Mutation(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name="_debug")

    create_reservation = ReservationComponentMutation.Field()


class Query(YourQuery, graphene.ObjectType):
    pass


class Mutation(Mutation, graphene.ObjectType):
    pass


root_schema = graphene.Schema(query=Query, mutation=Mutation)
