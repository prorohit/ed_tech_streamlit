import streamlit as st
import pandas as pd
from ed_tech_leaner import Learner
from ad_tech_instructor import Instructor
from ed_tech_user import User
from ed_tech_course import Course


def init_session_state():
    if 'users' not in st.session_state:
        st.session_state.users = []
    if 'courses' not in st.session_state:
        st.session_state.courses = []

def main():
    init_session_state()
    learner = Learner()
    instructor = Instructor()
    course = Course()
    st.sidebar.title("SL Tech System")
    choice = st.sidebar.radio("Learner Menu", ['Add Learners', 
                                       'Display Leaners', 
                                       'Add course(s) to learner', 
                                       'Remove course from learner',
                                       "*Instructor Module*",
                                       "Add Instructor",
                                       "Display Instructors",
                                       "Add course(s) to Instructor",
                                       "Remove course from Instructor",
                                       "*Course Module*",
                                       "Add Course",
                                       "Display all courses",
                                       "Remove course",
                                       "Assign course to a learner",
                                       "Fetch all leaners",
                                       'Exit'])
    

    if choice == "*Course Module*":
        st.write("""# In this module we will be managing all the operations for course management""")
        st.write("""### 1. Add Course""")
        st.write("""### 2. Display all courses""")
        st.write("""### 3. Remove course""")
        st.write("""### 4. Assign course to a learner""")


    if choice == "Add Course":
        course_name = st.text_input("Enter course name:")
        if st.button("Add Course"):
            course.add_course(course_name)
            st.session_state.courses = course.courses_database
            st.success(f"{course_name} added in courses successfully!")
    
    if choice == "Display all courses":
        if st.session_state.courses:
            tableHeaders, available_courses_list = course.print_records_in_tabular_form()      
            df_course_info = pd.DataFrame(available_courses_list, columns=tableHeaders)
            st.write(df_course_info)
        else:
            st.warning("No courses found. Please add a course first.")  

    if choice == "Remove course":
        tableHeaders, available_courses_list = course.print_records_in_tabular_form()     
        table_learnr_Headers, available_learners_list = learner.print_records_in_tabular_form()  
 
        pretty_course_array = []
        for value in available_courses_list:
            str = f"{value[0]} - {value[1]}"
            pretty_course_array.append(str)
        option = st.selectbox("Do you want to remove course?", pretty_course_array, index=None,placeholder="Select course to remove...",)
        if option is not None:
            st.write("You selected:", None if option is None else option)
        
        if st.button("Remove Course"):
            course_delete_id = option.split(" - ")
            st.success(course.remove_course(course_delete_id[0], learner.users_database))
    
    if choice == "Assign course to a learner":
        tableHeaders, available_learners_list = learner.print_records_in_tabular_form()  
        tableHeaders, available_courses_list = course.print_records_in_tabular_form()   

        pretty_course_array = []
        for value in available_courses_list:
            str = f"{value[0]} - {value[1]}"
            pretty_course_array.append(str)

        pretty_learners_array = []
        for value in available_learners_list:
            str = f"{value[0]} - {value[2]}"
            pretty_learners_array.append(str)   

        option_course = st.selectbox("Courses List", pretty_course_array, index=None,placeholder="Select course...",)
        option_learner = st.selectbox("Learner List", pretty_learners_array, index=None,placeholder="Select learner...",)

        if st.button("Assign Course"):
            course_info= option_course.split(" - ")
            learner_info = option_learner.split(" - ")
            st.success(learner.add_course_info_to_learner_profile_st(learner_info[0], course_info[0], course_info[1]))

    if choice == "Fetch all leaners":
        tableHeaders, available_courses_list = course.print_records_in_tabular_form()      
        pretty_course_array = []
        for value in available_courses_list:
            str = f"{value[0]} - {value[1]}"
            pretty_course_array.append(str)
        option = st.selectbox("Fetch users for the below course", pretty_course_array, index=None,placeholder="Select course...",)
        if option is not None:
            st.write("You selected:", None if option is None else option)

        if st.button("Fetch learners"):
            course_info= option.split(" - ")
            tableHeaders, filtered_learners = course.get_all_learners_records_with_course_id(course_info[0], learner.users_database)
            df_learners_info = pd.DataFrame(filtered_learners, columns=tableHeaders)
            st.write(df_learners_info)

            
    if choice == "*Instructor Module*":
        st.write("""# In this module we will be managing all the operations for Instructor""")
        st.write("""### 1. Add Instructor""")
        st.write("""### 2. Display all Instructors""")
        st.write("""### 3. Assign course which will be tought by Instructor""")
        st.write("""### 4. Remove any assigned to the Instructor""")

    if choice == "Add Instructor":
        instructor_name = st.text_input("Enter Instructor name:")
        instructor_email_id = st.text_input("Enter Instructor email id:")
       
        if st.button("Add Instructor"):
             instructor.create_user_info(instructor_name, instructor_email_id, "user_instructor")
             instructor.create_instructor_info_with_name_email()
             instructor.add_user_to_instructor_db_st()
             st.session_state.users = instructor.users_database
             st.success(f"{instructor_email_id} email id added successfully!")
    
    elif choice == 'Display Instructors':
        if st.session_state.users:
            tableHeaders, available_instructors_list = instructor.print_records_in_tabular_form()      
            headers = ["Used ID", "User Type", "Name", "Email Id", "Password", "Course info"]
            df_instructors_info = pd.DataFrame(available_instructors_list, columns=tableHeaders)
            st.write(df_instructors_info)
        else:
            st.warning("No instructors found. Please add a instructor first.")   

    elif choice == 'Add course(s) to Instructor':
        if st.session_state.users:
            st.write("""# Choose user id from this list """)
            tableHeaders, available_instructors_list = instructor.print_records_in_tabular_form()      
            headers = ["Used ID","User Type", "Name", "Email Id", "Password", "Course info"]
            df_instructors_info = pd.DataFrame(available_instructors_list, columns=tableHeaders)
            st.write(df_instructors_info)

            instructor_id = st.text_input("Enter user id:")
            course_name = st.text_input("Enter course name:") 

            if st.button("Assign course"):
                result = instructor.add_course_info_to_instructor_st(instructor_id, course_name)
                st.success(result)
        else:
            st.warning("No course and instructors found. Please add a instructor and a course first.")        

    elif choice == 'Remove course from Instructor':
        if st.session_state.users:
            st.write("""# Choose user id and course from this list """)
            tableHeaders, available_instructors_list = instructor.print_records_in_tabular_form()      
            headers = ["Used ID","User Type", "Name", "Email Id", "Password", "Course info"]
            df_instructors_info = pd.DataFrame(available_instructors_list, columns=tableHeaders)
            st.write(df_instructors_info)

            instructor_id = st.text_input("Enter user id:")
            course_id = st.text_input("Enter course id:") 

            if st.button("Remove course from Instructor"):
                result = instructor.delete_course_info_of_instructor_st(instructor_id, course_id)
                st.success(result)
        else:
            st.warning("No courses and instructors found. Please add a instructor and a course first.")
    #
        #Leaerner's Module start
    #
    if choice == 'Add Learners':
        leaner_name = st.text_input("Enter learner name:")
        leaner_email_id = st.text_input("Enter learner email id:")
       
        if st.button("Add Learner"):
             learner.create_user_info(leaner_name, leaner_email_id)
             learner.create_learner_info_with_name_email()
             status = learner.add_user_to_learner_db_st()
             if status is True:
                 st.session_state.users = learner.users_database
                 st.success(f"{leaner_email_id} email id added successfully!")
             else:
                st.error(f"{leaner_email_id} email id already exists!")
             
    elif choice == 'Display Leaners':
        if st.session_state.users:
            tableHeaders, available_learners_list = learner.print_records_in_tabular_form()      
            headers = ["Used ID", "User Type" "Name", "Email Id", "Password", "Course info"]
            df_available_cars = pd.DataFrame(available_learners_list, columns=tableHeaders)
            st.write(df_available_cars)
        else:
            st.warning("No learners found. Please add a learner first.")

    elif choice == 'Add course(s) to learner':
        if st.session_state.users and st.session_state.courses:
            
            table_learnr_Headers, available_learners_list = learner.print_records_in_tabular_form()  
            table_course_Headers, available_courses_list = course.print_records_in_tabular_form()   

            pretty_course_array = []
            for value in available_courses_list:
                str = f"{value[0]} - {value[1]}"
                pretty_course_array.append(str)

            pretty_learners_array = []
            for value in available_learners_list:
                str = f"{value[0]} - {value[2]}"
                pretty_learners_array.append(str)   

            option_course = st.selectbox("Courses List", pretty_course_array, index=None,placeholder="Select course...",)
            option_learner = st.selectbox("Learner List", pretty_learners_array, index=None,placeholder="Select learner...",)

            if st.button("Assign Course"):
                course_info= option_course.split(" - ")
                learner_info = option_learner.split(" - ")
                learner.add_course_info_to_learner_profile_st(learner_info[0], course_info[0], course_info[1])
        else:
            st.warning("No course and instructors found. Please add a instructor and a course first.")

    elif choice == 'Remove course from learner':
        if st.session_state.users and st.session_state.courses:
          
            table_learnr_Headers, available_learners_list = learner.print_records_in_tabular_form()  
            table_course_Headers, available_courses_list = course.print_records_in_tabular_form()   

            pretty_course_array = []
            for value in available_courses_list:
                str = f"{value[0]} - {value[1]}"
                pretty_course_array.append(str)

            pretty_learners_array = []
            for value in available_learners_list:
                str = f"{value[0]} - {value[2]}"
                pretty_learners_array.append(str)   

            option_course = st.selectbox("Courses List", pretty_course_array, index=None,placeholder="Select course...",)
            option_learner = st.selectbox("Learner List", pretty_learners_array, index=None,placeholder="Select learner...",)

            if st.button("Remove course"):
                course_info= option_course.split(" - ")
                learner_info = option_learner.split(" - ")
                result = learner.delete_course_info_of_learner_st(learner_info[0], course_info[0])
                st.success(result)
        else:
            st.warning("No course and leaners found. Please add a learner and a course first.")


    elif choice == 'Exit':
        learner.clear_users()
        st.success("Clearing all users")
        st.write("Exiting the system. Goodbye!")

if __name__ == "__main__":
    main()
