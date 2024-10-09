import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import json
import glob
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go

#pd.set_option('display.max_columns', 100)
plt.style.use('dark_background')
warnings.filterwarnings('ignore')



def formula_barplot(player_df, sorting_col, color, col1, col2, col3, col4, width):
    '''
    This function plots multiple seaborn cat plots for
    team player stats, returns top 10 batsmen, bowlers, 
    batsmen with best strike rate(20 games min), bowlers
    with best strike rates with minimum 20 games.
    These plot data are sorted on runs_scored then on strike_rates
    and wickets_taken then on strike_rates
    '''

    team_30_bowling = player_df.sort_values(sorting_col, ascending=False).head(30)
    team_30_col1 = team_30_bowling.sort_values(col1, ascending=False).head(20)
    team_30_col2 = team_30_bowling.sort_values(col2, ascending=False).head(20)
    team_30_col3 = team_30_bowling.sort_values(col3, ascending=False).head(20)
    team_30_col4 = team_30_bowling.sort_values(col4, ascending=False).head(20)

    
    ax1 = px.bar(team_30_col1, x=sorting_col,
                y=col1, color=color, text='player_name')

    ax1.update_traces(width=width)
    ax1.show()
    
    ax2 = px.bar(team_30_col2, x=sorting_col, 
                y=col2, color=color, text='player_name')

    ax2.update_traces(width=width)
    ax2.show()

    ax3 = px.bar(team_30_col3, x=sorting_col,
                y=col3, color=color, text='player_name')

    ax3.update_traces(width=width)
    ax3.show()
    
    ax4 = px.bar(team_30_col4, x=sorting_col, 
                y=col4, color=color, text='player_name')

    ax4.update_traces(width=width)
    ax4.show()



def formula_scatterplot(player_df, sorting_col, color, col1, col2, col3, col4, size, hover_data):
    '''
    This function plots multiple seaborn cat plots for
    team player stats, returns top 10 batsmen, bowlers, 
    batsmen with best strike rate(20 games min), bowlers
    with best strike rates with minimum 20 games.
    These plot data are sorted on runs_scored then on strike_rates
    and wickets_taken then on strike_rates
    '''

    team_30_bowling = player_df.sort_values(sorting_col, ascending=False).head(30)
    team_30_col1 = team_30_bowling.sort_values(col1, ascending=False).head(20)
    team_30_col2 = team_30_bowling.sort_values(col2, ascending=False).head(20)
    team_30_col3 = team_30_bowling.sort_values(col3, ascending=False).head(20)
    team_30_col4 = team_30_bowling.sort_values(col4, ascending=False).head(20)

    ax1 = px.scatter(team_30_col1, x=sorting_col,
                y=col1, color=color, size=team_30_col1[size].tolist(),
                hover_data=hover_data)

    ax1.show()
    
    ax2 = px.scatter(team_30_col2, x=sorting_col, 
                y=col2, color=color, size=team_30_col2[size].tolist(),
                hover_data=hover_data)
    
    ax2.show()

    ax3 = px.scatter(team_30_col3, x=sorting_col,
                y=col3, color=color, size=team_30_col3[size].tolist(),
                hover_data=hover_data)
    
    ax3.show()
    
    ax4 = px.scatter(team_30_col4, x=sorting_col, 
                y=col4, color=color, size=team_30_col4[size].tolist(),
                hover_data=hover_data)

    ax4.show()


