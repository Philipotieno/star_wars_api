import graphene

from starwars.schema import Query as snippets_query

# from starwars.schema import Mutation as mutation


class Query(snippets_query):
    pass


# class Mutation(mutation):
#     pass

schema = graphene.Schema(query=Query)
