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

    def simulate_season(self, team_a:Team, team_b:Team, games, display_lineup, display_batter_stats, display_game_result):
        if display_lineup:
            self.display_lineup(team_a)
            self.display_lineup(team_b)
        team_a_win, team_b_win, draw = 0, 0, 0
        for i in range(games):
            if i % 2 == 0:
                game = self.simulate_game(team_a, team_b, False, display_game_result, False, False)
                team_a_score, team_b_score = game.top_score, game.bottom_score
            else:
                game = self.simulate_game(team_b, team_a, False, display_game_result, False, False)
                team_a_score, team_b_score = game.bottom_score, game.top_score

            if team_a_score == team_b_score:
                draw += 1
            elif team_a_score > team_b_score:
                team_a_win += 1
            else:
                team_b_win += 1

        print("###########")
        print(f"{team_a.name} {team_a_win}勝 {team_b_win}敗 {draw}分")
        print(f"{team_b.name} {team_b_win}勝 {team_a_win}敗 {draw}分")

        if display_batter_stats:
            for batter in team_a.players:
                batter.display_season_stats()
            for batter in team_b.players:
                batter.display_season_stats()

        print("###########")
        print(f"{team_a.name} 　スタッツ")
        team_a.display_season_team_stats()
        print("")
        print(f"{team_b.name}　スタッツ")
        team_b.display_season_team_stats()
