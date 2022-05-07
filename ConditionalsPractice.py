

#Python Conditionals

from operator import truediv


language = "dansk"

if language == "dansk":
    print("condition was true")
elif language == "svensk":
    print("no")
else:
    print("condition was false")



raider = "shaman"
main = False

if raider == "shaman" and main:
    print("in Roster")
else:
    print("benched")


#man vender en boolean conditional ved brug af "not" og ikke !
if raider == "shaman" and not main:
    print("in Roster")
else:
    print("benched")