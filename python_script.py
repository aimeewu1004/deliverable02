import csv

# Define your CSV file path
csv_file = "athletes/womens_team/Adrienne Stewart21142907.csv"
athlete_name = ""
athlete_id = ""
athlete_year = ""
season_records = []
races_data = []
image_data = []

# Read the CSV file
with open(csv_file, newline='') as infile:
    reader = csv.reader(infile)
    rows = list(reader)

    # Athlete's name and ID
    athlete_name = rows[0][0]   # First line, first column is the athlete name
    athlete_id = rows[1][0]     # Second line, first column is the athlete ID
    
    # # Finding the last occurrence of "Grade" where it's not empty
    # for row in reversed(rows):
    #     if "Grade" in row:
    #         grade_index = row.index("Grade")
    #         if len(row) > grade_index + 1 and row[grade_index + 1]:  # Ensure it's not empty
    #             athlete_year = row[grade_index + 1]
    #             break
    
#TEST
    for row in rows[5:-1]: #use -1 instead of empty [5:]to avoid index error
        if len(row[2]) > 0: #get from only the rows that have a value for grade not the empty ones
            athlete_year = int(row[2]) #turn into number
     
# TEST



    # Extracting season records
    last_grade_index = None
    for i, row in enumerate(rows):
        if "Grade" in row:
            grade_index = row.index("Grade")
            if len(row) > grade_index + 1 and row[grade_index + 1]:  # Ensure it's not empty
                last_grade_index = i

    if last_grade_index is not None:
        for row in rows[last_grade_index + 1:]:
            if len(row) > grade_index and row[grade_index].isdigit():  # Check if the year is numeric
                season_records.append(row)
            else:
                races_data.append(row)
    else:
        # Handle case where no grade is found
        for row in rows:
            if len(row) > 2 and row[2].strip().isdigit():
                season_records.append(row)
            else:
                races_data.append(row)

    for row in races_data:
        if len(row) > 7 and row[7]:  # Photo column
            image_data.append(row)

# Helper functions to create season records and race sections
def create_season_records(data):
    records = []
    for row in data:
        if len(row) > grade_index:
            year = row[grade_index]
            overall_place = row[1]
            time = row[3]
            records.append((year, overall_place, time))
    return records

def create_race_sections(data):
    race_sections = {}
    for row in data:
        if len(row) <= 4 or not row[4]:
            continue
        # Extract the year from the date column
        date_parts = row[4].split()
        if len(date_parts) >= 3:  # Ensure date has at least a year
            year = date_parts[-1]
        else:
            year = "Unknown Year"
        if year not in race_sections:
            race_sections[year] = []
        # Safely access row columns
        race_sections[year].append(f"<tr><td>{row[5] if len(row) > 5 else ''}</td>"
                                   f"<td>{row[1] if len(row) > 1 else ''}</td>"
                                   f"<td>{row[3] if len(row) > 3 else ''}</td>"
                                   f"<td>{row[4]}</td>"
                                   f"<td>{row[6] if len(row) > 6 else ''}</td></tr>")
    return race_sections

season_records_data = create_season_records(season_records)
race_sections = create_race_sections(races_data)

# Convert season records data to HTML
def records_to_html(records, distance):
    rows = "".join([f"<tr><td>{year}</td><td>{grade}</td><td>{time}</td></tr>" for year, grade, time in records])
    return f"<h4>{distance}</h4><table><thead><tr><th>Year</th><th>Grade</th><th>Record Time</th></tr></thead><tbody>{rows}</tbody></table>"

records_html_5000m = records_to_html(season_records_data, "5000 meters")


# Preparing race sections for HTML
race_sections_html = ""
for year, races in sorted(race_sections.items(), reverse=True):
    race_sections_html += f"<h3>{year}</h3>\n"
    race_sections_html += f"<table>\n<thead>\n<tr><th>Race Name</th><th>Place</th><th>Time</th><th>Date</th><th>Coach Comments</th></tr>\n</thead>\n<tbody>\n"
    race_sections_html += "".join(races)
    race_sections_html += "</tbody>\n</table>\n"

