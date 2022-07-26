import random
from unidecode import unidecode
from typing import Any, AnyStr, List

import discord
from discord.ext import commands



bot = commands.Bot("i!", description="Parce qu'il faut... Je veux dire, parce qu'ELLE faut que les gens se mettent a l'écriture inclusive")
NON_INCLUSIVE_PATTERN = "il"


CORRECTION_PHRASES = [
    "Pardon, je crois que tu voulais dire",
    "Si je puis me permettre",
    "Selon moi, une manière moins faschiste de dire ça serait",
    "On voit que tu es contre le droit des femmes"
]


def find(pattern: AnyStr, array: List[AnyStr]) -> List[int]:
    found = []
    
    for index, element in enumerate(array):
        if pattern in element:
            found.append(element)

    return found


def get_next_word(word: AnyStr, array: List[AnyStr]) -> AnyStr:
    return array[find(word, array)+1] if find(word, array) != len(array)-1 else ""


def get_previous_word(word: AnyStr, array: List[AnyStr]) -> AnyStr:
    return array[find(word, array)-1] if find(word, array) != 0 else ""



@bot.event
async def on_ready():
    print(f"Logged in\n")


@bot.event
async def on_message(message):
    if not NON_INCLUSIVE_PATTERN in unidecode(message.content).lower():
        return
    
    # for non_inclusive_word in find(NON_INCLUSIVE_PATTERN, message.split(' ')):
    
    inclusive_message = message.content.lower().replace("il", "__**elle**__")
    await message.reply(f"{random.choice(CORRECTION_PHRASES)}: {inclusive_message}")
    
    
    await bot.process_commands(message)

        

bot.run("")
