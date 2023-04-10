from typing import List
from itertools import combinations

from simulator.player import Team
from simulator.situation import GameSituation, InningSituation


class Simulator:
    def __init__(self):
        pass

    @staticmethod
    def display_lineup(team: Team):
        for i, batter in enumerate(team.players):
            batter.display_original_stats(i + 1)

    def simulate_game(self, top_team: Team, bot_team: Team, display_lineup, display_result, display_player_result, display_play_detail):
        if display_lineup:
            print(f"# 先攻 {top_team.name}")
            self.display_lineup(top_team)
            print(f"# 後攻 {bot_team.name}")
            self.display_lineup(bot_team)

        game = GameSituation(top_team, bot_team)
        limit_inning = 12
        end_inning = 9
        for idx in range(limit_inning):
            inning = idx + 1
            game.now_inning = inning
            game.now_inning_bot = False
            top_inning = InningSituation(inning, False)
            top_inning.inning_start_score = game.top_score
            top_batter_idx = 0
            if len(game.inning_top_situations) > 0:
                top_batter_idx = (game.inning_top_situations[-1].last_batter_idx + 1) % 9
            while True:
                batter = game.top_team.players[top_batter_idx]
                top_inning.set_atbat_player(batter, top_batter_idx)
                top_inning.set_position(game.bottom_team.players, game.bottom_team.pitcher)
                top_inning.simulate(display_play_detail)
                top_batter_idx = (top_batter_idx + 1) % 9
                if top_inning.out_count >= 3:
                    break
            game.inning_top_situations.append(top_inning)
            game.top_score += top_inning.inning_score

            # 裏の攻撃
            game.now_inning_bot = True
            bot_inning = InningSituation(inning, True)
            bot_inning.inning_start_score = game.bottom_score
            if inning >= end_inning and game.top_score < game.bottom_score:
                game.cross = True
                game.inning_bot_situations.append(bot_inning)
                break
            bot_batter_idx = 0
            if len(game.inning_bot_situations) > 0:
                bot_batter_idx = (game.inning_bot_situations[-1].last_batter_idx + 1) % 9
            while True:
                batter = game.bottom_team.players[bot_batter_idx]
                bot_inning.set_atbat_player(batter, bot_batter_idx)
                bot_inning.set_position(game.top_team.players, game.top_team.pitcher)
                bot_inning.simulate(display_play_detail)
                bot_batter_idx = (bot_batter_idx + 1) % 9
                if inning >= end_inning and game.top_score < game.bottom_score + bot_inning.inning_score:
                    game.cross = True
                    break
                if bot_inning.out_count >= 3:
                    break
            game.inning_bot_situations.append(bot_inning)
            game.bottom_score += bot_inning.inning_score
            if inning >= end_inning and game.top_score != game.bottom_score:
                break
        if display_result:
            game.print_game_result()
        if display_player_result:
            game.print_game_player_results()
            game.print_pitcher_results()

        for batter in game.top_team.players:
            batter.end_game()
        for batter in game.bottom_team.players:
            batter.end_game()
        return game

    @staticmethod
    def display_season_title(teams):
        average_king, homerun_king, rbi_king, steel_king, error_king, strike_out_king = None, None, None, None, None, None
        for team in teams:
            for batter in team.players:
                atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, steel_success, steel_failed, error, strike_out = batter.season_stats.count_player_stats()
                if not average_king or average_king[2] < hit / atbat:
                    average_king = (team.name, batter.name, hit / atbat)
                if not homerun_king or homerun_king[2] < home_run:
                    homerun_king = (team.name, batter.name, home_run)
                if not rbi_king or rbi_king[2] < rbi:
                    rbi_king = (team.name, batter.name, rbi)
                if not steel_king or steel_king[2] < steel_success:
                    steel_king = (team.name, batter.name, steel_success)
                if not error_king or error_king[2] < error:
                    error_king = (team.name, batter.name, error)
                if not strike_out_king or strike_out_king[2] < strike_out:
                    strike_out_king = (team.name, batter.name, strike_out)
        print("##########")
        print(f"首位打者:{average_king[1]}({average_king[0]})", "打率:{:.3f}".format(average_king[2]))
        print(f"本塁打王:{homerun_king[1]}({homerun_king[0]}) {homerun_king[2]}本")
        print(f"打点王:{rbi_king[1]}({rbi_king[0]}) {rbi_king[2]}点")
        print(f"盗塁王:{steel_king[1]}({steel_king[0]}) {steel_king[2]}個")
        print(f"エラー王:{error_king[1]}({error_king[0]}) {error_king[2]}個")
        print(f"三振王:{strike_out_king[1]}({strike_out_king[0]}) {strike_out_king[2]}個")

    def simulate_season(self, teams: List[Team], each_games, display_lineup, display_batter_stats, display_game_result):
        if display_lineup:
            for team in teams:
                self.display_lineup(team)
        for comb in combinations(teams, 2):
            team_a, team_b = comb[0], comb[1]
            for i in range(each_games):
                if i < each_games / 2:
                    game = self.simulate_game(team_a, team_b, False, display_game_result, False, False)
                    team_a_score, team_b_score = game.top_score, game.bottom_score
                else:
                    game = self.simulate_game(team_b, team_a, False, display_game_result, False, False)
                    team_a_score, team_b_score = game.bottom_score, game.top_score

                if team_a_score == team_b_score:
                    team_a.draw += 1
                    team_b.draw += 1
                elif team_a_score > team_b_score:
                    team_a.win += 1
                    team_b.lose += 1
                else:
                    team_b.win += 1
                    team_a.lose += 1

        teams.sort(key=lambda x: (x.win / (x.win + x.lose)), reverse=True)
        print("###########")
        for i, team in enumerate(teams):
            win_rate = "{:.3f}".format(team.win / (team.win + team.lose))
            print(f"{i + 1}位 {team.name} {team.win}勝 {team.lose}敗 {team.draw}分 勝率:{win_rate}")

        for i, team in enumerate(teams):
            print("###########")
            print(f"{i + 1}位 {team.name} チーム成績")
            team.display_season_team_stats()

        self.display_season_title(teams)

        if display_batter_stats:
            for team in teams:
                for batter in team.players:
                    batter.display_season_stats()

