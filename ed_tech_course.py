import random
# import tabulate
from ed_tech_leaner import Learner

class Course:
    courses_database = []
    course_name = ""
    id = 0
    learner = Learner()
    def __init__(self):
        pass

    def create_course_info(self, course_name):
        self.id = str(random.randint(100, 999))
        self.course_name = course_name
    
    def create_course_info_dict(self):
        return {"course_id": self.id, "course_name": self.course_name}

    def retrieve_courses(self):
        return self.courses_database

    def clear_courses(self):
        return self.courses_database.clear()
    
    def add_course(self, course_name):
        self.create_course_info(course_name)
        course = self.create_course_info_dict()
        self.courses_database.append(course)

    def remove_course(self, course_id, users = []):
         record_found = False
         for index, course in enumerate(self.courses_database):
            if str(course["course_id"]) == str(course_id):
                record_found = True
                self.courses_database.remove(course)
                for user in users:
                    user_courses  = user["courses_enrolled"]
                    for course in user_courses:
                        if str(course["course_id"] == course_id):
                            self.learner.delete_course_info_of_learner_st(str(user["user_id"] == str(course_id)))
                return "Course deleted successfully"

            if record_found is False:
                return f"No course found with course id{course_id}"

    def print_records_in_tabular_form(self):
        headers = ["Course Id", "Course Name"]
        course_objects_array = self.retrieve_courses()
        all_courses = []
        for value in course_objects_array:
            all_courses.append((value["course_id"], value["course_name"]))

        # table = tabulate.tabulate(all_users, headers, tablefmt = "pretty")
        # print(table)
        return (headers, all_courses)
    

    def get_all_learners_records_with_course_id(self, course_id, users):

        filtered_users = []
        for user in users:
            courses = user["courses_enrolled"]
            for course in courses:
                if str(course_id) == str(course["course_id"]):
                    filtered_users.append(user)
                
        headers = ["Used ID", "User Type", "Name", "Email Id", "Password", "Course info"]

        all_users = []
        for value in filtered_users:
            if value["user_type"] == "user_learner":
                all_users.append(
                (value["user_id"], value["user_type"], value["name"], value["email_id"], value["password"], str(value["courses_enrolled"])))
        return headers, all_users

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
        """

        """
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
