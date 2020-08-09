from utility import uuid_util


class Resource:
    def __init__(self, resource_id=None, resource_name=None, resource_type=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.resource_id = resource_id
            self.resource_name = resource_name
            if resource_type is not None:
                self.resource_type = resource_type
            else:
                self.resource_type = "DEFAULT"

    @staticmethod
    def add_resource(resource_name, st):
        resource_id = uuid_util.get_short_uuid()
        st.resource_data[resource_id] = Resource(resource_id=resource_id, resource_name=resource_name)
        return resource_id

    @staticmethod
    def delete_resource(resource_id, st):
        del st.resource_data[resource_id]

