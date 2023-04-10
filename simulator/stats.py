from typing import List

from simulator.result import BattingResult


class SeasonStats:
    def __init__(self):
        self.game_stats: List[GameStats] = []

    def count_player_stats(self):
        atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, error = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        steel_success, steel_failed = 0, 0
        for game_stats in self.game_stats:
            for br in game_stats.batting_results:
                if br.result == "四球":
                    walk += 1
                    continue
                atbat += 1
                if br.result == "安打":
                    hit += 1
                    single += 1
                if br.result == "二塁打":
                    hit += 1
                    double += 1
                if br.result == "三塁打":
                    hit += 1
                    triple += 1
                if br.result == "本塁打":
                    hit += 1
                    home_run += 1
                if br.result == "犠牲フライ":
                    gisei += 1
                if br.result == "併殺":
                    getsu += 1
            rbi += game_stats.rbi
            run += game_stats.run
            steel_success += game_stats.steel_success
            steel_failed += game_stats.steel_failed
            error += game_stats.error
        return atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, steel_success, steel_failed, error

    def display_season_player_stats(self):
        self.print_stats(*self.count_player_stats())

    @staticmethod
    def print_stats(atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, steel_success, steel_failed, error):
        print(f"{atbat}打数 {hit}安打 {walk}四球 {home_run}本塁打 {double}二塁打 {triple}三塁打 {gisei}犠牲フライ {getsu}併殺")
        steel_success_ratio = "{:.3f}".format(steel_success / (steel_success + steel_failed)) if steel_success + steel_failed != 0 else "-"
        print(f"打点:{rbi} 得点:{run} 盗塁:{steel_success} 盗塁死:{steel_failed} 盗塁成功率:{steel_success_ratio}")
        ave = "{:.3f}".format(hit / atbat)
        obp = "{:.3f}".format((hit + walk) / (atbat + walk - gisei))
        slg = "{:.3f}".format((base := single + double * 2 + triple * 3 + home_run * 4) / atbat)
        ops = "{:.3f}".format((hit + walk) / (atbat + walk - gisei) + base / atbat)
        print(f"打率:{ave} 出塁率:{obp} 長打率:{slg} OPS:{ops}")
        print(f"エラー:{error}")


class GameStats:
    def __init__(self):
        self.batting_results: List[BattingResult] = []
        self.rbi = 0
        self.run = 0
        self.steel_success = 0
        self.steel_failed = 0
        self.error = 0

        # 投手として奪った数
        self.strike_out = 0
        self.run_allows = 0
        self.walk_allows = 0

    def set_result(self, inning, position, result, is_super):
        self.batting_results.append(BattingResult(inning, position, result, is_super))

    def print_result(self):
        print([f"{br.position}{br.result}" for br in self.batting_results])
        atbat, walk, hit, home_run = 0, 0, 0, 0
        for br in self.batting_results:
            if br.result == "四球":
                walk += 1
                continue
            atbat += 1
            if br.result.endswith("塁打"):
                hit += 1
            if br.result == "本塁打":
                home_run += 1
        print(f"{atbat}打数 {hit}安打 {walk}四球 {home_run}本塁打")
        print(f"打点:{self.rbi} 得点:{self.run} 盗塁:{self.steel_success} 盗塁死:{self.steel_failed}")
        print(f"エラー: {self.error}")
