import streamlit as st
import pandas as pd
from ed_tech_leaner import Learner
from ed_tech_user import User


def init_session_state():
    if 'users' not in st.session_state:
        st.session_state.users = []


def main():
    init_session_state()
    learner = Learner()
    st.sidebar.title("SL Tech System")
    choice = st.sidebar.radio("Learner Menu", ['Add Learners', 
                                       'Display Leaners', 
                                       'Add course(s) to learner', 
                                       'Remove course from leaner',
                                    #    "*Instructor Module*",
                                    #    "Add Instructor",
                                    #    "Display Instructors",
                                    #    "Add course(s) to Instructor",
                                    #    "Remove course from Instructor",
                                       'Exit'])
    
  
    if choice == "*Instructor Module*":
        st.write("""# In this module we will be managing all the operations for Instructor""")
        st.write("""### 1. Add Instructor""")
        st.write("""### 2. Display all Instructors""")
        st.write("""### 3. Assign course which will be tought by Instructor""")
        st.write("""### 4. Remove any assigned to the Instructor""")

    if choice == "Add Instructor":
        leaner_name = st.text_input("Enter Instructor name:")
        leaner_email_id = st.text_input("Enter Instructor email id:")
       
        if st.button("Add Instructor"):
             learner.create_user_info(leaner_name, leaner_email_id)
             learner.create_learner_info_with_name_email()
             learner.add_user_to_learner_db_st()
             st.session_state.users = learner.users_database
             st.success(f"{leaner_email_id} email id added successfully!")

    if choice == 'Add Learners':
        leaner_name = st.text_input("Enter learner name:")
        leaner_email_id = st.text_input("Enter learner email id:")
       
        if st.button("Add Users"):
             learner.create_user_info(leaner_name, leaner_email_id)
             learner.create_learner_info_with_name_email()
             learner.add_user_to_learner_db_st()
             st.session_state.users = learner.users_database
             st.success(f"{leaner_email_id} email id added successfully!")


    elif choice == 'Display Leaners':
        if st.session_state.users:
            tableHeaders, available_learners_list = learner.print_records_in_tabular_form()      
            headers = ["Used ID", "Name", "Email Id", "Password", "Course info"]
            df_available_cars = pd.DataFrame(available_learners_list, columns=tableHeaders)
            st.write(df_available_cars)
        else:
            st.warning("No learners found. Please add a learner first.")

    elif choice == 'Add course(s) to learner':
        if st.session_state.users:
            st.write("""# Choose user id from this list """)
            tableHeaders, available_learners_list = learner.print_records_in_tabular_form()      
            headers = ["Used ID", "Name", "Email Id", "Password", "Course info"]
            df_available_cars = pd.DataFrame(available_learners_list, columns=tableHeaders)
            st.write(df_available_cars)

            learner_id = st.text_input("Enter user id:")
            course_name = st.text_input("Enter course name:") 

            if st.button("Add course"):
                result = learner.add_course_info_to_learner_st(learner_id, course_name)
                st.success(result)
        else:
            st.warning("No course and leaners found. Please add a learner and a course first.")

    elif choice == 'Remove course from leaner':
        if st.session_state.users:
            st.write("""# Choose user id and course from this list """)
            tableHeaders, available_learners_list = learner.print_records_in_tabular_form()      
            headers = ["Used ID", "Name", "Email Id", "Password", "Course info"]
            df_available_cars = pd.DataFrame(available_learners_list, columns=tableHeaders)
            st.write(df_available_cars)

            learner_id = st.text_input("Enter user id:")
            course_id = st.text_input("Enter course id:") 

            if st.button("Remove course"):
                result = learner.delete_course_info_of_learner_st(learner_id, course_id)
                st.success(result)
        else:
            st.warning("No course and leaners found. Please add a learner and a course first.")


    elif choice == 'Exit':
        learner.clear_users()
        st.success("Clearing all users")
        st.write("Exiting the system. Goodbye!")

if __name__ == "__main__":
    main()
