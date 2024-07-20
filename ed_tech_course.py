import random
# import tabulate
from ed_tech_enrollment import Enrollment

class Course:
    courses_database = []
    course_name = ""
    id = 0
    enrollemnt = Enrollment()
    
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

    def remove_course(self, course_id, users):
         info = self.find_course_from_course_db(course_id)[0]
         course_data = self.find_course_from_course_db(course_id)[1]
         if info:
            self.courses_database.remove(course_data)
            for user in users:
                user_courses  = user["courses_enrolled"]
                tuple = self.try_course_from_course_db(course_id, user_courses)
                if tuple[0]:
                    self.enrollemnt.delete_course_info_of_learner_st(user["user_id"] , course_id)    
                    return "Course deleted successfully"
            return "Course deleted successfully"
         else:
            if info is False:
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
        print(users)
        filtered_users = []
        for user in users:
            print("User info", user)
            if user["user_type"] == "user_learner":
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
        
    def get_all_instructors_records_with_course_id(self, course_id, users):

        filtered_users = []
        for user in users:
            print("User info", user)
            if user["user_type"] == "user_instructor":
                courses = user["courses_to_be_tought"]
                for course in courses:
                    if str(course_id) == str(course["course_id"]):
                        filtered_users.append(user)
                
        headers = ["Used ID", "User Type", "Name", "Email Id", "Password", "Courses To Be Tought"]

        all_users = []
        for value in filtered_users:
            if value["user_type"] == "user_instructor":
                all_users.append(
                (value["user_id"], value["user_type"], value["name"], value["email_id"], value["password"], str(value["courses_to_be_tought"])))
            
        return headers, all_users
    
    def find_course_from_course_db(self, course_id):
        record_found = False
        cours_info = {}
        for index, course in enumerate(self.courses_database):
            if ((course["course_id"] == course_id)):
                record_found = True
                cours_info = course
                break

        return record_found, cours_info
    
    def try_course_from_course_db(self, course_id, courses):
        record_found = False
        cours_info = {}
        for index, course in enumerate(courses):
            if ((course["course_id"] == course_id)):
                record_found = True
                cours_info = course
                break

        return record_found, cours_info

