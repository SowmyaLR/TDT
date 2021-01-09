from datetime import datetime


class GraphBuilder:
    def __init__(self, data):
        self.data = data
        self.relations = {}
        self.vertex = []
        self.edges = []
        self.now = datetime.now()

    def get_vertex(self):
        return self.vertex

    def get_edges(self):
        return self.edges

    def _construct_properties(self, properties, query):
        properties.pop("TimeCreated", None)
        for key, value in properties.items():
            query = query + f".property('{key}', '{value}')"
        query = query + f".property('TimeCreated', '{self.now}')"
        return query

    def _construct_vertex(self, data):
        properties = data['Property']
        ref_labels = str(data['Label'][1:]).replace("'", '')
        query = f"g.addV('{data['Label'][0]}')" \
                f".property(list, 'ReferenceLabels', '{ref_labels}')"
        query = self._construct_properties(properties, query)
        self.vertex.append(query)

    def _construct_edge(self, data):
        key = data["FromIdObject"] + "::" + data["ToIdObject"]
        if data["DeDuplication"] == "TRUE" and key in self.relations and data["Type"] in self.relations[key]:
            return
        if key in self.relations:
            self.relations[key].append(data["Type"])
        else:
            self.relations[key] = [data["Type"]]
        properties = data['Property']
        query = f"g.V().hasLabel('{data['FromLabel']}').has('IdObject', '{data['FromIdObject']}')" \
                f".has('TimeCreated', '{self.now}')" \
                f".addE('{data['Type']}')" \
                f".to(g.V().hasLabel('{data['ToLabel']}').has('IdObject', '{data['ToIdObject']}'))" \
                f".has('TimeCreated', '{self.now}')"
        query = self._construct_properties(properties, query)
        self.edges.append(query)

    def construct_graph(self):
        for _data in self.data:
            if _data['Kind'] == "node":
                self._construct_vertex(_data)
            else:
                self._construct_edge(_data)
