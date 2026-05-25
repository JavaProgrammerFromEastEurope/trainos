class EntityManager:

    def __init__(self):
        self.next_entity_id = 1
        self.components = {}

    def create_entity(self):
        entity_id = self.next_entity_id
        self.next_entity_id += 1
        return entity_id

    def add_component(self, entity_id, component):
        component_type = type(component)
        if component_type not in self.components:
            self.components[component_type] = {}

        self.components[component_type][entity_id] = component

    def get_components(self, component_type):
        return self.components.get(component_type, {})
