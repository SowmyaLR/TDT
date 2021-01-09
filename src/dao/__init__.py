from gremlin_python.driver import client, serializer
from decouple import config
import logging

__author__ = "SowmyaLR"


class GremlinSession:
    """
    GremlinSession handles all the db operations.
    """
    def __init__(self):
        self.endpoint = config("ENDPOINT")
        self.db = config("DATABASE")
        self.collection = config("COLLECTION")
        self.pk = config("PRIMARY_KEY")
        self.gc = client.Client(
            message_serializer=serializer.GraphSONSerializersV2d0(),
            url=self.endpoint, traversal_source='g',
            username="/dbs/" + self.db + "/colls/" + self.collection,
            password=self.pk
        )

    def insert_vertices(self, vertices):
        for vertex in vertices:
            callback = self.gc.submitAsync(vertex)
            if callback.result() is not None:
                logging.info("Inserted this vertex:\n{0}".format(callback.result().one()))
            else:
                logging.info("Something went wrong with this query: {0}".format(vertex))

    def insert_edges(self, edges):
        for edge in edges:
            callback = self.gc.submitAsync(edge)
            if callback.result() is not None:
                logging.info("Inserted this edge:\n{0}".format(callback.result().one()))
            else:
                logging.info("Something went wrong with this query:\n{0}".format(edge))
