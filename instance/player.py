from simulator.player import Player


class PlayerInstance:
    @staticmethod
    def ichiro(position):
        player = Player("イチロー", position)
        player.at_bat = 3619
        player.hit = 1278
        player.double = 211
        player.triple = 23
        player.homer = 118
        player.walk = 443
        player.strike_out = 333
        player.setup_goro_fly_out(5, 1, 1, 3)
        player.steel_try_ratio = 0.3
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.1
        player.fielding = 0.999
        return player

    @staticmethod
    def ohtani(position):
        player = Player("大谷 翔平", position)
        player.at_bat = 537
        player.hit = 138
        player.double = 26
        player.triple = 8
        player.homer = 46
        player.walk = 100
        player.strike_out = 189
        player.setup_goro_fly_out(3, 1, 4, 2)
        player.steel_try_ratio = 0.15
        player.steel_success_ratio = 0.75
        player.super_fielding = 0.01
        player.fielding = 0.99

        player.control = 0.4
        player.doctor_k = 0.6
        player.pitch_power = 0.55
        player.goro_fly_ratio = 0.5
        return player

    @staticmethod
    def kikuchi(position):
        player = Player("菊池 涼介", position)
        player.at_bat = 5455
        player.hit = 1477
        player.double = 271
        player.triple = 26
        player.homer = 117
        player.walk = 379
        player.strike_out = 984
        player.setup_goro_fly_out(4, 2, 2, 2)
        player.steel_try_ratio = 0.1
        player.steel_success_ratio = 0.7
        player.super_fielding = 0.2
        player.fielding = 0.999
        return player

    @staticmethod
    def genda(position):
        player = Player("源田 壮亮", position)
        player.at_bat = 3042
        player.hit = 827
        player.double = 105
        player.triple = 45
        player.homer = 14
        player.walk = 238
        player.strike_out = 487
        player.setup_goro_fly_out(4, 2, 2, 2)
        player.steel_try_ratio = 0.1
        player.steel_success_ratio = 0.7
        player.super_fielding = 0.2
        player.fielding = 0.99
        return player

    @staticmethod
    def akahoshi(position):
        player = Player("赤星 憲広", position)
        player.at_bat = 4330
        player.hit = 1276
        player.double = 117
        player.triple = 36
        player.homer = 3
        player.walk = 488
        player.strike_out = 664
        player.setup_goro_fly_out(6, 1, 1, 2)
        player.steel_try_ratio = 0.5
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.08
        player.fielding = 0.99
        return player

    @staticmethod
    def murakami(position):
        player = Player("村上 宗隆", position)
        player.at_bat = 1934
        player.hit = 543
        player.double = 98
        player.triple = 3
        player.homer = 160
        player.walk = 408
        player.strike_out = 565
        player.setup_goro_fly_out(2, 2, 5, 1)
        player.steel_try_ratio = 0.05
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.97
        return player

    @staticmethod
    def hatsushiba(position):
        player = Player("初芝 清", position)
        player.at_bat = 5762
        player.hit = 1525
        player.double = 332
        player.triple = 35
        player.homer = 232
        player.walk = 555
        player.strike_out = 1082
        player.setup_goro_fly_out(2, 3, 3, 2)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.3
        player.super_fielding = 0.001
        player.fielding = 0.93
        return player

    @staticmethod
    def yoshida(position):
        player = Player("吉田 正尚", position)
        player.at_bat = 2703
        player.hit = 884
        player.double = 161
        player.triple = 7
        player.homer = 133
        player.walk = 457
        player.strike_out = 300
        player.setup_goro_fly_out(4, 2, 2, 2)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.5
        player.super_fielding = 0.005
        player.fielding = 0.95
        return player

    @staticmethod
    def furuta(position):
        player = Player("古田 敦也", position)
        player.at_bat = 7141
        player.hit = 2097
        player.double = 368
        player.triple = 19
        player.homer = 217
        player.walk = 859
        player.strike_out = 951
        player.setup_goro_fly_out(2, 2, 4, 2)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.5
        player.super_fielding = 0.05
        player.fielding = 0.99
        return player

    @staticmethod
    def betts(position):
        player = Player("M.ベッツ", position)
        player.at_bat = 4460
        player.hit = 1306
        player.double = 307
        player.triple = 33
        player.homer = 213
        player.walk = 558
        player.strike_out = 692
        player.setup_goro_fly_out(4, 1, 4, 1)
        player.steel_try_ratio = 0.15
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.05
        player.fielding = 0.99
        return player

    @staticmethod
    def trout(position):
        player = Player("M.トラウト", position)
        player.at_bat = 5094
        player.hit = 1543
        player.double = 296
        player.triple = 51
        player.homer = 350
        player.walk = 1011
        player.strike_out = 1354
        player.setup_goro_fly_out(2, 1, 5, 2)
        player.steel_try_ratio = 0.2
        player.steel_success_ratio = 0.84
        player.super_fielding = 0.1
        player.fielding = 0.99
        return player

    @staticmethod
    def goldschmidt(position):
        player = Player("P.ゴールドシュミット", position)
        player.at_bat = 5927
        player.hit = 1750
        player.double = 382
        player.triple = 22
        player.homer = 315
        player.walk = 960
        player.strike_out = 1545
        player.setup_goro_fly_out(2, 1, 5, 2)
        player.steel_try_ratio = 0.1
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.05
        player.fielding = 0.98
        return player

    @staticmethod
    def arenado(position):
        player = Player("N.アレナド", position)
        player.at_bat = 5268
        player.hit = 1520
        player.double = 338
        player.triple = 31
        player.homer = 299
        player.walk = 496
        player.strike_out = 852
        player.setup_goro_fly_out(4, 1, 4, 1)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.5
        player.super_fielding = 0.2
        player.fielding = 0.99
        return player

    @staticmethod
    def schwarber(position):
        player = Player("K.シュワーバー", position)
        player.at_bat = 2782
        player.hit = 648
        player.double = 111
        player.triple = 11
        player.homer = 199
        player.walk = 452
        player.strike_out = 918
        player.setup_goro_fly_out(2, 1, 5, 2)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.95
        return player

    @staticmethod
    def jeter(position):
        player = Player("D.ジーター", position)
        player.at_bat = 11195
        player.hit = 3465
        player.double = 544
        player.triple = 66
        player.homer = 260
        player.walk = 1252
        player.strike_out = 1840
        player.setup_goro_fly_out(4, 1, 4, 1)
        player.steel_try_ratio = 0.12
        player.steel_success_ratio = 0.78
        player.super_fielding = 0.2
        player.fielding = 0.98
        return player

    @staticmethod
    def molina(position):
        player = Player("Y.モリーナ", position)
        player.at_bat = 7817
        player.hit = 2168
        player.double = 408
        player.triple = 7
        player.homer = 176
        player.walk = 618
        player.strike_out = 922
        player.setup_goro_fly_out(2, 1, 5, 2)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.65
        player.super_fielding = 0.15
        player.fielding = 0.99
        return player

    @staticmethod
    def arozarena(position):
        player = Player("R.アロサレーナ", position)
        player.at_bat = 1199
        player.hit = 323
        player.double = 76
        player.triple = 6
        player.homer = 20
        player.walk = 141
        player.strike_out = 352
        player.setup_goro_fly_out(4, 1, 4, 1)
        player.steel_try_ratio = 0.25
        player.steel_success_ratio = 0.71
        player.super_fielding = 0.15
        player.fielding = 0.99
        return player

    @staticmethod
    def altuve(position):
        player = Player("J.アルトゥーベ", position)
        player.at_bat = 6305
        player.hit = 1935
        player.double = 379
        player.triple = 29
        player.homer = 192
        player.walk = 573
        player.strike_out = 840
        player.setup_goro_fly_out(6, 1, 2, 1)
        player.steel_try_ratio = 0.3
        player.steel_success_ratio = 0.77
        player.super_fielding = 0.05
        player.fielding = 0.99
        return player

    @staticmethod
    def kershaw(position):
        player = Player("C.カーショー", position)
        player.at_bat = 1000
        player.hit = 150
        player.double = 20
        player.triple = 1
        player.homer = 1
        player.walk = 100
        player.strike_out = 500
        player.setup_goro_fly_out(6, 1, 2, 1)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.5
        player.super_fielding = 0.02
        player.fielding = 0.99

        player.control = 0.6
        player.doctor_k = 0.6
        player.pitch_power = 0.58
        player.goro_fly_ratio = 0.6
        return player

    @staticmethod
    def tanpopo(position, name="たんぽぽ"):
        player = Player(name, position)
        player.at_bat = 5000
        player.hit = 150
        player.double = 20
        player.triple = 1
        player.homer = 1
        player.walk = 15
        player.strike_out = 3600
        player.setup_goro_fly_out(1, 90, 1, 8)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.0
        return player

    @staticmethod
    def watage(position, name="わたげ"):
        player = Player(name, position)
        player.at_bat = 5000
        player.hit = 150
        player.double = 20
        player.triple = 1
        player.homer = 1
        player.walk = 15
        player.strike_out = 3600
        player.setup_goro_fly_out(1, 90, 1, 8)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.0

        player.control = 0.2
        player.doctor_k = 0.05
        player.pitch_power = 0.2
        player.goro_fly_ratio = 0.8
        return player

    @staticmethod
    def tempura(position, name="てんぷら"):
        player = Player(name, position)
        player.at_bat = 5000
        player.hit = 150
        player.double = 20
        player.triple = 1
        player.homer = 1
        player.walk = 15
        player.strike_out = 3600
        player.setup_goro_fly_out(1, 8, 1, 90)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.0
        return player

    @staticmethod
    def banto_geinin(position, name="バント芸人"):
        player = Player(name, position)
        player.at_bat = 5000
        player.hit = 150
        player.double = 20
        player.triple = 1
        player.homer = 1
        player.walk = 15
        player.strike_out = 3600
        player.setup_goro_fly_out(90, 1, 1, 8)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.0
        return player

    @staticmethod
    def konoe(position="一", name="近衛"):
        player = Player(name, position)
        player.at_bat = 500
        player.hit = 150
        player.double = 23
        player.triple = 1
        player.homer = 55
        player.walk = 111
        player.strike_out = 117
        player.setup_goro_fly_out(3, 2, 4, 1)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.99
        return player

    @staticmethod
    def maibara(position="二", name="米原"):
        player = Player(name, position)
        player.at_bat = 500
        player.hit = 140
        player.double = 34
        player.triple = 6
        player.homer = 30
        player.walk = 60
        player.strike_out = 60
        player.setup_goro_fly_out(4, 1, 3, 2)
        player.steel_try_ratio = 0.1
        player.steel_success_ratio = 0.75
        player.super_fielding = 0.05
        player.fielding = 0.98
        return player

    @staticmethod
    def miyazaki(position="遊", name="宮崎"):
        player = Player(name, position)
        player.at_bat = 450
        player.hit = 120
        player.double = 30
        player.triple = 8
        player.homer = 15
        player.walk = 30
        player.strike_out = 40
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.04
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.04
        player.fielding = 0.98
        return player

    @staticmethod
    def kyoto(position="三", name="京都"):
        player = Player(name, position)
        player.at_bat = 500
        player.hit = 130
        player.double = 30
        player.triple = 8
        player.homer = 35
        player.walk = 50
        player.strike_out = 20
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.04
        player.fielding = 0.99
        return player

    @staticmethod
    def iwashiro(position="左", name="岩城"):
        player = Player(name, position)
        player.at_bat = 480
        player.hit = 130
        player.double = 30
        player.triple = 8
        player.homer = 22
        player.walk = 30
        player.strike_out = 40
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.02
        player.fielding = 0.99
        return player

    @staticmethod
    def awaji(position="中", name="淡路"):
        player = Player(name, position)
        player.at_bat = 480
        player.hit = 140
        player.double = 36
        player.triple = 5
        player.homer = 45
        player.walk = 120
        player.strike_out = 90
        player.setup_goro_fly_out(3, 2, 4, 1)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.1
        player.fielding = 0.99
        return player

    @staticmethod
    def nagaoka(position="右", name="長岡"):
        player = Player(name, position)
        player.at_bat = 460
        player.hit = 130
        player.double = 30
        player.triple = 8
        player.homer = 22
        player.walk = 30
        player.strike_out = 40
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.1
        player.steel_success_ratio = 0.7
        player.super_fielding = 0.08
        player.fielding = 0.97
        return player

    @staticmethod
    def nagahama(position="捕", name="永濱"):
        player = Player(name, position)
        player.at_bat = 510
        player.hit = 130
        player.double = 30
        player.triple = 8
        player.homer = 22
        player.walk = 30
        player.strike_out = 40
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.99
        return player

    @staticmethod
    def nitta(position="DH", name="新田"):
        player = Player(name, position)
        player.at_bat = 460
        player.hit = 130
        player.double = 30
        player.triple = 8
        player.homer = 22
        player.walk = 30
        player.strike_out = 40
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.99
        return player

    @staticmethod
    def nagase(position="投", name="長瀬"):
        player = Player(name, position)
        player.super_fielding = 0.01
        player.fielding = 0.99
        player.control = 0.58
        player.doctor_k = 0.57
        player.pitch_power = 0.56
        player.goro_fly_ratio = 0.5
        return player

    @staticmethod
    def power_warrior(position, name):
        player = Player(name, position)
        player.at_bat = 400
        player.hit = 110
        player.double = 30
        player.triple = 1
        player.homer = 35
        player.walk = 80
        player.strike_out = 100
        player.setup_goro_fly_out(2, 3, 4, 1)
        player.steel_try_ratio = 0.01
        player.steel_success_ratio = 0.4
        player.super_fielding = 0.01
        player.fielding = 0.95
        return player

    @staticmethod
    def average_hitter(position, name):
        player = Player(name, position)
        player.at_bat = 400
        player.hit = 140
        player.double = 30
        player.triple = 1
        player.homer = 10
        player.walk = 50
        player.strike_out = 30
        player.setup_goro_fly_out(2, 3, 3, 2)
        player.steel_try_ratio = 0.03
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.01
        player.fielding = 0.98
        return player

    @staticmethod
    def speed_star(position, name):
        player = Player(name, position)
        player.at_bat = 400
        player.hit = 105
        player.double = 30
        player.triple = 8
        player.homer = 5
        player.walk = 30
        player.strike_out = 50
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.2
        player.steel_success_ratio = 0.8
        player.super_fielding = 0.05
        player.fielding = 0.98
        return player

    @staticmethod
    def diffence_star(position, name):
        player = Player(name, position)
        player.at_bat = 400
        player.hit = 105
        player.double = 30
        player.triple = 2
        player.homer = 3
        player.walk = 30
        player.strike_out = 50
        player.setup_goro_fly_out(4, 1, 2, 3)
        player.steel_try_ratio = 0.05
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.1
        player.fielding = 0.999
        return player

    @staticmethod
    def normal(position, name):
        player = Player(name, position)
        player.at_bat = 400
        player.hit = 108
        player.double = 25
        player.triple = 2
        player.homer = 5
        player.walk = 40
        player.strike_out = 60
        player.setup_goro_fly_out(3, 2, 2, 3)
        player.steel_try_ratio = 0.02
        player.steel_success_ratio = 0.6
        player.super_fielding = 0.02
        player.fielding = 0.98
        return player
