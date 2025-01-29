#Bot memberikan pesan selamat datang ke member yg baru join
#Thumbnail akan diberikan secara random 
#Bot memberikan role ke new member


import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

# Daftar thumbnails random
thumbnails = [
    "https://cdn.discordapp.com/attachments/1086169289242976268/1308717915025182720/image0.gif?ex=67483089&is=6746df09&hm=d8c9969ea56767000c8322672353a75c0e4dbd24cee21f0dbb2a2f489de283cb&",  
    "https://cdn.discordapp.com/attachments/1085865647566757958/1285865216009310228/1256550810041454684.gif?ex=67481bcd&is=6746ca4d&hm=54bc7da80cc15d0c8bf96d6d92c24af58034aa9b1727c8817c6c0c12b255c91d&",  
    "https://cdn.discordapp.com/attachments/1085865647566757958/1266583207411712000/animeahhhhh.gif?ex=6747d588&is=67468408&hm=d480965c033166bea9bcc0191f1286cd2fc423e1c8c3985ab8d6b06e56b6f4ce&",  
    "https://cdn.discordapp.com/attachments/1085865647566757958/1311282851668561940/IMG_2860.gif?ex=67484ad2&is=6746f952&hm=df94bb3a0c76f12236591e89417293f8b2fb0410ece967504c4c44131d99ca80&",
    "https://cdn.discordapp.com/attachments/1085865647566757958/1311282852087730237/image0-1_2.gif?ex=67484ad2&is=6746f952&hm=869533ca0fc99e090f2ecb01f9c07fa6eab852a1a9aca694ad7e54e8f726f6ed&"
]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} telah online!!")

@bot.event
async def on_member_join(member):
    # Saluran tempat pesan dikirim
    channel = discord.utils.get(member.guild.text_channels, name="👋┃welcome")
    # ID Role buat new member
    role_id = 1085860594323832842

    # Kasih role ke member yg baru join 
    role = member.guild.get_role(role_id)
    if role:
        try:
            await member.add_roles(role)
            print(f"Role '{role.name}' berhasil diberikan kepada {member.name}")
        except Exception as e:
            print(f"Gagal memberikan role '{role.name}' kepada {member.name}: {e}")
    else:
        print(f"Role dengan ID '{role_id}' tidak ditemukan di server.")

    random_thumbnail = random.choice(thumbnails)

    if channel:
        embed = discord.Embed(
            title=f"Hello cutie {member.mention}! <a:z_SilvervaleLoves:1289848710745817159> "
            "Welcome to xxx server^^",
            description=(
                "<a:z_heart:1289805228450775082> Setelah ini jangan lupa untuk membaca peraturan server di <#1086228959047454802>dan mengambil role di <#1085861625095016548>"
            ),
            color=discord.Color.pink(),
        )
        embed.set_thumbnail(url=random_thumbnail)
        embed.set_footer(
    text=f"We now have {len(member.guild.members)} members!",
    #icon_url="https://i.imgur.com/xyz.png" 
)
        await channel.send(embed=embed)

#Ganti TOKEN dengan token botnya
bot.run("TOKEN") 