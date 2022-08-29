motorcycles = ['honda','yamaha','suzuki']
print (motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('harley davidson')
print(motorcycles)

motorcycle = []

motorcycle.append('honda')
motorcycle.append('yamaha')
motorcycle.append('suzuki')
print(motorcycle)
del motorcycle[2]
print(motorcycle)

motorcycle.remove('honda')
print(motorcycle)

popped_motorcycle = motorcycles.pop(0)
print (popped_motorcycle)
print (motorcycles)