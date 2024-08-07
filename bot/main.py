import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from ui_commands import my_commands
from handlers import callbacks, commands, messages


logging.basicConfig(
    level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - [%(name)s - %(filename)s]: %(message)s"
)

logging.getLogger('asyncio').setLevel(logging.ERROR)
logging.getLogger('aiogram').setLevel(logging.ERROR)


async def on_startup():
    logging.info("Bot has beed started")


async def main():
    bot = Bot(config.BOT_TOKEN)
    dp = Dispatcher()

    dp.startup.register(on_startup)
    dp.include_routers(
        callbacks.router,
        commands.router,
        messages.router
    )
    
    await bot.set_my_commands(my_commands)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("The bot has been stopped")
