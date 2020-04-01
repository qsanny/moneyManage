import graphene
from graphene_django import DjangoObjectType
import company.schema as cs
import moneymanager.schema as mms

class Query(cs.Query, mms.Query, graphene.ObjectType):
    pass

class Mutation(cs.Mutation,mms.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query = Query,  mutation = Mutation)