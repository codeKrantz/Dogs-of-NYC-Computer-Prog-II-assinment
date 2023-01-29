def spayedDogs(fileIn, fileOut):
  fin = open(fileIn, "r")
  fout = open(fileOut, "w")
  header = fin.readline()
  DogBreed = {} #this will contain the breed(the key) and then a list of the numbers
  PercentDict = {}
  PercentList = []
  for line in fin:
    section = line.split(",")
    breed = section[2]
    
    if breed in DogBreed.keys():
      if section[7].lower() == "yes":
        DogBreed[breed][0] += 1
      else:
        DogBreed[breed][1] += 1
    else:
      if section[7].lower == "yes":
        DogBreed[breed] = [0,1,0]
      else:
        DogBreed[breed] = [1,0,0]
  JustBreed = list(DogBreed.keys())
  JustBreed.sort()
  for x in JustBreed:
    number = DogBreed[x]
    Neutered = number[0]
    NonNeutered = number[1]
    total = Neutered+NonNeutered
    PercentNumber = (Neutered/total)*100
    PercentNumber = round(PercentNumber,2)
    number[2] = PercentNumber
    PercentDict[x+","+str(number[0])+","+str(number[1])+","+str(number[2])] = PercentNumber

  PercentList = list(PercentDict.values())
  PercentList.sort(reverse=True)

  fout.write("Breed,Neutered,Non-Neutered, percent\n")

  for p in PercentList:
    for k,v in PercentDict.items():
      if p == v:
        fout.write(k+"\n")
  
spayedDogs("dogs_of_nyc.csv", "results.csv")