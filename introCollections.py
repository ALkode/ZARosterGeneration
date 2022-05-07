
courses = ['english', 'danish', 'math', 'pe', 'history', 'physics']

print(courses)
print(len(courses))
# man kan bruge -1 til at vælge det sidste index
print(courses[-1])

print(courses[0:3])


courses.append('art')
print(courses)

courses.insert(0, 'biology')
print(courses)


#you can add 2 collections together by using the extend function

courses_2 = ['archery', 'swimming']

courses.extend(courses_2)

print(courses)


courses.remove('math')
print(courses)

removed_course = courses.pop()
print(courses)
print(removed_course)

courses.reverse()

print(courses)

courses.sort()

#sorterer efter alfabetisk rækkefølge når det er strings
print(courses)


print(max(courses))

for index, item in enumerate(courses):
    print(index, item)
 


courses_str = ', '.join(courses)

print(courses_str)


new_list = courses_str.split(', ')
print(new_list)


# tuples er collections der er noteret med () istedet for brackets. de kan ikke ændres efter første assignment
# sets er noteret med curly brackets, rækkefølgen fra sets er forskellig per execution
# man kan finde overenstemmelser mellem 2 sets ved metoden "intersection() tager et set til sammenligning som parameter
# man kan finde forskelligheder ved metoden "difference()"
#man kan kombinere og fjerne duplicates ved metoden union()







