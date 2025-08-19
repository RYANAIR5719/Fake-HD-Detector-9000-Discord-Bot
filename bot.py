import discord
import re
import os

# Intents required to read messages
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# Regex patterns to detect "GeoFS free HD" add-ons
patterns = [
    re.compile(r'(?i)(better\s*res(olution)?(\s*terrain)?)'),
    re.compile(r'(?i)(fake\s*hd|pirat(e|ed)\s*hd|free\s*hd|hd\s*(for\s*free|free))'),
    re.compile(r'(?i)(hd\s*(add[\s-]*on|addon)|geofs\s*(free\s*hd|hd\s*free))'),
    re.compile(r'(?i)(no\s*pay|without\s*(pay|subscription))'),
    re.compile(r'(?i)(google\s*(maps|earth)|apple\s*maps|bing\s*maps|3d\s*tiles?|photogrammetry)'),
    re.compile(r'(?i)(geofs\s*hd|hd\s*watermark|better\s*resolution\s*terrain)')
]

# Replace with your channel ID where logs should be sent
LOG_CHANNEL_ID = 1406701692443033753

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return  # ignore bots

    # Check regex patterns against each message
    for pattern in patterns:
        if pattern.search(message.content):
            log_channel = client.get_channel(LOG_CHANNEL_ID)
            if log_channel:
                await log_channel.send(
                    f"🚨 Possible GeoFS HD mention detected!\n"
                    f"👤 User: {message.author.mention}\n"
                    f"💬 Message: {message.content}\n"
                    f"📍 Channel: {message.channel.mention}"
                )
            break  # stop after first match

# Run bot
client.run(os.getenv("DISCORD_TOKEN"))
