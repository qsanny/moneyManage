import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
import django_filters

from .models import Budget, Gains, Historique, DepensesBudget

class BudgetNode(DjangoObjectType):
    class Meta:
        model = Budget
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'montant':['exact', 'icontains', 'istartswith']}
        interfaces = (graphene.relay.Node, )

class DepensesBudgetNode(DjangoObjectType):
    class Meta:
        model = DepensesBudget
        filter_fields = ['titre','description','montant']
        interfaces = (graphene.relay.Node, )

class GainsNode(DjangoObjectType):
    class Meta:
        model = Gains
        filter_fields = ['titre','description','montant']
        interfaces = (graphene.relay.Node, )

class HistoriqueNode(DjangoObjectType):
    class Meta:
        model = Historique
        filter_fields = ['titre','description']
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    budget = graphene.relay.Node.Field(BudgetNode)
    depense = graphene.relay.Node.Field(DepensesBudgetNode)
    gain = graphene.relay.Node.Field(GainsNode)
    historique = graphene.relay.Node.Field(HistoriqueNode)

    budgets = DjangoFilterConnectionField(BudgetNode)
    depenses = DjangoFilterConnectionField(DepensesBudgetNode)
    gains = DjangoFilterConnectionField(GainsNode)
    historiques = DjangoFilterConnectionField(HistoriqueNode)
