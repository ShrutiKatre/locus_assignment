from utility import uuid_util


class User:
    def __init__(self, user_name=None, user_id=None, first_name=None, last_name=None, phone=None, email_id=None,
                 entitlements=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.user_name = user_name
            self.user_id = user_id
            if first_name is not None:
                self.first_name = first_name
            if last_name is not None:
                self.last_name = last_name
            if phone is not None:
                self.phone = phone
            if first_name is not None:
                self.email_id = email_id
            if entitlements is not None:
                self.entitlements = entitlements

    @staticmethod
    def add_user(user_name, st):
        user_id = uuid_util.get_short_uuid()
        st.user_data[user_id] = User(user_name=user_name, user_id=user_id)
        return user_id

    @staticmethod
    def delete_user(user_id, st):
        del st.user_data[user_id]

