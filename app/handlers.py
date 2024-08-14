# import asyncio
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, CommandObject
from aiogram.enums import ChatAction

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.bot.send_chat_action(
        chat_id=message.from_user.id,
        action=ChatAction.TYPING
    )
    # await asyncio.sleep(2)
    await message.reply('Привет!', reply_markup=kb.inline_main)
    await message.answer('Какие дела, бро?')


@router.message(Command('photo'))
async def cmd_photo(message: Message) -> None:
    await message.answer_photo(photo='https://ru.freepik.com/free-photo/close-up-kitten-surrounded-by-flowers_65553494.htm#query=кошки&position=12&from_view=keyword&track=ais_hybrid&uuid=3b64089f-c96d-402e-81c5-6300ec8b7a4b',
                               caption='Вот фото котика)')


@router.message(F.text == 'привет')
async def echo(message: Message) -> None:
    await message.reply(
        f'Привет, {message.from_user.first_name}!'
    )
    await message.answer('Какой у тебя вопрос)?')


@router.message(F.photo)
async def echo(message: Message) -> None:
    photo_id = message.photo[-1].file_id
    await message.answer_photo(photo=photo_id,
                               caption='Это ваше фото')


@router.message(F.document)
async def echo(message: Message) -> None:
    await message.answer_document(document=message.document.file_id)


@router.message(F.audio)
async def echo(message: Message) -> None:
    await message.answer_audio(
        audio=message.audio.file_id
        )


@router.message(F.animation)
async def echo(message: Message) -> None:
    await message.answer_animation(
        animation=message.animation.file_id
        )
    await message.answer('Это стикер)')


@router.message(Command('take'))
async def cmd_take(
        message: Message,
        command: CommandObject
) -> None:
    value1, value2 = command.args.split(' ', maxsplit=1)
    value3 = int(value1) + int(value2)
    await message.reply(f'Я сложил твои числа и получилось {value3}')


@router.callback_query(F.data == 'basket')
async def basket(callback: CallbackQuery) -> None:
    await callback.answer('Выбрана корзина', show_alert=True)
    await callback.message.answer('Корзина пуста')


@router.callback_query(F.data == 'contact')
async def contact(callback: CallbackQuery) -> None:
    await callback.answer('WTF MATHER F*CKER?????')
    await callback.message.answer('HEY GAY!', reply_markup=await kb.catalog())
