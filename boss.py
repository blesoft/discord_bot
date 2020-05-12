
#######ボスの名前,各種防御力#####
boss_name = [':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5']
boss1_deffence = [[100,100],[120,120],[140,140],[200,200]] 
boss2_deffence = [[120,120],[140,140],[200,200],[300,500]]
boss3_deffence = [[140,140],[200,200],[300,300],[300,500]]
boss4_deffence = [[10,10],[120,120],[200,300],[300,500]]
boss5_deffence = [[100,100],[120,120],[200,300],[300,500]]
##############################

########## 周回上限数 #########
lap = 50
#############################

# 以下サンプルになります
# マルチタゲの敵には,1つの値に 1000/50/100 のように書き込んでください
# boss_name = [':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5']
# boss1_deffence = (1体目:)[[1段階目/物防,1段階目/魔防],[2段階目/物防,2段階目/魔防],[3段階目/物防,3段階目/魔防],[4段階目/物防,4段階目/魔防]] 
# boss2_deffence = (2体目:)....
# boss3_deffence = ...
# boss4_deffence = ...
# boss5_deffence = ...


###以下特に変更しなくて大丈夫です###
# 1段階目データ
boss_date_formal1 = [[':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5'],
                    [boss1_deffence[0][0],boss2_deffence[0][0],boss3_deffence[0][0],boss4_deffence[0][0],boss5_deffence[0][0]],
                    [boss1_deffence[0][1],boss2_deffence[0][1],boss3_deffence[0][1],boss4_deffence[0][1],boss5_deffence[0][1]]]
# 2段階目データ
boss_date_formal2 = [[':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5'],
                    [boss1_deffence[1][0],boss2_deffence[1][0],boss3_deffence[1][0],boss4_deffence[1][0],boss5_deffence[1][0]],
                    [boss1_deffence[1][1],boss2_deffence[1][1],boss3_deffence[1][1],boss4_deffence[1][1],boss5_deffence[1][1]]]
# 3段階目データ
boss_date_formal3 = [[':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5'],
                    [boss1_deffence[2][0],boss2_deffence[2][0],boss3_deffence[2][0],boss4_deffence[2][0],boss5_deffence[2][0]],
                    [boss1_deffence[2][1],boss2_deffence[2][1],boss3_deffence[2][1],boss4_deffence[2][1],boss5_deffence[2][1]]]
# 4段階目データ
boss_date_formal4 = [[':dog: ボス1',':penguin: ボス2',':cat: ボス3',':fish: ボス4',':rabbit: ボス5'],
                    [boss1_deffence[3][0],boss2_deffence[3][0],boss3_deffence[3][0],boss4_deffence[3][0],boss5_deffence[3][0]],
                    [boss1_deffence[3][1],boss2_deffence[3][1],boss3_deffence[3][1],boss4_deffence[3][1],boss5_deffence[3][1]]]



