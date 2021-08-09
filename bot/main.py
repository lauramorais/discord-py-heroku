import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if "fingers in her ass" in msg:
        await message.channel.send('https://www.youtube.com/watch?v=0fgHac3sOW0')

    if "porn addiction" in msg:
        await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874317320464510986/step.mp4')

    if "surgery" in msg:
     await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874318134549565460/surgery.mp4')

    if "bruh moment" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874318631838830722/bm.mp4')

    if "i love beastars so much" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874318779935490048/bs.mp4')

    if "my name is lucy" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874328423361818765/who_is_she.mp4')

    if message.content.startswith('what the hell'):
      await message.channel.send('https://tenor.com/view/nagito-komaeda-neil-cicierega-lemon-demon-mmd-what-the-hell-gif-17669723')

    if "hampster" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874339285673852988/hampster.mp4')

    if "bingus death" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874361342268670032/bingus_death.gif')

    if "bingus genocide" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874361809480593458/bingus_death2.gif')

    if "bingus ethnostate" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874362333261099078/bingus.gif')

    if "out of touch thursday" in msg:
      await message.channel.send('https://www.youtube.com/watch?v=pWX73Op-V7c')

    if "elon musk fancam" in msg:
      await message.channel.send('https://www.youtube.com/watch?v=Xs7Hpzry7Sw')

    if "he's just troyna go vegan" in msg:
      await message.channel.send('https://cdn.discordapp.com/attachments/862308719819489303/874370990392614912/unknown.png')

    if "ari" in message.content:
      await message.add_reaction("🩸")

    if "gegg" in message.content:
      await message.add_reaction("🥚")

    if "george" in message.content:
      await message.add_reaction("🥚")

    if "bushy" in message.content:
      await message.add_reaction("🇵🇸")

    if "loai" in message.content:
      await message.add_reaction("😶")

    if "belomy" in message.content:
      await message.add_reaction("🍈")

    if "luka" in message.content:
      await message.add_reaction("🍈")

    if "bomb televiv" in message.content:
      await message.add_reaction("💣")
      await message.add_reaction("🇮🇱")

    if "israhell" in message.content:
      await message.add_reaction("💣")
      await message.add_reaction("🇮🇱")

    if "diabetes" in message.content:
      await message.add_reaction("🇵🇸")

    if "emlons" in message.content:
      await message.add_reaction("🍈")

    if "beloms" in message.content:
      await message.add_reaction("🍈")

    if "mamma mia" in message.content:
      await message.add_reaction("🩸")

client.run(os.getenv('TOKEN'))