import graphene
from graphene_django import DjangoObjectType
import django_filters

from .models import Budget, Gains, Historique, DepensesBudget
from django.db.models import Q

class BudgetNode(DjangoObjectType):
    class Meta:
        model = Budget
        fields = '__all__'
        filter_fields = {
            'titre': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
            'montant':['exact', 'icontains', 'istartswith']}

class DepensesBudgetNode(DjangoObjectType):
    class Meta:
        model = DepensesBudget
        fields = '__all__'
        filter_fields = ['titre','description','montant']

class GainsNode(DjangoObjectType):
    class Meta:
        model = Gains
        fields = '__all__'
        filter_fields = ['titre','description','montant']

class HistoriqueNode(DjangoObjectType):
    class Meta:
        model = Historique
        fields = '__all__'
        filter_fields = ['titre','description']

class Query(graphene.ObjectType):
    budget = graphene.List(BudgetNode, search=graphene.String())
    depense = graphene.Field(DepensesBudgetNode)
    gain = graphene.Field(GainsNode)
    historique = graphene.Field(HistoriqueNode)

    detail_budget = graphene.Field(BudgetNode, id=graphene.ID())
    depenses = graphene.List(DepensesBudgetNode)
    gains = graphene.List(GainsNode)
    historiques = graphene.List(HistoriqueNode)

    def resolve_budget(self, info, search=None):
        if search:
            filte = (
                Q(titre__icontains=search) | 
                    Q(description__icontains=search)
                    )
            return Budget.objects.filter(filte)
        return Budget.objects.all()
    
    def resolve_detail_budget(sefl, info, id):
        budget = Budget.objects.get(pk=id)
        if budget:
            return budget

class CreateBudget(graphene.Mutation):
    budget = graphene.Field(BudgetNode)

    class Arguments:
        titre = graphene.String()
        description = graphene.String()
        montant = graphene.Int()
        duree = graphene.Int()
        restant = graphene.Int()
        update = graphene.Boolean()
        id = graphene.ID()
    
    def mutate(self, info, titre,description, montant, duree, restant, update=False, id=None):
        if not update:
            budget = Budget(titre = titre, description = description, montant = montant, duree = duree, restant = restant)
            budget.save()

            return CreateBudget(budget = budget)
        else:
            if id:
                budget = Budget.objects.get(pk=id)
                if budget:
                    budget.titre = titre
                    budget.description = description
                    budget.montant = montant
                    budget.duree = duree
                    budget.restant = restant
                    budget.save()
                    return CreateBudget(budget = budget)

class CreateDepense(graphene.Mutation):
    depense = graphene.Field(DepensesBudgetNode)

    class Arguments:
        titre = graphene.String()
        description = graphene.String()
        montant = graphene.Int()
        date = graphene.String()
        id_budget = graphene.ID()

        update = graphene.Boolean()
        id = graphene.ID()
    
    def mutate(self, info, titre,description, montant, date, id_budget, update=False, id=None):
        if not update:
            budget = Budget.objects.get(pk=id_budget)
            depense = DepensesBudget(titre = titre, description = description, montant = montant, date = date, budget = budget)
            depense.save()

            return CreateDepense(depense = depense)
        else:
            if id:
                depense = DepensesBudget.objects.get(pk=id)
                if depense:
                    depense.titre = titre
                    depense.description = description
                    depense.montant = montant
                    depense.date = date
                    depense.save()
                    
                    return CreateDepense(depense = depense)

class DeleteBudget(graphene.Mutation):
    budget = graphene.Field(BudgetNode)

    class Arguments:
        id = graphene.ID()
    
    def mutate(self, info, id):
        budget = Budget.objects.get(pk=id)
        if budget:
            budget.delete()

class DeleteDepense(graphene.Mutation):
    depense = graphene.Field(DepensesBudgetNode)

    class Arguments:
        id = graphene.ID()
    
    def mutate(self, info, id):
        depense = DepensesBudget.objects.get(pk=id)
        if depense:
            depense.delete()

class Mutation(graphene.ObjectType):
    createBudget = CreateBudget.Field()
    deleteBudget = DeleteBudget.Field()
    createDepense = CreateDepense.Field()
    deleteDepense = DeleteDepense.Field()

    
