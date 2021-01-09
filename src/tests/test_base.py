import unittest

from builder import GraphBuilder
from dao import GremlinSession


class TestTDT(unittest.TestCase):
    def setUp(self):
        self.gs = GremlinSession()

    def test_create_node(self):
        data = [
            {"Kind": "node", "IdUnique": "328b7ed1-296d-42dd-b9d8-992ae55450c8",
             "Label": ["OrganizationEntity", "Tag", "OrganizationMatch", "ObjectiveTag", "Tribes", "MaintenanceScript",
                       "VendorGoogle", "PlatformKnowledgeGraph"], "Type": None, "FromLabel": None, "FromIdObject": None,
             "ToLabel": None, "ToIdObject": None,
             "Property": {
                 "IdObject": "dummy1", "IdMaster": "dummy1", "Name": "laser", "NameLower": "laser"
             }, "DeDuplication": None,
             "IdDatastoreAppend": "TRUE"},
            {"Kind": "node", "IdUnique": "aff64fe5-bc8c-4b11-81e6-90b9b7d8336a",
             "Label": ["Organization", "OrganizationMatch", "ObjectiveTag", "Tribes", "MaintenanceScript",
                       "VendorGoogle", "PlatformKnowledgeGraph"], "Type": None, "FromLabel": None, "FromIdObject": None,
             "ToLabel": None, "ToIdObject": None,
             "Property": {
                 "IdObject": "dummy2", "IdMaster": "dummy2", "NameLower": "dummy2"},
             "DeDuplication": None, "IdDatastoreAppend": "TRUE"}]
        gb = GraphBuilder(data)
        gb.construct_graph()
        self.gs.insert_vertices(gb.get_vertex())

    def test_create_edge(self):
        data = [{"Kind": "relationship", "IdUnique": "b590facb-c9cb-4358-969b-ecbfee3c00a0", "Label": None,
                 "Type": "DUMMY_EDGE", "FromLabel": "Organization", "FromIdObject": "dummy2",
                 "ToLabel": "OrganizationEntity", "ToIdObject": "dummy1",
                 "Property": {"Effort": "FALSE", "TimeLoaded": "2020-05-14T05:45:50.971100Z",
                              "Pair": "(Organization)->(OrganizationEntity)"},
                 "DeDuplication": "TRUE", "IdDatastoreAppend": "TRUE"}]
        gb = GraphBuilder(data)
        gb.construct_graph()
        self.gs.insert_edges(gb.get_edges())

    def test_get_data(self):
        query = "g.V().hasLabel('OrganizationEntity').has('IdObject', 'dummy1')"
        call_back = self.gs.gc.submitAsync(query)
        if call_back.result() is not None:
            print(f"result {call_back.result().one()}")
        else:
            print("No results found")

    def test_delete_nodes(self):
        ids = [{'OrganizationEntity': 'dummy1'}, {'Organization': 'dummy2'}]
        for id in ids:
            key = list(id.keys())[0]
            value = list(id.values())[0]
            query = f"g.V().hasLabel('{key}').has('IdObject', '{value}').drop()"
            call_back = self.gs.gc.submitAsync(query)
            if call_back.result() is not None:
                print(call_back.result().one())
            else:
                print("No results found")
