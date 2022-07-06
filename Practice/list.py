car = ['honda', 'benz', 'bmw', 'ferrari']
'''
#Reading list data
x = int(input('Enter value:'))
print(car[x].upper())

#Appending list data
car.append('truck')
print(car)

#Insert list data
car.insert(0,'bugatti')
print(car)

#pop operation
car.pop()
print(car)

poped = car.pop(0)
print('My first car is ' + poped.title())
'''
