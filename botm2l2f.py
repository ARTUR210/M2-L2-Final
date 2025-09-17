import discord
from discord.ext import commands
import random
import os
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents) 

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mul(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left * right)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def min(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left - right)

@bot.command()
async def div(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left / right)


@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("Image"))
    with open(f'Image/{img_name}', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

async def get_duck_image_url():
    url = "https://random-d.uk/api/random"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data["url"]

@bot.command(name="duck")
async def duck(ctx):
    """Perintah $duck untuk kirim gambar bebek random"""
    image_url = await get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def daurulang(ctx):
    saran = [
        "Gunakan kembali botol plastik untuk dijadikan pot tanaman.",
        "Kertas bekas bisa digunakan untuk catatan sebelum dibuang.",
        "Jangan buang kardus, gunakan sebagai tempat penyimpanan.",
        "Bawa tas belanja sendiri untuk mengurangi penggunaan kantong plastik.",
        "Kaleng bekas bisa dijadikan wadah alat tulis."
    ]
    await ctx.send(f"Saran daur ulang: {random.choice(saran)}")

bot.run()
