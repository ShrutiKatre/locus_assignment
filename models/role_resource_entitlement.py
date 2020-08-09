class RoleResourceEntitlement:
    def __init__(self, role_id=None, action_type=None, resource_id=None, resource_type=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.role_id = role_id
            self.action_type = action_type
            self.resource_id = resource_id
            if resource_type is not None:
                self.resource_type = resource_type

    @staticmethod
    def get_entitilement_key(role_id, action_type, resource_id):
        return role_id + "_" + action_type + "_" + resource_id

    @staticmethod
    def add_role_resource_entitlement(role_id, action_type, resource_id, st):
        entitlement_key = RoleResourceEntitlement.get_entitilement_key(role_id, action_type, resource_id)
        st.role_resource_entitlement_data[entitlement_key] = \
            RoleResourceEntitlement(role_id=role_id, action_type=action_type, resource_id=resource_id)

    @staticmethod
    def delete_role_resource_entitlement(role_id, action_type, resource_id, st):
        entitlement_key = RoleResourceEntitlement.get_entitilement_key(role_id, action_type, resource_id)
        del st.role_resource_entitlement_data[entitlement_key]
