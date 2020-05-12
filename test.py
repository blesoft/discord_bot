import discord
from discord.ext import commands
import asyncio
import boss

TOKEN = 'NzA5MDMwMTYxMTgxMzExMjI2.Xrf-Fw.68K-J1g6s3sz5dSPFdNWQl6r-Lc'
CHANNEL_ID = 708906395457814538

boss_date_1 = boss.boss_date_formal1
boss_date_2 = boss.boss_date_formal2
boss_date_3 = boss.boss_date_formal3
boss_date_4 = boss.boss_date_formal4
boss_date = boss_date_1

bot = commands.Bot(command_prefix='.')
# 現在の周回数をカウントする
count = 1

# 予約表のlist[何周目][予約メンバー]
# presev_date = [[[boss_date[0][0]],[boss_date[0][1]],[boss_date[0][2]],[boss_date[0][3]],[boss_date[0][4]]]]    
presev_date1 = [[boss.boss_name[0]]for i in range(boss.lap)]  # 1体目
presev_date2 = [[boss.boss_name[1]]for i in range(boss.lap)] # 2体目
presev_date3 = [[boss.boss_name[2]]for i in range(boss.lap)] # 3体目
presev_date4 = [[boss.boss_name[3]]for i in range(boss.lap)] # 4体目
presev_date5 = [[boss.boss_name[4]]for i in range(boss.lap)] # 5体目

# 起動時イベント
@bot.event
async def on_ready():
    print('ログインしました') 

#.init 予約機能開始 or データ初期化
@bot.command()
async def init(ctx):
    await initEvent(ctx,count)

#.now 現在の予約表を表示
@bot.command() 
async def now(ctx):
    await nowEvent(ctx,count)

#.next 次周の予約表を表示
@bot.command()
async def next(ctx):
    await nextEvent(ctx,count)

#.finish 予約表の更新
@bot.command()
async def finish(ctx):
    await finishEvent(ctx,count)

#.set 指定した数字を現在の予約表に更新
@bot.command()
async def set(ctx,number:int):
    await setEvent(ctx,number)

#.help ヘルプ
@bot.command()
async def h(ctx):
    await helpCommand(ctx)


###関数###
async def initEvent(ctx,count):
    if count == 1:
        embed = discord.Embed(title='お破断剣!!!',description='起動します',color=0x4169e1)
        await ctx.send(embed=embed)
        await nowEvent(ctx,count)
    else:
        embed = discord.Embed(title='全ての予約表を初期化します',description='本当に初期化してもよろしいですか?',color=0xff0000)
        await ctx.send(embed=embed)
        @bot.command()
        async def yes(ctx):
            await setEvent(ctx,1)

async def nowEvent(ctx,count):
    embed = discord.Embed(title='第'+str(count)+'周の予約表 お破断剣!!!',description='現在の予約表になります',color=0x4169e1)
    i = 1
    await presev(embed,count,ctx,i)

async def nextEvent(ctx,count):
    count_next = count + 1
    embed = discord.Embed(title='第'+str(count_next)+'周の予約表 お破断剣!!!',description='第'+ str(count_next) + '周の予約表になります',color=0x4169e1)
    i = 0
    await presev(embed,count_next,ctx,i)

async def finishEvent(ctx,count):
    number = count + 1
    await numCount(100)
    embed = discord.Embed(title='Conglaturations!',description='次周の予約表に移ります',color=0x4169e1)
    await ctx.send(embed=embed)
    await nowEvent(ctx,number)

async def setEvent(ctx,number):
    i = int(number)
    await numCount(i)
    embed = discord.Embed(title='予約表セット'+str(number),description='現在の予約表を'+str(number)+'に更新します',color=0x4169e1)
    await nowEvent(ctx,number)

async def helpCommand(ctx):
    embed = discord.Embed(title='コマンド一覧',description='以下コマンド一覧になります',color=0xffd900)
    embed.add_field(name='.init',value='予約機能の開始,または予約表の初期化',inline=False)
    embed.add_field(name='.now',value='現在の予約表を表示',inline=False)
    embed.add_field(name='.next',value='次周の予約表を表示',inline=False)
    embed.add_field(name='.finish',value='周を更新する',inline=False)
    embed.add_field(name='.set (半角数字)',value='指定した周を現在の周に更新する',inline=False)
    embed.add_field(name='注意事項',value='全てのコマンドは半角で打ち込んでください.また,上記のセットコマンドにおいて set と (半角数字) の間に必ず半角スペースを入れてください.わかりづらい,やりにくい,直して欲しいなどありましたらお気軽にお申し付けください.善処します.',inline=False)
    await ctx.send(embed=embed)

