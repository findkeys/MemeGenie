import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import os

bot = commands.Bot(command_prefix='!',intents=discord.Intents.all())

@bot.command()
async def meme(ctx, image_name, *text):
    image_path = f'images/{image_name}.png'
    if not os.path.exists(image_path):
        await ctx.send(f"Image '{image_name}' not found.")
        return

    # Load the image
    image = Image.open(image_path)

    # Load the font
    font = ImageFont.truetype('impact.ttf', 50)

    # Add text to the image
    draw = ImageDraw.Draw(image)
    text = ' '.join(text)
    draw.text((10, 10), text, font=font, fill='black')

    # Save the modified image
    image.save('meme.png')

    # Send the modified image
    await ctx.send(file=discord.File('meme.png'))



bot.run('TOKEN')
