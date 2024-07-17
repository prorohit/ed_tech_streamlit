import random
import tabulate
class User:
    users_database = []
    name = ""
    email_id = ""
    password = ""
    id = 0

    def __init__(self):
        pass

    def create_user(self):
        name = input("Enter user name")
        email_id = input("Enter user email id")
        password = input("Enter user password")

        name = "Rohit" + str(random.randint(1, 20))
        email_id = "Rohit@Gmail.com" + str(random.randint(1, 20))
        password = str(random.randint(1000, 9999))

        self.id = random.randint(10000, 50000)
        self.name = name
        self.email_id = email_id
        self.password = password

    def create_user_info(self, name, email_id):
        self.id = str(random.randint(10000, 50000))
        self.name = name
        self.email_id = email_id
        self.password = str(random.randint(100000, 600000))

    def create_user_info_dict(self):
        return {"user_id": self.id, "name": self.name, "email_id": self.email_id, "password": self.password}

    def retrieve_users(self):
        return self.users_database

    def clear_users(self):
        return self.users_database.clear()

    def print_records_in_tabular_form(self):
        headers = ["Used ID", "Name", "Email Id", "Password"]
        users_objects_array = self.retrieve_users()
        all_users = []
        for value in users_objects_array:
            all_users.append((value["user_id"], value["name"], value["email_id"], value["password"]))

        table = tabulate.tabulate(all_users, headers, tablefmt = "pretty")
        print(table)

    def update_email_id(self, email_id, newEmailId):
        """
        :param email_id:
        :param newEmailId:
        """
        record_found = False
        for index, user in enumerate(self.users_database):
            if user["email_id"] == email_id:
                record_found = True
                dict_user = {"email_id": newEmailId, "user_id": user["user_id"], "password": user["password"],
                             "name": user["name"]}
                self.users_database[index] = dict_user

        if record_found:
            print("Record updated successfully")
        else:
            print(f"{email_id} does not exists")

    def update_password(self, email_id, new_pass):
        record_found = False
        for index, user in enumerate(self.users_database):
            if user["email_id"] == email_id:
                record_found = True
                dict_user = {"email_id": user["email_id"], "user_id": user["user_id"], "password": new_pass,
                             "name": user["name"]}
                self.users_database[index] = dict_user

        if record_found:
            print("Record updated successfully")
        else:
            print(f"{email_id} does not exists to update the password")
