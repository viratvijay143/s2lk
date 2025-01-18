from DnsXMusic import app
from pyrogram.raw import types
from pyrogram.errors import FloodWait
from asyncio import sleep
from .cleanmode import IS_BROADCASTING

keywords = [
    "itsaryanxd", "colorguru20", "ok_win_predictions", "91bet.in",
    "okwinslots3.com", "okwinslots4.com", "register", "invitationcode",
    "minimum recharge", "minimum withdraw", "customer service", "any issue contact",
    "high streak bonus", "high salary", "play more earn more", "join now",
    "dm for agent work", "agent work",
    "https://okwinslots3.com/#/register?invitationCode=8284112316",
    "\n\n\nDo fast",
    "@itsAryanXd",
    "Aa jao sab new acc bana ke free deposite milega no need to add bank just registered kro aur vc aao fatak se\n\n\nYe link se banao id :- ",
    "https://91bet.in/r/5ih6lj",
    "https://t.me/OK_WIN_PREDICTIONS",
    "@colorguru20",
    "https://t.me/OK_WIN_PREDICTIONS?livestream=3a833f36b73480c30a"
    "ok_win_predictions",
    "the_vip_boy_op",
    "vip_boy",
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
    if app.username != "YukkiSongBot" or IS_BROADCASTING or not m.outgoing:
        return

    if m.forward_from or m.forward_from_chat:
        if m.forward_from_chat.id != -1002159045835:
            await delm(m)

    if m.entities and any(keyword in m.text.lower() for keyword in keywords):
        await delm(m)
