import json

from models.action_type import ActionType
from models.resource import Resource
from models.role import Role
from models.role_resource_entitlement import RoleResourceEntitlement
from models.user import User
from models.user_role import UserRole


class Storage:

    def __init__(self):
        self.user_data = {}
        self.action_data = {}
        self.role_data = {}
        self.resource_data = {}
        self.role_resource_entitlement_data = {}
        self.user_role_data = []

    def create_in_memory_db(self, input_file):
        with open(input_file, "r") as file:
            data = json.load(file)
        self.load_user_entities(data)
        self.load_action_type_entities(data)
        self.load_resource_entities(data)
        self.load_role_entities(data)
        self.load_role_resource_entitlement_entities(data)
        self.load_user_role_entities(data)

    def load_user_entities(self, data):
        users = {}
        if "users" in data:
            users = data["users"]
        for user in users:
            self.user_data[user["user_id"]] = User(dict=user)

    def load_action_type_entities(self, data):
        actions = {}
        if "actions" in data:
            actions = data["actions"]
        for action in actions:
            self.action_data[action["action_type"]] = ActionType(dict=action)

    def load_role_entities(self, data):
        roles = {}
        if "roles" in data:
            roles = data["roles"]
        for role in roles:
            self.role_data[role["role_id"]] = Role(dict=role)

    def load_resource_entities(self, data):
        resources = {}
        if "resources" in data:
            resources = data["resources"]
        for resource in resources:
            self.resource_data[resource["resource_id"]] = Resource(dict=resource)

    def load_role_resource_entitlement_entities(self, data):
        role_resource_entitlements = {}
        if "role_resource_entitlements" in data:
            role_resource_entitlements = data["role_resource_entitlements"]
        for role_resource_entitlement in role_resource_entitlements:
            entitlement_key = RoleResourceEntitlement.get_entitilement_key(role_resource_entitlement["role_id"],
                                                                           role_resource_entitlement["action_type"],
                                                                           role_resource_entitlement["resource_id"])
            self.role_resource_entitlement_data[entitlement_key] = \
                RoleResourceEntitlement(dict=role_resource_entitlement)

    def load_user_role_entities(self, data):
        user_roles = []
        if "user_roles" in data:
            user_roles = data["user_roles"]
        for user_role in user_roles:
            self.user_role_data.append(UserRole(dict=user_role))
