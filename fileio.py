# Name : faith nyambura
# date : 24/02/2026
#program to perform file operation

#create new file
new_file = open("student_data.txt","r+")

# write to new file
new_file.write("student name : faith nyambura, id:75390 , email:ndegwafay8.com")
new_file.close

#read from the file
new_file.write("student name : faith nyambura, id:75390 , email:ndegwafay8.com")
data = new_file.read()

print(data)

new_file.close()

#delete file
# us os module
import os
os.reemove("remove.txt")

#delete folder
os.rmdir("folder")
