inFile = open("data.txt")
g=open("data_2.txt","a")

from geopy.geocoders import Nominatim

geolocator = Nominatim()
index = 0

for line in inFile:
    split1 = line.split(",")

    location = geolocator.geocode(split1[0] + split1[2])
    index = index +1
    g.write(str(index) + " -> " + str(location.latitude)+ " " + str(location.longitude) + "\n")



inFile.close()
g.close()
