# info4310_hw4

## The Data Set

### Source
- [r/dataisbeautiful post by u/LongTermMtabolite](https://old.reddit.com/r/dataisbeautiful/comments/h94umw/oc_most_frequent_nba_shot_locations/)
- OP claims the [data was sourced from the NBA API](https://old.reddit.com/r/dataisbeautiful/comments/h94umw/oc_most_frequent_nba_shot_locations/fuv4qtx/)
- **Update**: Link to dataset -> [Data World](https://data.world/sportsvizsunday/june-2020-nba-shots-1997-2019/workspace/file?filename=NBA+Shot+Locations+1997+-+2020.csv)

## Field Definitions
team_name – TEXT, Shooting player's team

period – INT, Game period (1-4)

shot_type – INT, 2PT or 3PT shot

shot_zone_basic – TEXT, General shot location

shot_zone_area – TEXT, Court area of shot

shot_zone_range – TEXT, Distance category

shot_distance – INT, Exact shot distance (ft)

x_location – INT, X coordinate of shot (-250,250) but -250 is the most right and 250 is the most left

y_location – INT, Y coordinate of shot (-50 furthest down, 420 highest up)

shot_made_flag – INT, Shot success (1=Made, 0=Missed)

game_date – DATETIME, Date of game

playoffs – INT, Regular season (0) or Playoffs (1)

time_remaining – DATETIME, Seconds left in period

player_first – TEXT, Shooter's first name

player_last – TEXT, Shooter's last name