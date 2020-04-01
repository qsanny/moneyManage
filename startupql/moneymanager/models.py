from django.db import models


# Create your models here.

class Budget(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    montant = models.IntegerField()
    restant = models.IntegerField()
    duree = models.IntegerField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.titre+": "+str(self.montant)

class DepensesBudget(models.Model):
    titre = models.CharField(max_length=101)
    description = models.TextField(null=True)
    montant = models.IntegerField()
    date = models.DateField()
    created_at = models.DateField(auto_now=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

    def __str__(self):
        return "depense "+self.titre+": "+str(self.montant)

class Gains(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    montant = models.IntegerField()
    created_at = models.DateField(auto_now=True)

class Historique(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    created_at = models.DateField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name