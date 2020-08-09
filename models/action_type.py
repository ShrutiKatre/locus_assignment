class ActionType:
    def __init__(self, action_type=None, description=None, dict=None):
        if dict:
            self.__dict__ = dict
        else:
            self.action_type = action_type
            if description is not None:
                self.description = description

    @staticmethod
    def add_action_type(action_type, st):
        st.action_data[action_type] = ActionType(action_type=action_type)

    @staticmethod
    def delete_action_type(action_type, st):
        del st.action_data[action_type]
