
# Role Based Access Control
The RBAC application controls access for a user based on roles and action types registered in the system. 
This is designed to be a command line application. However design is extensible to support API level implementation.

## Entities
1. User: Class for users
2. Resource: Class for resources.
3. Action Type: Class for action types. Eg: READ, WRITE etc
4. Role: Class for roles. Eg: ADMIN, SUPERADMIN
5. Role Resource Entitlements:\
   Entitlement: Association of action type, resource and role\
   This class contains Role ID, Action Type and Resource ID
6. User Roles:
   Class contains User ID and Role ID, denotes users added in roles\
A detailed class diagram, is present in file [RBAC_ED.png](RBAC_ED.png).


## Setup
$python setup.py install

## Run
### version: python3
```$python main.py seed_file.json```\
Using this command the program will be loaded with seed data. This seed data will help in testing the required functionality on command line interface.\
** seed_file.json - sample data file

(OR)

```$python main.py```


## Assumptions
1. The user is already authenticated once it enters the application.
2. The application is designed for frequent changes in roles, entitlements and users added in roles.
3. The user running the application is superuser, so he can see all the roles and entitlements.
4. The actions provided for entities are create and delete for the sake of simplicity.


## Functionality
1. All the IDs are generated as UUIDs(apart from the data which comes from seed file) for User, Role and Resource
2. For role resource entitlememt, primary key = role_id + "_" + action_type + "_" + resource_id
3. Resource id in entitlement can be * to give permission for all resources
4. Add resource method for User, Role and Resource creates new object with new ID
5. To check a user has permission for particular resource for action type: e.g.\
    select option ```7. Check user Entitlement for user for action type on resource```\
    Enter space separated user_id, action_type, resource_id. ```user_1 DELETE model1```
6. seed_file.json has sample data. 
7. Program can be run with or without seed_file.json. 
8. Without input file, default storage for all classes will be empty.

## Future scope
1. API framework can be added to ease manipulation of the resources.
2. In order to persist data, ORM can be added for database management where RDBMS will be used for storing data.
2. Update API can be added for all entities.
3. As the application grows, Resource Type can be used to group resources. I have added a class for this feature.
4. ###### Another Approach:
   The approach I have used is accurate for an growing application where roles and entitlements are created and changed 
   regularly.\
   If the application is stable where roles and entitlements are rarely changed, following approach can be used.
   1. User will have entitlements column.
   2. Entitlement column will have all the entitlements from roles and its role resource entitlements.
      e.g. entitlements 
      ```json
      [
        {"resource_id": "r1", "action_type": "DELETE"},
        {"resource_id": "r1", "action_type": "CREATE"},
        {"resource_id": "r2", "action_type": "READ"},
        {"resource_id": "r1", "action_type": "WRITE"}
      ]
      ```
                           
   3. This entitlement will be updated, when 
        1. Role resource entitlement associated with user role is updated
        2. User is added to new role
        3. User is deleted from role
   4. The input for checking the entitlement will be checked against the entitlements column from user.
   5. This will reduce calls to get Roles and Entitlements for each check.
