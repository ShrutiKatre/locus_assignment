from utility import uuid_util


class Role:
    def __init__(self, role_id=None, role_name=None, description=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.role_id = role_id
            self.role_name = role_name
            if description is not None:
                self.description = description

    @staticmethod
    def add_role(role_name, st):
        role_id = uuid_util.get_short_uuid()
        st.role_data[role_id] = Role(role_name=role_name, role_id=role_id)
        return role_id

    @staticmethod
    def delete_role(role_id, st):
        del st.role_data[role_id]
