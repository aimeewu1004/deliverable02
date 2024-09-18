import csv

with open("athletes/womens_team/Adrienne Stewart21142907.csv", newline='', encoding='utf-8') as file:
   reader = csv.reader(file)
   data = list(reader)


# Extract the data from the CSV
athlete_name = data[0][0]
print(f"athlete name {athlete_name}")

athlete_records_year_1 = data[5][1]
print(f"athlete records year 1 {athlete_records_year_1}")

athlete_records_year_1_time = data[5][3]
print(f"athlete records year 1 time {athlete_records_year_1_time}")

meet_name = data[8][5]
print(f"meet name {meet_name}")

meet_time = data[8][3]
print(f"meet time {meet_time}")


# runner_grade = data[5][2]
# if runner_grade <  
# print(f"runner's grade {runner_grade}")