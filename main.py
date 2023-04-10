from instance.player import PlayerInstance
from simulator.player import Team
from simulator.simulator import Simulator

japan = Team("ジャパン", [
    PlayerInstance.ichiro("右"),
    PlayerInstance.ohtani("DH"),
    PlayerInstance.murakami("三"),
    PlayerInstance.yoshida("左"),
    PlayerInstance.furuta("捕"),
    PlayerInstance.akahoshi("中"),
    PlayerInstance.hatsushiba("一"),
    PlayerInstance.kikuchi("二"),
    PlayerInstance.genda("遊"),
], PlayerInstance.ohtani("投"))

trouts = Team("トラウツ", [
    PlayerInstance.trout("一"),
    PlayerInstance.trout("二"),
    PlayerInstance.trout("三"),
    PlayerInstance.trout("遊"),
    PlayerInstance.trout("左"),
    PlayerInstance.trout("中"),
    PlayerInstance.trout("右"),
    PlayerInstance.trout("捕"),
    PlayerInstance.trout("DH"),
], PlayerInstance.ohtani("投"))

stars = Team("スーパースターズ", [
    PlayerInstance.betts("右"),
    PlayerInstance.trout("中"),
    PlayerInstance.jeter("遊"),
    PlayerInstance.arenado("三"),
    PlayerInstance.goldschmidt("一"),
    PlayerInstance.altuve("二"),
    PlayerInstance.schwarber("DH"),
    PlayerInstance.arozarena("左"),
    PlayerInstance.molina("捕"),
], PlayerInstance.kershaw("投"))

super_hiroshima = Team("アレ広", [
    PlayerInstance.miyazaki(),
    PlayerInstance.maibara(),
    PlayerInstance.awaji(),
    PlayerInstance.konoe(),
    PlayerInstance.kyoto(),
    PlayerInstance.nitta(),
    PlayerInstance.iwashiro(),
    PlayerInstance.nagahama(),
    PlayerInstance.nagaoka(),
], PlayerInstance.nagase())

npbs = Team("プロ連合", [
    PlayerInstance.speed_star("中", "黒鱒"),
    PlayerInstance.average_hitter("二", "猫屋敷"),
    PlayerInstance.normal("三", "神田"),
    PlayerInstance.power_warrior("一", "ゴメス"),
    PlayerInstance.normal("左", "森内"),
    PlayerInstance.normal("右", "久米"),
    PlayerInstance.normal("DH", "バレンズエラ"),
    PlayerInstance.normal("捕", "鬼怒"),
    PlayerInstance.diffence_star("遊", "武者小路"),
], PlayerInstance.normal("投", "菅井"))

tanpopo = Team("たんぽぽ製作所", [
    PlayerInstance.tanpopo("右", "たんぽぽ"),
    PlayerInstance.tempura("左", "てんぷら"),
    PlayerInstance.banto_geinin("中", "つくし"),
    PlayerInstance.tanpopo("一", "ひのき"),
    PlayerInstance.tempura("二", "さしみ"),
    PlayerInstance.banto_geinin("DH", "おから"),
    PlayerInstance.tanpopo("三", "おけら"),
    PlayerInstance.tempura("捕", "ぽんかん"),
    PlayerInstance.banto_geinin("遊", "いよかん"),
], PlayerInstance.watage("投", "わたげ"))

if __name__ == '__main__':
    simulator = Simulator()
    #simulator.simulate_season([japan, npbs, stars, super_hiroshima], 54, False, False, False)
    simulator.simulate_game(stars, super_hiroshima, True, True, True, True)
