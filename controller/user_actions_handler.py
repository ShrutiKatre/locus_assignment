from models.action_type import ActionType
from models.resource import Resource
from models.role import Role
from models.role_resource_entitlement import RoleResourceEntitlement
from models.user import User
from models.user_role import UserRole


def has_access(user_id, action_type, resource_id, storage_object):
    if user_id not in storage_object.user_data or storage_object.user_data[user_id] is None:
        raise Exception("User {} is not registered".format(user_id))
    role_list = []
    if action_type not in storage_object.action_data:
        raise Exception("Action type {} is not registered".format(action_type))
    for user_role in storage_object.user_role_data:
        if user_role.user_id == user_id:
            role_list.append(user_role.role_id)
    entitlememt = False
    for role in role_list:
        # if role is for * then return true
        role_resource_entitlement_star = RoleResourceEntitlement.get_entitilement_key(role, action_type, "*")
        if role_resource_entitlement_star in storage_object.role_resource_entitlement_data and \
                storage_object.role_resource_entitlement_data[role_resource_entitlement_star] is not None:
            entitlememt = True
        role_resource_entitlement_key = RoleResourceEntitlement.get_entitilement_key(role, action_type, resource_id)
        if role_resource_entitlement_key in storage_object.role_resource_entitlement_data and \
                storage_object.role_resource_entitlement_data[role_resource_entitlement_key] is not None:
            entitlememt = True
    return entitlememt


def add_user(user_name, storage_object):
    return User.add_user(user_name, storage_object)


def remove_user(user_id, storage_object):
    if user_id not in storage_object.user_data or storage_object.user_data[user_id] is None:
        raise Exception("User {} is not registered".format(user_id))
    User.delete_user(user_id, storage_object)


def add_action_type(action_type, storage_object):
    if action_type in storage_object.action_data:
        raise Exception("Action type {} is already registered".format(action_type))
    ActionType.add_action_type(action_type, storage_object)


def remove_action_type(action_type, storage_object):
    if action_type not in storage_object.action_data:
        raise Exception("Action type {} is not registered".format(action_type))
    ActionType.delete_action_type(action_type, storage_object)


def add_role(role_name, storage_object):
    return Role.add_role(role_name, storage_object)


def remove_role(role_id, storage_object):
    if role_id not in storage_object.role_data or storage_object.role_data[role_id] is None:
        raise Exception("Role {} is not registered".format(role_id))
    Role.delete_role(role_id, storage_object)


def add_resource(resource_name, storage_object):
    return Resource.add_resource(resource_name, storage_object)


def remove_resource(resource_id, storage_object):
    if resource_id not in storage_object.resource_data or storage_object.resource_data[resource_id] is None:
        raise Exception("Resource {} is not registered".format(resource_id))
    Resource.delete_resource(resource_id, storage_object)


def add_role_resource_entitlement(role_id, action_type, resource_id, storage_object):
    if action_type not in storage_object.action_data:
        raise Exception("Action type {} is not registered".format(action_type))
    if role_id not in storage_object.role_data or storage_object.role_data[role_id] is None:
        raise Exception("Role {} is not registered".format(role_id))
    if resource_id not in storage_object.resource_data or storage_object.resource_data[resource_id] is None:
        raise Exception("Resource {} is not registered".format(resource_id))
    entitlememt_key = RoleResourceEntitlement.get_entitilement_key(role_id, action_type, resource_id)
    if entitlememt_key in storage_object.role_resource_entitlement_data:
        raise Exception("Entitlement for {} and {} for {} is already registered".format(role_id, action_type, resource_id))
    RoleResourceEntitlement.add_role_resource_entitlement(role_id, action_type, resource_id, storage_object)


def remove_role_resource_entitlement(role_id, action_type, resource_id, storage_object):
    entitlememt_key = RoleResourceEntitlement.get_entitilement_key(role_id, action_type, resource_id)
    if entitlememt_key not in storage_object.role_resource_entitlement_data:
        raise Exception("Entitlement for {} and {} for {} is not registered".format(role_id, action_type, resource_id))
    RoleResourceEntitlement.delete_role_resource_entitlement(role_id, action_type, resource_id, storage_object)


def add_user_role(user_id, role_id, storage_object):
    if user_id not in storage_object.user_data or storage_object.user_data[user_id] is None:
        raise Exception("User {} is not registered".format(user_id))
    if role_id not in storage_object.role_data or storage_object.role_data[role_id] is None:
        raise Exception("Role {} is not registered".format(role_id))
    for element in storage_object.user_role_data:
        if element.user_id == user_id and element.role_id == role_id:
            raise Exception("User {} is already added to role {}".format(user_id, role_id))
    UserRole.add_user_role(user_id, role_id, storage_object)


def remove_user_role(user_id, role_id, storage_object):
    if user_id not in storage_object.user_data or storage_object.user_data[user_id] is None:
        raise Exception("User {} is not registered".format(user_id))
    if role_id not in storage_object.role_data or storage_object.role_data[role_id] is None:
        raise Exception("Role {} is not registered".format(role_id))
    UserRole.delete_user_role(user_id, role_id, storage_object)

