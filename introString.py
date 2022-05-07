

# Dette er en kommentar

#quotation marks kan inkluderes i en string ved at escape dem med en blackslash
my_message = 'New\'s Message'

# ved brug af double Quotation marks ignorere den single quotations og omvendt

print(my_message)

# len() er length function
print(len(my_message))


# Dette tager all values fra array position 4 til 10 (inkluderer ikke position 10)
print(my_message[4:10])

# ved ikke at inkludere en position for end point kører den til slutningen
print(my_message[4:])


#makes sense
print(my_message.lower())

print(my_message.upper())

print(my_message.count('s'))

#returnerer index position i array hvor argument starter.
print(my_message.find('Message'))

# returnerer -1 hvis det ikke ekisterer
print(my_message.find('eksisterer ikke'))


my_message = (my_message.replace('New', 'Old'))

print(my_message)

greeting = "hello"
name = 'Mikael'

print(greeting + ' ' + name)

name = ' john '

#curly brackets fungerer som et variabel placeholder, og kan udfyldes med .format argumenter
my_message = '{} {}'.format(greeting, name)
print(my_message)

# kan også udføres på en anden måde F strings
my_message = F'{greeting} {name}{name}'
print(my_message)

#viser funktioner der er tilgængelige på denne variabeltype.
print(dir(name))

#kan give en forklaring på funktionen
print(help(str.title))
print(my_message.title())

#fjerner start og end spaces
print(name.strip())
