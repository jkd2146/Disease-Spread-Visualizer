import csv

#1.a)
def obtain_dictionary(method):

    #Opening file and setting up datareader
    with open('air_quality.csv', 'r', encoding='utf-8-sig') as file_measurements:
      datareader_measurements = csv.reader(file_measurements)
  
      #Instantiating Dictionaries
      dic_UFH = {}
      dic_date = {}
  
      for row in datareader_measurements: #Going through each row in file
  
          #Populating dicitonaries

          #if key is already in dictionary then append the tuple to the list
          if row[0] in dic_UFH: 
              dic_UFH[row[0]].append((row[0],row[1],row[2],row[3]))
          else:
              #if it isn't then create a new key value pair
              dic_UFH[row[0]] = [(row[0],row[1],row[2],row[3])] 
            
          #if key is already in dictionary then append the tuple to the list
          if row[2] in dic_date:
              dic_date[row[2]].append((row[0],row[1],row[2],row[3]))
          else:
              #if it isn't then create a new key value pair
              dic_date[row[2]] = [(row[0],row[1],row[2],row[3])]
  
    #1.b)
    #Opening file and setting up datareader
    with open('uhf.csv','r', encoding='utf-8-sig') as file_ufh:
      datareader_ufh = csv.reader(file_ufh)
  
      #Instantiating Dictionaries
      dic_zip = {}
      dic_borough = {}
  
      for row in datareader_ufh: #Going through each row in file
  
          #Start at index 3 because thats where the zip codes start in the csv.
          #Go for len(row) because each row has a different amount of columns
        
          for c in range(3,len(row)): 
                                      
              #Populating dicitonaries
            
              #if key is already in dictionary then append the tuple to the list
              if row[c] in dic_zip: 
  
                  dic_zip[row[c]].append(row[2])
              else:
                  #if it isn't then create a new key value pair
                  dic_zip[row[c]] = [row[2]]
                
          #if key is already in dictionary then append the tuple to the list
          if row[0] in dic_borough: 
  
              dic_borough[row[0]].append(row[2])
          else:
              #if it isn't then create a new key value pair
              dic_borough[row[0]] = [row[2]]
            
    #Create a dictionary of all the dictionaries
    dictionaries = {
        1: dic_UFH,
        2: dic_date,
        3: dic_zip,
        4: dic_borough
    }
    #Take parameter Method and return the corresponding dictionary for the search method
    return(dictionaries[method])

#1.c
def search_method():

    #Ask for search Method
    method = int(input("Please input the number associated with the method: " 
                       "\n 1. UFH ID\n 2. Date\n 3. Zip Code\n 4. Borough\n"))

    #Call obtain dictionary and obtain the dictionary
    dic = obtain_dictionary(method)

    #if-elif for the methods of search

    if method == 1: #Search by UFH id

        #Ask for UFH Id
        ans = input("\nPlease input the UFH id: ")
        #Create list with the meausrements associated with that UFH id
        li = dic[ans]
        #Go through list and print out the measurements
        for c in li:
            print(f"{c[2]} UFH {c[0]} {c[1]} {c[3]} mcg/m^3")

    elif method == 2:#Search by Date

        #Ask for Date
        ans = input("\nPlease input the Date: ")
        #Create list with the meausrements associated with that Date
        li = dic[ans]
        #Go through list and print out the measurements
        for c in li:
            print(f"{c[2]} UFH {c[0]} {c[1]} {c[3]} mcg/m^3")

    elif method == 3: #Search by Zip Code

        #Ask for Zip Code
        ans = input("\nPlease input the Zip Code: ")
        #Need to obtain the dictionary with Dates as the keys
        dic2 = obtain_dictionary(1)
        #create a list 'res' and add the val
        res = dic2[dic[ans][0]]

        for c in res:
            print(f"{c[2]} UFH {c[0]} {c[1]} {c[3]} mcg/m^3")

    else: #Seacrh by Borough

        #Ask for Borough
        ans = input("\nPlease input the Borough: ")

        #Obtain list of UFH ids from the borough dictionary
        borough_ufh = dic[ans]

        #Obtain the dictionary with the UFH id as key
        dic2 = obtain_dictionary(1)

        #Instantiate list 'res'
        res = []

        #Go through borough_ufh and access dic2 with each UFH id in borough_ufh 
        #to obtain the meausrments for that borough
        for ufh in borough_ufh:
            res.append(dic2[ufh])

        #The measurements in res are in a 2D array from we need to has a nested for loop
        for c in res:#iterate through main list
            for mes in c:#iterate for each value within the sub list
                print(f"{mes[2]} UFH {mes[0]} {mes[1]} {mes[3]} mcg/m^3")

def main():
  #Call search_method
  search_method()
  #pollution()
  
if __name__ == '__main__':
  main()