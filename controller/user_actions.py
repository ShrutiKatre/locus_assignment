from controller.user_actions_handler import *


class Switcher(object):
    def __init__(self, storage_object):
        self.s = storage_object

    def user_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add User")
        print("2. Delete User")
        print("3. Get all Users")
        inp = input("Operation:")
        if inp == '1':
            user_name = input("User Name: ")
            user_id = add_user(user_name, self.s)
            print("Added user {} {}".format(user_id, user_name))
        if inp == '2':
            user_id = input("User Id: ")
            remove_user(user_id, self.s)
            print("Deleted user {}".format(user_id))
        if inp == '3':
            print("All users:")
            for user in self.s.user_data.values():
                print(user.__dict__)

    def action_type_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add Action Type")
        print("2. Delete Action Type")
        print("3. Get all Action Types")
        inp = input("Operation:")
        if inp == '1':
            action_type = input("Action Type: ")
            add_action_type(action_type, self.s)
            print("Added action type {}".format(action_type))
        if inp == '2':
            action_type = input("Action Type: ")
            remove_action_type(action_type, self.s)
            print("Deleted action type {}".format(action_type))
        if inp == '3':
            print("All action types:")
            for action in self.s.action_data.values():
                print(action.__dict__)

    def resource_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add Resource")
        print("2. Delete Resource")
        print("3. Get all Resources")
        inp = input("Operation:")
        if inp == '1':
            resource_name = input("Resource Name: ")
            resource_id = add_resource(resource_name, self.s)
            print("Added resource {}  {}".format(resource_id, resource_name))
        if inp == '2':
            resource_id = input("Resource Id: ")
            remove_resource(resource_id, self.s)
            print("Deleted resource {}".format(resource_id))
        if inp == '3':
            print("All resources:")
            for resource in self.s.resource_data.values():
                print(resource.__dict__)

    def role_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add Role")
        print("2. Delete Role")
        print("3. Get all Roles")
        inp = input("Operation:")
        if inp == '1':
            role_name = input("Role Name: ")
            role_id = add_role(role_name, self.s)
            print("Added role {}  {}".format(role_id, role_name))
        if inp == '2':
            role_id = input("Role Id: ")
            remove_role(role_id, self.s)
            print("Deleted role {}".format(role_id))
        if inp == '3':
            print("All roles:")
            for role in self.s.role_data.values():
                print(role.__dict__)

    def entitlement_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add role resource entitlement")
        print("2. Delete role resource entitlement")
        print("3. Get all role resource entitlements")
        inp = input("Operation:")
        if inp == '1':
            role_id, action_type, resource_id = input("Enter role_id, action_type, resource_id: ").split()
            add_role_resource_entitlement(role_id, action_type, resource_id, self.s)
            print("Added role resource entitlement")
        if inp == '2':
            role_id, action_type, resource_id = input("Enter role_id, action_type, resource_id: ").split()
            remove_role_resource_entitlement(role_id, action_type, resource_id, self.s)
            print("Deleted role resource entitlement")
        if inp == '3':
            print("All entitlements:")
            for entitlement in self.s.role_resource_entitlement_data.values():
                print(entitlement.__dict__)

    def user_role_operations(self):
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. Add user to role")
        print("2. Delete user from role")
        print("3. Get all user roles")
        inp = input("Operation:")
        if inp == '1':
            user_id, role_id = input("Enter user_id, role_id: ").split()
            add_user_role(user_id, role_id, self.s)
            print("Added role {} for user {}".format(role_id, user_id))
        if inp == '2':
            user_id, role_id = input("Enter user_id, role_id: ").split()
            remove_user_role(user_id, role_id, self.s)
            print("Removed role {} for user {}".format(role_id, user_id))
        if inp == '3':
            print("All user roles:")
            for user_role in self.s.user_role_data:
                print(user_role.__dict__)

    def check_entitlement(self):
        user_id, action_type, resource_id = input("Enter user_id, action_type, resource_id: ").split()
        print("Access: {}".format(has_access(user_id, action_type, resource_id, self.s)))

    def select_operation(self, inp):
        switcher = {
            '1': self.user_operations,
            '2': self.action_type_operations,
            '3': self.resource_operations,
            '4': self.role_operations,
            '5': self.entitlement_operations,
            '6': self.user_role_operations,
            '7': self.check_entitlement
        }
        func = switcher.get(inp, lambda: "Invalid Operation")
        return func()
