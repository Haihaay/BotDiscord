#Bot memberikan pesan selamat datang ke member yg baru join
#Thumbnail akan diberikan secara random 
#Bot memberikan role ke new member


import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

# Daftar thumbnails random, masukkan link nya
thumbnails = [
    "https://thumbnail1",  
    "https://thumbnail2",  
    "https://thumbnail3",  
    "https://thumbnail4",
    "https://thumbnail5"
]

@bot.event
async def on_ready():
    print(f"Bot {bot.user} telah online!!")

@bot.event
async def on_member_join(member):
    # Saluran tempat pesan dikirim
    channel = discord.utils.get(member.guild.text_channels, name="👋┃welcome")
    # ID Role buat new member, masukkan id role nya
    role_id = 12345678910

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
            title=f"Hello cutie {member.mention}!"
            "Welcome to xxx server^^",
            description=(
                "deskripsi"
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