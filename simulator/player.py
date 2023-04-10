from typing import List
from random import randint, random
from enum import Enum
from copy import deepcopy

from simulator.stats import GameStats, SeasonStats


class Play(Enum):
    single_hit = "single hit"
    double_hit = "double hit"
    triple_hit = "triple hit"
    homer = "home run"
    walk = "walk"
    goro_super = "goro super play"
    goro_positive = "goro positive out"
    goro_negative = "goro negative out"
    fly_super = "fly super play"
    fly_positive = "fly positive out"
    fly_negative = "fly negative out"
    strike_out = "strike out"
    error = "error"


class Player:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.order = 0  # 試合開始時に設定
        self.at_bat = 0  # 打数を採用
        self.hit = 0
        self.double = 0
        self.triple = 0
        self.homer = 0
        self.walk = 0
        self.goro_ok_out = 0
        self.goro_ng_out = 0  # ダブルプレーになりうる
        self.fly_ok_out = 0  # アウトカウントが 0 or 1 の時、三塁ランナーがホームインする
        self.fly_ng_out = 0
        self.strike_out = 0
        self.steel_try_ratio: float = 0
        self.steel_success_ratio: float = 0
        self.game_stats: GameStats = GameStats()
        self.season_stats: SeasonStats = SeasonStats()
        self.super_fielding: float = 0
        self.fielding: float = 0  # 1に近いほどエラーしづらい

        # pitcher専用
        self.control = 0.5  # 0に近いほど四球確率が上がる。0.5を平均的なコントロールとする
        self.doctor_k = 0.5  # 1に近いほど三振奪取確率が上がる。0.5を平均的な三振奪取能力とする
        self.pitch_power = 0.5  # 1に近いほど被安打率が下がる。0.5を平均的な能力とする
        self.goro_fly_ratio = 0.5  # 1に近いほどゴロが増える。0.5を平均的な比率とする

    def super_play(self):
        if self.super_fielding > random():
            return True
        return False

    def break_error(self):
        if self.fielding < random():
            return True
        return False

    def setup_goro_fly_out(self, goro_ok_ratio, goro_ng_ratio, fly_ok_ratio, fly_ng_ratio):
        mass = goro_ok_ratio + goro_ng_ratio + fly_ok_ratio + fly_ng_ratio
        out = self.at_bat - self.hit - self.walk
        self.goro_ok_out = int(out * goro_ok_ratio / mass)
        self.goro_ng_out = int(out * goro_ng_ratio / mass)
        self.fly_ok_out = int(out * fly_ok_ratio / mass)
        self.fly_ng_out = int(out * fly_ng_ratio / mass)

    def calc_atbat(self):
        single = self.hit - (self.double + self.triple + self.homer)
        plate_appear = self.at_bat + self.walk
        return single, plate_appear

    def display_original_stats(self, order=None):
        single, plate_appear = self.calc_atbat()
        print("###############")
        if order:
            print(f"{order}.{self.name}({self.position})")
        else:
            print(f"{self.name}({self.position})")
        print("打率 {:.3f}".format(self.hit / self.at_bat))
        print("出塁率 {:.3f}".format(obp := ((self.hit + self.walk) / plate_appear)))
        print("長打率 {:.3f}".format(slg := ((single + self.double * 2 + self.triple * 3 + self.homer * 4) / self.at_bat)))
        print("OPS {:.3f}".format(obp + slg))
        mass = (self.goro_ng_out + self.goro_ok_out + self.fly_ng_out + self.fly_ok_out)
        print(f"ゴロ/フライ {int((self.goro_ng_out + self.goro_ok_out) * 100/mass)}/{int((self.fly_ng_out + self.fly_ok_out) * 100/mass)}")
        print("ホームラン率 {:.3f}".format(self.homer / self.at_bat), "三振率 {:.3f}".format(self.strike_out / self.at_bat))
        print("盗塁企画率 {:.3f}".format(self.steel_try_ratio), "盗塁成功率 {:.3f}".format(self.steel_success_ratio))

    def display_game_pitch_stats(self, innings):
        print("###############")
        print(f"投手.{self.name}")
        print(f"{innings}回 {self.game_stats.strike_out}奪三振 {self.game_stats.walk_allows}四球 {self.game_stats.run_allows}失点")

    def display_game_stats(self):
        print("###############")
        print(f"{self.order}.{self.name}({self.position})")
        self.game_stats.print_result()

    def end_game(self):
        self.season_stats.game_stats.append(deepcopy(self.game_stats))
        self.game_stats = GameStats()

    def display_season_stats(self):
        print("###############")
        print(f"{self.order}.{self.name}({self.position})")
        self.season_stats.display_season_player_stats()

    def check_batting(self, pitcher) -> Play:
        single, plate_appear = self.calc_atbat()
        rand_result = randint(1, plate_appear)
        walk = self.walk * (1.0 - pitcher.control) / 0.5
        strike_out = self.strike_out * pitcher.doctor_k / 0.5
        double = self.double * (1.0 - pitcher.pitch_power) / 0.5
        triple = self.triple * (1.0 - pitcher.pitch_power) / 0.5
        homer = self.homer * (1.0 - pitcher.pitch_power) / 0.5
        goro_ok_out = self.goro_ok_out * pitcher.goro_fly_ratio / 0.5
        goro_ng_out = self.goro_ng_out * pitcher.goro_fly_ratio / 0.5
        fly_ok_out = self.fly_ok_out * (1.0 - pitcher.goro_fly_ratio) / 0.5
        fly_ng_out = self.fly_ng_out * (1.0 - pitcher.goro_fly_ratio) / 0.5
        if rand_result <= strike_out:
            return Play.strike_out
        if rand_result <= strike_out + double:
            return Play.double_hit
        if rand_result <= strike_out + double + triple:
            return Play.triple_hit
        if rand_result <= strike_out + double + triple + homer:
            return Play.homer
        if rand_result <= strike_out + double + triple + homer + walk:
            return Play.walk
        if rand_result <= strike_out + double + triple + homer + walk + goro_ok_out:
            return Play.goro_positive
        if rand_result <= strike_out + double + triple + homer + walk + goro_ok_out + goro_ng_out:
            return Play.goro_negative
        if rand_result <= strike_out + double + triple + homer + walk + goro_ok_out + goro_ng_out + fly_ok_out:
            return Play.fly_positive
        if rand_result <= strike_out + double + triple + homer + walk + goro_ok_out + goro_ng_out + fly_ok_out + fly_ng_out:
            return Play.fly_negative
        return Play.single_hit


class Team:
    def __init__(self, name, players: List[Player], pitcher: Player):
        self.name = name
        self.players = players
        self.pitcher = pitcher

    def display_season_team_stats(self):
        atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, steel_success, steel_failed, error = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        for batter in self.players:
            _atbat, _walk, _hit, _single, _double, _triple, _home_run, _rbi, _run, _gisei, _getsu, _steel_success, _steel_failed, _error = batter.season_stats.count_player_stats()
            atbat += _atbat
            walk += _walk
            hit += _hit
            single += _single
            double += _double
            triple += _triple
            home_run += _home_run
            rbi += _rbi
            run += _run
            gisei += _gisei
            getsu += _getsu
            steel_success += _steel_success
            steel_failed += _steel_failed
            error += _error
        SeasonStats.print_stats(atbat, walk, hit, single, double, triple, home_run, rbi, run, gisei, getsu, steel_success,
                         steel_failed, error)
