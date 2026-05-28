class EntityManager:

    def __init__(self):
        #
        # ENTITY COUNTER
        #
        self.next_entity_id = 1
        self.components = {}

    def create_entity(self):
        #
        # GENERATE UNIQUE ENTITY ID
        #
        entity_id = self.next_entity_id
        self.next_entity_id += 1
        return entity_id

    def add_component(self, entity_id, component):
        component_type = type(component)
        if component_type not in self.components:
            self.components[component_type] = {}
        self.components[component_type][entity_id] = component

    def get_component(self, entity_id, component_type):
        component_storage = self.components.get(component_type)
        if not component_storage:
            return None
        return component_storage.get(entity_id)

    def get_components(self, component_type):
        return self.components.get(component_type, {})

    def remove_component(self, entity_id, component_type):
        component_storage = self.components.get(component_type)
        if not component_storage:
            return
        if entity_id in component_storage:
            del component_storage[entity_id]

    def remove_entity(self, entity_id):
        for component_storage in self.components.values():
            if entity_id in component_storage:
                del component_storage[entity_id]

    def entity_exists(self, entity_id):
        for component_storage in self.components.values():
            if entity_id in component_storage:
                return True
        return False
