# -------------- Exceptions ------------------ #

# # FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# my_dict = {"key": "Value"}
# value = my_dict["non_existent_key"]

# # IndexError
# friend_list = ["Harshit", "Pinky", "Raghav"]
# friend = my_list[3]

# # TypeError
# my_number = "450"
# print(my_number + 45)

# -------------- Exception Handling ------------------ #

# try : Something that might cause an exception

# except : Do this if there was an exception

# else : Do this if there were no exception

# finally : Do this no matter what happens

# -------------- Exception Handling Practice ------------------ #

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Write something")
# except KeyError as error_massage:
#     print(f"Key: {error_massage} not found")
# else:
#     print("No error Generated")
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is raised Type error")
#     # file.close()
#     # print("File was closed")

# ------------------ Why we need to raise exceptions -------------- #

# height = float(input("Height: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be greater than 3 meter")
#
# weight = float(input("Weight: "))
#
# bmi = weight / height ** 2
# print(bmi)
