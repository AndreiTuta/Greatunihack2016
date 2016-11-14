inFile = open("data.txt")

from geopy.geocoders import Nominatim

geolocator = Nominatim()
index = 0

for line in inFile:
    split1 = line.split(",")

    # if split1[3] != " ":
    #     print (split1[3])
    # location = geolocator.geocode(split1[0] + split1[3])
    # else:
    location = geolocator.geocode(split1[0] + split1[2])
    # pr1int(location.address)
    index = index + 1
    print(index)
    print(location.latitude, location.longitude)

    #
    # location = geolocator.geocode("A579 Derby Street, Street Bolton")
    # print((location.latitude, location.longitude))
    #     # print(location.raw)


inFile.close()
