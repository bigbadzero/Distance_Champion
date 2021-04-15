# function that converts distances into yards
def ConvertDistance(measurment,distance):
    if measurment == "yd":
        distance = distance* 0.0009144
    elif measurment == "mi":
        distance = distance * 1.609344
    else:
        distance = distance
    return distance

# open file and read lines
distances_file = open("distances.txt","r")
distances = distances_file.readlines()
distances_file.close()

# declare vars
listOfPeople = list()
largestDistance = 0

# get list of people with all distances converted to km
for x in range(len(distances)):
    stringList = distances[x].split()
    Person = {
        "firstName": stringList[0],
        "lastName": stringList[1],
        "distance": ConvertDistance(stringList[3], float(stringList[2]))
    }
    listOfPeople.append(Person)

# get largest distance
for x in range(len(listOfPeople)):
    if(listOfPeople[x]["distance"] > largestDistance):
        largestDistance = listOfPeople[x]["distance"]

# determine winner and write winner name to file
for x in range(len(listOfPeople)):
    if listOfPeople[x]["distance"] == largestDistance:
        winner_file = open("winner.txt","w+")
        winner_file.write(listOfPeople[x]["firstName"] +" " + listOfPeople[x]["lastName"])
        winner_file.close()




