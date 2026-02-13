# 🤖 AI Voice Discord Bot

A modular Discord bot built with Python and discord.py, featuring AI integrations and real-time Text-to-Speech (TTS) capabilities. This project showcases API integration, voice channel automation, modular architecture using Cogs, and scalable bot design.

---

## 🚀 Features

### 🧠 AI Chat Integration
- Integrated with **OpenRouter API**
- Supports free and experimental models
- Easy model switching
- Structured response handling

🔗 [OpenRouter](https://openrouter.ai)

### 🎨 AI Image Generation
- Text-to-image generation powered by **Stable Horde API**
- Compatible with Stable Diffusion-based models
- Free tier available

🔗 [Stable Horde](https://stablehorde.net)

### 🎤 Voice & TTS System
- Automatically joins voice channels
- Spanish Text-to-Speech *(configurable in `tts.py`)*
- User control lock system (owner-based control)
- Automatic reading of assigned user's messages
- Manual disconnect command
- Audio playback powered by **FFmpeg**

### ⚙️ Architecture
- **Modular Cog-based structure** for organized code
- Dedicated `commands/` folder
- Global error handling
- Environment variable management via `.env`
- Designed for scalability and future expansion

---

## 📌 Note

This project is built for **educational and experimental purposes**. Keep in mind that free AI APIs may have usage limits or may not always generate expected results.

I hope to make future improvements, but for now, this is my bot. :)

---

## 🛠️ Setup

### Prerequisites

1. **Create a Discord Application**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and add a bot
   - Generate your bot token from the **Bot** section
   - Invite the bot to your server using the **OAuth2 URL Generator** with admin permissions
   - Save your token for the `.env` file

2. **Install FFmpeg** (required for voice/TTS)
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html)
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Create a `.env` file

Create a file named `.env` in the root directory with the following content:

```env
DISCORD_TOKEN=your_discord_bot_token
OPENROUTER_API_KEY=your_openrouter_api_key
STABLE_HORDE_API_KEY=your_stable_horde_api_key  # optional
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the bot

```bash
python bot.py
```

Or if you're using **VS Code**, simply press the **Run** button in the top right corner.

---

## 📝 Usage

Once the bot is running and invited to your server, you can use the following commands:

- **AI Chat**: Interact with AI models through chat commands
- **Image Generation**: Generate images from text prompts
- **Voice Commands**: Join voice channels and use TTS features

*For a full list of commands, check the `commands/` folder or use the help command in Discord.*

---

## 🤝 Contributing

Have ideas for improvements? Feel free to:
- Open an issue
- Submit a pull request
- Share your suggestions!

---

## 📄 License

This project is open source and available for educational purposes.

---

## 🙏 Acknowledgments

- [discord.py](https://github.com/Rapptz/discord.py) - Discord API wrapper
- [OpenRouter](https://openrouter.ai) - AI model access
- [Stable Horde](https://stablehorde.net) - Image generation API

---

**Made with ❤️ for learning and experimentation**
