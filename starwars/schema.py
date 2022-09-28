import json
from collections import namedtuple

import requests
from graphene import Field, List, ObjectType, String, Mutation, Int
import graphql_jwt
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

base_url = "https://swapi.dev/api/people/"
headers = {}
data = {}


def _json_object_hook(d):
    return namedtuple("X", d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

"""
User Type
"""
class UserType(DjangoObjectType):
  class Meta:
    model = get_user_model()
    # fields = ('id','username', 'password')
    # username = String(required=True)

class CreateUser(Mutation):
    user = Field(UserType)

    class Arguments:
        username = String(required=True)
        password = String(required=True)

    def mutate(self, info, username, password):
        user = get_user_model()(
            username=username
        )

        user.set_password(password)
        user.save()
        return CreateUser(user=user)
"""
People Type
"""
class PeopleType(ObjectType):

    name = String(description="Persons name")
    height = String(description="Persons height")
    mass = String(description="Persons mass")
    gender = String(description="Persons gender")
    homeworld = String(description="Persons homeworld")
    # page = String(description="Page")


class Query(ObjectType):
    user = Field(UserType, id=Int(required=True))
    self_user = Field(UserType)
    all_user = List(UserType)
    people = List(PeopleType, page=Int())
    search = Field(PeopleType, name=String(required=True))

    # Return all users
    def resolve_all_user(self, info, **kwargs):
        user_qs = get_user_model().objects.all()
        return user_qs

    #Resolve one user
    def resolve_user(self, info, id):
            return get_user_model().objects.get(id=id)


    # Resolve all people
    def resolve_people(self, info, **args):
        page = args.get("page")

        user = info.context.user
        if user.is_anonymous:
            raise Exception("Login is required")

        url = f'{base_url}?page={page}'
        _resp = requests.get(url, headers)
        resp = _resp.json()

        return resp["results"]
        
    # Resolve person
    def resolve_search(self, info, **args):
        name = args.get("name")

        user = info.context.user
        if user.is_anonymous:
            raise Exception("Login is required")

        resp = requests.get(base_url, headers)
        resp = resp.json()

        my_item = next((item for item in resp["results"] if item["name"] == name), None)

        return my_item

class Mutation(ObjectType):
    create_user = CreateUser.Field()
    
    # jwt authentication
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()