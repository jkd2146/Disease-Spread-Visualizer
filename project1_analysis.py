import csv
from project1 import obtain_dictionary


# Function to find the highest and lowest pollution measurements in zip code 10027
def find_highest_lowest_10027(dictionaries):
  zip_ufh = dictionaries['10027']
  ufh_dic = obtain_dictionary(1)

  pollution_data = ufh_dic[zip_ufh[0]]

  min_val,max_val = 100.0,-100.0 #Instantiate min/max values
  for data in pollution_data: #Iterate through the 10027 pollution data
    temp = data[3] #set temp to pollution value
    min_val = min(float(temp),min_val)  # Finding lowest pollution in 10027
    max_val = max(float(temp),max_val)  # Finding highest pollutiom in 10027

  return max_val, min_val

# Function to find the UHF ID with the worst pollution in 2019
def find_worst_pollution_2019(dictionaries):
  #Instantiate
  temp = -100.0
  worst_ufh19 = ""
  pollution_data = dictionaries
  
  for ufh in pollution_data:#Iterate through each UFH id list in dic
    for data in pollution_data[ufh]: #Iterate through each pollution data for each UFH id
      if (float(data[3]) > temp) and data[2][len(data[2])-2:] == "19" : #If pollution value is greater than temp and ends with 2019
        temp = float(data[3])#Set temp to pollution data
        worst_ufh19 = ufh #Set to UFH w/ worst pollution data
  return worst_ufh19

# Function to find the average air pollution in Manhattan in 2008 and 2019
def find_average_air_pollution_in_manhattan(ufh,borough):
  borough_data = borough["Manhattan"]#Get UFH IDs of Manhattan borough
  pollution_data = []
  for id in borough_data:#Iterate through each UFH ID in Manhattan
    pollution_data.append(ufh[id])#append the data to pollution_data
    
  #Instantiate 
  data08 = []
  data19 = []

  
  for ufh in pollution_data:#Iterate through each UFH ID in Manhattan
    for data in ufh:#Iterate through each pollution data for each UFH ID
      if data[2][len(data[2])-2:] == "08":#If date ends in 08
        data08.append(float(data[3]))#add data to data08
      if data[2][len(data[2])-2:] == "19":#If date ends in 19
        data19.append(float(data[3]))#add data to data19

  #AVG Data
  avg08 = sum(data08)/len(data08)
  avg19 = sum(data19)/len(data19)

  return avg08, avg19

# Additional Questions

# Function to find the UHF ID with the worst pollution in 2013
def find_worst_pollution_2013(dictionaries):
  #Instantiate
  temp = -100.0
  worst_ufh13 = ""
  pollution_data = dictionaries

  
  for ufh in pollution_data:#Iterate through each UFH id list in dic
    for data in pollution_data[ufh]: #Iterate through each pollution data for each UFH id
      if (float(data[3]) > temp) and data[2][len(data[2])-2:] == "13" :#If pollution value is greater than temp and ends with 2013
        temp = float(data[3]) #Set temp to pollution data
        worst_ufh13 = ufh  #Set to UFH w/ worst pollution data
  return worst_ufh13

# Function to find the highest and lowest pollution measurements in zip code 11239
def find_highest_lowest_11239(dictionaries):
  #Instantiate dictionaries and min/max
  zip_ufh = dictionaries['11239']
  ufh_dic = obtain_dictionary(1)
  pollution_data = ufh_dic[zip_ufh[0]]
  min_val,max_val = 100.0,-100.0

  
  for data in pollution_data:#Iterate through each data in pollution_data
    temp = data[3]
    min_val = min(float(temp),min_val)
    max_val = max(float(temp),max_val)

  return max_val, min_val
   
def main():
    # a) What was the highest and lowest pollution measurement ever recorded in zip code 10027?
    highest, lowest = find_highest_lowest_10027(obtain_dictionary(3))
    if highest and lowest:
        print("a) Highest pollution in 10027:", highest, "mcg/m^3")
        print("   Lowest pollution in 10027:", lowest, "mcg/m^3")
    else:
        print("a) No pollution data found for zip code 10027.")

    # b) Which UHF ID had the worst pollution in 2019?
    worst_uhf_id = find_worst_pollution_2019(obtain_dictionary(1))
    print("b) UHF ID with the worst pollution in 2019:", worst_uhf_id)

    # c) What was the average air pollution in Manhattan in 2008 and in 2019?
    avg_2008, avg_2019 = find_average_air_pollution_in_manhattan(obtain_dictionary(1),obtain_dictionary(4))
    print("c) Average air pollution in Manhattan in 2008:", avg_2008, "mcg/m^3")
    print("   Average air pollution in Manhattan in 2019:", avg_2019, "mcg/m^3")
    
    # Additional
        #1 Which UHF ID had the worst air pollution in 2019
    worst_uhf_id13 = find_worst_pollution_2013(obtain_dictionary(1))
    print("Additional #1: UHF ID with the worst pollution in 2013:", worst_uhf_id13)
        #2 What was the highest and lowest pollution in zip code 11239?
    highest, lowest = find_highest_lowest_11239(obtain_dictionary(3))
    if highest and lowest:
        print("  Highest pollution in 11239:", highest, "mcg/m^3")
        print("  Lowest pollution in 11239:", lowest, "mcg/m^3")
    else:
        print("a) No pollution data found for zip code 11239.")
    
if __name__ == '__main__':
    main()