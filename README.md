🤖 AI Voice Discord Bot

A modular Discord bot built with Python and discord.py, featuring AI integrations and real-time Text-to-Speech (TTS) capabilities.
This project showcases API integration, voice channel automation, modular architecture using Cogs, and scalable bot design.

🚀 Features

🧠 AI Chat Integration

- Integrated with OpenRouter API
- Supports free and experimental models
- Easy model switching
- Structured response handling

🔗 https://openrouter.ai

🎨 AI Image Generation

- Text-to-image generation
- Integrated with Stable Horde API
- Compatible with Stable Diffusion-based models

🔗 https://stablehorde.net

🎤 Voice & TTS System

- Automatically joins voice channels
- Spanish Text-to-Speech (you can change it on the tts.py)
- User control lock system (owner-based control)
- Automatic reading of assigned user's messages
- Manual disconnect command
- Audio playback powered by FFmpeg

⚙️ Architecture

- Modular Cog-based structure
- Organized commands/ folder
- Global error handling
- Environment variable management via .env
- Designed for scalability and future expansion

📌 Note

This project is built for educational and experimental purposes.
Keep in mind that free AI APIs may have usage limits of may not generate what you expect.

I hope to make future improvements but for now this is my bot. :)

🛠️ Setup

Before running the project:

-Create a Discord application and bot at: https://discord.com/developers/applications
- Generate your bot token from the Bot section.
- Invite the bot to your server using the OAuth2 URL generator with admin permissions.
- Add your token to the .env file you will create


I will let you with the steps to clone the repo and run your bot, if you have any new ideas please let me know :D

- Clone the repository
  
    git clone <your-repo>
    cd <your-repo>

- Create a .env file wiht this on it

  DISCORD_TOKEN=your_token
  OPENROUTER_API_KEY=your_api_key
  STABLE_HORDE_API_KEY=your_api_key  # optional


- Install dependencies
  
  pip install -r requirements.txt

- Run the bot
  
  python bot.py or if you're using VS Code just press on the Run option on the top right.
