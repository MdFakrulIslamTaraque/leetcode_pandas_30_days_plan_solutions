"""
link: https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to find the first login date for each player.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
"""

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # order the df by 'event_date'
    # drop the duplicates based on 'palyer_id', 
    # keeping the 'first' entry, drop 'device_id', 'games_played' columns 
    # rename the 'event_date' to 'first_login'
    return activity.sort_values(by=['event_date']).drop_duplicates(subset=['player_id'], keep='first').drop(['device_id', 'games_played'], axis= 1).rename(columns={'event_date':'first_login'})