def formula_scatterplot_multiple_data(player_df1, player_df2, player_df3, sorting_col, color, col1, 
                                      size, hover_data, title1, title2, title3):
    '''
    This function plots multiple seaborn cat plots for
    team player stats, returns top 10 batsmen, bowlers, 
    batsmen with best strike rate(20 games min), bowlers
    with best strike rates with minimum 20 games.
    These plot data are sorted on runs_scored then on strike_rates
    and wickets_taken then on strike_rates
    '''

    team_30_bowling1 = player_df1.sort_values(sorting_col, ascending=False).head(30)
    team_30_bowling2 = player_df2.sort_values(sorting_col, ascending=False).head(30)
    team_30_bowling3 = player_df3.sort_values(sorting_col, ascending=False).head(30)
    team_30_col1 = team_30_bowling1.sort_values(col1, ascending=False).head(20)
    team_30_col2 = team_30_bowling2.sort_values(col1, ascending=False).head(20)
    team_30_col3 = team_30_bowling3.sort_values(col1, ascending=False).head(20)
    

    ax1 = px.scatter(team_30_col1, x=sorting_col,
                y=col1, color=color, size=team_30_col1[size].tolist(),
                hover_data=hover_data, title=title1)

    ax1.show()
    
    ax2 = px.scatter(team_30_col2, x=sorting_col, 
                y=col1, color=color, size=team_30_col2[size].tolist(),
                hover_data=hover_data, title=title2)
    
    ax2.show()

    ax3 = px.scatter(team_30_col3, x=sorting_col,
                y=col1, color=color, size=team_30_col3[size].tolist(),
                hover_data=hover_data, title=title3)
    
    ax3.show()



def all_players_stats_year(player_list, all_data_list, player_df, year):
    '''
        This function takes in player_names list, all_game_data list,
        player_df, year as text which is the dataframe containing all players data
        and returns their stats
    '''
    
    for index, i in enumerate(player_list):
        trophies = 0
        strike_rate_30 = []
        man_of_match = 0
        multi_wickets = 0
        matches = 0
        innings_batted = 0
        matches_won = 0
        runs_scored = 0
        balls_played = 0
        catches = 0
        run_outs = 0
        innings_bowled = 0
        balls_bowled = 0
        runs_given = 0
        wickets_taken = 0
        four_scored = 0
        six_scored = 0
        four_given = 0
        six_given = 0
        extras_for = 0
        extras_against = 0
        scored_above_30 = 0
        for j in all_data_list:
            scores_of_30 = 0
            m_wickets = 0
            balls_above_30 = 0
            if j['info']['dates'][0][:4] == year:
                values = list(j['info']['players'].values())
                players_list = [x for xs in values for x in xs]
                if i in players_list:
                    matches += 1
                try:
                    if j['info']['player_of_match'][0] == i:
                        man_of_match += 1
                except:
                    None
                for k in j['innings']:
                    batsmen = []
                    bowler = []
                    for over in k['overs']:
                        for delivery in over['deliveries']:
                            if i == delivery['batter']:
                                runs_scored += delivery['runs']['batter']
                                scores_of_30 += delivery['runs']['batter']
                                if i not in batsmen:
                                    batsmen.append(i)
                                balls_played += 1
                                balls_above_30 += 1
                                extras_for += delivery['runs']['extras']
                                if delivery['runs']['batter'] == 4:
                                    four_scored += 1
                                elif delivery['runs']['batter'] == 6:
                                    six_scored += 1
                    
                            elif i == delivery['bowler']:
                                balls_bowled += 1
                                if i not in bowler:
                                    bowler.append(i)
                                if delivery['runs']['batter'] == 4:
                                    four_given += 1
                                elif delivery['runs']['batter'] == 6:
                                    six_given += 1
                                runs_given += delivery['runs']['batter']
                                extras_against += delivery['runs']['extras']
                                try:
                                    if delivery['wickets'][0]['kind'] != 'run out':
                                        wickets_taken += 1
                                        m_wickets += 1
                                    elif delivery['wickets'][0]['fielders'][0]['name'] == i:
                                        catches += 1
                                    elif delivery['wickets'][0]['kind'] == 'run out':
                                        run_outs += 1
                                except:
                                    None
                                    
                            try:
                                if delivery['wickets'][0]['kind'] != 'run out':
                                    if delivery['wickets'][0]['fielders'][0]['name'] == i:
                                        catches += 1
                                if delivery['wickets'][0]['kind'] == 'run out':
                                    if delivery['wickets'][0]['fielders'][0]['name'] == i:
                                        run_outs += 1
                            except:
                                None
                                
                    if i in batsmen:
                        innings_batted += 1
                    if i in bowler:
                        innings_bowled += 1

                    if scores_of_30 >= 30:
                        scored_above_30 += 1
                        strike_rate_30.append((scores_of_30/balls_above_30) * 100)
    
                if m_wickets >= 2:
                    multi_wickets += 1
    
                        
                try:
                    if i in j['info']['players'][j['info']['outcome']['winner']]:
                        #print(j['info']['players'][j['info']['outcome']['winner']])
                        #print(i)
                        matches_won += 1
                except:
                    continue

                try:
                    if j['info']['event']['stage'] == 'Final':
                        
                        if i in j['info']['players'][j['info']['outcome']['winner']]:
                            #print(j['info']['players'][j['info']['outcome']['winner']])
                            #print(i)
                            trophies += 1
                except:
                    continue

        try:
            bat_avg = runs_scored/innings_batted
        except:
            bat_avg = 0.

        try:
            strike_rate = (runs_scored/balls_played) * 100
        except:
            strike_rate = 0.

        try:
            wickets_per_inni = wickets_taken/innings_bowled
        except:
            wickets_per_inni = 0.

        try:
            bowl_avg = runs_given/wickets_taken
        except:
            bowl_avg = 0.

        try:
            bowl_sr = balls_bowled/wickets_taken
        except:
            bowl_sr = 0.

        try:
            bowl_eco = runs_given/(balls_bowled/6)
        except:
            bowl_eco = 0.

        strike_rate_above_30 = np.mean(strike_rate_30)

        try:
            formula_batter = (four_scored + six_scored + bat_avg) + (scored_above_30 * 
                                                                     strike_rate_above_30)
        except:
            formula_batter = 0.

        try:
            formula_bowler = (wickets_taken + multi_wickets) + (wickets_taken / innings_bowled)
        except:
            formula_bowler = 0.

        try:
            formula_fielder = man_of_match + catches + run_outs
        except:
            formula_fielder = 0.
        
        player_df.loc[index,:] = [i, matches, innings_batted, innings_bowled, matches_won, runs_scored, 
                                  balls_played, bat_avg, strike_rate, catches, run_outs, balls_bowled, 
                                  runs_given, wickets_taken, wickets_per_inni, bowl_avg, bowl_sr, 
                                  bowl_eco, four_scored, six_scored, four_given, six_given, extras_for,
                                  extras_against, scored_above_30, strike_rate_above_30, multi_wickets,
                                  man_of_match, trophies, formula_batter, formula_bowler,
                                  formula_fielder]


    return player_df


