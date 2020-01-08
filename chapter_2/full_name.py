# Using variables in Strings.
# F-strings. The F is for format, this is because python formats the string byy replacing the name of the variable with its value


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"

#print(f"Hello, {full_name.title()}")


#One can use the fstring to compost a message, and then assign the entire message to a variable.

message = f"{full_name.title()}!"
print(message)



#Dealing with whitespace, rstrip will permanately remove the whitespace.

favorite_langauge = "python "
favorite_language = favorite_language.rstrip(). # lstrip(), will still whitespace from the left site and the same of rstrip(). strip() will remove all whitespace

print(favorite_language)