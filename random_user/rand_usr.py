#!/usr/bin/python3
"""
Random User Generator is an open-source, free API providing developers with \
        randomly generated users to be used as placeholders for testing purposes.\
        - similar to Lorem Ipsum, but is placeholder for people instead of text.
        """

from randomuser import RandomUser
import pandas as pd

#ra = RandomUser()
#users_list = ra.generate_users(10)
# Get the users full name and email addresses
#for user in users_list:
#    print(user.get_full_name(), " ", user.get_email())

# Generate photos of the 10 random users
#for user in users_list:
#    print(user.get_picture())

def get_users():
    users = []
# name, gender city state email dob picture
    for user in RandomUser.generate_users(10):
        users.append({
            'name':user.get_full_name(), 'gender':user.get_gender(), 'city':user.get_city(),
            'state':user.get_state(), 'email':user.get_email(), 'DOB':user.get_dob(), 
            'picture':user.get_picture()})
    return pd.DataFrame(users)

df1 = get_users()
print(df1)

# Now we have a pandas dataframe that can be used any testing that the tester might have.
