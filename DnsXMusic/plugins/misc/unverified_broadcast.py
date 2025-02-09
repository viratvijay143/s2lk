from DnsXMusic import app
from pyrogram.enums import ChatType
from pyrogram.raw import types
from pyrogram.errors import FloodWait
from asyncio import sleep
from .cleanmode import IS_BROADCASTING

keywords = [
    "LOVE YOU ALL MAMBER", "RAM RAM", "GOOD MORNING", "@sukriti_b",
    "https://envs.sh/Omh.jpg", "https://envs.sh/Omh.jpg", "register", "invitationcode",
    "minimum recharge", "minimum withdraw", "customer service", "any issue contact",
    "🍎", "high salary", "😛", "HI",
    "Sujit bhai", "SAHU BHAI KIDHAR HO",
    "My owner Sukoon bahut cute hai ",
    "\n\n\nDo fast",
    "@II_S_meri_jaan_ll",
    "Aa jao sab ",
    "AAP LOG APNE GROUP MAI MUJHE AAD KARO",
    "@vijaysahu_2",
    "@helper_hu",
    "KAISE HO AAP LOG"
    "@sukriti_b",
    "@helper_hu",
    "@II_S_meri_jaan_ll",
]

async def delm(m):
    try:
        await m.delete()
    except FloodWait as e:
        await sleep(e.value)
def extract_text_from_entities(entities, text):
    extracted_texts = []
    for entity in entities:
        offset = entity.get("offset")
        length = entity.get("length")
        if offset is not None and length is not None:
            extracted_texts.append(text[offset:offset + length])
    return extracted_texts

@app.on_message(group=-99)
async def stop_unverified_gcast(c, m):
    if app.username == "YukkiSongBot":
        if m.chat and m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
            await m.leave_chat(m.chat.id)

    if app.username != "YukkiSongBot" or IS_BROADCASTING or not m.outgoing:
        return

    if m.forward_from_chat and m.forward_from_chat.id == -1002437144325:
        return
    if m.forward_from or m.forward_from_chat:
        await delm(m)

    if m.entities and any(keyword in m.text.lower() for keyword in keywords):
        await delm(m)
