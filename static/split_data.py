import pandas as pd

# Load the original dataset
df = pd.read_csv('static/nba_shot_locs_1997_2020.csv')

# Extract season/year from game_date
df['season'] = pd.to_datetime(df['game_date']).dt.year

# Get unique seasons and calculate split points
seasons = sorted(df['season'].unique())
q1 = seasons[len(seasons)//4]      # First quartile season
median = seasons[len(seasons)//2]  # Median season
q3 = seasons[3*len(seasons)//4]    # Third quartile season

# Split the data into 4 parts based on seasons
df_part1 = df[df['season'] <= q1]
df_part2 = df[(df['season'] > q1) & (df['season'] <= median)]
df_part3 = df[(df['season'] > median) & (df['season'] <= q3)]
df_part4 = df[df['season'] > q3]

# Save all four parts
df_part1.to_csv('static/nba_shot_locs_part1.csv', index=False)
df_part2.to_csv('static/nba_shot_locs_part2.csv', index=False)
df_part3.to_csv('static/nba_shot_locs_part3.csv', index=False)
df_part4.to_csv('static/nba_shot_locs_part4.csv', index=False)

# Print summary
print(f"Split into 4 parts with row counts:")
print(f"Part 1 (seasons ≤ {q1}): {len(df_part1)} rows")
print(f"Part 2 ({q1+1}-{median}): {len(df_part2)} rows")
print(f"Part 3 ({median+1}-{q3}): {len(df_part3)} rows")
print(f"Part 4 (seasons > {q3}): {len(df_part4)} rows")