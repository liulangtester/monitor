from wechaty import Wechaty, Message

async def on_message(msg: Message):
    """
    Message handler for the bot
    """
    if msg.text() == 'ding' and msg.room() is None:
        await msg.say('dong')

async def main():
    """
    Main function to start the bot
    """
    bot = Wechaty()
    bot.on('message', on_message)
    await bot.start()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
