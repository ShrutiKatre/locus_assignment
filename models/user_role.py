class UserRole:
    def __init__(self, user_id=None, role_id=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.user_id = user_id
            self.role_id = role_id

    @staticmethod
    def add_user_role(user_id, role_id, st):
        st.user_role_data.append(UserRole(user_id=user_id, role_id=role_id))

    @staticmethod
    def delete_user_role(user_id, role_id, st):
        for element in st.user_role_data:
            if element.user_id == user_id and element.role_id == role_id:
                st.user_role_data.remove(element)
