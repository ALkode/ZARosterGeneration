

# dictionary øvelse
student = {'name': 'John','age':25,'courses':['math', 'art']}


# denne metode returnerer none ved ingen value på sendt key, istedet for error
print(student.get('name'))

student.update({'name': 'Dennis'})
print(student)
student.update({'name': 'jane', 'phone':12345})
print(student)

#deletes key value pair in dictionary, kan også fjernes ved pop function
del student['phone']

#returnerer keys fra dictionary
print(student.keys())
#returnerer values fra dictionary
print(student.values())
#returnerer keys og values fra dictionary
print(student.items())
print(student)