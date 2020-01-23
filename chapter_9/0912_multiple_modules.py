#Gabriel Abraham
#notesonartificialintelligence
#Python Crash Course - Chapter 9

#Store the following classes in seperate modules, then create
#an Admin instance, and call show_privileges() to show that everything is still working correctly.

#Store the classes User, Privilieges and Admin in one module.
from admin import Admin
#This will be the seperate file, make an Admin instance, and call show_privileges()


#Create an instance of Admin, and call your method.

sarah_admin = Admin('James', 'Khan', 37)
sarah_admin.privileges.show_privileges()
sarah_admin.describe_user()