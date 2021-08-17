import discord, datetime, random, asyncio

from discord.activity import Game
token = "ODQ5MTQ0OTE1NDIyNDc4MzQ2.YLW51A.5C6x0Htba8KrCkUotwGuM3N0O1g"
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("봇 준비 완료!")
    print(client.user)
    print("===================")
    game = discord.Game("오늘은 영어가 5시 30분이라 늦게까지 된다 히히")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    await member.send(f"어서오세요 {member}")

@client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")
    if message.content == "톡쿤유튜브":
        await message.channel.send("https://www.youtube.com/channel/UCjtxUB9eML_TbClpNtsiL1Q")
    if message.content == "시간표":
        await message.channel.send("https://cdn.discordapp.com/attachments/821613146572718120/859004738686943252/unknown.png")
    if message.content == "네코서버템플릿":
        await message.channel.send("https://discord.new/YcHXWpMTqzj4")
    if message.content == "네코서버주소":
        await message.channel.send("https://discord.gg/J7hn3wcJWe")
    if message.content == "네코유튜브":
        await message.channel.send("https://youtube.com/channel/UCptipCtuP5DdAa9kY_9hamQ")
    if message.content == "ㄴㅋㅊㅇ":
        await message.channel.send("좆까세요")
    if message.content == "네코차이":
        await message.channel.send("ㅇㅇㄴㅇ")
    if message.content == "배고파":
        await message.channel.send("굶어")
    if message.content == ".":
        await message.channel.send("!d bump")
    if message.content == "Daisuke":
        await message.channel.send("https://youtu.be/XUV863a1Lok")






    if message.content == "임베드내놔":
        embed = discord.Embed(colour=discord.Colour.purple(), title="제목", description="설명")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/791955661230702593/859001668674519040/common.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/791955661230702593/859004845225410560/common.png")
        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
        embed.add_field(name="필드 제목", value="필드 설명", inline=False)
        await message.channel.send(embed=embed)
    
    if message.content.startswith(f"!채널메세지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])
    
    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름 / 아이디 / 닉네임 : {user.name} / {user.id} / {user.display_name}")
        await message.channel.send(user.status)
        await message.channel.send(message.author.avatar_url)
    
    if message.content == "서버 유저 불러와":
        await message.channel.send(len(message.guild.members))

    if message.content == "유저 상태 불러와":
        await message.channel.send(message.author.status)
    
    if message.content == "랜덤":
        await message.channel.send(random.randint(1, 10))
        await message.channel.send(random.choice(['가', '나', '다', '라']))

    if message.content == "라인":
        await message.channel.send(random.choice(['탑', '정글','미드', '원딜', '서폿']))
    
    if message.content =="팀":
        await message.channel.send(random.randint(1, 2))

    if message.content == "10초":
        await message.channel.send("시작.")
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 끝.")

    if message.content.startswith(".청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지 삭제 완료.")
    
    if message.content.startswith("!추방"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.kick(member, reason=' '.join(message.content.split(" ")[2:]))
        await message.channel.send("처리완료.")

    if message.content.startswith("!차단"):
        member = message.guild.get_member(int(message.content.split(" ")[1]))
        await message.guild.ban(member, reason=' '.join(message.content.split(" ")[2:]))
        await message.channel.send("처리완료.")

client.run(token)