async def presev(embed,num:int,ctx,i:int): 
    embed.add_field(name=boss_date[0][0],value='予約 ' + str(len(presev_date1[num])-1) + '  物防:' + str(boss_date[1][0]) + '　魔防:' + str(boss_date[2][0]),inline=False)
    embed.add_field(name=boss_date[0][1],value='予約 ' + str(len(presev_date2[num])-1) + '  物防:' + str(boss_date[1][1]) + '　魔防:' + str(boss_date[2][1]),inline=False)
    embed.add_field(name=boss_date[0][2],value='予約 ' + str(len(presev_date3[num])-1) + '  物防:' + str(boss_date[1][2]) + '　魔防:' + str(boss_date[2][2]),inline=False)
    embed.add_field(name=boss_date[0][3],value='予約 ' + str(len(presev_date4[num])-1) + '  物防:' + str(boss_date[1][3]) + '　魔防:' + str(boss_date[2][3]),inline=False)
    embed.add_field(name=boss_date[0][4],value='予約 ' + str(len(presev_date5[num])-1) + '  物防:' + str(boss_date[1][4]) + '　魔防:' + str(boss_date[2][4]),inline=False)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🐶')
    await msg.add_reaction('🐧')
    await msg.add_reaction('🐱')
    await msg.add_reaction('🐟')
    await msg.add_reaction('🐰')
    msg_id = msg.id
    while 1:
        reaction, user = await bot.wait_for('reaction_add',check=check,timeout=None)
        if str(reaction.emoji) == '🐶':
            await edit_msg(msg,num,i,ctx)
            presev_date1[num].append(user.name)
        if str(reaction.emoji) == '🐧':
            await edit_msg(msg,num,i,ctx)
            presev_date2[num].append(user.name)
        if str(reaction.emoji) == '🐱':
            await edit_msg(msg,num,i,ctx)
            presev_date3[num].append(user.name)
        if str(reaction.emoji) == '🐟':
            presev_date4[num].append(user.name)
            await edit_msg(msg,num,i,ctx)
        if str(reaction.emoji) == '🐰':
            presev_date5[num].append(user.name)
            await edit_msg(msg,num,i,ctx)
            print('#######1111111##########')
            print('#########')
            print(presev_date5)
            print('#########')
            print('#################')

async def edit_msg(msg,num,i,ctx):
    if i == 0:
        embed = discord.Embed(title='第'+str(num)+'周の予約表 お破断剣!!!',description='第'+ str(num) + '周の予約表になります',color=0x4169e1)
    if i == 1:
        embed = discord.Embed(title='第'+str(num)+'周の予約表 お破断剣!!!',description='現在の予約表になります',color=0x4169e1)
        
    embed.add_field(name=boss_date[0][0],value='予約 ' + str(len(presev_date1[num])-1) + '  物防:' + str(boss_date[1][0]) + '　魔防:' + str(boss_date[2][0]),inline=False)
    embed.add_field(name=boss_date[0][1],value='予約 ' + str(len(presev_date2[num])-1) + '  物防:' + str(boss_date[1][1]) + '　魔防:' + str(boss_date[2][1]),inline=False)
    embed.add_field(name=boss_date[0][2],value='予約 ' + str(len(presev_date3[num])-1) + '  物防:' + str(boss_date[1][2]) + '　魔防:' + str(boss_date[2][2]),inline=False)
    embed.add_field(name=boss_date[0][3],value='予約 ' + str(len(presev_date4[num])-1) + '  物防:' + str(boss_date[1][3]) + '　魔防:' + str(boss_date[2][3]),inline=False)
    embed.add_field(name=boss_date[0][4],value='予約 ' + str(len(presev_date5[num])-1) + '  物防:' + str(boss_date[1][4]) + '　魔防:' + str(boss_date[2][4]),inline=False)
    await msg.edit(embed=embed)
    print('#######2222222##########')
    print('#########')
    print(presev_date5)
    print('#########')
    print('#################')

async def numCount(i:int):
    global count
    if i == 100:
        count += 1
    else :
        count = i

async def check(reaction,user):
    emoji = str(reaction,emoji)
    if user.bot == True:    #botは無視
        pass
    else:
        return emoji == '🐶' or emoji == '🐧' or emoji == '🐱' or emoji == '🐟' or emoji == '🐰'

bot.run(TOKEN)