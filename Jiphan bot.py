import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("------------------")
    await client.change_presence(game=discord.Game(name='집한봇 도움말', type=1))

@client.event
async def on_message(message):
    if "집한봇 도움말" == message.content:
        await client.send_message(message.channel, embed=discord.Embed(title="집한봇을 명령시키실러면\n집한못 <할말> 을 쳐주세요!", color=0x00ffbb))

    if "집한봇" == message.content:
        await client.send_message(message.channel, "뭐욧")
    if "집한봇 바보" == message.content:
        await client.send_message(message.channel, "무지개 바아아안사!")
    if "집한봇 뭐해" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 뭐함" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 뭐하냐" == message.content:
        await client.send_message(message.channel, "히오스 갓겜")
    if "집한봇 사랑해" == message.content:
        await client.send_message(message.channel, "You are a gay! okay? okay.")
    if "집한봇 멍청이" == message.content:
        await client.send_message(message.channel, "난 알파고라서 너보다는 똑똑함 ㅅㄱ")
    if "집한봇 123" == message.content:
        await client.send_message(message.channel, "456")
    if "집한봇 집한" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 집한은" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 집한은?" == message.content:
        await client.send_message(message.channel, "천재")
    if "집한봇 456" == message.content:
        await client.send_message(message.channel, "789")
    if "집한봇 화이트" == message.content:
        await client.send_message(message.channel, "내 쫄따구(?)")
    if "집한봇 화이트는" == message.content:
        await client.send_message(message.channel, "내 쫄따구(?)")
    if "집한봇 화이트는?" == message.content:
        await client.send_message(message.channel, "내 쫄따구(?)")

    if message.content.startswith('집한봇 프로필'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x67cbb0)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버이름", value=message.server.name, inline=True)
        embed.add_field(name="계정생성일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await client.send_message(message.channel, embed=embed)

client.run("NTEyNTkwODY0OTA4OTQzMzYw.Dweo-g.rtmJ57uCcRS41C0DZRzsYPU5QNk")
