car_registration = {
    "XVX-512": "Skoda",
    "LSF-865": "Tesla",
    "GHF-784": "Anadol",
    "HSV-541": "Tofas",
    "SFC-963": "VW",
    "SFT-412": "Opel",
    "JFS-538": "Mercedes",
    "JBN-523": "Opel",
    "HVU-745": "Toyota",
    "KFL-412": "Ford",
}

#print(sorted(car_registration))
#print(sorted(car_registration.values()))

# Sorted by license plate
sorted_reg = dict(sorted(car_registration.items(), key = lambda x: x[0].lower()))

for k, v in sorted_reg.items():
    print('{}: {}'.format(k, v))
    
# Sorted by maker
sorted_reg = dict(sorted(car_registration.items(), key = lambda x: x[1].lower()))

for k, v in sorted_reg.items():
    print('{}: {}'.format(k, v))
