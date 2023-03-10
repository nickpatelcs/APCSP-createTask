#imports CSV module
import csv


def averageTemperatures(tempList, values):
  sum = 0
  index = 0
  #Iterates through each temperature
  if values == 0:
    while index <= tempList.__len__():
      #Adds each temperature to the sum
      sum += tempList[index-1]
      index+=1
    #Sets the average to the sum divided by the length of the temperature list
    average = sum/tempList.__len__()
  else:
    while index <= values:
      #Adds each temperature to the sum
      sum += tempList[index-1]
      index+=1
    #Sets the average to the sum divided by the length of the temperature list
    average = sum/values
  return average

def maxTemperatures(tempList, values):
  #sets the initial max value to the first temperature in the list
  max = tempList[0]
  index = 1
  if values == 0:

    while index < tempList.__len__():
      #if the current temperature is greater than the max, it sets it equal to max
      if tempList[index] > max:
        max = tempList[index]
      index+=1
  else:
    while index < values:
      #if the current temperature is greater than the max, it sets it equal to max
      if tempList[index] > max:
        max = tempList[index]
      index+=1

  return max

#Has user select year
csvFile = 0
while csvFile == 0:
  year = input("What year would you like your data from?")
  #Checks to see if year is between 2000 - 2010
  if int(year) > 2020 or int(year) < 2000:
    print("Invalid year.")
  
  #Sets variable for selecting which CSV file to use. The first file has data from 2000-2009, the second has data from 2010-2020
  if int(year) >= 2010:
    csvFile = 2
  elif int(year) >= 2000:
    csvFile = 1

#Has user select month
correctMonth = 0
while correctMonth == 0:
  month = input("What month would you like your data from? \nEnter in a numerical format.\nIf you want to select January, input: 1\n")
  #Makes sure month is between 1-12
  if int(month) > 12 or int(month) < 1:
    print("Invalid month.")
  else:
    correctMonth = 1



index = 0
tList = []
if csvFile == 1:
  #opens file for temperatures from 2000-2009
  with open('2000-2009.csv', newline = "") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')

    #Runs a loop and iterates through each line in CSV file
    for STATION,NAME,DATE,TAVG,TMAX,TMIN in csv_reader:
      
      #Checks to see if the last 4 digits of the date match with selected year
      if DATE[-4:] == year:

        #Checks to see if the current iteration of the date is a month with a double digit (October - December)
        if DATE[1] != '/':

          #Checks first two digits of month with selected month
          if DATE[:2] == month:

            #Adds the avg temperature for each day to a list 
            tList.append(int(TAVG))

        #Single digit months:
        else:
          #Checks to see if the first digit of the date matches with selected month
          if DATE[:1] == month:
          
            tList.append(int(TMAX))
        index += 1
    csv_file.seek(0)

#temperatures from the dates 2010-2020
if csvFile == 2:
  with open('2010-2020.csv', newline = "") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')


    for STATION,NAME,DATE,TMAX,TAVG,TMIN in csv_reader:
          
      #Checks to see if the last 4 digits of the date match with selected year
      if DATE[-4:] == year:

        #Checks to see if the current iteration of the date is a month with a double digit (October - December)
        if DATE[1] != '/':

          #Checks first two digits of month with selected month
          if DATE[:2] == month:

            #Adds the avg temperature for each day to a list 
            tList.append(int(TMAX))

        #Single digit months:
        else:
          #Checks to see if the first digit of the date matches with selected month
          if DATE[:1] == month:
          
            tList.append(int(TMAX))
        index += 1
    csv_file.seek(0)

#Prints the current list of temperatures
print(tList)
#Calls in the average temperature and max functions and concatenates them
print("The average temperature of your month was " + str(int(averageTemperatures(tList, 0))) + " degrees Fahrenheit. The highest temperature was " + str(maxTemperatures(tList, 0)) + " .")

#Call the max and average function on the current temperatures and save them in variables
firstMax = maxTemperatures(tList, 0)
firstAvg = int(averageTemperatures(tList, 0))

#Prints 3 blank lines
print()
print()
print()

#Repeats date selection process from above, but slightly altered for second iteration
csvFile = 0
while csvFile == 0:
  year = input("You're going to pick another month to compare your current data too\nWhat year would you like to choose the second set of temperatures from?\n")
  if int(year) > 2020 or int(year) < 2000:
    print("Invalid year.")
  if int(year) >= 2010:
    csvFile = 2
  elif int(year) >= 2000:
    csvFile = 1
correctMonth = 0
while correctMonth == 0:
  month = input("What month would you like your data from? \nEnter in a numerical format again.\n")
  if int(month) > 12 or int(month) < 1:
    print("Invalid month.")
  else:
    correctMonth = 1

amount = int(input("\nHow many days of this month do you want data from? "))
tList = []
repeat = 1

index = 0
tList = []
if csvFile == 1:
  #opens file for temperatures from 2000-2009
  with open('2000-2009.csv', newline = "") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')

    #Runs a loop and iterates through each line in CSV file
    for STATION,NAME,DATE,TAVG,TMAX,TMIN in csv_reader:
      
      #Checks to see if the last 4 digits of the date match with selected year
      if DATE[-4:] == year:

        #Checks to see if the current iteration of the date is a month with a double digit (October - December)
        if DATE[1] != '/':

          #Checks first two digits of month with selected month
          if DATE[:2] == month:

            #Adds the avg temperature for each day to a list 
            tList.append(int((TMAX-TMIN)/2))

        #Single digit months:
        else:
          #Checks to see if the first digit of the date matches with selected month
          if DATE[:1] == month:
          
            tList.append(int(TMAX))
        index += 1
    csv_file.seek(0)
if csvFile == 2:
  with open('2010-2020.csv', newline = "") as csv_file:

    csv_reader = csv.reader(csv_file, delimiter = ',')


    for STATION,NAME,DATE,TMAX,TAVG,TMIN in csv_reader:
          
      #Checks to see if the last 4 digits of the date match with selected year
      if DATE[-4:] == year:

        #Checks to see if the current iteration of the date is a month with a double digit (October - December)
        if DATE[1] != '/':

          #Checks first two digits of month with selected month
          if DATE[:2] == month:

            #Adds the avg temperature for each day to a list 
            tList.append(int(TAVG))

        #Single digit months:
        else:
          #Checks to see if the first digit of the date matches with selected month
          if DATE[:1] == month:
          
            tList.append(int(TAVG))
        index += 1
    csv_file.seek(0)

print(tList[:amount])
#Calls in the average temperature and max functions and concatenates them, as well as compares them to the max and average data stored in the variables
print("The average temperature of this month was " + str(int(averageTemperatures(tList, amount))) + " degrees Fahrenheit. This is a change of " + str(abs(int(averageTemperatures(tList, 0) - firstAvg))) + " degrees Fahrenheit from your original month.\n\n" + "The highest temperature was " + str(maxTemperatures(tList, amount)) + " degrees Fahrenheit. This is a change of " + str(abs(int(maxTemperatures(tList, 0) - firstMax))) + " degrees Fahrenheit from your original month.")
repeat =2

    
  
