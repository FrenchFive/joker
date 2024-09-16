# JOKER
<sub> Discord Python Card Picker </sub>

# Image Combiner Discord Bot 🤖

This Discord bot, built with Nextcord, allows users to combine random images from a specified directory into a single image. It responds to a slash command within Discord and sends the resulting image as a file attachment.

## Features 🌟

- **Slash Command**: Users can easily trigger the bot using the `/pick` slash command.
- **Image Processing**: Combines multiple images into a single image horizontally.
- **Interactive Responses**: Uses deferred responses to handle longer processing times without timing out.

## Requirements 📋

- Python 3.8 or higher
- Nextcord
- Pillow

## Installation 🛠️

Follow these steps to set up the bot on your local machine:

1. **Clone the Repository**:
   ```bash
   https://github.com/FrenchFive/joker.git
   ```

**Get all required dependencies.**

2. **Get Your Discord Bot Token**: 🔑

To use the bot, you need to set up a bot in the Discord Developer Portal:

- Go to the Discord Developer Portal and click New Application.
- Give your application a name (e.g., "JOKER Bot") and create it.
- In the application dashboard, go to the Bot tab and click Add Bot.
- Under the TOKEN section, click Copy to copy your bot token. You’ll need this to run the bot.
- Save the Key in a file called `discord.password` in the same directory as the project.

3. Create a folder named cards in the project directory:

```
cards
```