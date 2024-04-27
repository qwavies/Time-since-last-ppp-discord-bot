from typing import Final, Union
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

#Load token from somehwere safe
load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
#print(TOKEN)


#get intents from discord
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("(Message was empty because intents were not enabled probably)")
        return
    
    if is_private := user_message[0] == "?":
        user_message = user_message[1:]

    try:
        response: Union[str,None] = get_response(user_message , message.author)
        if isinstance(response,str):
            await message.channel.send(response)
            print(response)
    except Exception as e:
        print(e)


#handling bot startup
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running")


#handling incoming messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


#main entry point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == "__main__":
    main()