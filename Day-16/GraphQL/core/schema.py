import graphene
from gql_api.schema import Query as query1
from cookbook.schema_new import Query as query2
from custom_users.schema import Query as user_query
from cookbook.schema_new import Mutation as mutation1
from custom_users.schema import AuthMutation as auth_mutation

class Query(query1, query2,user_query):
    pass


class Mutation(mutation1, auth_mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
