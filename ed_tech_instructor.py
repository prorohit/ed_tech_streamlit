import random
# import tabulate
from ed_tech_user import User


class Instructor(User):
    courses_to_be_tought = []

    def enroll_for_course(self, courses_to_be_tought):
        self.courses_to_be_tought = courses_to_be_tought
    
    def create_instructor_info_with_name_email(self):
        dict_instrcutor = self.create_user_info_dict()
        self.enroll_for_course([])
        dict_instrcutor["courses_to_be_tought"] = self.courses_to_be_tought
        return dict_instrcutor

    def add_course_info_to_instructor_st(self, user_id, course_name, course_id):
        tuple_user = self.find_user_from_instructor_db(user_id)
        if tuple_user[0] is True:
            course_info = {"course_name": course_name, "course_id": course_id}
            for index, userInfo in enumerate(self.users_database):
                if userInfo["user_id"] == tuple_user[1]["user_id"]:
                    userInfo["courses_to_be_tought"].append(course_info)
                    self.users_database[index] = userInfo
                    return f"{course_info} added successfully"
                    break
        else:
            return "User does not exist"

    def update_course_info_for_user_st(self, user_id, courses):
        record_found = False
        for index, user in enumerate(self.users_database):
            if str(user["user_id"]) == str(user_id):
                dict_user = {"email_id": user["email_id"], "user_id": user["user_id"], "password": user["password"],
                             "user_type": user["user_type"],
                             "name": user["name"], "courses_to_be_tought": courses}
                self.users_database[index] = dict_user
                return "Record deleted successfully"

        if record_found:
            return "Record deleted successfully"
        else:
            return f"{user_id} user id does not exists"

    def delete_course_info_of_instructor_st(self, user_id, course_id):
        tuple_user = self.find_user_from_instructor_db(user_id)
        user_info = tuple_user[1]
        course_found = False
        if tuple_user[0] is True:
            if user_info["courses_to_be_tought"] is not None:
                courses_array = user_info["courses_to_be_tought"]               
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

    def add_user_to_instructor_db_st(self):
        userLearner = self.create_instructor_info_with_name_email()
        self.users_database.append(userLearner)

    # def delete_user_to_learner_db(self, user_id):
    #     self.print_records_in_tabular_form()
    #     print("Please copy the user id from above table to which you want to delete")
    #     record_found = False
    #     for index, user in enumerate(self.users_database):
    #         if user["user_id"] == user_id:
    #             record_found = True
    #             self.users_database.remove(user)

    #     if record_found:
    #         print("Record deleted successfully")
    #         self.print_records_in_tabular_form()
    #     else:
    #         print(f"User with {user_id} does not exists")

    def find_user_from_instructor_db(self, user_id):
        record_found = False
        user_info = Instructor()
        for index, user in enumerate(self.users_database):
            if ((user["user_id"] == user_id) and (user["user_type"] == "user_instructor")):
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
        all_users = []
        for value in users_objects_array:
            print(value)
            if value["user_type"] == "user_instructor":
                all_users.append(
                (value["user_id"], value["user_type"], value["name"], value["email_id"], value["password"], str(value["courses_to_be_tought"])))

        # table = tabulate.tabulate(all_users, headers, tablefmt = "pretty")
        # print(table)
        return headers, all_users
