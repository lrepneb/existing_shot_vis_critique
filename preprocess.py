import pandas as pd

def preprocess_csv(file_path, output_path):
    # Load CSV
    df = pd.read_csv(file_path)

    # Drop unwanted fields
    columns_to_drop = ["Game ID", "Game Event", "Player ID", "Team ID"]
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Convert "Game Date" from YYYYMMDD to MM-DD-YYYY
    if "Game Date" in df.columns:
        df["Game Date"] = pd.to_datetime(df["Game Date"], format='%Y%m%d').dt.strftime('%m-%d-%Y')

    # Combine "Minutes Remaining" and "Seconds Remaining" into "Time Remaining"
    if "Minutes Remaining" in df.columns and "Seconds Remaining" in df.columns:
        df["Time Remaining"] = df["Minutes Remaining"] * 60 + df["Seconds Remaining"]
        df["Time Remaining"] = pd.to_datetime(df["Time Remaining"], unit='s').dt.strftime('%M:%S')
        df = df.drop(columns=["Minutes Remaining", "Seconds Remaining"])

    # Split "Player Name" into "player_first" and "player_last"
    if "Player Name" in df.columns:
        df[["player_first", "player_last"]] = df["Player Name"].str.split(" ", n=1, expand=True)
        df = df.drop(columns=["Player Name"])

    # Convert column names to snake_case
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]

    # Save the cleaned dataset
    df.to_csv(output_path, index=False)

    print(f"Preprocessed file saved to: {output_path}")

# Mapping of full team names to abbreviations, considering historical teams
TEAM_ABBREVIATIONS = {
    # Current NBA teams
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BKN",
    "Charlotte Hornets": "CHA",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHX",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",

    # Historical Teams
    "Seattle SuperSonics": "SEA",  # Became OKC Thunder in 2008
    "New Jersey Nets": "NJN",  # Became Brooklyn Nets in 2012
    "Charlotte Bobcats": "CHA",  # Renamed to Hornets in 2014
    "Vancouver Grizzlies": "VAN",  # Became Memphis Grizzlies in 2001
    "New Orleans Hornets": "NOH",
}

def preprocess_nba_data(input_file, output_file):
    # Load dataset
    df = pd.read_csv(input_file)

    # Drop unwanted fields
    columns_to_drop = ["game_event_id", "home_team", "away_team"]
    df = df.drop(columns=[col for col in columns_to_drop if col in df.columns])

    # Rename 'season_type' to 'playoffs' and convert values
    if "season_type" in df.columns:
        df = df.rename(columns={"season_type": "playoffs"})
        df["playoffs"] = df["playoffs"].map({"Regular Season": 0, "Playoffs": 1})

    # Convert full team names to abbreviations
    if "team_name" in df.columns:
        df["team_name"] = df["team_name"].map(TEAM_ABBREVIATIONS).fillna(df["team_name"])  # Retain original name if not found

    # Save preprocessed data
    df.to_csv(output_file, index=False)
    print(f"Preprocessed file saved to: {output_file}")

def clean_shot_data(file_path, output_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Map shot_type to 2 or 3
    df['shot_type'] = df['shot_type'].replace({'2PT Field Goal': 2, '3PT Field Goal': 3})

    # Map action_type to abbreviations
    action_type_map = {
        'Jump Shot': 'JS', 'Layup Shot': 'LS', 'Driving Layup Shot': 'DLS',
        'Slam Dunk Shot': 'SDS', 'Dunk Shot': 'DS', 'Tip Shot': 'TS',
        'Running Jump Shot': 'RJS', 'Driving Dunk Shot': 'DDS',
        'Turnaround Jump Shot': 'TAJS', 'Hook Shot': 'HS',
        'Turnaround Hook Shot': 'TAHS', 'Jump Bank Shot': 'JBS',
        'Fadeaway Jump Shot': 'FJS', 'Reverse Layup Shot': 'RLS'
    }
    df['action_type'] = df['action_type'].replace(action_type_map)

    # Map shot_zone_basic to abbreviations
    shot_zone_basic_map = {
        'Mid-Range': 'MR', 'Restricted Area': 'RA', 'In The Paint (Non-RA)': 'ITP',
        'Above the Break 3': 'AB3', 'Left Corner 3': 'LC3', 'Right Corner 3': 'RC3',
        'Back Court Shot': 'BCS'
    }
    df['shot_zone_basic'] = df['shot_zone_basic'].replace(shot_zone_basic_map)

    # Map shot_zone_area to abbreviations
    shot_zone_area_map = {
        'Left Side(L)': 'L', 'Right Side(R)': 'R', 'Center(C)': 'C',
        'Left Side Center(LC)': 'LC', 'Right Side Center(RC)': 'RC',
        'Back Court(BC)': 'BC', 'Back Court': 'BC'
    }
    df['shot_zone_area'] = df['shot_zone_area'].replace(shot_zone_area_map)

    # Map shot_zone_range to abbreviations
    shot_zone_range_map = {
        'Less Than 8 ft.': '<8', '8-16 ft.': '8-16',
        '16-24 ft.': '16-24', '24+ ft.': '24+'
    }
    df['shot_zone_range'] = df['shot_zone_range'].replace(shot_zone_range_map)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

def rmm(file_path, output_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # df = df.drop(columns=['action_type'])
    # df = df[~((df['shot_zone_basic'] == 'Back Court') | (df['shot_zone_range'] == 'Back Court Shot'))]

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

# Example usage
input_file = "static/nba_shot_locs_1997_2020.csv"  # Change to your actual file path
output_file = "static/nba_shot_locs_1997_2020.csv"
# clean_shot_data(input_file, output_file)
rmm(input_file, output_file)
