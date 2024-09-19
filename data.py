import csv

with open("athletes/womens_team/Adrienne Stewart21142907.csv", newline='', encoding='utf-8') as file:
   reader = csv.reader(file)
   data = list(reader)


# Extract the data from the CSV
athlete_name = data[0][0]
print(f"athlete name {athlete_name}")

# how to get their records? some of more records if they did more years 
#how to know which index to stop at?

athlete_records_year_1 = data[5][1]
print(f"athlete records year 1 {athlete_records_year_1}")

athlete_records_year_1_time = data[5][3]
print(f"athlete records year 1 time {athlete_records_year_1_time}")


#would we need to do this for each meet? 
race_name = data[8][5]
print(f"race name {race_name}")

race_place = data[8][1]
print(f"race placement {race_place}")

race_time = data[8][3]
print(f"race time {race_time}")

race_date = data[8][4]
print(f"race date {race_date}")
#the date in the csv has no year so not sure how we can separate the tables/data into years

race_comments = data[8][6]
print(f"race comments {race_comments}")

race_photo = data[8][7]
print(f"race photo {race_photo}")

runner_grade = data[5][2]
print(f"runner's grade {runner_grade}")
# How to get their latest grade?


# for index, row in enumerate(data[5:6]):
#     runner_grade = data[index][2]

    
#how to connect to html? import the python file? then use {variable name}?