import csv

arr = []

with open('elements.csv', mode ='r') as file:
   
  # Read File
  csvFile = csv.reader(file)
 
  # Add Contents of File
  for line in csvFile:
        arr.append(line)

top = len(arr)
key = 0
place = 0

for i in range(1, top):
    key = arr[i]
    place = i - 1
    if len(arr[place][0]) < len(key[0]):
        while place >= 0 and len(arr[place][0]) < len(key[0]):
            temp = arr[place + 1]
            arr[place + 1] = arr[place]
            arr[place] = temp
            place = place - 1
        arr[place + 1] = key

with open('elements.txt', mode ='w') as file:

	# Write to File
	file.write(str(arr))
