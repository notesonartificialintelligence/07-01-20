#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Store the classes User, Privilieges and Admin in one module.
from admin import Admin, Users, Privileges
#This will be the seperate file, make an Admin instance, and call show_privileges()


#Create an instance of Admin, and call your method.

sarah_admin = Admin('sarah', 'abraham', 37)
sarah_admin.privileges.show_privileges()
sarah_admin.describe_user()

#The line to import has been made redundant, this is due to me rearranging the other files.