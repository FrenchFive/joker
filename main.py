print("Joker - Initialization - ...")

import nextcord
from nextcord.ext import commands, application_checks
import os
import random
from PIL import Image

# KEY
#read from file 
with open("discord.password", "r") as file:
    discord_key = file.read()

# Setup the bot
intents = nextcord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='/', intents=intents)

def cands(directory):
    # List all image files in the given directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.endswith(('.png', '.jpg', '.jpeg'))]
    # Randomly pick 5 image paths
    selected_files = random.sample(files, 5)
    return selected_files

async def image_con(paths):
    images = [Image.open(path) for path in paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    # Create a new image with the combined width and max height
    new_img = Image.new('RGB', (total_width, max_height))
    
    x_offset = 0
    for img in images:
        new_img.paste(img, (x_offset, 0))
        x_offset += img.width

    # Save the combined image
    combined_image_path = 'combined_image.jpg'
    new_img.save(combined_image_path)
    return combined_image_path

@bot.slash_command(description="Combine random images into one and send it.")
async def combine(interaction: nextcord.Interaction):
    # Defer the response
    await interaction.response.defer()

    script_dir = os.path.dirname(__file__)
    img_dir = os.path.join(script_dir, "cards")
    image_paths = cands(img_dir)
    result_image_path = await image_con(image_paths)
    
    # Send the result image
    await interaction.followup.send(file=nextcord.File(result_image_path))

bot.run(discord_key)
