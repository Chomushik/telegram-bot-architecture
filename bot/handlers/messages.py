from aiogram import Router
from aiogram.types import Message


router = Router()


@router.message()
async def message_handle(message: Message):
    await message.send_copy(message.chat.id)


