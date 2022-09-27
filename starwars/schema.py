import json
from collections import namedtuple

import requests
from graphene import Field, List, ObjectType, String

url = "https://swapi.dev/api/people/"
headers = {}
data = {}
resp = requests.get(url, headers)
resp = resp.json()


def _json_object_hook(d):
    return namedtuple("X", d.keys())(*d.values())


def json2obj(data):
    return json.loads(data, object_hook=_json_object_hook)


class PeopleType(ObjectType):

    name = String(description="Persons name")
    height = String(description="Persons height")
    mass = String(description="Persons mass")
    gender = String(description="Persons gender")
    homeworld = String(description="Persons homeworld")


class Query(ObjectType):
    people = List(PeopleType)
    search = Field(PeopleType, name=String(required=True))

    def resolve_people(self, info):
        return resp["results"]

    def resolve_search(self, info, **args):
        name = args.get("name")
        my_item = next((item for item in resp["results"] if item["name"] == name), None)

        return my_item
