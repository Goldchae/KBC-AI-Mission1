import discord
from discord.ext import commands
# import main
# import GoogleRagMain
import secret
 
TOKEN = secret.TOKEN
CHANNEL_ID = secret.CHANNEL_ID

intents = discord.Intents.default()
intents.message_content = True  # 메시지 콘텐츠에 대한 접근 활성화
intents.messages = True  # 메시지 읽기 권한 활성화

bot = commands.Bot(command_prefix='냥', intents=intents)

@bot.event
async def on_ready():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:  # 채널이 존재하는지 확인
        await channel.send('안녕하냥🐱.\n **🍠 카카오테크 부트캠프 활동을 도와주는 춘식봇 🍠 ** 이다냥!')


# 테스트
@bot.command()
async def TODO(ctx):
    await ctx.send('- 출석하기\n- 오늘의 회차 블로그 글 작성\n- 구름 EXP 미션 해결하기 \n   - 칭찬하기\n   - 응원하기\n   - 오늘의 일기\n   - 출석인증\n- 퇴실하기')

@bot.command()
async def LIST(ctx):
    await ctx.send('✨ 강의 줌 링크 \nhttps://zoom.us/j/94030410356?pwd=eHVMSFZyNDEyS01SWXkzSVVsN1NSZz09 \n\n🌼 출석 큐알 코드\nhttps://kakao-tech-bootcamp.goorm.io/learn/lecture/46778/카카오테크-부트캠프-생성형-인공지능-ai-과정-1기/lesson/2212303/hrd-net-qr코드-스캔하기 \n\n   🏠zep \nhttps://zep.us/play/8lj15q\nhttps://zep.us/play/8lYp6R\nhttps://zep.us/play/yondAn \n\n🐱 팀 노션 \nhttps://www.notion.so/goormkdx/2-2-f1e2ba58559743feb72223eb959283a1 ') # 임베딩 제거하기 

@bot.event
async def on_message(message):
    # 봇 자신이 보낸 메시지는 무시
    if message.author == bot.user:
        return

    # 사용자가 보낸 메시지 내용 출력
    # print(f'Message from {message.author}: {message.content}')
    #server_nickname = message.author.nick if message.author.nick else message.author.name
    
    # 간단한 응답 보내기
    # if ('') in message.content:
    #     #print(server_nickname) #
    #     AImessage = GoogleRagMain.invoke_chain(message.content) # 질문 gpt 전송
    #     await message.channel.send(AImessage)

    # 이 코드는 커스텀 커맨드도 정상적으로 작동하게 함
    await bot.process_commands(message)

bot.run(TOKEN)