def all_players_stats_year_list(player_list, all_data_list, player_df, year_list):
    '''
        This function takes in player_names list, all_game_data list,
        player_df, year as text which is the dataframe containing all players data
        and returns their stats
    '''
    
    for index, i in enumerate(player_list):
        trophies = 0
        strike_rate_30 = []
        man_of_match = 0
        multi_wickets = 0
        matches = 0
        innings_batted = 0
        matches_won = 0
        runs_scored = 0
        balls_played = 0
        catches = 0
        run_outs = 0
        innings_bowled = 0
        balls_bowled = 0
        runs_given = 0
        wickets_taken = 0
        four_scored = 0
        six_scored = 0
        four_given = 0
        six_given = 0
        extras_for = 0
        extras_against = 0
        scored_above_30 = 0
        for j in all_data_list:
            scores_of_30 = 0
            m_wickets = 0
            balls_above_30 = 0
            for year in year_list:
                if j['info']['dates'][0][:4] == year:
                    values = list(j['info']['players'].values())
                    players_list = [x for xs in values for x in xs]
                    if i in players_list:
                        matches += 1
                    try:
                        if j['info']['player_of_match'][0] == i:
                            man_of_match += 1
                    except:
                        None
                    for k in j['innings']:
                        batsmen = []
                        bowler = []
                        for over in k['overs']:
                            for delivery in over['deliveries']:
                                if i == delivery['batter']:
                                    runs_scored += delivery['runs']['batter']
                                    scores_of_30 += delivery['runs']['batter']
                                    if i not in batsmen:
                                        batsmen.append(i)
                                    balls_played += 1
                                    balls_above_30 += 1
                                    extras_for += delivery['runs']['extras']
                                    if delivery['runs']['batter'] == 4:
                                        four_scored += 1
                                    elif delivery['runs']['batter'] == 6:
                                        six_scored += 1
                        
                                elif i == delivery['bowler']:
                                    balls_bowled += 1
                                    if i not in bowler:
                                        bowler.append(i)
                                    if delivery['runs']['batter'] == 4:
                                        four_given += 1
                                    elif delivery['runs']['batter'] == 6:
                                        six_given += 1
                                    runs_given += delivery['runs']['batter']
                                    extras_against += delivery['runs']['extras']
                                    try:
                                        if delivery['wickets'][0]['kind'] != 'run out':
                                            wickets_taken += 1
                                            m_wickets += 1
                                        elif delivery['wickets'][0]['fielders'][0]['name'] == i:
                                            catches += 1
                                        elif delivery['wickets'][0]['kind'] == 'run out':
                                            run_outs += 1
                                    except:
                                        None
                                        
                                try:
                                    if delivery['wickets'][0]['kind'] != 'run out':
                                        if delivery['wickets'][0]['fielders'][0]['name'] == i:
                                            catches += 1
                                    if delivery['wickets'][0]['kind'] == 'run out':
                                        if delivery['wickets'][0]['fielders'][0]['name'] == i:
                                            run_outs += 1
                                except:
                                    None
                                    
                        if i in batsmen:
                            innings_batted += 1
                        if i in bowler:
                            innings_bowled += 1
    
                        if scores_of_30 >= 30:
                            scored_above_30 += 1
                            strike_rate_30.append((scores_of_30/balls_above_30) * 100)
        
                    if m_wickets >= 2:
                        multi_wickets += 1
        
                            
                    try:
                        if i in j['info']['players'][j['info']['outcome']['winner']]:
                            #print(j['info']['players'][j['info']['outcome']['winner']])
                            #print(i)
                            matches_won += 1
                    except:
                        continue
    
                    try:
                        if j['info']['event']['stage'] == 'Final':
                            
                            if i in j['info']['players'][j['info']['outcome']['winner']]:
                                #print(j['info']['players'][j['info']['outcome']['winner']])
                                #print(i)
                                trophies += 1
                    except:
                        continue

        try:
            bat_avg = runs_scored/innings_batted
        except:
            bat_avg = 0.

        try:
            strike_rate = (runs_scored/balls_played) * 100
        except:
            strike_rate = 0.

        try:
            wickets_per_inni = wickets_taken/innings_bowled
        except:
            wickets_per_inni = 0.

        try:
            bowl_avg = runs_given/wickets_taken
        except:
            bowl_avg = 0.

        try:
            bowl_sr = balls_bowled/wickets_taken
        except:
            bowl_sr = 0.

        try:
            bowl_eco = runs_given/(balls_bowled/6)
        except:
            bowl_eco = 0.

        strike_rate_above_30 = np.mean(strike_rate_30)

        try:
            formula_batter = (four_scored + six_scored + bat_avg) + (scored_above_30 * 
                                                                     strike_rate_above_30)
        except:
            formula_batter = 0.

        try:
            formula_bowler = (wickets_taken + multi_wickets) + (wickets_taken / innings_bowled)
        except:
            formula_bowler = 0.

        try:
            formula_fielder = man_of_match + catches + run_outs
        except:
            formula_fielder = 0.
        
        player_df.loc[index,:] = [i, matches, innings_batted, innings_bowled, matches_won, runs_scored, 
                                  balls_played, bat_avg, strike_rate, catches, run_outs, balls_bowled, 
                                  runs_given, wickets_taken,
                                  wickets_per_inni, bowl_avg, bowl_sr, bowl_eco, four_scored, 
                                  six_scored, four_given, six_given, extras_for, extras_against,
                                  scored_above_30, strike_rate_above_30, multi_wickets, man_of_match, 
                                  trophies, formula_batter, formula_bowler, formula_fielder]


    return player_df



