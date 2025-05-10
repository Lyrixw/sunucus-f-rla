import discord
from discord.ext import commands
import aiohttp
import asyncio

async def test_connection():
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get("https://discord.com") as resp:
                print("Bağlantı başarılı:", resp.status)
        except Exception as e:
            print("HATA:", e)

asyncio.run(test_connection())

OWNER_ID = 1174371148897718292  # kendi id

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif !")

@bot.command()
async def temizle(ctx):
    if ctx.author.id != OWNER_ID:
        await ctx.send("Komut iznin yok.")
        return

    
    # Komut : !temizle hiç bi buton yoktur direk başlar sunucu ayarlarını adam akılı yapın olmadı die ağlamayın botun rolunu en üste koyun  

    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Kanal silindi: {channel.name}")
        except Exception as e:
            print(f"Kanal silinemedi: {channel.name} | Hata: {e}")

    
    for role in ctx.guild.roles:
        if role.name != "@everyone":
            try:
                await role.delete()
                print(f"Rol silindi: {role.name}")
            except Exception as e:
                print(f"Rol silinemedi: {role.name} | Hata: {e}")

    await ctx.send(" temizlendi.")

bot.run("koy token")
