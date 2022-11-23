import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from cookbook.models import Category, Ingredient


# Graphene will automatically map the Category model's fields onto the CategoryNode.
# This is configured in the CategoryNode's Meta class (as you can see below)
class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = "__all__"
        interfaces = (relay.Node, )


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'notes': ['exact', 'icontains'],
            'category': ['exact'],
            'category__name': ['exact'],
        }
        interfaces = (relay.Node, )

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"
        
class Query(ObjectType):
    category_by_id = relay.Node.Field(CategoryNode)
    filter_categories = DjangoFilterConnectionField(CategoryNode)
    all_categories=graphene.List(CategoryType)

    ingredient_by_id = relay.Node.Field(IngredientNode)
    filter_ingredients = DjangoFilterConnectionField(IngredientNode)
    
    def resolve_all_categories(root, info):
        return Category.objects.all()





class CategoryMutationInsert(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutationInsert(category=category)


class CategoryMutationUpdate(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id, name):
        category = Category.objects.get(pk=id)
        category.name = name
        category.save()
        return CategoryMutationUpdate(category=category)

class CategoryMutationDelete(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    category = graphene.Field(CategoryType)
    message = graphene.String(default_value="Deleted!")

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(pk=id)
        category.delete()
        return CategoryMutationDelete(message="Category deleted!")

class Mutation(ObjectType):
    insert_category = CategoryMutationInsert.Field()
    update_category = CategoryMutationUpdate.Field()
    delete_category = CategoryMutationDelete.Field()
