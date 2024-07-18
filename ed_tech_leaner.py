import random
# import tabulate
from ed_tech_user import User


class Learner(User):
    courses_enrolled = []

    def enroll_for_course(self, courses_enrolled):
        self.courses_enrolled = courses_enrolled
    
    def create_learner_info_with_name_email(self):
        dict_learner = self.create_user_info_dict()
        self.enroll_for_course([])
        dict_learner["courses_enrolled"] = self.courses_enrolled
        return dict_learner

    def add_course_info_to_learner_st(self, user_id, course_name):
        tuple_user = self.find_user_from_learner_db(user_id)
        if tuple_user[0] is True:
            course_id = str(random.randint(100, 500))
            course_info = {"course_name": course_name, "course_id": course_id}
            for index, userInfo in enumerate(self.users_database):
                if userInfo["user_id"] == tuple_user[1]["user_id"]:
                    userInfo["courses_enrolled"].append(course_info)
                    self.users_database[index] = userInfo
                    return f"{course_info} added successfully"
        else:
            return "User does not exist"
        
    def add_course_info_to_learner_profile_st(self, user_id, course_id, course_name):
        tuple_user = self.find_user_from_learner_db(user_id)
        if tuple_user[0] is True:
            course_info = {"course_name": course_name, "course_id": course_id}
            for index, userInfo in enumerate(self.users_database):
                if userInfo["user_id"] == tuple_user[1]["user_id"]:
                    userInfo["courses_enrolled"].append(course_info)
                    self.users_database[index] = userInfo
                    return f"{course_info} added successfully"
        else:
            return "User does not exist"

    def update_course_info_for_user_st(self, user_id, courses):
        record_found = False
        for index, user in enumerate(self.users_database):
            if str(user["user_id"]) == str(user_id):
                dict_user = {"email_id": user["email_id"],  "user_type": user["user_type"], "user_id": user["user_id"], "password": user["password"],
                             "name": user["name"], "courses_enrolled": courses}
                self.users_database[index] = dict_user
                return "Record deleted successfully"

        if record_found:
            return "Record deleted successfully"
        else:
            return f"{user_id} user id does not exists"


    def delete_course_info_of_learner_st(self, user_id, course_id):
        tuple_user = self.find_user_from_learner_db(user_id)
        user_info = tuple_user[1]
        course_found = False
        if tuple_user[0] is True:
            if user_info["courses_enrolled"] is not None:
                courses_array = user_info["courses_enrolled"]               
                for index, course in enumerate(courses_array):
                    if str(course["course_id"]) == str(course_id):
                        course_found = True
                        courses_array.remove(course)
                        return self.update_course_info_for_user_st(user_id, courses_array)

            if course_found:
                return f"Course with course id {course_id} is deleted"
            else:
                return f"Course with course id {course_id} does not exist"
        else:
            "User does not exist"

    def add_user_to_learner_db_st(self):
        userLearner = self.create_learner_info_with_name_email()
        if len(self.users_database) > 0:
            for user in self.users_database:
                if str(userLearner["email_id"]) == str(user["email_id"]):
                    return False
                
        self.users_database.append(userLearner)
        return True
    
    def delete_user_to_learner_db(self, user_id):
        self.print_records_in_tabular_form()
        print("Please copy the user id from above table to which you want to delete")
        record_found = False
        for index, user in enumerate(self.users_database):
            if user["user_id"] == user_id:
                record_found = True
                self.users_database.remove(user)

        if record_found:
            print("Record deleted successfully")
            self.print_records_in_tabular_form()
        else:
            print(f"User with {user_id} does not exists")

    def find_user_from_learner_db(self, user_id):
        record_found = False
        user_info = User()
        for index, user in enumerate(self.users_database):
            if ((user["user_id"] == user_id) and (user["user_type"] == "user_learner")):
                record_found = True
                user_info = user
                break

        if record_found:
            print("Record found successfully")
        else:
            print(f"User with {user_id} does not exists")

        print(user_info)
        return record_found, user_info

    def print_records_in_tabular_form(self):
        headers = ["Used ID", "User Type", "Name", "Email Id", "Password", "Course info"]
        users_objects_array = self.users_database
        # print(users_objects_array)
        all_users = []
        for value in users_objects_array:
            if value["user_type"] == "user_learner":
                all_users.append(
                (value["user_id"], value["user_type"], value["name"], value["email_id"], value["password"], str(value["courses_enrolled"])))

        # table = tabulate.tabulate(all_users, headers, tablefmt = "pretty")
        # print(table)
        return headers, all_users
