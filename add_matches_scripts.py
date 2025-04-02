# Format: (datum, čas, hometeam, awayTeam, specialType)
match_data = [
    # Group A
    ("09.04.2025", "13:00", "e8d6fe20-5017-49f8-bff8-71cdbc90b456", "2d1c341a-63fb-4d29-aa6f-9379bf3e0543", None),  # Finsko–USA
    ("09.04.2025", "17:00", "4a05566b-51e8-4a64-8d27-b0829083b250", "5e9877c1-dc25-4dfc-a107-89f8c3f55fdf", None),  # Česko–Švýcarsko
    ("10.04.2025", "17:00", "32dcd684-7f52-4de8-afb3-3870abb960c0", "e8d6fe20-5017-49f8-bff8-71cdbc90b456", None),  # Kanada–Finsko
    ("11.04.2025", "13:00", "5e9877c1-dc25-4dfc-a107-89f8c3f55fdf", "32dcd684-7f52-4de8-afb3-3870abb960c0", None),  # Švýcarsko–Kanada
    ("11.04.2025", "17:00", "2d1c341a-63fb-4d29-aa6f-9379bf3e0543", "4a05566b-51e8-4a64-8d27-b0829083b250", None),  # USA–Česko
    ("12.04.2025", "17:00", "e8d6fe20-5017-49f8-bff8-71cdbc90b456", "4a05566b-51e8-4a64-8d27-b0829083b250", None),  # Finsko–Česko
    ("13.04.2025", "17:00", "32dcd684-7f52-4de8-afb3-3870abb960c0", "2d1c341a-63fb-4d29-aa6f-9379bf3e0543", None),  # Kanada–USA
    ("14.04.2025", "13:00", "5e9877c1-dc25-4dfc-a107-89f8c3f55fdf", "e8d6fe20-5017-49f8-bff8-71cdbc90b456", None),  # Švýcarsko–Finsko
    ("14.04.2025", "17:00", "4a05566b-51e8-4a64-8d27-b0829083b250", "32dcd684-7f52-4de8-afb3-3870abb960c0", None),  # Česko–Kanada
    ("15.04.2025", "17:00", "2d1c341a-63fb-4d29-aa6f-9379bf3e0543", "5e9877c1-dc25-4dfc-a107-89f8c3f55fdf", None),  # USA–Švýcarsko

    # Group B
    ("09.04.2025", "09:00", "38aa4c12-4d12-4ec5-9331-3dbf1c06a79e", "526a2988-c11e-4091-b427-aa08d6a5ab55", None),  # Švédsko–Německo
    ("10.04.2025", "09:00", "ce53e4a6-6380-49f6-9639-8e4e931fd029", "3265c00a-d0da-4466-a0c0-746e333099f4", None),  # Japonsko–Norsko
    ("10.04.2025", "13:00", "38aa4c12-4d12-4ec5-9331-3dbf1c06a79e", "8ef98d7b-050b-4555-b489-317f3c7c17fc", None),  # Švédsko–Maďarsko
    ("11.04.2025", "09:00", "8ef98d7b-050b-4555-b489-317f3c7c17fc", "ce53e4a6-6380-49f6-9639-8e4e931fd029", None),  # Maďarsko–Japonsko
    ("12.04.2025", "13:00", "3265c00a-d0da-4466-a0c0-746e333099f4", "526a2988-c11e-4091-b427-aa08d6a5ab55", None),  # Norsko–Německo
    ("13.04.2025", "09:00", "8ef98d7b-050b-4555-b489-317f3c7c17fc", "3265c00a-d0da-4466-a0c0-746e333099f4", None),  # Maďarsko–Norsko
    ("13.04.2025", "13:00", "ce53e4a6-6380-49f6-9639-8e4e931fd029", "38aa4c12-4d12-4ec5-9331-3dbf1c06a79e", None),  # Japonsko–Švédsko
    ("14.04.2025", "09:00", "526a2988-c11e-4091-b427-aa08d6a5ab55", "8ef98d7b-050b-4555-b489-317f3c7c17fc", None),  # Německo–Maďarsko
    ("15.04.2025", "09:00", "3265c00a-d0da-4466-a0c0-746e333099f4", "38aa4c12-4d12-4ec5-9331-3dbf1c06a79e", None),  # Norsko–Švédsko
    ("15.04.2025", "13:00", "526a2988-c11e-4091-b427-aa08d6a5ab55", "ce53e4a6-6380-49f6-9639-8e4e931fd029", None),  # Německo–Japonsko

    # Playoffs
    ("17.04.2025", "08:00", None, None, "ctvrtfinale"),  # Čtvrtfinále 1
    ("17.04.2025", "11:30", None, None, "ctvrtfinale"),  # Čtvrtfinále 2
    ("17.04.2025", "15:00", None, None, "ctvrtfinale"),  # Čtvrtfinále 3
    ("17.04.2025", "18:30", None, None, "ctvrtfinale"),  # Čtvrtfinále 4
    ("19.04.2025", "13:00", None, None, "semifinale"),  # Semifinále 1
    ("19.04.2025", "17:00", None, None, "semifinale"),  # Semifinále 2
    ("20.04.2025", "12:00", None, None, "oTretiMisto"),  # O 3. místo
    ("20.04.2025", "16:00", None, None, "finale")  # Finále
]


# Vzorový skript pro vložení do databáze:
import uuid
import psycopg2
from datetime import datetime
from psycopg2.extras import RealDictCursor

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
EVENT_ID = "3247309f-4e93-4ec3-b8b3-01ccb2666dca"

# Insert matches
for date_str, time_str, home_team_id, away_team_id, special_type in match_data:
    match_id = str(uuid.uuid4())

    # Parse date and time
    datetime_str = f"{date_str} {time_str}"
    match_datetime = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")

    # For playoff matches where we don't have team IDs
    if home_team_id is None or away_team_id is None:
        # Insert special match with NULL for team IDs but include special type
        cursor.execute(
            '''
            INSERT INTO "tipovacka_matches" (id, start, "home_team_id", "away_team_id", "event_id", "specialType") 
            VALUES (%s, %s, NULL, NULL, %s, %s)
            ''',
            (match_id, match_datetime, EVENT_ID, special_type)
        )
    else:
        # Insert regular match with team IDs
        cursor.execute(
            '''
            INSERT INTO "tipovacka_matches" (id, start, "home_team_id", "away_team_id", "event_id", "specialType") 
            VALUES (%s, %s, %s, %s, %s, %s)
            ''',
            (match_id, match_datetime, home_team_id, away_team_id, EVENT_ID, special_type)
        )

# Close connection
cursor.close()
conn.close()

print("Data successfully imported to database!")
