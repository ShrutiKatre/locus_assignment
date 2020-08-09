import sys

from controller.user_actions import Switcher
from controller.storage import Storage


if __name__ == '__main__':
    print("############## Role Based Access Control ##############")
    s = Storage()
    if len(sys.argv) == 2:
        s.create_in_memory_db(sys.argv[1])

    while True:
        print("\n")
        print("        -------------------------------------")
        print("Select an operation to perform:")
        print("1. User Operations")
        print("2. Action Type Operations")
        print("3. Resource Operations")
        print("4. Role Operations")
        print("5. Role Resource Entitlement Operations")
        print("6. User Role Operations")
        print("7. Check user Entitlement for user for action type on resource")
        print("0: To exit")

        inp = input("Operation: ")
        if inp == '0':
            exit()
        switcher = Switcher(s)
        try:
            switcher.select_operation(inp)
        except Exception as e:
            print(str(e))