def season_player_team_stats(all_data, all_teams, all_players, team_list,  year='2008'):

    team_stat = {}
    for team in team_list:
        player_stat = {}
        for player in all_players:
            stats = {}
            runs = []
            wickets = []
            dot_balls = []
            catch = []
            four_for = []
            four_against = []
            six_for = []
            six_against = []
            strike_rate = []
            runs_against = []
            match_won = []
            balls_bowled = []
            balls = []
            dot_balls_bat = []
            dot_ball_perc_bat = []
            bowling_eco = []
            #dot_ball_perc_bowl = []
            for data in all_data:
                if data['info']['dates'][0][:4] == year:
                    try:
                        if player in data['info']['players'][team]:
                            multi_wickets = 0
                            dots_played = 0
                            dots = 0
                            matches = 0
                            innings_batted = 0
                            won = 'no'
                            runs_scored = 0
                            balls_played = 0
                            catches = 0
                            run_outs = 0
                            innings_bowled = 0
                            balls_b = 0
                            runs_given = 0
                            wickets_taken = 0
                            four_scored = 0
                            six_scored = 0
                            four_given = 0
                            six_given = 0
                            extras_for = 0
                            extras_against = 0
                            scored_above_30 = 0
                            scores_of_30 = 0
                            m_wickets = 0
                            balls_above_30 = 0
                            
                            for innings in data['innings']:
                                for overs in innings['overs']:
                                    for delivery in overs['deliveries']:
                                        if player == delivery['batter']:
                                            runs_scored += delivery['runs']['batter']
                                            scores_of_30 += delivery['runs']['batter']
                                            if delivery['runs']['extras'] == 0:
                                                balls_played += 1
                                                balls_above_30 += 1
                                            extras_for += delivery['runs']['extras']
                                            if delivery['runs']['batter'] == 4:
                                                four_scored += 1
                                            elif delivery['runs']['batter'] == 6:
                                                six_scored += 1
                                            elif delivery['runs']['batter'] == 0 and \
                                            delivery['runs']['extras'] == 0:
                                                dots_played += 1
                                            try:
                                                if delivery['wickets']:
                                                    balls_played += 1
                                            except:
                                                None
                                                
                                        elif player == delivery['bowler']:
                                            balls_b += 1
                                            if delivery['runs']['batter'] == 4:
                                                four_given += 1
                                            elif delivery['runs']['batter'] == 6:
                                                six_given += 1
                                            elif delivery['runs']['batter'] == 0:
                                                dots += 1
                                            runs_given += delivery['runs']['batter']
                                            extras_against += delivery['runs']['extras']
                                            try:
                                                if delivery['wickets'][0]['kind'] != 'run out':
                                                    wickets_taken += 1
                                                    m_wickets += 1
                                                elif delivery['wickets'][0]['fielders'][0]['name'] == \
                                                player:
                                                    catches += 1
                                                elif delivery['wickets'][0]['kind'] == 'run out':
                                                    run_outs += 1
                                            except:
                                                None
    
                                        try:
                                            if delivery['wickets'][0]['kind'] != 'run out':
                                                if delivery['wickets'][0]['fielders'][0]['name'] == \
                                                player:
                                                    catches += 1
                                            if delivery['wickets'][0]['kind'] == 'run out':
                                                if delivery['wickets'][0]['fielders'][0]['name'] == \
                                                player:
                                                    run_outs += 1
                                        except:
                                            None

                            try:
                                if player in data['info']['players'][data['info']['outcome']['winner']]:
                                    #print(j['info']['players'][j['info']['outcome']['winner']])
                                    #print(i)
                                    won = 'yes'
                            except:
                                continue

                            runs.append(runs_scored)
                            wickets.append(wickets_taken)
                            dot_balls.append(dots)
                            catch.append(catches)
                            four_for.append(four_scored)
                            six_for.append(six_scored)
                            six_against.append(six_given)
                            four_against.append(four_given)
                            balls.append(balls_played)
                            runs_against.append(runs_given)
                            match_won.append(won)
                            balls_bowled.append(balls_b)
                            try:
                                strike_rate.append(np.round((runs_scored)/(balls_played)*100, 2))
                            except:
                                strike_rate.append(0.)
                            dot_balls_bat.append(dots_played)
                            try:
                                dot_ball_perc_bat.append(np.round((np.sum(dot_balls_bat)/np.sum(balls)) 
                                                                  * 100, 2))
                            except:
                                dot_ball_perc_bat.append(0.)

                            try: bowling_eco.append(np.round((runs_given)/((balls_b)/6.), 2))
                            except: bowling_eco.append(0.)
                                
                            stats['runs'] = runs
                            stats['total_runs'] = np.sum(runs)
                            stats['balls_faced'] = balls
                            stats['total_balls_played'] = np.sum(balls)
                            stats['four_for'] = four_for
                            stats['total_four_for'] = np.sum(four_for)
                            stats['six_for'] = six_for
                            stats['total_six_for'] = np.sum(six_for)
                            stats['catches'] = catch
                            stats['total_catches'] = np.sum(catch)
                            stats['wickets'] = wickets
                            stats['total_wickets'] = np.sum(wickets)
                            stats['balls_bowled'] = balls_bowled
                            stats['total_balls_bowled'] = np.sum(balls_bowled)
                            stats['runs_given'] = runs_against
                            stats['total_runs_given'] = np.sum(runs_against)
                            stats['dots_bowled'] = dot_balls
                            stats['total_dot_balls_bowled'] = np.sum(dot_balls)
                            stats['four_against'] = four_against
                            stats['total_four_against'] = np.sum(four_against)
                            stats['six_against'] = six_against
                            stats['total_six_against'] = np.sum(six_against)
                            stats['match_won'] = match_won
                            stats['strike_rate'] = strike_rate
                            stats['dots_played'] = dot_balls_bat
                            stats['dot_ball_perc_bat'] = dot_ball_perc_bat
                            stats['bowling_eco'] = bowling_eco
                                

                    except:
                        None
                                            
                    
                player_stat[player] =  stats
            player_stat = {k: v for k, v in player_stat.items() if v}
        team_stat[team] = player_stat
    return team_stat


def plot_all_top_5_dict(top_5_dict, team_player_dict):

    for team in all_teams:
        for key, top_5 in top_5_dict.items():
            #print(top_5)
            if top_5 != []:
                for player in top_5:
                    #print(player)
                    try:
                        fig = px.scatter(team_player_dict[team][player], y='runs', color='match_won', 
                                         hover_data=['balls_faced', 'total_runs', 'six_for'])
                        fig.update_layout(xaxis_title=player, title=team)
                        fig.show()
                    except:
                        None
        print('seperator')


def plot_team_top_5(top_5_dict, team_player_dict, team, yval='runs'):

    for top_5 in top_5_dict[team]:
        #fig = make_subplots(rows=1, cols=5)
        try:
            fig = px.scatter(team_player_dict[team][top_5], y=yval, color='match_won', 
                             hover_data=['total_runs', 'balls_faced', 'dot_ball_perc_bat', 
                                         'strike_rate', 'six_for', 'wickets', 'bowling_eco',
                                         'catches', 'six_against', 'dots_bowled', 'balls_bowled'])
            fig.update_layout(xaxis_title=top_5, title=team)
            fig.show()
        except Exception as e:
            print(str(e))





