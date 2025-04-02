import uuid
import psycopg2
from datetime import datetime
from psycopg2.extras import RealDictCursor

# All the arrays ware genereted from a screenshot by ai. thats why its in this shape

# Database connection parameters - replace with your actual credentials
conn = psycopg2.connect(
    host="",
    database="",
    user="",
    password=""
)
conn.autocommit = True
cursor = conn.cursor(cursor_factory=RealDictCursor)

# Event ID to link matches with
EVENT_ID = "c97a9ac5-1e41-432e-af3c-54c56e8fe5ed"

# Team data with images and sport type
team_data = [
    ('Česko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/cz.svg', 'hokej'),
    ('Kanada Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/ca.svg', 'hokej'),
    ('USA Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/us.svg', 'hokej'),
    ('Finsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/fi.svg', 'hokej'),
    ('Švýcarsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/ch.svg', 'hokej'),
    ('Německo Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/de.svg', 'hokej'),
    ('Švédsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/se.svg', 'hokej'),
    ('Japonsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/jp.svg', 'hokej'),
    ('Norsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/no.svg', 'hokej'),
    ('Maďarsko Ž', 'https://raw.githubusercontent.com/lipis/flag-icons/260c91531be024944c6514130c5defb2ebb02b7d/flags/4x3/hu.svg', 'hokej')
]

# Insert teams and store their IDs
team_ids = {}
for team_name, img_url, sport in team_data:
    team_id = str(uuid.uuid4())
    team_ids[team_name] = team_id

    # Insert into teams table
    cursor.execute(
        """
        INSERT INTO tipovacka_teams (id, name, "imgURL", sport) 
        VALUES (%s, %s, %s, %s)
        """,
        (team_id, team_name, img_url, sport)
    )

    # Connect team to event
    cursor.execute(
        """
        INSERT INTO tipovacka_teams_to_events ("team_id", "event_id") 
        VALUES (%s, %s)
        """,
        (team_id, EVENT_ID)
    )

# Match data from the schedule
match_data = [

]

# Insert matches
for date_str, time_str, team_1, team_2 in match_data:
    match_id = str(uuid.uuid4())

    # Parse date and time
    datetime_str = f"{date_str} {time_str}"
    match_datetime = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")

    # Get team IDs or set to NULL for playoff matches
    team_1_id = team_ids.get(team_1)
    team_2_id = team_ids.get(team_2)

    # For playoff matches where we don't have team IDs
    if team_1_id is None or team_2_id is None:
        # Create a placeholder team ID for teams that don't exist yet
        placeholder_id = str(uuid.uuid4())

        # Use SQL NULL for homeTeamId/away_team_id for these special matches
        cursor.execute(
            """
            INSERT INTO tipovacka_matches (id, start, "home_team_id", "away_team_id", "event_id") 
            VALUES (%s, %s, NULL, NULL, %s)
            """,
            (match_id, match_datetime, EVENT_ID)
        )
    else:
        # Insert regular match with team IDs
        cursor.execute(
            """
            INSERT INTO tipovacka_matches (id, start, "home_team_id", "away_team_id", "event_id") 
            VALUES (%s, %s, %s, %s, %s)
            """,
            (match_id, match_datetime, team_1_id, team_2_id, EVENT_ID)
        )

# Close connection
cursor.close()
conn.close()

print("Data successfully imported to database!")
