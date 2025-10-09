import pickle

with open('vehicledetail.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print("vehicle details -")
print('name:  ' + vehicle['brand'] + '' + vehicle['model'])
print('year: ' + str(vehicle['year']))
print('color: ' + vehicle['color'])

