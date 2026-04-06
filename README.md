# Statcast Raw Data Export

This repo contains a simple script for downloading raw Statcast pitch data with `pybaseball`.

The script is in:

- `statcast_raw_called_pitches.py`

## What It Does

The script:

- downloads raw Statcast data for the selected date range
- keeps the original columns returned by `pybaseball`
- creates raw-data subsets for:
- all pitches
- called pitches (`called_strike` and `ball`)
- called pitches with complete tracking fields (`plate_x`, `plate_z`, `sz_bot`, `sz_top`)
- saves each dataframe as a CSV
- prints a short summary and the first 10 rows of each dataframe
- triggers CSV downloads when run in Google Colab

It does not calculate any extra fields, summaries, or plots.

## Date Range

Update these values in `statcast_raw_called_pitches.py`:

- `START_DATE`
- `END_DATE`

## Output Files

The script writes:

- `statcast_raw_data.csv`
- `statcast_called_pitches_raw.csv`
- `statcast_called_pitches_tracked_only.csv`

## Data Dictionary

These definitions describe the columns returned in `statcast_raw_data.csv` for this pull. Some deprecated or experimental Statcast fields may be empty for many rows.

- `pitch_type`: pitch classification code such as `FF`, `SL`, `CH`
- `game_date`: date of the game
- `release_speed`: pitch velocity at release, in mph
- `release_pos_x`: horizontal release position, in feet
- `release_pos_z`: vertical release position, in feet
- `player_name`: pitcher name
- `batter`: batter MLBAM player ID
- `pitcher`: pitcher MLBAM player ID
- `events`: result of the plate appearance on the pitch, if the pitch ended the PA
- `description`: pitch-by-pitch outcome description such as `ball`, `called_strike`, `foul`
- `spin_dir`: deprecated spin direction field
- `spin_rate_deprecated`: deprecated spin rate field
- `break_angle_deprecated`: deprecated break angle field
- `break_length_deprecated`: deprecated break length field
- `zone`: Statcast zone number for the pitch location
- `des`: longer text description of the play result
- `game_type`: game type such as spring training, regular season, postseason
- `stand`: batter stance, `L` or `R`
- `p_throws`: pitcher throwing hand, `L` or `R`
- `home_team`: home team abbreviation
- `away_team`: away team abbreviation
- `type`: high-level pitch result code, typically ball/strike/in-play classification
- `hit_location`: scoring location code for balls put in play
- `bb_type`: batted-ball type such as ground ball, line drive, fly ball
- `balls`: ball count before the pitch
- `strikes`: strike count before the pitch
- `game_year`: season year
- `pfx_x`: horizontal pitch movement relative to a spinless pitch, in feet
- `pfx_z`: vertical pitch movement relative to a spinless pitch, in feet
- `plate_x`: horizontal pitch location as it crossed home plate, in feet
- `plate_z`: vertical pitch location as it crossed home plate, in feet above ground
- `on_3b`: runner on third MLBAM player ID
- `on_2b`: runner on second MLBAM player ID
- `on_1b`: runner on first MLBAM player ID
- `outs_when_up`: number of outs when the batter came up
- `inning`: inning number
- `inning_topbot`: `Top` or `Bot`
- `hc_x`: hit-coordinate x value for balls in play
- `hc_y`: hit-coordinate y value for balls in play
- `tfs_deprecated`: deprecated time field
- `tfs_zulu_deprecated`: deprecated zulu time field
- `umpire`: home plate umpire identifier or name, if provided by source
- `sv_id`: Statcast pitch/video identifier
- `vx0`: initial x-velocity component, in feet per second
- `vy0`: initial y-velocity component, in feet per second
- `vz0`: initial z-velocity component, in feet per second
- `ax`: x-acceleration component, in feet per second squared
- `ay`: y-acceleration component, in feet per second squared
- `az`: z-acceleration component, in feet per second squared
- `sz_top`: top of the batter-specific strike zone, in feet
- `sz_bot`: bottom of the batter-specific strike zone, in feet
- `hit_distance_sc`: estimated hit distance, in feet
- `launch_speed`: exit velocity, in mph
- `launch_angle`: launch angle, in degrees
- `effective_speed`: effective pitch speed, in mph
- `release_spin_rate`: pitch spin rate, in rpm
- `release_extension`: extension toward home plate, in feet
- `game_pk`: MLB game identifier
- `fielder_2`: catcher MLBAM player ID
- `fielder_3`: first baseman MLBAM player ID
- `fielder_4`: second baseman MLBAM player ID
- `fielder_5`: third baseman MLBAM player ID
- `fielder_6`: shortstop MLBAM player ID
- `fielder_7`: left fielder MLBAM player ID
- `fielder_8`: center fielder MLBAM player ID
- `fielder_9`: right fielder MLBAM player ID
- `release_pos_y`: release position toward home plate, in feet
- `estimated_ba_using_speedangle`: estimated batting average from launch speed and angle
- `estimated_woba_using_speedangle`: estimated wOBA from launch speed and angle
- `woba_value`: wOBA value assigned to the event
- `woba_denom`: wOBA denominator contribution
- `babip_value`: BABIP contribution for the event
- `iso_value`: isolated power contribution for the event
- `launch_speed_angle`: Statcast launch-speed/launch-angle bucket code
- `at_bat_number`: plate appearance number within the game
- `pitch_number`: pitch number within the plate appearance
- `pitch_name`: human-readable pitch name
- `home_score`: home score before the pitch
- `away_score`: away score before the pitch
- `bat_score`: batting team score before the pitch
- `fld_score`: fielding team score before the pitch
- `post_away_score`: away score after the pitch
- `post_home_score`: home score after the pitch
- `post_bat_score`: batting team score after the pitch
- `post_fld_score`: fielding team score after the pitch
- `if_fielding_alignment`: infield alignment description
- `of_fielding_alignment`: outfield alignment description
- `spin_axis`: estimated pitch spin axis
- `delta_home_win_exp`: change in home team win expectancy from the pitch
- `delta_run_exp`: change in run expectancy from the pitch
- `bat_speed`: estimated bat speed
- `swing_length`: estimated swing length
- `estimated_slg_using_speedangle`: estimated slugging from launch speed and angle
- `delta_pitcher_run_exp`: pitcher-side run expectancy change from the pitch
- `hyper_speed`: Statcast bat-tracking speed-related field
- `home_score_diff`: home team lead/deficit before the pitch
- `bat_score_diff`: batting team lead/deficit before the pitch
- `home_win_exp`: home team win expectancy before the pitch
- `bat_win_exp`: batting team win expectancy before the pitch
- `age_pit_legacy`: legacy pitcher age field
- `age_bat_legacy`: legacy batter age field
- `age_pit`: pitcher age
- `age_bat`: batter age
- `n_thruorder_pitcher`: times through the order for the pitcher
- `n_priorpa_thisgame_player_at_bat`: batter's prior plate appearances in the game
- `pitcher_days_since_prev_game`: days since the pitcher last appeared
- `batter_days_since_prev_game`: days since the batter last appeared
- `pitcher_days_until_next_game`: days until the pitcher next appeared
- `batter_days_until_next_game`: days until the batter next appeared
- `api_break_z_with_gravity`: API vertical break measure including gravity reference
- `api_break_x_arm`: API horizontal break measure from the pitcher's arm-side perspective
- `api_break_x_batter_in`: API horizontal break measure from the batter-in perspective
- `arm_angle`: estimated pitcher arm angle
- `attack_angle`: estimated bat attack angle
- `attack_direction`: estimated swing attack direction
- `swing_path_tilt`: estimated swing path tilt
- `intercept_ball_minus_batter_pos_x_inches`: x-distance between ball intercept point and batter position, in inches
- `intercept_ball_minus_batter_pos_y_inches`: y-distance between ball intercept point and batter position, in inches

## Run In Google Colab

Install the dependency:

```python
!pip install pybaseball
```

Then run the script:

```python
!python statcast_raw_called_pitches.py
```

If `google.colab.files` is available, the CSV files will download automatically.
