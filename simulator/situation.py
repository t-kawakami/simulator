from typing import Optional, Tuple, Dict, List
from random import random, shuffle

from simulator.player import Player, Play, Team


class GameSituation:
    def __init__(self, top_team: Team, bottom_team: Team):
        self.top_team: Team = top_team
        self.bottom_team: Team = bottom_team
        for i, batter in enumerate(self.top_team.players):
            batter.order = i + 1
        for i, batter in enumerate(self.bottom_team.players):
            batter.order = i + 1
        self.inning_top_situations: List[InningSituation] = []
        self.inning_bot_situations: List[InningSituation] = []
        self.now_inning: int = 1
        self.now_inning_bot: bool = False  # Trueだと裏、Falseだと表
        self.cross = False  # 最終回裏にXがつくか
        self.top_score: int = 0
        self.bottom_score: int = 0

    def print_board_score(self, inning_situation, end_inning):
        if self.cross and inning_situation.inning_bot and inning_situation.inning == end_inning:
            if inning_situation.inning_score == 0:
                return " X"
            return f"{str(inning_situation.inning_score)}X"
        return str(inning_situation.inning_score).rjust(2)

    def print_game_result(self):
        end_inning = len(self.inning_top_situations)
        print("###############################")
        print(f"|　|{'|'.join([str(i + 1).rjust(2) for i in range(end_inning)])}| H| E| S|")
        top_scores = '|'.join([self.print_board_score(i, end_inning) for i in self.inning_top_situations])
        top_hits = str(sum([i.hit_num for i in self.inning_top_situations])).rjust(2)
        top_errors = str(sum([i.error_num for i in self.inning_top_situations])).rjust(2)
        print(f"|{self.top_team.name[0]}|{top_scores}|{top_hits}|{top_errors}|{str(self.top_score).rjust(2)}|")
        bot_scores = '|'.join([self.print_board_score(i, end_inning) for i in self.inning_bot_situations])
        bot_hits = str(sum([i.hit_num for i in self.inning_bot_situations])).rjust(2)
        bot_errors = str(sum([i.error_num for i in self.inning_top_situations])).rjust(2)
        print(f"|{self.bottom_team.name[0]}|{bot_scores}|{bot_hits}|{bot_errors}|{str(self.bottom_score).rjust(2)}|")

    def print_game_player_results(self):
        print("###############################")
        print(self.top_team.name)
        for batter in self.top_team.players:
            batter.display_game_stats()
        print(self.bottom_team.name)
        for batter in self.bottom_team.players:
            batter.display_game_stats()

    def count_inning_pitch(self, inning_situations):
        pitched_out = 0
        for inning_situation in inning_situations:
            pitched_out += min(inning_situation.out_count, 3)
        return f"{str(int(pitched_out / 3))}.{str(pitched_out % 3)}"

    def print_pitcher_results(self):

        self.top_team.pitcher.display_game_pitch_stats(self.count_inning_pitch(self.inning_bot_situations))
        self.bottom_team.pitcher.display_game_pitch_stats(self.count_inning_pitch(self.inning_top_situations))


