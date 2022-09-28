import json
from collections import namedtuple

import requests
from graphene import Field, List, ObjectType, String, Mutation
import graphql_jwt
import jwt
from django.contrib.auth import get_user_model

url = "https://swapi.dev/api/people/"
headers = {}
data = {}
resp = requests.get(url, headers)
resp = resp.json()


def _json_object_hook(d):
    return namedtuple("X", d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)

"""
User Type
"""
class UserType(ObjectType):
#   class Meta:
#     model = get_user_model()
#     fields = ('id','username', 'password')
    username = String(required=True)

"""
People Type
"""
class PeopleType(ObjectType):

    name = String(description="Persons name")
    height = String(description="Persons height")
    mass = String(description="Persons mass")
    gender = String(description="Persons gender")
    homeworld = String(description="Persons homeworld")


class Query(ObjectType):
    people = List(PeopleType)
    search = Field(PeopleType, name=String(required=True))

    # Resolve all people
    def resolve_people(self, info, search=None, **kwargs):
        # user = info.context.user
        # if user.is_anonymous:
        #     raise Exception("Login is required")
        return resp["results"]
        
    # Resolve person
    def resolve_search(self, info, **args):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Login is required")
        name = args.get("name")
        my_item = next((item for item in resp["results"] if item["name"] == name), None)

        return my_item

class AuthMutation(Mutation):
    token = String()
    class Arguments:
        username = String()

    def mutate(self, info , username):
        user = {"username" : username}

        jwt_token = jwt.encode(user, "secret", algorithm="HS256")
        res = AuthMutation(token = jwt_token.decode("utf-8"))
        return res

class Mutation(ObjectType):
    token_auth = AuthMutation.Field()