# Preparing the photo gallery for HTML
photo_gallery = "".join([f"<img src='images/{row[5]}/{row[7]}' alt='{row[5]}' class='race-photo'>\n" for row in image_data if len(row) > 7])

# Define the HTML template with placeholders
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{athlete_name} Dashboard</title>
    <link rel="stylesheet" href="css/reset.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="#athlete_profile">Athlete Profile</a></li>
                <li><a href="#athlete_races">Athlete Races</a></li>
                <li><a href="#photo_gallery">Photo Gallery</a></li>
            </ul>
        </nav>
    </header>

    <!-- Top Half -->
    <section id="athlete_profile">
        <div class="left-side">
            <!-- Athlete Profile Info -->
            <div class="athlete-info">
                <img src="images/AthleteImages/{athlete_photo}" alt="{athlete_name}" id="athlete-picture">
                <h1 class="athlete-name">{athlete_name}</h1>
                <p class="athlete-grade">Year: {athlete_grade}</p>
            </div>

            <!-- Athlete's School Info -->
            <div class="school-info">
                <a href="{team_page_link}">
                    <img src="{team_logo_url}" alt="School Logo" id="school-logo">
                    <h4>Ann Arbor Skyline</h4>
                </a>
            </div>

            <!-- Athlete Race Data -->
            <div class="season-records">
                <h3>Season Records</h3>
                
                {records_5000m}
            
            </div>

            <!-- Athlete Rankings/Placement -->
            <div class="rankings">
                <h3>Rankings</h3>
                <h4>5000 meters</h4>
                <ul>
                    <li>Team: {team_rank}</li>
                    <li>Region 4: {region_ranking}</li>
                    <li>Division 1: {division_ranking}</li>
                    <li>Lower Peninsula: {lower_peninsula_ranking}</li>
                    <li>Michigan: {state_ranking}</li>
                    <li>United States: {national_ranking}</li>
                </ul>
            </div>
        </div>

        <div class="right-side">
            <!-- Athlete's Progress Graph -->
            <div id="progress-graph">
                <h3>Runner's Progress Over the Years</h3>
                <canvas id="progressChart" width="400" height="300"></canvas>
            </div>
        </div>
    </section>

    <!-- Middle Section -->
    <section id="athlete_races">
        {race_sections}
    </section>

    <!-- Bottom Half -->
    <section id="photo_gallery">
        <h2>Photo Gallery</h2>
        <div class="gallery">
            <p>Upload and view race photos:</p>
            <form action="/upload-photo" method="post" enctype="multipart/form-data">
                <label for="race-photo">Upload a race photo:</label>
                <input type="file" name="race-photo" id="race-photo">
                <button type="submit">Upload Photo</button>
            </form>

            <div class="photos">
                <h3>Uploaded Photos</h3>
                {photo_gallery}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2024 Cross Country Dashboard</p>
    </footer>

</body>
</html>
"""

# Fill the HTML template with the actual data
html_content = html_template.format(
    athlete_name=athlete_name,
    athlete_photo=image_data[0][7] if image_data else "",
    athlete_grade=athlete_year,
    team_page_link="team_page_link",  # Substitute with the actual team page link
    team_logo_url="team_logo_url",  # Substitute with the actual team logo URL
    records_5000m=records_html_5000m,
    race_sections=race_sections_html,
    photo_gallery=photo_gallery,
    team_rank="team_rank",  # Substitute with actual ranking details
    region_ranking="region_ranking",  # Substitute with actual ranking details
    division_ranking="division_ranking",  # Substitute with actual ranking details
    lower_peninsula_ranking="lower_peninsula_ranking",  # Substitute with actual ranking details
    state_ranking="state_ranking",  # Substitute with actual ranking details
    national_ranking="national_ranking"  # Substitute with actual ranking details
)

# Write the HTML content to a file
output_file = "athlete_dashboard.html"
with open(output_file, "w") as outfile:
    outfile.write(html_content)

print(f"HTML file '{output_file}' has been created.")