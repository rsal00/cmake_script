import os

folder_name = input("Folder Name: ")
choice = input("Which folder? 1)... 2)... ")

if choice == "1":
    # A random folder
    os.chdir() # directory 1
elif choice == "2":
    # Another random folder
    os.chdir() # directory 2
else:
    print("Invalid input!")

# Making the directory/folder with the name inputted
os.mkdir(folder_name)
os.mkdir("{}/src".format(folder_name))

# Creating main.cpp file
file = open("{}/src/main.cpp".format(folder_name), "x")

# Making a default program
cpp_default = "#include <iostream>\n\nint main()\n{\n    return 0;\n}"
file.write(cpp_default)

cmake_file = open("{}/CMakeLists.txt".format(folder_name), "x")
cmake = "cmake_minimum_required(VERSION 3.10)\nproject({})\nadd_executable({} src/main.cpp)\nset(CMAKE_CXX_STANDARD 17)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)".format(folder_name, folder_name)
cmake_file.write(cmake)

os.mkdir("{}/build".format(folder_name))

os.chdir("{}/build".format(folder_name))
cmake_command = "cmake .."
os.system(cmake_command)

make_command = "make"
os.system(make_command)
