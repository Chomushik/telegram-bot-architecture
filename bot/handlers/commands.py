from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import Command


router = Router()


@router.message(Command(commands="start"))
async def start_cmd(message: Message):
    await message.answer("Hello")


