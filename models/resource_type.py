class ResourceType:
    def __init__(self, resource_type, description=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.resource_type = resource_type
            if description is not None:
                self.description = description

    @staticmethod
    def add_resource_type(resource_type):
        ResourceType(resource_type)

    @staticmethod
    def delete_resource_type(resource_type):
        del resource_type
