from instance.player import PlayerInstance

from simulator.player import Team
from simulator.simulator import Simulator


if __name__ == '__main__':
    simulator = Simulator()
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

    #simulator.simulate_season(japan, stars, 16, False, True, True)
    simulator.simulate_game(japan, stars, False, True, True, False)