class InningSituation:
    def __init__(self, inning: int, inning_bot: bool):
        self.inning_start_score: int = 0
        self.inning: int = inning
        self.inning_bot: bool = inning_bot  # Trueだと裏、Falseだと表
        self.inning_score: int = 0
        self.first_base: Optional[Player] = None
        self.second_base: Optional[Player] = None
        self.third_base: Optional[Player] = None
        self.out_count: int = 0
        self.strike_count: int = 0
        self.ball_count: int = 0
        self.hit_num: int = 0
        self.error_num: int = 0
        self.atbat_player: Optional[Player] = None
        self.atbat_batter_idx: int = 0
        self.last_batter_idx: int = 0
        self.positions:Dict[str:Player] = {}

    def set_atbat_player(self, player: Player, batter_idx: int):
        self.atbat_player = player
        self.atbat_batter_idx = batter_idx

    def set_position(self, players: List[Player], pitcher: Player):
        for player in players:
            self.positions[player.position] = player
        self.positions["投"] = pitcher

    def reset_count(self):
        self.strike_count = 0
        self.ball_count = 0

    def call_strike(self):
        self.strike_count += 1
        if self.strike_count == 3:
            self.occurred_strikeout()

    def call_ball(self):
        self.ball_count += 1
        if self.ball_count == 4:
            self.occurred_walk()

    def display_situation(self):
        print("##")
        print(f"{self.inning}回{'裏' if self.inning_bot else '表'} {self.out_count}アウト {self.inning_start_score + self.inning_score}点")
        print(f"打席:{self.atbat_player.name} 投手:{self.positions['投'].name} {self.positions['投'].game_stats.strike_out}K")
        print(f"一塁走者:{self.first_base.name if self.first_base else 'なし'}")
        print(f"二塁走者:{self.second_base.name if self.second_base else 'なし'}")
        print(f"三塁走者:{self.third_base.name if self.third_base else 'なし'}")

    def check_steel(self, display_play_detail=False):
        # 盗塁チェックはランナーが一塁にいるときのみ
        if not self.first_base:
            return
        # ダブルスチールもなし
        if self.second_base:
            return
        if self.first_base.steel_try_ratio >= 1 - random():
            steel_player_name = self.first_base.name
            if success := self.first_base.steel_success_ratio >= 1 - random():
                self.first_base.game_stats.steel_success += 1
                self.second_base = self.first_base
            else:
                self.first_base.game_stats.steel_failed += 1
                self.out_count += 1
            self.first_base = None
            if display_play_detail:
                self.display_situation()
                print(f"盗塁結果: {steel_player_name} {'成功'if success else '失敗'}")

    def check_position(self, tmp_result: Play) -> Tuple[str, Play]:
        # 四球・三振はそのまま
        if tmp_result == Play.walk or tmp_result == Play.strike_out:
            return "", tmp_result

        # ヒットはスーパープレー判定
        if tmp_result == Play.single_hit:
            positions = ["一", "二", "三", "遊", "捕", "投", "左", "右", "中"]
            shuffle(positions)
            def_player = self.positions[positions[0]]
            if def_player.super_play():
                if def_player.position in ["一", "二", "三", "遊", "捕", "投"]:
                    return def_player.position, Play.goro_super
                else:
                    return def_player.position, Play.fly_super
            else:
                return def_player.position, tmp_result
        elif tmp_result in [Play.double_hit, Play.triple_hit, Play.homer]:
            positions = ["左", "右", "中"]
            shuffle(positions)
            def_player = self.positions[positions[0]]
            return def_player.position, Play.fly_super if def_player.super_play() else tmp_result
        # 凡退はエラー判定
        elif tmp_result == Play.fly_positive:
            positions = ["左", "右", "中"]
            shuffle(positions)
            def_player = self.positions[positions[0]]
            return def_player.position, Play.error if def_player.break_error() else tmp_result
        else:
            positions = ["一", "二", "三", "遊", "捕", "投"]
            shuffle(positions)
            def_player = self.positions[positions[0]]
            return def_player.position, Play.error if def_player.break_error() else tmp_result

    def simulate(self, display_play_detail=False):
        self.check_steel(display_play_detail)
        if self.out_count >= 3:
            self.last_batter_idx = 8 if self.atbat_batter_idx == 0 else self.atbat_batter_idx - 1
            return
        pitcher = self.positions["投"]
        position, result = self.check_position(self.atbat_player.check_batting(pitcher))
        if display_play_detail:
            self.display_situation()
        if result == Play.single_hit:
            self.occurred_single(position)
        elif result == Play.double_hit:
            self.occurred_double(position)
        elif result == Play.triple_hit:
            self.occurred_triple(position)
        elif result == Play.homer:
            self.occurred_home_run(position)
        elif result == Play.walk:
            self.occurred_walk()
        elif result in [Play.goro_positive, Play.goro_super]:
            self.occurred_goro_positive_out(position, result == Play.goro_super)
        elif result == Play.goro_negative:
            self.occurred_goro_negative_out(position)
        elif result in [Play.fly_positive, Play.fly_super]:
            self.occurred_fly_positive_out(position, result == Play.fly_super)
        elif result == Play.fly_negative:
            self.occurred_fly_negative_out(position)
        elif result == Play.strike_out:
            self.occurred_strikeout()
        else:
            self.occurred_error(position)
        if self.out_count >= 3:
            self.last_batter_idx = self.atbat_batter_idx

        if display_play_detail:
            result = self.atbat_player.game_stats.batting_results[-1]
            if result.is_super:
                print(f"打席結果: {result.position}{result.result} {self.positions[result.position].name}のスーパープレー！！")
            elif result.result == "エラー":
                print(f"打席結果: {result.position}{result.result}({self.positions[result.position].name})")
            else:
                print(f"打席結果: {result.position}{result.result}")

    def occurred_single(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "安打", False)
        self.hit_num += 1
        self.reset_count()
        if self.third_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        if self.second_base:
            self.third_base = self.second_base
            self.second_base = None
        if self.first_base:
            self.second_base = self.first_base
        self.first_base = self.atbat_player

    def occurred_double(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "二塁打", False)
        self.hit_num += 1
        self.reset_count()
        if self.third_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        if self.second_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.second_base.game_stats.run += 1
        if self.first_base:
            self.third_base = self.first_base
            self.first_base = None
        self.second_base = self.atbat_player

    def occurred_triple(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "三塁打", False)
        self.hit_num += 1
        self.reset_count()
        if self.third_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
        if self.second_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.second_base.game_stats.run += 1
            self.second_base = None
        if self.first_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.first_base.game_stats.run += 1
            self.first_base = None
        self.third_base = self.atbat_player

    def occurred_home_run(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "本塁打", False)
        self.hit_num += 1
        self.reset_count()
        self.inning_score += 1
        self.atbat_player.game_stats.rbi += 1
        self.positions["投"].game_stats.run_allows += 1
        self.atbat_player.game_stats.run += 1
        if self.third_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        if self.second_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.second_base.game_stats.run += 1
            self.second_base = None
        if self.first_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.first_base.game_stats.run += 1
            self.first_base = None

    def occurred_walk(self):
        self.atbat_player.game_stats.set_result(self.inning, "", "四球", False)
        self.reset_count()
        self.positions["投"].game_stats.walk_allows += 1
        if not self.first_base:
            self.first_base = self.atbat_player
        elif not self.second_base:
            self.second_base = self.first_base
            self.first_base = self.atbat_player
        else:
            if self.third_base:
                self.inning_score += 1
                self.atbat_player.game_stats.rbi += 1
                self.positions["投"].game_stats.run_allows += 1
                self.third_base.game_stats.run += 1
            self.third_base = self.second_base
            self.second_base = self.first_base
            self.first_base = self.atbat_player

    def occurred_goro_positive_out(self, position, is_super):
        # 進塁できるゴロアウト。三塁ランナーいれば加点
        self.atbat_player.game_stats.set_result(self.inning, position, "ゴロ", False)
        self.reset_count()
        self.out_count += 1
        if self.out_count >= 3:
            return
        if self.third_base:
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        if self.second_base:
            self.third_base = self.second_base
            self.second_base = None
        if self.first_base:
            self.second_base = self.first_base
            self.first_base = None

    def occurred_goro_negative_out(self, position):
        # 進塁できないゴロアウト。フォースプレーならダブルプレー判定にする
        self.reset_count()
        self.out_count += 1
        if not self.first_base or self.out_count >= 3:
            self.atbat_player.game_stats.set_result(self.inning, position, "ゴロ", False)
            return
        self.out_count += 1
        self.atbat_player.game_stats.set_result(self.inning, position, "併殺", False)
        if self.third_base and self.second_base:
            # 満塁からはホームゲッツーとする
            self.third_base = self.second_base
            self.second_base = self.first_base
            self.first_base = None
        elif self.third_base:
            self.first_base = None
        elif self.second_base:
            # 一二塁からのゴロダブルプレーはパターンが 3つあるが、セカンドとバッタランナーのアウトとする
            self.second_base = self.first_base
            self.first_base = None

    def occurred_fly_positive_out(self, position, is_super):
        # 犠牲フライ可能なフライアウト。二塁→三塁も認める
        self.reset_count()
        self.out_count += 1
        if self.out_count <= 2 and self.third_base:
            self.atbat_player.game_stats.set_result(self.inning, position, "犠牲フライ", is_super)
            self.inning_score += 1
            self.atbat_player.game_stats.rbi += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        else:
            self.atbat_player.game_stats.set_result(self.inning, position, "フライ", is_super)

        if self.out_count <= 2 and self.second_base:
            self.third_base = self.second_base
            self.second_base = None

    def occurred_fly_negative_out(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "フライ", False)
        self.reset_count()
        self.out_count += 1

    def occurred_strikeout(self):
        self.atbat_player.game_stats.set_result(self.inning, "", "三振", False)
        self.positions["投"].game_stats.strike_out += 1
        self.out_count += 1
        self.reset_count()

    def occurred_error(self, position):
        self.atbat_player.game_stats.set_result(self.inning, position, "エラー", False)
        self.positions[position].game_stats.error += 1
        self.error_num += 1
        self.reset_count()
        if self.third_base:
            self.inning_score += 1
            self.positions["投"].game_stats.run_allows += 1
            self.third_base.game_stats.run += 1
            self.third_base = None
        if self.second_base:
            self.third_base = self.second_base
            self.second_base = None
        if self.first_base:
            self.second_base = self.first_base
        self.first_base = self.atbat_player