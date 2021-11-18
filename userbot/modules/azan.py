# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Asena UserBot - Yusuf Usta

# @NaytSeyd tarafından portlanmıştır.
# @frknkrc44 tarafından düzenlenmiştir.

import requests
from userbot import CMD_HELP
from userbot.events import register
from bs4 import BeautifulSoup
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("azan")

# ████████████████████████████████ #


PLACE = ""


@register(outgoing=True, pattern=r"^\.azan (.*)")
async def get_adzan(adzan):
    await adzan.edit("Gözləyin 🕋")
    if not adzan.pattern_match.group(1):
        LOCATION = PLACE
        if not LOCATION:
            await adzan.edit("`Xaiş bir şəhər adı yazın.`")
            return
    else:
        LOCATION = adzan.pattern_match.group(1)

    # url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    url = f"https://api.pray.zone/v2/times/today.json?city={LOCATION}"
    request = requests.get(url)
    if request.status_code == 500:
        return await adzan.edit(f"Axtardığınız sorğu yalnışdır : `{LOCATION}`")

    parsed = json.loads(request.text)

    city = parsed["results"]["location"]["city"]
    country = parsed["results"]["location"]["country"]
    timezone = parsed["results"]["location"]["timezone"]
    date = parsed["results"]["datetime"][0]["date"]["gregorian"]

    imsak = parsed["results"]["datetime"][0]["times"]["Imsak"]
    subuh = parsed["results"]["datetime"][0]["times"]["Fajr"]
    zuhur = parsed["results"]["datetime"][0]["times"]["Dhuhr"]
    ashar = parsed["results"]["datetime"][0]["times"]["Asr"]
    maghrib = parsed["results"]["datetime"][0]["times"]["Maghrib"]
    isya = parsed["results"]["datetime"][0]["times"]["Isha"]

    result = (
        f"**Namaz vaxtları :**\n\n"
        f"📅 **{date} **\n"
        f"🌏 __{city}__\n\n"
        f"**İmsak //** `{imsak}`\n"
        f"**Sübh //** `{subuh}`\n"
        f"**Zöhr //** `{zuhur}`\n"
        f"**Əsr //** `{ashar}`\n"
        f"**Məğrib //** `{maghrib}`\n"
        f"**İşa //** `{isya}`\n"
    )

    await adzan.edit(result)


Help = CmdHelp('azan')
Help.add_command('azan şəhər adı',  None, 'Namaz vaxtlarını göstərər').add()
CMD_HELP.update({
    "ezanvakti":
    ".ezanvakti <şehir> \
    \nKullanım: Belirtilen şehir için namaz vakitlerini gösterir. \
    \nÖrnek: .ezanvakti istanbul"
})
