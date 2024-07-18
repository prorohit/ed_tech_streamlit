import random
from ed_tech_user import User
from ed_tech_instructor import Instructor
from ed_tech_leaner import Learner
# import tabulate
class Enrollment:

    learner= Learner()
    instructor = Instructor()

    def __init__(self):
        pass

    def add_course_info_to_learner_profile_st(self, user_id, course_id, course_name):
        tuple_user = self.find_learner_from_user_db(user_id)
        if tuple_user[0] is True:
            course_info = {"course_name": course_name, "course_id": course_id}
            for index, userInfo in enumerate(self.learner.users_database):
                if userInfo["user_id"] == tuple_user[1]["user_id"]:
                    userInfo["courses_enrolled"].append(course_info)
                    self.learner.users_database[index] = userInfo
                    return f"{course_name} assigned to {tuple_user[1]["email_id"]} successfully"
        else:
            return "User does not exist"
        
    def delete_course_info_of_learner_st(self, user_id, course_id):
        tuple_user = self.find_learner_from_user_db(user_id)
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

    def update_course_info_for_user_st(self, user_id, courses):
        record_found = False
        for index, user in enumerate(self.learner.users_database):
            if str(user["user_id"]) == str(user_id):
                dict_user = {"email_id": user["email_id"],  "user_type": user["user_type"], "user_id": user["user_id"], "password": user["password"],
                             "name": user["name"], "courses_enrolled": courses}
                self.learner.users_database[index] = dict_user
                return "Record deleted successfully"

        if record_found:
            return "Record deleted successfully"
        else:
            return f"{user_id} user id does not exists"
        
    def add_course_info_to_instructor_st(self, user_id, course_name, course_id):
        tuple_user = self.find_instructor_from_user_db(user_id)
        if tuple_user[0] is True:
            course_info = {"course_name": course_name, "course_id": course_id}
            for index, userInfo in enumerate(self.instructor.users_database):
                if userInfo["user_id"] == tuple_user[1]["user_id"]:
                    userInfo["courses_to_be_tought"].append(course_info)
                    self.instructor.users_database[index] = userInfo
                    return f"{course_info} added successfully"
                    break
        else:
            return "User does not exist"
        
    def find_learner_from_user_db(self, user_id):
        record_found = False
        user_info = User()
        for index, user in enumerate(self.learner.users_database):
            if ((user["user_id"] == user_id) and (user["user_type"] == "user_learner")):
                record_found = True
                user_info = user
                break

        if record_found:
            print("Record found successfully")
        else:
            print(f"User with {user_id} does not exists")
        return record_found, user_info
    
    def find_instructor_from_user_db(self, user_id):
        record_found = False
        user_info = Instructor()
        for index, user in enumerate(self.instructor.users_database):
            if ((user["user_id"] == user_id) and (user["user_type"] == "user_instructor")):
                record_found = True
                user_info = user
                break

        if record_found:
            print("Record found successfully")
        else:
            print(f"User with {user_id} does not exists")
        return record_found, user_info