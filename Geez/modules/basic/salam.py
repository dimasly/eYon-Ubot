"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from geezlibs.geez import geez
from geezlibs.geez.helper.basic import edit_or_reply
from geezlibs.geez.helper.PyroHelpers import ReplyCheck
from Geez.modules.basic import add_command_help
from Geez import cmds

@geez("p", cmds)
async def salamone(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@geez("pe", cmds)
async def salamdua(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Assalamualaikum Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@geez("l", cmds)
async def jwbsalam(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam...",
            reply_to_message_id=ReplyCheck(message),
        ),
    )


@geez("el", cmds)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Wa'alaikumsalam Warahmatullahi Wabarakatuh",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

        
@geez("pp", cmds)
async def proses(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Pesanan mu sedang di proses mohon menunggu sesuai dengan antrian",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

    
@geez("pay", cmds)
async def bayar(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Lakukan Pembayaran di @YokPay jangan lupa kirim bukti tf",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

    
@geez("done", cmds)
async def selesai(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "Terimakasih telah belanja di @NusantaraStores",
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
    
    
@geez("as", cmds)
async def salamarab(client: Client, message: Message):
    xx = await edit_or_reply(message, "Salam Dulu Gua..")
    await asyncio.sleep(2)
    await xx.edit("السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

add_command_help(
    "salam",
    [
        [f"{cmds}p", "Assalamualaikum."],
        [f"{cmds}pe", "Assalamualaikum Warahmatullahi Wabarakatuh."],
        [f"{cmds}l", "Wa'alaikumsalam."],
        [f"{cmds}as", "Assalamualaikum Bahas arab."],
    ]
)
