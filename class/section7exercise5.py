# Create a program that:
# 1. prompts the user to enter a new member.
# 2. adds that member to members.txt at the end of the existing members.
#
# For example, the user here has entered the member Solomon Right.
# In the above example, Solomon Right will be added to members.txt updating the content of the file to:
# John Smith
# Sen Lakmi
# Sono Octonot
# Solomon Right

document = open('../files/s7e5-members.txt', 'r')
members = document.readlines()
document.close()

members_list = list(members)
print(members_list)
# for index, member in enumerate(members_list):
#     print(members_list[index])

user_input = input("Add a new member: ")
members.append(user_input + "\n")
document = open('../files/s7e5-members.txt', 'w')
document.writelines(members)
document.close()