import graphene
from graphene_django import DjangoObjectType
from .models import City, Employee, Title

class CityType(DjangoObjectType):
    class Meta:
        model = City

class EmployeeType(DjangoObjectType):
    class Meta:
        model = Employee

class TitleType(DjangoObjectType):
    class Meta:
        model = Title

class Query(graphene.ObjectType):
    all_city = graphene.List(CityType)
    all_title = graphene.List(TitleType)
    all_employee = graphene.List(EmployeeType)

    def resolve_all_city(self, info):
        return City.objects.all()
    
    def resolve_all_title(self, info):
        return Title.objects.all()
    
    def resolve_all_employee(self, info):
        return Employee.objects.all()

class CreateEmployee(graphene.Mutation):
    employee = graphene.Field(EmployeeType)

    class Arguments:
        employee_name = graphene.String()
        employee_city = graphene.String()
        employee_title = graphene.String()

    def mutate(self, info, employee_name, employee_city, employee_title):
        employee = Employee(employee_name = employee_name, employee_city = employee_city, employee_title = employee_title)
        employee.save()

        return EmployeeType(employee = employee)    

class Mutation(graphene.ObjectType):
    created_employee = CreateEmployee.Field()