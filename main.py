# coding=utf-8
import discord
import os
from keep_alive import keep_alive
from numpy import array
from math import *
from replit import db
from time import sleep
from random import randint, choices
from PIL import Image
import numpy as np
from datetime import datetime
import asyncio
from discord.ext import commands
bot = commands.Bot(command_prefix=".", intents = discord.Intents.default())
import typing
from discord.ext.tasks import loop

authors = [373707498479288330, 743371453730127872]
keys = db.prefix("")
print(keys)
defaulttime = datetime.utcnow()
database = [[None, None]]
defaultoption = [True, False, 0x000000, 0, False, False, False, False]
#v.o.l., unused, color, language, privacy, link to dex, see game stats (secret), Color depending on rarity (secret)

buyableitems = [[1, "Pokéball", 200], [2, "Greatball", 300], [3, "Ultraball", 750], [4, "Masterball", 100000], [5, "Recoilball", 500], [6, "Beastball", 10000], [7, "Quickball", 1000], [8, "Dreamball", 5000], [9, "Cloneball", 5000], [10, "Premier ball", "-"], [11, "Fifty-fifty ball", 5000], [12, "Amulet coin", 5000000], [13, "Fake razz", 5000], [14, "Rare razz", 5000]]
#10 : Premier ball
listballs = ["pb", "gb", "ub", "mb", "rb", "bb", "qb", "db", "cb", "prb", "fb"]
releasemoney = [150, 300, 600, 1000, 1200, 1500, 5000, 10000, 7500, 1000000, 5000]
catchrate = [71, 55, 50, 40, 30, 15, -5, -10, -20, -99, -1000]
#commoncr, uncommoncr, rarecr, rarercr, veryrarecr, pseudolegendarycr, legendarycr, mythicalcr, ultrabeatcr, godcr, eggcr
ballcr = [10, 15, 25, 0, 100, 20, 15, 10, 10, 10, 0]
rarityname = ["Common", "Uncommon", "Rare", "Rarer", "Very Rare", "Pseudo legendary", "Legendary", "Mythical", "Ultra-beast", "God", "Egg", "Unknown"]

spawnweight = [1511000000, 750000000, 150000000, 50000000, 7000000, 5000000, 1890000, 20000, 10000, 1]

commonpool = [10, 11, 13, 14, 16, 19, 21, 27, 29, 32, 37, 39, 41, 43, 46, 48, 50, 52, 54, 56, 58, 60, 63, 66, 69, 72, 73, 74, 77, 79, 81, 84, 86, 88, 90, 92, 95, 96, 98, 100, 104, 109, 114, 116, 118, 120, 129, 161, 162, 163, 165, 166, 167, 168, 177, 183, 187, 188, 190, 191, 193, 194, 198, 200, 204, 207, 209, 216, 218, 220, 222, 228, 231, 234, 238, 261, 263, 265, 270, 273, 276, 278, 283, 285, 287, 290, 293, 296, 304, 307, 309, 316, 318, 320, 322, 325, 328, 331, 339, 341, 343, 353, 355, 361, 363, 366, 370, 396, 399, 401, 403, 406, 412, 415, 417, 418, 420, 422, 425, 427, 431, 433, 434, 436, 449, 451, 453, 458, 459, 504, 506, 509, 511, 513, 515, 519, 522, 524, 527, 529, 532, 535, 540, 543, 546, 548, 551, 554, 557, 559, 562, 568, 572, 574, 577, 580, 582, 585, 590, 592, 595, 599, 602, 607, 613, 619, 659, 661, 664, 669, 672, 674, 676, 677, 682, 684, 686, 688, 690, 692, 694, 703, 708, 710, 712, 714, 731, 734, 736, 739, 742, 746, 749, 751, 753, 755, 757, 759, 761, 769, 771, 775]

uncommonpool = [12, 15, 17, 20, 22, 23, 25, 28, 30, 33, 35, 40, 42, 44, 47, 49, 51, 53, 55, 57, 61, 67, 70, 75, 82, 85, 89, 91, 93, 97, 99, 102, 105, 110, 111, 119, 121, 127, 137, 138, 140, 164, 178, 179, 182, 189, 192, 195, 201, 202, 203, 210, 211, 214, 215, 217, 219, 221, 223, 226, 232, 236, 239, 240, 262, 264, 266, 268, 274, 277, 279, 284, 286, 288, 291, 294, 299, 300, 305, 308, 310, 311, 312, 313, 314, 315, 317, 326, 327, 329, 332, 342, 345, 347, 354, 356, 357, 358, 364, 367, 368, 397, 400, 402, 404, 408, 410, 413, 414, 419, 421, 423, 432, 456, 505, 507, 510, 512, 514, 516, 517, 520, 525, 528, 533, 536, 541, 547, 549, 552, 556, 558, 560, 564, 566, 573, 575, 578, 581, 583, 586, 588, 591, 597, 600, 603, 605, 608, 616, 618, 620, 624, 660, 662, 665, 667, 670, 673, 675, 678, 679, 683, 685, 693, 696, 698, 702, 707, 711, 732, 735, 737, 743, 747, 750, 752, 754, 756, 758, 762, 764, 770, 774, 777, 779]

rarepool = [1, 4, 7, 18, 24, 36, 38, 45, 59, 62, 64, 68, 71, 78, 80, 83, 87, 101, 103, 106, 107, 108, 112, 113, 117, 122, 123, 124, 125, 126, 128, 139, 141, 152, 155, 158, 170, 180, 184, 186, 205, 224, 225, 229, 233, 235, 237, 241, 252, 255, 258, 267, 269, 271, 280, 292, 297, 301, 302, 303, 319, 323, 324, 333, 335, 336, 337, 338, 340, 344, 346, 348, 351, 352, 359, 362, 369, 387, 390, 393, 405, 409, 411, 416, 424, 426, 428, 429, 430, 435, 450, 452, 454, 455, 457, 495, 498, 501, 508, 521, 523, 530, 531, 534, 537, 538, 539, 542, 544, 550, 553, 555, 561, 563, 565, 567, 569, 584, 587, 589, 593, 594, 596, 598, 601, 606, 609, 614, 615, 617, 622, 625, 626, 650, 653, 656, 663, 666, 668, 680, 687, 689, 691, 695, 697, 699, 701, 709, 713, 715, 722, 725, 728, 733, 738, 740, 741, 744, 748, 760, 763, 776]

rarerpool = [2, 5, 8, 26, 31, 34, 65, 76, 94, 115, 130, 133, 142, 153, 156, 159, 171, 181, 185, 199, 208, 213, 227, 230, 253, 256, 259, 272, 275, 281, 295, 306, 349, 365, 388, 391, 394, 398, 460, 496, 499, 502, 518, 526, 545, 576, 579, 604, 631, 632, 651, 654, 657, 671, 681, 723, 726, 729, 745, 765, 766, 767, 781]

veryrarepool = [3, 6, 9, 131, 132, 134, 135, 136, 143, 154, 157, 160, 169, 172, 173, 174, 175, 176, 196, 197, 206, 212, 242, 254, 257, 260, 282, 289, 298, 321, 330, 334, 350, 360, 389, 392, 395, 407, 437, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 497, 500, 503, 621, 623, 652, 655, 658, 700, 724, 727, 730, 768, 778, 780]

pseudolegendarypool = [147, 148, 149, 246, 247, 248, 371, 372, 373, 374, 375, 376, 443, 444, 445, 610, 611, 612, 633, 634, 635, 704, 705, 706, 782, 783, 784, ]

legendarypool = [144, 145, 146, 150, 243, 244, 245, 249, 250, 377, 378, 379, 380, 381, 382, 383, 384, 480, 481, 482, 483, 484, 485, 486, 487, 488, 638, 639, 640, 641, 642, 643, 644, 645, 646, 716, 717, 718, 772, 773, 785, 786, 787, 788, 789, 790, 791, 792, 800]
mythicalpool = [151, 251, 385, 386, 489, 490, 491, 492, 494, 647, 648, 649, 719, 720, 721, 801, 802]
ultrabeastpool = [793, 794, 795, 796, 797, 798, 799, 803, 804, 805, 806, 807]
god = [493]

egg = [438, 439, 440, 441, 442, 446, 447, 448, 570, 571, 627, 628, 629, 630, 636, 637]
#438, 439, 440, 441, 442, 446, 447, 448, 570, 571, 627, 628, 629, 630, 636, 637
@bot.event
async def on_ready():
  print("Logged in as {0.user}".format(bot))

@loop(seconds = 60)
async def updata():
  print(datetime.utcnow())
  print("Database "+str(len(database)))
  length = len(database)
  for i in range(1, length):
    db["player_data"+database[length-i][0]] = database[length-i][1]
    database.pop(length-i)

##Options updater
def optionupdater():
  keys = db.prefix("option")
  for data in keys:
    newdatas = db[data]
    while len(newdatas) > len(defaultoption):
      newdatas.pop()
    if len(newdatas) < len(defaultoption):
      for i in range(len(newdatas), len(defaultoption)):
        newdatas.append(defaultoption[i])
      db[data] = newdatas

##Player_data updater
def dataupdater():
  keys = db.prefix("player_data")
  datas = [None, 2, [False for _ in range(len(dex))], [0 for _ in range(len(dex))], [0 for _ in range(len(dex))], [False for _ in range(len(dex))], [None, None, None, None, None, None], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(len(dex))], 2, 1000, [20, 10, 5]+[0 for _ in range(997)], 0, 0, [0 for _ in range(len(dex))], 1000, False, [0 for _ in range(len(dex))], 0, [1, 1, 1], [None, None], [], [False, 0, 0], [0, 0, 0], [0 for _ in range(15)], 0   ]
  datanumbers = len(datas) #Voir game.py
  for data in keys:
    newdatas = db[data]
    while len(newdatas) > datanumbers:
      newdatas.pop()
    if len(newdatas) < datanumbers:
      for i in range(len(newdatas), datanumbers):
        newdatas.append(datas[i])
      db[data] = newdatas

def setlanguage(id):
  keys = db.prefix("option")
  if "option"+str(id) in keys:
    return db["option"+str(id)][3]
  else:
    return 0

def setoption(id):
  keys = db.prefix("option")
  if "option"+str(id) in keys:
    return db["option"+str(id)]
  else:
    db["option"+str(id)] = defaultoption
    return defaultoption

def setdata(id, name, create = False):
  keys = db.prefix("player_data")
  id = str(id)
  if "player_data"+id in keys:
    for i in range(len(database)):
      if id == database[i][0]:
        return database[i][1]
    datas = db["player_data"+id]
    database.append([id, datas])
    return database[-1][1]
  else:
    if create:
      datas = [str(name), 2, [False for _ in range(len(dex))], [0 for _ in range(len(dex))], [0 for _ in range(len(dex))], [False for _ in range(len(dex))], [None, None, None, None, None, None], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(len(dex))], 2, 1000, [20, 10, 5]+[0 for _ in range(997)], 0, 0, [0 for _ in range(len(dex))], 1000, False, [0 for _ in range(len(dex))], 0, [1, 1, 1], [None, None], [], [False, 0, 0], [0, 0, 0], [0 for _ in range(15)], 0    ]
      db["player_data"+id] = datas
      return datas

def additems(item, amount, id, name):
  try:
    item = int(item) -1
    if item < len(buyableitems) and amount > 0:
      datas = setdata(id, name)
      price = buyableitems[item][2]*amount
      if price > datas[9]:
        return False, False, 51
      if datas[10][10] + amount > 50 and item == 10: #Amulet coins
        return False, False, 51
      if True: #À modifier ?
        datas[10][item] += amount
        datas[9] -= price
        if item == 0 and amount > 9:
          datas[10][9] += amount//10
        db["player_data"+str(id)] = datas
        return True, datas[9], datas[10][10]
    return False, False, 51
  except:
    return False, False, 51

play_cooldown = 5
languages = ["en", "fr", "ge", "ch", "ko", "jr", "ja"]

forms = ["cosplayeur-pikachu換裝皮卡丘换装옷갈아입기피카츄okigaeおきがえピカチュウ",
"starrockeurrocker-pikachu重搖滾皮卡丘하드록피카츄hardハードロック・ピカチュウ",
"belleladymadamen-pikachu貴婦皮卡丘마담피카츄マダム・ピカチュウ",
"popstar-pikachu偶像皮卡丘아이돌피카츄idolアイドル・ピカチュウ",
"ph.d.docteurprofessoren-pikachu,博士皮卡丘doctorドクター・ピカチュウ",
"librecatcheurwrestler-pikachu蒙面皮卡丘마스크드피카츄maskedマスクド・ピカチュウ",
"originalecapcasquetteoriginal-kappepikachu初始帽子皮卡丘오리지널캡피카츄	オリジナルキャップピカチュウ",
"capcasquettedehoenn-kappepikachu豐緣帽子皮卡丘호연캡피카츄ホウエンキャップピカチュウ",
"capcasquettedesinnoh-kappePikachu神奧帽子皮卡丘신오캡피카츄シンオウキャップピカチュウ",
"unovacapcasquetted'unyseinall-kappepikachu合眾帽子皮卡丘하나캡피카츄Isshuイッシュキャップピカチュウ",
"capcasquettedekalos-kappepikachu卡洛斯帽子皮卡丘칼로스캡피카츄カロスキャップピカチュウ",
"capcasquetted'alola-kappepikachu阿羅拉帽子皮卡丘알로라캡피카츄アローラキャップピカチュウ",
"capcasquettepartenairepartnerkappepikachu就決定是你了帽子皮卡丘너로정했다캡피카츄ichooseyouキミにきめたキャップピカチュウ",
"worldcapcasquettemondeweltreise-kappepikachu世界帽子皮卡丘월드캡피카츄ワールドキャップピカチュウ"]

#datas = setdata(609471857346740259, None)
#datas[10][0] = 50
#datas[10][9] = 5
#datas[10][3] = 1
'''
dex_forms = [["Cosplay Pikachu", "Pikachu Cosplayeur", "Cosplay-Pikachu", "换装皮卡丘", "옷갈아입기 피카츄", "Okigae Pikachu", "おきがえピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-cosplay.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-cosplay.gif"],
["Pikachu Rock Star", "	Pikachu Rockeur", "Rocker-Pikachu", "	重搖滾皮卡丘", "하드록 피카츄", "Hard Rock Pikachu", "ハードロック・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-rockstar.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-rockstar.gif"],
["Pikachu Belle", "	Pikachu Lady", "Damen-Pikachu", "貴婦皮卡丘", "마담 피카츄", "Madame Pikachu", "マダム・ピカチュウ", 24, [12], base_stats[24] ,"https://play.pokemonshowdown.com/sprites/ani/pikachu-belle.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-belle.gif"],
["Pikachu Pop Star", "	Pikachu Star", "Star-Pikachu", "偶像皮卡丘", "아이돌 피카츄", "Idol Pikachu", "アイドル・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-popstar.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-popstar.gif"],
["Pikachu, Ph.D.", "Pikachu Docteur", "	Professoren-Pikachu", "博士皮卡丘", "닥터 피카츄", "Doctor Pikachu", "ドクター・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-phd.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-phd.gif"],
["Pikachu Libre", "Pikachu Catcheur", "	Wrestler-Pikachu", "蒙面皮卡丘", "마스크드 피카츄", "Masked Pikachu", "マスクド・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-libre.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-libre.gif"],
["Original Cap Pikachu", "Pikachu Casquette Originale", "Original-Kappe Pikachu", "初始帽子皮卡丘", "오리지널캡 피카츄", "Original Cap Pikachu", "オリジナルキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-original.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-kantocap.gif"],
["Hoenn Cap Pikachu", "Pikachu Casquette de Hoenn", "Hoenn-Kappe Pikachu", "豐緣帽子皮卡丘", "칼로스캡 피카츄", "Kalos Cap Pikachu", "カロスキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-hoenn.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-hoenncap.gif"],
["Sinnoh Cap Pikachu", "Pikachu Casquette de Sinnoh", "Sinnoh-Kappe Pikachu", "神奧帽子皮卡丘", "신오캡 피카츄", "Sinnoh Cap Pikachu", "シンオウキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-sinnoh.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-sinnohcap.gif"],
["Unova Cap Pikachu", "Pikachu Casquette d'Unys", "Einall-Kappe Pikachu", "合眾帽子皮卡丘", "하나캡 피카츄", "Isshu Cap Pikachu", "イッシュキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-unova.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-unovacap.gif"],
["Kalos Cap Pikachu", "Pikachu Casquette de Kalos", "Kalos-Kappe Pikachu", "卡洛斯帽子皮卡丘", "칼로스캡 피카츄", "Kalos Cap Pikachu", "カロスキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-kalos.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-kaloscap.gif"],
["Alola Cap Pikachu", "Pikachu Casquette d'Alola", "Alola-Kappe Pikachu", "阿羅拉帽子皮卡丘", "알로라캡 피카츄", "Alola Cap Pikachu", "アローラキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-alola.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-alolacap.gif"],
["Partner Cap Pikachu", "Pikachu Casquette Partenaire", "Partnerkappe Pikachu", "就決定是你了帽子皮卡丘", "너로정했다캡 피카츄", "I Choose You Cap Pikachu", "キミにきめたキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-partner.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-partner.gif"],
["World Cap Pikachu", "Pikachu Casquette Monde", "Weltreise-Kappe Pikachu", "世界帽子皮卡丘", "월드캡 피카츄", "World Cap Pikachu", "ワールドキャップピカチュウ", 24, [12], base_stats[24], "https://media.tenor.com/images/31e4cf180a51406e2944a79bc5e7f660/tenor.gif", "https://media.tenor.com/images/31e4cf180a51406e2944a79bc5e7f660/tenor.gif"]
]
'''

def getdex(list_name, found_types, stats, sprite, language, options, number, id, name, shiny):
  datas = setdata(id, name)
  if number == None:
    embed = discord.Embed(title = "Pokédex", description = list_name[language].capitalize(), colour = [0xA8A878, 0xC03028, 0xA890F0, 0xA040A0, 0xE0C068, 0xB8A038, 0xA8B820, 0x705898, 0xB8B8D0, 0xF08030, 0x6890F0, 0x78C850, 0xF8D030, 0xF85888, 0x98D8D8, 0x7038F8, 0x705848, 0xEE99AC][types[0]], timestamp = datetime.utcnow())
  else:
    embed = discord.Embed(title = "Pokédex", description = list_name[language].capitalize()+" #"+str(int(number)+1)+" "+rarityname[getrarity(number+1)], colour = [0xA8A878, 0xC03028, 0xA890F0, 0xA040A0, 0xE0C068, 0xB8A038, 0xA8B820, 0x705898, 0xB8B8D0, 0xF08030, 0x6890F0, 0x78C850, 0xF8D030, 0xF85888, 0x98D8D8, 0x7038F8, 0x705848, 0xEE99AC][found_types[0]], timestamp = datetime.utcnow())
  embed.set_footer(text = "SHAdOw")
  embed.set_image(url=sprite)
  strypes = types_name[found_types[0]][language]
  defense_effectiveness = [row[found_types[0]] for row in type_chart]
  weakness, double_weakness, immunity, resistance, double_resistance = [], [], [], [], []
  if len(found_types) == 2:
    strypes += ", "+types_name[found_types[1]][language]
    for i in range(18):
      defense_effectiveness[i] *= type_chart[i,found_types[1]]
  for i in range(18):
    if defense_effectiveness[i] == 2:
      weakness.append(i)
    elif defense_effectiveness[i] == 4:
      double_weakness.append(i)
    elif defense_effectiveness[i] == 0:
      immunity.append(i)
    elif defense_effectiveness[i] == 0.5:
      resistance.append(i)
    elif defense_effectiveness[i] == 0.25:
      double_resistance.append(i)
  embed.add_field(name = ["`Types`","`Types`", "`Typen`", "`属性`", "`유형`", "`Taipu`", "`タイプ`"][language], value = strypes, inline = False)
  embed.add_field(name = ["`Base stats (Hp/Atk/Def/Spa/Spd/Spe)`", "`Stats de base (Pv/Att/Def/ASp/DSp/Vit)`", "`Statuswerte (Kra/Ang/Ver/SpA/SpV/Ini)`", "`能力 (Hp/攻击/防御/特攻/特防/速度)`", "`통계 (Hp/공격/방어/특수공격/특수방어/스피드)`", "`Sutētasu (Kō geki/Bōgyo/Toku kō/Toku bō/Subaya-sa)`", "`ステータス (Hp/こうげき/ぼうぎょ/とくこう/とくぼう/すばやさ)`"][language], value = str(stats[0])+"/"+str(stats[1])+"/"+str(stats[2])+"/"+str(stats[3])+"/"+str(stats[4])+"/"+str(stats[5]), inline = False)
  if len(weakness) != 0:
    weak = types_name[weakness[0]][language]
    for i in range(1,len(weakness)):
        weak += ", "+types_name[weakness[i]][language]
  else:
    weak = ["None", "Aucun", "Nein", "沒有", "아니", "Bangō", "番号"][language]
  if len(double_weakness) != 0:
    douweak = types_name[double_weakness[0]][language]
    for i in range(1,len(double_weakness)):
      douweak += ", "+types_name[double_weakness[i]][language]
  else:
    douweak = ["None", "Aucun", "Nein", "沒有", "아니", "Bangō", "番号"][language]
  if len(immunity) != 0:
    immune = types_name[immunity[0]][language]
    for i in range(1,len(immunity)):
      douweak += ", "+types_name[immunity[i]][language]
  else:
    immune = ["None", "Aucun", "Nein", "沒有", "아니", "Bangō", "番号"][language]
  if len(resistance) != 0:
    resist = types_name[resistance[0]][language]
    for i in range(1,len(resistance)):
      resist += ", "+types_name[resistance[i]][language]
  else:
    resist = ["None", "Aucun", "Nein", "沒有", "아니", "Bangō", "番号"][language]
  if len(double_resistance) != 0:
    dousist = types_name[double_resistance[0]][language]
    for i in range(1,len(double_resistance)):
      dousist += ", "+types_name[double_resistance[i]][language]
  else:
    dousist = ["None", "Aucun", "Nein", "沒有", "아니", "Bangō", "番号"][language]
  embed.add_field(name = ["`Double weakness", "`Double faiblesse", "`Doppelte Schwäche", "`雙重弱點", "`이중 약점", "`Nijū no jakuten", "`二重の弱点"][language]+" (x4)`", value = douweak, inline = True)
  embed.add_field(name = ["`Weakness", "`Faiblesse", "`Schwäche", "`弱點", "`약점", "`Jakuten", "`弱点"][language]+" (x2)`", value = weak, inline = True)
  embed.add_field(name = ["`Immunity", "`Immunité", "`Immunität", "`免疫", "`면역", "`Men'eki", "`免疫"][language]+" (x0)`", value = immune, inline = True)
  embed.add_field(name = ["`Resistance", "`Résistance", "`Widerstand", "`抵抗", "`저항", "`Teikō", "`抵抗"][language]+" (x0.5)`", value = resist, inline = True)
  embed.add_field(name = ["`Double resistance", "`Double résistance", "`Doppelter Widerstand", "`雙重抵抗", "`이중 저항", "`Nijū teikō", "`二重抵抗"][language]+" (x0.25)`", value = dousist, inline = True)
  if options[0]: #View other languages.
    embed.add_field(name = ["`Name in other languages`", "`Noms dans d'autres langues`", "`Namen in anderen Sprachen`", "`用其他語言命名`", "`다른 언어로 된 이름`", "`Hoka no gengo no namae`", "`他の言語の名前`"][language], value = ["English", "Anglais", "Englische Sprache", "英文", "영어", "Eigo", "英語"][language]+" : "+list_name[0].capitalize()+"\n"+["French", "Français", "Französisch Sprache", "法文", "프랑스 국민", "Furansugo", "フランス語"][language]+" : "+list_name[1].capitalize()+"\n"+["Japanese", "Japonais", "Japanisch Sprache", "日文", "일본어", "Hifumi", "日本語"][language]+" : "+list_name[6]+" / "+list_name[5].capitalize()+"\n"+["Chinese", "Chinois", "Chinesische Sprache", "中文", "중국어", "Chūgokugo", "中国語"][language]+" : "+list_name[3]+"\n"+["German", "Allemand", "Deutsche Sprache", "德國的語言", "독일어", "Doitsugo", "ドイツ語"][language]+" : "+list_name[2].capitalize()+"\n"+["Korean", "Coréen", "Koreanische Sprache", "朝鮮語", "한국어", "Kankoku-go", "韓国語"][language]+" : "+list_name[4], inline = False)
  if options[5]: #View links
    embed.add_field(name = ["`Link`", "`Lien`", "`Link`", "`網站`", "`사이트 링크`", "`Saito rinku`", "`サイトリンク`"][language], value = ["https://bulbapedia.bulbagarden.net/wiki/"+list_name[language]+"_(Pok%C3%A9mon)", "https://www.pokepedia.fr/"+list_name[language], "https://www.pokewiki.de/"+list_name[language], "https://wiki.52poke.com/wiki/"+list_name[language], "https://pokemonkorea.co.kr/pokedex", "https://wiki.xn--rckteqa2e.com/wiki/"+list_name[language], "https://wiki.xn--rckteqa2e.com/wiki/"+list_name[language]][language], inline = True)
  if options[6]: #View game stats
    embed.add_field(name = ["`Caught`", "`Capturé`", "`Erfassung`", "`捕獲`", "`포착`", "`Kyapuchā`", "`キャプチャー`"][language], value = datas[13+3*int(shiny)][number], inline = True)
    embed.add_field(name = ["`Inbox`", "`Dans la boîte`", "`Erfassung`", "`捕獲`", "`포착`", "`Kyapuchā`", "`キャプチャー`"][language], value = datas[7][number][int(shiny)], inline = True)
    embed.add_field(name = ["`IVs (Hp/Atk/Def/Spa/Spd/Spe)`", "`IVs (Pv/Att/Def/ASp/DSp/Vit)`", "`IVs (Kra/Ang/Ver/SpA/SpV/Ini)`", "`IVs (Hp/攻击/防御/特攻/特防/速度)`", "`IVs (Hp/공격/방어/특수공격/특수방어/스피드)`", "`IVs (Kō geki/Bōgyo/Toku kō/Toku bō/Subaya-sa)`", "`IVs (Hp/こうげき/ぼうぎょ/とくこう/とくぼう/すばやさ)`"][language], value = "{}/{}/{}/{}/{}/{}".format(datas[7][number][2], datas[7][number][3], datas[7][number][4], datas[7][number][5], datas[7][number][6], datas[7][number][7]), inline = True)
  return embed

@commands.command()
async def hi(self, ctx, arg):
  print("There.")
  await ctx.send("Hi.")
  print("Here.")








class Owner(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(hidden = True)
  @commands.cooldown(1, 1, commands.BucketType.user)
  async def reset(self, ctx):
    if ctx.message.author.id in authors:
      data = db.prefix("player")
      for name in data:
        del db[name]
      await ctx.send("Successfully resetted all players\' data.")
    else:
      await ctx.send("This command is reserved to the *dealer*.")

  @commands.command(hidden = True)
  @commands.cooldown(1, 1, commands.BucketType.user)
  async def resoption(self, ctx):
    if ctx.message.author.id in authors:
      #Rajouter toutes les listes qui comportent les données des joueurs.
      data = db.prefix("option")
      for name in data:
        del db[name]
      await ctx.send("Successfully resetted all players\' options.")
    else:
      await ctx.send("This command is reserved to the *dealer*.")

  @commands.command(hidden = True)
  async def addpoke(self, ctx, id, number: typing.Optional[int] = 1, shiny: typing.Optional[bool] = False):
    if ctx.message.author.id in authors:
      try:
        id = str(ctx.message.mentions[0].id)
      except:
        id = str(id)
      number -= 1
      datas = setdata(id, None)
      datas = add_pokemon(id, number, datas, shiny)
      #db["player_data"+str(id)] = datas
      await ctx.send("You gave a{} {} to {}.".format(["", " shiny"][int(shiny)], dex[number][0].capitalize(), str(id)))



  @commands.command(hidden = True)
  async def se(self, ctx, giveid, dexnumber: typing.Optional[int] = 1, shiny: typing.Optional[bool] = False):
    if ctx.message.author.id in authors:
      try:
        giveid = ctx.message.mentions[0].id
      except:
        giveid = str(giveid)
      datas = setdata(giveid, None)
      datas[21] = [True, dexnumber, shiny]
      await ctx.send("You gave a {}{} special encounter to {}.".format(["", "shiny "][shiny], dex[dexnumber-1][0], giveid))
      #db["player_data"+giveid] = datas

  @commands.command(hidden = True)
  async def clearrb(self, ctx, clearid: typing.Optional[str] = "373707498479288330"):
    if ctx.message.author.id in authors:
      try:
        clearid = str(ctx.message.mentions[0].id)
      except:
        clearid = str(clearid)
      datas = setdata(clearid, None)
      datas[17] = 0
      #db["player_data"+clearid] = datas
      await ctx.send("Cleared the rb recoil.")

  @commands.command(hidden = True)
  async def moneymoneymoney(self, ctx, giveid: typing.Optional[str] = "373707498479288330"):
    if ctx.message.author.id in authors:
      try:
        giveid = str(ctx.message.mentions[0].id)
      except:
        giveid = str(giveid)
      datas = setdata(giveid, None)
      datas[9] += 10000
      #db["player_data"+giveid] = datas

class Main(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=["dex"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def d(self, ctx, *args):
    '''The dex command show the dex page of a specific Pokémon. Make sure to put the special forms name before the name of the Pokémon.\nExamples : \n`.dex bulbasaur`\n`.dex shiny bulbasaur`
    '''
    language = setlanguage(ctx.message.author.id)
    options = setoption(ctx.message.author.id)
    shiny = args[0].lower() in ["shiny", "chromatique", "schillernden", "schillerndes", "異色", "發光", "빛나는", "iro chigai", "色違い"]
    if shiny:
      argument = " ".join(args[1:]).lower()
    else:
      argument = " ".join(args).lower()
    if len(argument.split(" ")) > 1: #Cherche d'abord si le nom donné est exact
      found = -1
      if argument in ["mr. mime", "m. mime", "pantimos", "魔牆人偶", "마임맨", "barrierd", "バリヤード"]:
        found = 121
      for i in range(len(dex_forms)):
        for j in range(len(languages)):
          if argument == dex_forms[i][j].lower():
            found = i
            break
        if found != -1:
          break
      if found == -1: #Sinon cherche dans les mots-clés
        for i in range(len(forms)):
          check = 0 #Vérifie que tous les adjectifs de formes sont dans forms.
          for test in argument.split(" "):
            print(test)
            if test in forms[i]:
              check += 1
            else:
              break
          if check == len(argument.split(" ")):
            found = i
            break
      list_name = dex_forms[found]
      found_types = dex_forms[found][-4]
      stats = dex_forms[found][-3]
      number = dex_forms[found][-5]
      if shiny:
        sprite = dex_forms[found][-1]
      else:
        sprite = dex_forms[found][-2]
      if found == -1:
        await ctx.send("Form not found, please check the spelling.")
        return
    else:
      try:
        if 0<int(argument)<=len(dex):
          number = int(argument)-1
        else:
          await ctx.send("Invalid dex number.")
          return
      except:
        number = -1
        for i in range(len(dex)):
          if argument in dex[i]:
            number = i
            break
        if number == -1:
          await ctx.send(["Pokémon not found. Check the spelling.", "Pokémon non trouvé. Vérifie l'orthographe.", "Pokémon nicht gefunden. Prüfe die Rechtschreibung.", "找不到神奇寶貝。 檢查拼寫。", "포켓몬을 찾을 수 없습니다. 철자를 확인하십시오.", "Pokemon ga mitsukarimasen. Superu o kakuninshitekudasai.", "ポケモンが見つかりません。 スペルを確認してください。"][language])
          return
      list_name = dex[number]
      found_types = types[number]
      stats = base_stats[number]
      if shiny:
        sprite = "http://play.pokemonshowdown.com/sprites/ani-shiny/"+dex[number][0].replace(" ","_")+".gif"
      else:
        sprite = "http://play.pokemonshowdown.com/sprites/ani/"+dex[number][0].replace(". ","")+".gif"
    embed = getdex(list_name, found_types, stats, sprite, language, options, number, ctx.message.author.id, ctx.message.author, shiny)
    await ctx.send(embed = embed)

  @commands.command()
  @commands.cooldown(1, 900, commands.BucketType.user)
  async def typechart(self, ctx):
    await ctx.send("From Bulbapedia.")
    await ctx.send("https://cdn.discordapp.com/attachments/754349043714621540/792404761563496448/Capture_decran_2020-12-26_a_15.53.16.png")



class Miscellaneous(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def option(self, ctx, *args):
    '''The option command show the togglables options and the current options' state for you. To toggle an option make sure it is listed in the `.option` command and do `.option *OptionToToggle*`. You can toggle/change multiple options at a time by sparating them with a space.\nExamples : \n`.option`\n`.option v.o.l.`\n`.option color 0x123456`
    '''
    options = setoption(ctx.message.author.id)
    if len(args) == 0:
      embed = discord.Embed(title = "Options", description = "Use `.option *argument*` to toggle or change options. You can toggle multiple options at a time.", colour = options[2], timestamp = datetime.utcnow())
      embed.set_footer(text = "SHAdOw")
      embed.add_field(name = "`v.o.l.`", value = "Let the `.dex` command show the Pokémon names in other languages. Now "+["**off**", "**on**"][int(options[0])]+".", inline = True)
      embed.add_field(name = "`reset`", value = "Put your options to their default values.", inline = True)
      embed.add_field(name = "`color`", value = "Put the hexadecimal value of the color you want the embeds' line to be.", inline = True)
      embed.add_field(name = "`language`", value = "Put the language code you want the game and some commands to be. Available languages : `en`, `fr`, `ge`, `ch`, `ko`, `jr`, `ja`\nCurrently set language : "+["`English`", "`Français`", "`Deutsche`", "`中文`", "`한국어`", "`Hifumi`", "`日文`"][options[3]], inline = True)
      embed.add_field(name = "`link`", value = "Add a link to an external Dex page with the dex command. Now "+["**off**", "**on**"][int(options[5])]+".", inline = True)
      embed.add_field(name = "`gamestats`", value = "Add your stats to the dex page. Now "+["**off**", "**on**"][int(options[6])]+".", inline = True)
      embed.add_field(name = "`Privacy`", value = "Enable privacy to not let other people see your box. Now {}.".format(["**off**", "**on**"][int(options[6])]))
      embed.add_field(name = "Examples", value = "`.option v.o.l.`, `.option prefix ;`, `.option reset`, `.option color FFFBCA`", inline = True)
      await ctx.send(embed = embed)
      return
    if "v.o.l." in args: #view other languages
      options[0] = not(options[0])
    if "color" in args and args.index("color") < len(args):
      try:
        color = int(args[args.index("color")+1], 16)
        options[2] = color
      except:
        await ctx.send("Invalid color value.")
        return
    if "lang" in args and args.index("lang") < len(args):
      lang = args[args.index("lang")+1]
      if lang in languages:
        options[3] = languages.index(lang)
      else:
        await ctx.send("Incorrect language. It needs to be among `"+"`, `".join(languages)+"`.")
    if "link" in args: #view link
      options[5] = not(options[5])
    if "gamestats" in args: #view game stats
      options[6] = not(options[6])
    if "raritycolor" in args: #view game stats
      options[7] = not(options[7])
    if "reset" in args:
      options = defaultoption
    if "privacy" in args:
      options[4] = not(options[4])
    db["option"+str(ctx.message.author.id)] = options
    embed = discord.Embed(title = "Options", description = "Your current options", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "`v.o.l.`", value = ["`Off`", "`On`"][int(options[0])], inline = True)
    embed.add_field(name = "`Prefix`", value = "`.`", inline = True)
    embed.add_field(name = "`Language`", value = ["`English`", "`Français`", "`Deutsche`", "`中文`", "`한국어`", "`Hifumi`", "`日文`"][options[3]], inline = True)
    embed.add_field(name = "`Link`", value = ["`Off`", "`On`"][int(options[5])], inline = True)
    embed.add_field(name = "`Privacy`", value = ["`Off`", "`On`"][int(options[4])], inline = True)
    await ctx.send(embed = embed)

  @commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)
  async def randomen(self, ctx):
    await ctx.send("This brings you to a random page of Bulbapedia : https://bulbapedia.bulbagarden.net/wiki/Special:Random")

  @commands.command()
  @commands.cooldown(1, 1, commands.BucketType.user)
  async def randomfr(self, ctx):
    await ctx.send("This brings you to a random page of Poképédia : https://www.pokepedia.fr/Sp%C3%A9cial:Page_au_hasard")

  @commands.command()
  @commands.cooldown(1, 900, commands.BucketType.user)
  async def message(self, ctx, *message: typing.Optional[str]):
    '''Use this command to send a message to the owner of the bot. Don't be shy !
    '''
    options = setoption(ctx.message.author.id)
    try:
      embed = discord.Embed(title = "Message by user", description = "`Author :`"+str(ctx.message.author)+" / "+str(ctx.message.author.id), colour = options[2], timestamp = datetime.utcnow())
      embed.add_field(name = "`Message :`", value = " ".join(message), inline = False)
      embed.set_footer(text = "SHAdOw")
      await bot.get_channel(794211311214788608).send(embed = embed)
      await ctx.send("Message sent.")
    except:
      await ctx.send("Your message must be 1024 or fewer in length.")

  @commands.command()
  @commands.cooldown(1, 20, commands.BucketType.user)
  async def lang(self, ctx):
    '''Use this command to change the language of some parts of the bot. English : `en`\nFrench : `fr`\nGerman : `ge`\nChinese : `ch`\nKorean : `ko`\nJapanese (romaji) : `jr`\nJapanese : `ja`
    '''
    await ctx.send("English : `en`\nFrench : `fr`\nGerman : `ge`\nChinese : `ch`\nKorean : `ko`\nJapanese (romaji) : `jr`\nJapanese : `ja`")
    def check(m):
      return m.author.id == ctx.message.author.id and m.content.lower() in languages
    options = setoption(ctx.message.author.id)
    try:
      language = await bot.wait_for("message", check=check, timeout = 30)
      options[3] = languages.index(language.content.lower())
      db["option"+str(ctx.message.author.id)] = options
      await ctx.send("Changed language to "+language.content.lower()+".")
    except:
      await ctx.send("Timeout. Please retry.")

  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def calc(self, ctx, expression):
    try:
      if eval(expression)%1 == 0:
        await ctx.send(int(eval(expression)))
      else:
        await ctx.send(eval(expression))
    except:
      await ctx.send("Invalid syntax. Ask around or visit https://www.python.org/ to get helped.")


@commands.command(hidden = True)
async def test(self, ctx, mention):
  try:
    id = ctx.message.mentions[0].id
    await ctx.send(id)
  except:
    await ctx.send(mention)


class Game(commands.Cog):
  '''Those are the game's commands.
  '''
  def __init__(self, bot):
    self.bot = bot
  @commands.command(aliases=["tr"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def trade(self, ctx, idt, *args):
    '''Use this command to trade with other players. Syntax : `.trade <id or mention> <"shiny" (optional)> <Dexnumber1> <"shiny" (optional)> <Dexnumber2>`
    '''
    try:
      idt = str(ctx.message.mentions[0].id)
    except:
      idt = str(idt)
    id = str(ctx.message.author.id)
    tradero = setdata(id, None)
    tradert = setdata(idt, None)
    shiny1 = args[0].lower() in ["shiny", "chromatique", "schillernden", "schillerndes", "異色", "發光", "빛나는", "iro chigai", "色違い"]
    print(1)
    if shiny1:
      shiny2 = args[2].lower() in ["shiny", "chromatique", "schillernden", "schillerndes", "異色", "發光", "빛나는", "iro chigai", "色違い"]
      poke1 = int(args[1])
      if shiny2:
        poke2 = int(args[3])
      else:
        poke2 = int(args[2])
    else:
      shiny2 = args[1].lower() in ["shiny", "chromatique", "schillernden", "schillerndes", "異色", "發光", "빛나는", "iro chigai", "色違い"]
      poke1 = int(args[0])
      if shiny2:
        poke2 = int(args[2])
      else:
        poke2 = int(args[1])
        print(2)
    if tradero[7][poke1-1][int(shiny1)] < 1:
      await ctx.send("You don't have the Pokémon you're proposing.")
      return
    if tradert[7][poke2-1][int(shiny2)] < 1:
      await ctx.send("The other player doesn't have the Pokémon you want.")
      return
    def check1(m):
      return str(m.author.id) == id and m.channel == ctx.message.channel and m.content.lower() == "confirm"
    def check2(m):
      return str(m.author.id) == idt and m.channel == ctx.message.channel and m.content.lower() == "confirm"
    try:
      await ctx.send("<@{}> Type **`confirm`** to confirm this trade :\n Your **{}{}** for his/her **{}{}**.".format(id, ["", "shiny "][int(shiny1)], dex[poke1-1][0], ["", "shiny "][int(shiny2)], dex[poke2-1][0]))
      await bot.wait_for("message", check=check1, timeout=20.0)
    except asyncio.TimeoutError:
      return await ctx.send("Timeout. Trade canceled.")
    try:
      await ctx.send("<@{}> Type **`confirm`** to confirm this trade :\n Your **{}{}** for his/her **{}{}**.".format(idt, ["", "shiny "][int(shiny2)], dex[poke2-1][0], ["", "shiny "][int(shiny1)], dex[poke1-1][0]))
      await bot.wait_for("message", check=check2, timeout=20.0)
    except asyncio.TimeoutError:
      return await ctx.send("Timeout. Trade canceled.")
    tradero[7][poke1-1][int(shiny1)] -= 1
    tradert[7][poke2-1][int(shiny2)] -= 1
    tradero[7][poke2-1][int(shiny2)] += 1
    tradert[7][poke1-1][int(shiny1)] += 1
    await ctx.send("You traded succesfully.")

  @commands.command()
  @commands.cooldown(1, 2, commands.BucketType.user)
  async def e(self, ctx, spawnnumber: typing.Optional[int] = -1, shiny: typing.Optional[int] = 0):
    '''Use this command to catch some Pokémon.
    '''
    id = ctx.message.author.id
    datas = setdata(id, ctx.message.author)
    options = setoption(id)
    color, language = options[2], options[3]
    try:
      specialencounter = datas[21]
    except:
      await ctx.send("Do `.play` before playing !")
    fakee, raree, luckye = False, False, False
    spawnweight = [1511000000, 750000000, 150000000, 50000000, 7000000, 5000000, 1890000, 20000, 1, 1]
    def is_correct(m):
      return m.author.id == id and m.content.lower() in listballs and datas[10][listballs.index(m.content.lower())] > 0
    if datas[22][0] > 0:
      for i in range(6, len(spawnweight)):
        spawnweight[i] = int(spawnweight[i]/2)
      datas[22][0] -= 1
      fakee = True
    if datas[22][1] > 0:
      for i in range(6, len(spawnweight)):
        spawnweight[i] *= 2
      datas[22][1] -= 1
      raree = True
    if datas[22][2] > 0 and datas[9] > 2500:
      for i in range(6, len(spawnweight)):
        spawnweight[i] *= 2
      datas[22][2] -= 1
      datas[23][13] += 1
      datas[9] -= 2500
      #luckye = True
    if ctx.message.author.id in authors and spawnnumber > 0:
      shiny = bool(shiny)
      spawnnumber = spawnnumber - 1
      rarity = getrarity(spawnnumber+1)
    elif specialencounter[0]:
      spawnnumber = specialencounter[1] - 1
      shiny = specialencounter[2]
      rarity = getrarity(spawnnumber+1)
      datas[21] = [False, 0, 0]
    else:
      shiny = choices([True, False], weights = [1, 8192])[0]
      rarity = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weights = spawnweight)[0]
      spawnnumber = choices([commonpool, uncommonpool, rarepool, rarerpool, veryrarepool, pseudolegendarypool, legendarypool, mythicalpool, ultrabeastpool, god][rarity])[0] -1


    Rarity = rarityname[rarity]
    spawn = dex[spawnnumber]
    if options[7]:
      color = [0x77AA, 0x3388, 0x335566, 0x552222, 0x771111, 0x442255, 0x837465, 0x33FF33, 0x123456, 0xFFFFFF, 0x222211][rarity]


    name = datas[0]
    pokemon = spawn[language].capitalize()
    embedtitle = pokemon+" #"+str(spawnnumber+1)
    if shiny:
      embedtitle = ":star2: "+embedtitle
      color = 0xFFFFFF-color

    embed = discord.Embed(title = embedtitle, description = name, colour = color, timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    if rarity > 5 or shiny:
      rarespawns = discord.Embed(title = "A "+embedtitle+" spawned !", description = Rarity, colour = color, timestamp = datetime.utcnow())
      rarespawns.set_footer(text = "SHAdOw")
      if shiny:
        rarespawns.set_image(url="http://play.pokemonshowdown.com/sprites/ani-shiny/"+spawn[0].replace(" ", "_")+".gif")
      else:
        rarespawns.set_image(url="http://play.pokemonshowdown.com/sprites/ani/"+spawn[0].replace(". ", "")+".gif")
      await bot.get_channel(831389415858896896).send(embed = rarespawns)

    if shiny:
      text = "Rarity : 1/8192\nCaught : "+str(datas[7][spawnnumber][1])
    else:
      text = "Rarity : "+Rarity+"\nInbox : "+str(datas[7][spawnnumber][0])
    if datas[10][0] > 0:
      text += "\n`pb` Pokéball : "+str(datas[10][0])
    if datas[10][1] > 0:
      text += "\n`gb` Greatball : "+str(datas[10][1])
    if datas[10][2] > 0:
      text += "\n`ub` Ultraball : "+str(datas[10][2])
    if datas[10][3] > 0:
      text += "\n`mb` Masterball : "+str(datas[10][3])
    if datas[10][4] > 0:
      text += "\n`rb` Recoilball : "+str(datas[10][4])
    if datas[17] > 0:
      text += "\nRecoil left : "+str(datas[17])
    if datas[10][5] > 0:
      text += "\n`bb` Beastball : "+str(datas[10][5])
    if datas[10][6] > 0:
      text += "\n`qb` Quickball : "+str(datas[10][6])
    if datas[10][7] > 0:
      text += "\n`db` Dreamball : "+str(datas[10][7])
    if datas[10][8] > 0:
      text += "\n`cb` Cloneball : "+str(datas[10][8])
    if datas[10][9] > 0:
      text += "\n`prb` Premier ball : "+str(datas[10][9])


    embed.add_field(name = "`What to do ?`", value = text, inline = False)
    if shiny:
      embed.set_image(url="http://play.pokemonshowdown.com/sprites/ani-shiny/"+spawn[0].replace(" ", "_")+".gif")
    else:
      embed.set_image(url="http://play.pokemonshowdown.com/sprites/ani/"+spawn[0].replace(". ", "")+".gif")
    encounter = await ctx.send(embed = embed)

    try:
      sentball = await bot.wait_for("message", check=is_correct, timeout=20.0)
    except asyncio.TimeoutError:
      return await encounter.edit(content = "{} fled !".format(pokemon))
    sentball = sentball.content.lower()
    randomcatch = randint(0, 100)
    if sentball == "mb":
      iscaught = 99
    if sentball == "fb":
      iscaught == 50
    else:
      iscaught = catchrate[rarity] + ballcr[listballs.index(sentball)] -80*int(shiny) -50*(datas[17]>0) -int(2*datas[17]/(25*datas[18][1])) + 40*int(rarity == 8 and sentball == "bb") + 150*int(datas[19][1] == spawnnumber and sentball == "db") + 150*int(datas[19][0] == spawnnumber and sentball == "cb") -40*(int(spawnnumber>721))
    if fakee:
      iscaught += 20
    if raree:
      iscaught -= 20
    datas[17] = max(datas[17]-1, 0)
    if sentball == "rb":
      datas[17] += 100 -datas[18][0]
    datas[10][listballs.index(sentball)] -= 1 + int(fakee) + int(raree)
    datas[23][listballs.index(sentball)] += 1
    embed = discord.Embed(title = embedtitle, description = name, colour = color, timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    if shiny:
      embed.set_image(url="http://play.pokemonshowdown.com/sprites/ani-shiny/"+spawn[0].replace(" ", "_")+".gif")
    else:
      embed.set_image(url="http://play.pokemonshowdown.com/sprites/ani/"+spawn[0].replace(". ", "")+".gif")
    state = 0
    if randomcatch > iscaught and sentball == "qb":
      retry = choices([False, True], weights = [1, 1])[0]
      if retry and datas[10][9] < 1:
        state = 1 #Chanceux mais pas d'honor ball.
      elif retry and datas[10][9] > 0:
        datas[10][9] -= 1
        iscaught += 10
        randomcatch = randint(0, 100)
        state = 2 #Chanceux avec honor ball

    if randomcatch <= iscaught:
      gotmoney = randint([99, 120, 300, 600, 1300, 500, 10000, 20000, 10000, 200000][rarity], [120, 200, 400, 800, 1800, 750, 15000, 25000, 100000, 2000000][rarity])
      coinbonus = int(gotmoney*datas[10][10]*0.05)
      datas[14] += gotmoney
      datas[9] += gotmoney
      datas = add_pokemon(id, spawnnumber, datas, shiny, True)
      text = "You caught {} !\nRarity : {} \nCatch power : {} | Catch number : {}\nYou earned {} coins.".format(pokemon, Rarity, iscaught, randomcatch, gotmoney)
      if coinbonus > 0:
        text += "You got {} bonus coins.".format(coinbonus)
      if datas[17] > 0:
        luck = randint(1, 100+datas[18][2])
        if luck > 95:
          reduction = randint(1, 5)
          datas[17] = max(0, datas[17]-reduction)
          text += "\nLucky ! Your recoil got reduced by "+str(reduction)+"."
          if state > 0:
            text += "You got lucky and an Premier ball was thrown."

        #await message.channel.send("You caught {} !\nCatch power : {}  Catch number : {}\nYou earned {} coins.".format(pokemon, iscaught, randomcatch, gotmoney))
    else:
      text = "{} broke free !\nRarity : {} \nCatch power : {} | Catch number : {}".format(pokemon, Rarity, iscaught, randomcatch)
    if state > 0:
      if state == 1:
        text += "You got lucky but you didn't have Premier ball."
      elif state == 2:
        text += "You got lucky but the Pokémon still fled."

    embed.add_field(name = "`Result`", value = text)
    await encounter.edit(embed=embed)
    #db["player_data"+str(id)] = datas

  @commands.command(aliases = ["pc"])
  @commands.cooldown(1, 5, commands.BucketType.user)
  async def box(self, ctx, page: typing.Optional[int] = 1, sort: typing.Optional[int] = 1, id: typing.Optional[int] = -1):
    '''The box command show your owned Pokémon. The default box page is the first one with the national dex number order. You can choose to see a certain page or with a certain sorting order. You must give the page number if you specify the sorting order.\nSyntax : `.box <page> <sorting order number>`\nSorting order : \n`1 (Default)` : The national dex number order.\n`2` : The descending rarity order.\n`3` : The ascending rarity order.\n`4` : The descending order with shinies first.\nExamples : \n`.box`\n`.box 1 1`\n`.box 2 4`
    '''
    #sort = 1:Ordre pokédex, 2:Ordre rareté descendant, 3:Ordre rareté ascendant, 4:Ordre rareté descendant avec shinys en premiers
    print(1)
    if id != -1:
      try:
        id = str(ctx.message.mentions[0].id)
      except:
        id = str(id)
    else:
      id = ctx.message.author.id
    print(2)
    datas = setdata(id, None)
    options = setoption(id)
    sortedbox, text, total, color, language = 0, "", 0, options[2], options[3]
    print(3)
    if int(ctx.message.author.id) != id and options[4]:
      await ctx.send("You can't see his/her box.")
      return
    if sort > 4:
      sort = 4
    for i in range(len(dex)):
      scanning = datas[7][i]
      if scanning[0] > 0 or scanning[1] > 0:
        total += 1
    total = int((total-1)/20)+1
    try:
      if sort == 1:
        for i in range(len(dex)):
          if sortedbox >= 20*page:
            break
          scanning = datas[7][i]#[0]
          print(scanning)
          if scanning[0] > 0 or scanning[1] > 0:
            rarity = rarityname[getrarity(i+1)]
            sortedbox += 1
            if sortedbox > 20*(page-1):
              text += "`"+str(i+1)+"` `"+rarity+"` "+str(scanning[0])+" | "+str(scanning[1])+"  "+dex[i][language].capitalize()+"\n"
      elif sort in [2, 3]:
        if sort == 2:
          generalpool = god+ultrabeastpool+mythicalpool+legendarypool+egg+pseudolegendarypool+veryrarepool+rarerpool+rarepool+uncommonpool+commonpool
        else:
          generalpool = commonpool+uncommonpool+rarepool+rarerpool+veryrarepool+pseudolegendarypool+egg+legendarypool+mythicalpool+ultrabeastpool+god
        for i in generalpool:
          i -= 1
          if sortedbox >= 20*page:
            break
          scanning = datas[7][i]
          if scanning[0] > 0 or scanning[1] > 0:
            rarity = rarityname[getrarity(i+1)]
            sortedbox += 1
            if sortedbox > 20*(page-1):
              text += "`"+str(i+1)+"` `"+rarity+"` "+str(scanning[0])+" | "+str(scanning[1])+"  "+dex[i][language].capitalize()+"\n"
      elif sort == 4:
        generalpool = god+ultrabeastpool+mythicalpool+legendarypool+egg+pseudolegendarypool+veryrarepool+rarerpool+rarepool+uncommonpool+commonpool
        alreadyadded = []
        for i in generalpool:
          i -= 1
          if sortedbox >= 20*page:
            break
          scanning = datas[7][i]
          if scanning[1] > 0:
            rarity = rarityname[getrarity(i+1)]
            sortedbox += 1
            alreadyadded.append(i)
            if sortedbox > 20*(page-1):
              text += "`"+str(i+1)+"` `"+rarity+"` "+str(scanning[0])+" | "+str(scanning[1])+"  "+dex[i][language].capitalize()+"\n"
        for i in generalpool:
          i -= 1
          if sortedbox >= 20*page:
            break
          scanning = datas[7][i]
          if scanning[0] > 0 and i not in alreadyadded:
            rarity = rarityname[getrarity(i+1)]
            sortedbox += 1
            if sortedbox > 20*(page-1):
              text += "`"+str(i+1)+"` `"+rarity+"` "+str(scanning[0])+" | "+str(scanning[1])+"  "+dex[i][language].capitalize()+"\n"
    except:
      text = "Invalid page number."
    embed = discord.Embed(title = datas[0]+"'s box", colour = color, timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "Page "+str(page)+"/"+str(total), value = text, inline = True)
    await ctx.send(embed=embed)

  @commands.command()
  async def sr(self, ctx):
    '''Use this command to see your spawn rates.
    '''
    spawnweight = [1511000000, 750000000, 150000000, 50000000, 7000000, 5000000, 1890000, 20000, 1, 1]
    datas = setdata(ctx.message.author.id, str(ctx.message.author))
    if datas[22][0] > 0:
      for i in range(6, len(spawnweight)):
        spawnweight[i] = int(spawnweight[i]/2)
    if datas[22][1] > 0:
      for i in range(6, len(spawnweight)):
        spawnweight[i] *= 2
    if datas[22][2] > 0 and datas[9] > 2500:
      for i in range(6, len(spawnweight)):
        spawnweight[i] *= 2
    somme = sum(spawnweight)
    await ctx.send("`Common :` 1/{}\n`Uncommon :` 1/{}\n`Rare :` 1/{}\n`Rarer :` 1/{}\n`Very rare :` 1/{}\n`Pseudo legendary :` 1/{}\n`Legendary :` 1/{}\n`Mythical :` 1/{}\n`Ultra beast :` 1/{}\n`God :` 1/{}".format(int(not(spawnweight[0]==0))*somme/(spawnweight[0]**int(not(spawnweight[0]==0))), int(not(spawnweight[1]==0))*somme/(spawnweight[1]**int(not(spawnweight[1]==0))), int(not(spawnweight[2]==0))*somme/(spawnweight[2]**int(not(spawnweight[2]==0))), int(not(spawnweight[3]==0))*somme/(spawnweight[3]**int(not(spawnweight[3]==0))), int(not(spawnweight[4]==0))*somme/(spawnweight[4]**int(not(spawnweight[4]==0))), int(not(spawnweight[5]==0))*somme/(spawnweight[5]**int(not(spawnweight[5]==0))), int(not(spawnweight[6]==0))*somme/(spawnweight[6]**int(not(spawnweight[6]==0))), int(not(spawnweight[7]==0))*somme/(spawnweight[7]**int(not(spawnweight[7]==0))), int(not(spawnweight[8]==0))*somme/(spawnweight[8]**int(not(spawnweight[8]==0))), int(not(spawnweight[9]==0))*somme/(spawnweight[9]**int(not(spawnweight[9]==0)))))

  @commands.command(aliases = ["nickname"])
  @commands.cooldown(1, 900, commands.BucketType.user)
  async def rename(self, ctx, name: typing.Optional[str]):
    '''This command to rename yourself in the game.\nsSyntax : `.rename <newname>`
    '''
    datas = setdata(ctx.message.author.id, str(ctx.message.author))
    datas[0] = name
    #db["player_data"+str(ctx.message.author.id)] = datas
    await ctx.send("You successfully renamed yourself into "+name+".")

  @commands.command()
  @commands.cooldown(1, 900, commands.BucketType.user)
  async def quit(self, ctx):
    '''Use this command to erase all your game datas.
    '''
    keys = db.prefix("player_data")
    if "player_data"+str(ctx.message.author.id) in keys:
      await ctx.send("You have 10 seconds to type `yes` if you really want to erase your datas. You won't be able to retrieve them.")
      def check(m):
        return m.author.id == ctx.message.author.id and m.content.lower() == "yes"
      await bot.wait_for("message", check=check, timeout = 10)
      del db["player_data"+str(ctx.message.author.id)]
      await ctx.send("Your data was successfully deleted.")
    else:
      await ctx.send("You haven\'t started your adventure yet.")


  @commands.command(aliases = ["sh", "shop"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def s(self, ctx, buying: typing.Optional[int] = -1, amount: typing.Optional[int] = 1):
    '''Use this command to see the shop and buy things in it.\nSyntax : `.s <itemnumber> <amount>`
    '''
    id = ctx.message.author.id
    if buying > -1:
      if buying == 10:
        await ctx.send("You can't buy Premier ball !")
        return
      bought, moneyleft, amuletnumber = additems(buying, amount, id, str(ctx.message.author))
      if amuletnumber > 50 and buying == 11:
        await ctx.send("You already have 50 amulet coins !")
        return
      if bought:
        await ctx.send("You bought "+str(amount)+" "+buyableitems[buying-1][1]+" and have "+str(moneyleft)+" :coin: left.")
        return
    options = setoption(id)
    datas = setdata(id, str(ctx.message.author))
    embed = discord.Embed(title = "Shop", description = "`Buy what you need !` You have "+str(datas[9])+" :coin:.", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "`Items`", value = "\n".join([" | ".join(["`"+str(buyableitems[i][0])+" : "+buyableitems[i][1]+"`", "Cost : "+str(buyableitems[i][2])+" :coin:", "`Earned : "+str(datas[10][i])])+"`" for i in range(len(buyableitems))]), inline = True)
    await ctx.send(embed = embed)

  @commands.command(aliases = ["item", "items", "bag", "inventory"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def i(self, ctx):
    '''Use this command see what you got in your bag.
    '''
    id = ctx.message.author.id
    datas = setdata(id, str(ctx.message.author))
    options = setoption(id)
    embed = discord.Embed(title = "Bag", description = str(datas[9])+" :coin:", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "`Balls`", value = "\n".join([" : ".join(["`"+str(buyableitems[i][1])+"`", str(datas[10][i])]) for i in range(len(buyableitems))]), inline = True)
    await ctx.send(embed = embed)

  @commands.command(aliases=["release"])
  @commands.cooldown(1, 7, commands.BucketType.user)
  async def rls(self, ctx, releasing: typing.Optional[str] = "-1", amount: typing.Optional[int] = 1, shiny: typing.Optional[bool] = False):
    '''Use this command to release your Pokémon.\nSyntax : `.rls d` to release all your duplicates except Legendary, Mythical, Ultrabest and God ones.\n`.rls <dexnumber> <amount>
    '''
    id = str(ctx.message.author.id)
    datas = setdata(id, str(ctx.message.author))
    locked = datas[20]
    try:
      releasing = int(releasing)
    except:
      pass
    if releasing == "d":
      dupes = [0, 0, 0, 0, 0, 0]
      gotmoney = 0
      for i in range(len(datas[7])):
        if i in locked:
          continue
        release = datas[7][i]
        if release[0] > 0:
          rarity = getrarity(i+1)
          if rarity > 5:
            continue
          dupes[rarity] += release[0] -1
          gotmoney += (release[0]-1)*releasemoney[rarity]
          release[0] = 1
      datas[9] += gotmoney
      datas[14] += gotmoney
      #db["player_data"+id] = datas
      await ctx.send("You got {} coins by releasing\n{} common\n{} uncommon\n{} rare\n{} rarer\n{} very rare\n{} pseudo legendary".format(gotmoney, dupes[0], dupes[1], dupes[2], dupes[3], dupes[4], dupes[5]))
      return
    if releasing > 0:
      if datas[7][releasing-1][int(shiny)] - amount < 0:
        await ctx.send("You can't release something you don't own.")
        return
      language = setlanguage(id)
      datas[7][releasing-1][int(shiny)] -= amount
      rarity = getrarity(releasing)
      gotmoney = amount*releasemoney[rarity]*1000**int(shiny)
      datas[9] += gotmoney
      datas[14] += gotmoney
      #db["player_data"+id] = datas
      released = dex[releasing-1][language].capitalize()
      if shiny:
        released = "shiny "+released
      await ctx.send("You released {} {} and got {} coins.".format(amount, released, gotmoney))


  @commands.command()
  @commands.cooldown(1, 15, commands.BucketType.user)
  async def fr(self, ctx, amount: typing.Optional[int] = 0):
    '''Use this command to activate the fake razz's effect. Fake razz divides by 2 the Legendary, Mythical, Ultrabeast and God spawn rates but gives you a 20 catch power bonus for 50 encounters each.\nSyntax : `.fr <amount>`
    '''
    id = ctx.message.author.id
    datas = setdata(id, str(ctx.message.author))
    fakeamount = datas[10][11]
    if amount < 1:
      if datas[22][0] < 1:
        await ctx.send("You don't have any fake razz effect activated. Activate or buy some in the shop ! You currently have {} fake razz.".format(fakeamount))
      else:
        await ctx.send("The fake razz is activated for {} more encounter. You have {} fake razz now.".format(datas[22][0], fakeamount))
        return
    elif amount > fakeamount:
      await ctx.send("You don't have that many fake razz. You only have {} now.".format(fakeamount))
      return
    else:
      datas[10][11] -= amount
      datas[23][11] += amount
      datas[22][0] += amount*50
      await ctx.send("Fake razz is now activated for {} more encounters.".format(datas[22][0]))
      #db["player_data"+str(id)] = datas

  @commands.command(aliases = ["rarerazz"])
  @commands.cooldown(1, 15, commands.BucketType.user)
  async def rr(self, ctx, amount: typing.Optional[int] = 0):
    '''Use this command to activate the rare razz's effect. Rare razz doubles Legendary, Mythical, Ultrabeast and God spawn rates but gives you a -20 catch power malus for 50 encounters each.\nSyntax : `.rr <amount>`
    '''
    id = ctx.message.author.id
    datas = setdata(id, str(ctx.message.author))
    rareamount = datas[10][12]
    if amount < 1:
      if datas[22][1] < 1:
        await ctx.send("You don't have any rare razz effect activated. Activate or buy some in the shop ! You currently have {} rare razz.".format(rareamount))
      else:
        await ctx.send("The rare razz is activated for {} more encounter. You have {} rare razz now.".format(datas[22][1], rareamount))
        return
    elif amount > rareamount:
      await ctx.send("You don't have that many rare razz. You only have {} now.".format(rareamount))
      return
    else:
      datas[10][12] -= amount
      datas[23][12] += 1
      datas[22][1] += amount*50
      await ctx.send("Rare razz is now activated for {} more encounters.".format(datas[22][1]))
      #db["player_data"+str(id)] = datas

  @commands.command(aliases = ["luckymachine"])
  @commands.cooldown(1, 15, commands.BucketType.user)
  async def lm(self, ctx, amount: typing.Optional[int] = 0):
    '''Use this command to activate the lucky machine for a certain amount of encounters. It doubles the Legendary, Mythical, Ultrabeast and God spawn rates but costs 2500 coins each encounter.\nSyntax : `.lm <amount>`
    '''
    id = str(ctx.message.author.id)
    datas = setdata(id, str(ctx.message.author))
    if amount < 1:
      if datas[22][2] < 1:
        await ctx.send("The lucky machine isn't activated. Activate it by specifying the number of encounter.")
      else:
        await ctx.send("The lucky machine is activated for {} more encounter.".format(datas[22][2]))
    else:
      datas[22][2] += amount
      await ctx.send("The lucky machine is now activated for {} more encounters.".format(datas[22][2]))
      #db["player_data"+id] = datas

  @commands.command(aliases = ["recoilball"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def rb(self, ctx, upgrading: typing.Optional[str] = ""):
    '''Upgrade your recoilball here.\nReducer : Reduces the number of recoiled encounters a recoilball will give.\nEffect : Reduces the reduction of catch power due to recoil.\nLuck : Give you a higher chance of reducing your accumulated recoil when catching a Pokémon.\nSyntax : `.rb <reducer/effect/luck>`
    '''
    id = str(ctx.message.author.id)
    datas = setdata(id, str(ctx.message.author))
    if upgrading.lower() in ["reducer", "effect", "luck"]:
      upgrade = ["reducer", "effect", "luck"].index(upgrading.lower())
      cost = 100*20**datas[18][upgrade]
      if datas[9] < cost:
        await ctx.send("You need "+str(cost-datas[9])+" more coins to upgrade the "+["reducer.", "effect.", "luck."][upgrade])
      else:
        datas[9] -= cost
        datas[18][upgrade] += 1
        await ctx.send("You spent {} to upgrade the recoilball's {} to level {}.".format(cost, ["reducer", "effect", "luck"][upgrade], datas[18][upgrade]))
        #db["player_data"+id] = datas
        return
    options = setoption(id)
    embed = discord.Embed(title = "Recoilball", description = "Upgrades", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    reducertext = "Reduces the number of recoiled encounters a recoilball will give. Current level : "+str(datas[18][0])
    if datas[18][0] < 20:
      reducertext += "\nNext cost : "+str(100*20**datas[18][0])
    effecttext = "Reduces the reduction of catch power due to recoil. Current level : "+str(datas[18][1])
    if datas[18][1] < 20:
      effecttext += "\nNext cost : "+str(100*20**datas[18][1])
    lucktext = "Give you a higher chance of reducing your accumulated recoil. Current level : "+str(datas[18][2])
    if datas[18][2] < 20:
      lucktext += "\nNext cost : "+str(100*20**datas[18][2])
    embed.add_field(name = "`Reducer`", value = reducertext, inline = True)
    embed.add_field(name = "`Effect`", value = effecttext, inline = True)
    embed.add_field(name = "`Luck`", value = lucktext, inline = True)
    await ctx.send(embed = embed)

  @commands.command(aliases = ["profile", "stat"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def stats(self, ctx):
    '''`yaml
    Flex on your stats with this.
    '''
    print(ctx.message.author)
    datas = setdata(str(ctx.message.author.id), str(ctx.message.author))
    options = setoption(ctx.message.author.id)
    embed = discord.Embed(title = datas[0]+"'s stats", description = "`Stats`", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "`Caught Pokémon`", value = str(datas[12]), inline = True)
    embed.add_field(name = "`Total earned money`", value = str(datas[14]), inline = True)
    embed.add_field(name = "`Thrown balls`", value = "\n".join(["`{}` : {}".format(listballs[i], datas[23][i]) for i in range(len(listballs))]), inline = False)
    embed.add_field(name = "`Used razz`", value = "`Fake razz` : {}\n`Rare razz` : {}".format(datas[23][11], datas[23][12]), inline = True)
    embed.add_field(name = "`Lucky machine activation`", value = "{} encounters.".format(datas[23][13]), inline = False)
    await ctx.send(embed = embed)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def lock(self, ctx, locking: typing.Optional[int] = 0):
    '''Use this command to lock up to 50 Pokémon from being released by `.rls d`. Legendary, Mythical, Ultrabeast, God and Egg rarities are locked by default. \nSyntax : `.lock <dexnumber>`
    '''
    id = str(ctx.message.author.id)
    datas = setdata(id, str(ctx.message.author))
    locked = datas[20]
    language = setlanguage(id)
    if locking > 0:
      try:
        locking -= 1
        if locking in locked:
          locked.remove(locking)
          await ctx.send("You unlocked {} from release.".format(dex[locking][language].capitalize()))
        else:
          if len(locked) > 49:
            await ctx.send("You already locked 50 Pokémon from release.")
            return
          locked.append(locking)
          locked.sort()
          await ctx.send("You added {} to your locked Pokémon.".format(dex[locking][language].capitalize()))
        datas[20] = locked
        #db["player_data"+id] = datas
      except:
        await ctx.send("Invalid Pokémon number.")
        return
    if len(locked) == 0:
      await ctx.send("You can see your locked Pokémon here.")
      return
    text = "Locked Pokémon :\n"
    for i in locked:
      text += "`{} : {}` {}\n".format(i+1, rarityname[getrarity(i+1)], dex[i][language].capitalize())
    await ctx.send(text)

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def partner(self, ctx, partner: typing.Optional[int] = 0):
    '''Set your partner Pokémon to get the clone ball boost and some other advantages. \nSyntax : `.partner <dexnumber>`
    '''
    datas = setdata(ctx.message.author.id, str(ctx.message.author))
    language = setlanguage(ctx.message.author.id)
    try:
      if 0<partner<len(dex):
        if datas[7][partner-1][0]+datas[7][partner-1][1] > 0:
          datas[19][0] = partner-1
          await ctx.send("You set {} as your partner.".format(dex[partner-1][language]).capitalize())
          #db["player_data"+str(ctx.message.author.id)] = datas
        else:
          await ctx.send("You don't have {} yet !".format(dex[partner-1][language].capitalize()))
      else:
        await ctx.send("Your current partner is {}.".format(dex[datas[19][0]][language].capitalize()))
    except:
      await ctx.send("Invalid number.")

  @commands.command()
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def dream(self, ctx, dream: typing.Optional[int] = 0):
    '''Set your dreamed Pokémon here to get the dream ball boost. \nSyntax : `.dream <dexnumber>`
    '''
    datas = setdata(ctx.message.author.id, str(ctx.message.author))
    language = setlanguage(ctx.message.author.id)
    try:
      if 0<dream<len(dex):
        datas[19][1] = dream-1
        await ctx.send("You set {} as your dream Pokémon.".format(dex[dream-1][language].capitalize()))
        #db["player_data"+str(ctx.message.author.id)] = datas
      else:
        await ctx.send("Your current dream Pokémon is {}.".format(dex[datas[19][1]][language].capitalize()))
    except:
      await ctx.send("Invalid number.")

  @commands.command()
  @commands.cooldown(1, 60, commands.BucketType.user)
  async def play(self, ctx):
    '''Use this command to play the game !
    '''
    keys = db.prefix("player_data")
    if "player_data"+str(ctx.message.author.id) in keys:
      color = setoption(ctx.message.author.id)[2]
      player_data = db["player_data"+str(ctx.message.author.id)]
      name = player_data[0]
      embed = discord.Embed(title = places[player_data[1]][0], description = name, colour = color, timestamp = datetime.utcnow())
      embed.set_footer(text = "SHAdOw")
      embed.add_field(name = "`What to do ?`", value = "`.e` \nGame under development.", inline = False)
      embed.set_image(url=places_pic[places[player_data[1]][0]])
      await ctx.send(embed = embed)
    else:
      setdata(ctx.message.author.id, str(ctx.message.author), True)
      await ctx.send("https://cdn.discordapp.com/attachments/754349043714621540/793349869019856906/Professeur_Chen-LGPE.png") #Professeur Chen.
      await ctx.send("Hey you ! Welcome to the world of Pokémon.\nI\'m the professor Oak.\nI study Pokémon. They live everywhere in this world and in harmony with humans. Some use them as companions while others do battles with them.\nYour name is "+str(ctx.message.author)+", right ?\nReady to begin your adventure ?\nA brand new world is waiting you !\nDo `.play` to play.")

  @commands.command()
  @commands.cooldown(1, 3, commands.BucketType.user)
  async def give(self, ctx, recid: typing.Optional[str] = "373707498479288330", money: typing.Optional[int] = 0):
    '''Use this command to give money to other players. \nSyntax : `.give <id or mention> <amount>`
    '''
    id = str(ctx.message.author.id)
    try:
      recid = str(ctx.message.mentions[0].id)
    except:
      recid = str(recid)
    givedatas = setdata(id, str(ctx.message.author))
    receivedatas = setdata(recid, None)
    if money < 0 and int(id) not in authors:
      await ctx.send("You can't steal money !")
      return
    if givedatas[9] < money:
      await ctx.send("You don't have enough money !")
      return
    if id == recid:
      await ctx.send("You gave {} coins to {}. But it seems it's yourself.".format(money, recid))
      return
    givedatas[9] -= money
    receivedatas[9] += money
    #db["player_data"+id] = givedatas
    #db["player_data"+recid] = receivedatas
    await ctx.send("You gave {} coins to {}.".format(money, recid))
    print(recid)
    print(money)

  @commands.command(aliases = ["balls"])
  @commands.cooldown(1, 10, commands.BucketType.user)
  async def ball(self, ctx):
    '''Use this command to see what the balls do.`
    '''
    id = ctx.message.author.id
    options = setoption(id)
    datas = setdata(id, str(ctx.message.author))
    embed = discord.Embed(title = "Balls", description = "`Balls wiki`", colour = options[2], timestamp = datetime.utcnow())
    embed.set_footer(text = "SHAdOw")
    embed.add_field(name = "Pokéball `pb`", value = "Adds 10 catch power.\nYou own {} now.".format(datas[10][0]), inline = True)
    embed.add_field(name = "Greatball `gb`", value = "Adds 15 catch power.\nYou own {} now.".format(datas[10][1]), inline = True)
    embed.add_field(name = "Ultraball `ub`", value = "Adds 25 catch power.\nYou own {} now.".format(datas[10][2]), inline = True)
    embed.add_field(name = "Masterball `mb`", value = "Put the catch power to 99 no matter what except if a rare razz is activated.\nYou own {} now.".format(datas[10][3]), inline = True)
    embed.add_field(name = "Recoilball `rb`", value = "Adds 100 catch power but reduces the catch power by 50 for 100 encounters. During the recoil, every 12.5 recoiled encounters left reduces the catch power by 1. You can upgrade the recoilball using `.rb` to reduce those drawbacks.\nYou own {} now.".format(datas[10][4]), inline = True)
    embed.add_field(name = "Beastball `bb`", value = "Adds 20 catch power and gives 40 bonus catch power if you're catching an Ultra-beast.\nYou own {} now.".format(datas[10][5]), inline = True)
    embed.add_field(name = "Quickball `qb`", value = "Adds 15 catch power and has 50% chance to let you throw a Premierball to the same Pokémon. The catch power will then be augmented of 10. You need to have at least a Premierball in your bag to do this.\nYou own {} now.".format(datas[10][6]), inline = True)
    embed.add_field(name = "Dreamball `db`", value = "Adds 10 catch power and gives 150 bonus catch power if you're catching your dreamed Pokémon. To set your dreamed Pokémon do `.dream`.\nYou own {} now.".format(datas[10][7]), inline = True)
    embed.add_field(name = "Cloneball `cb`", value = "Adds 10 catch power and gives 150 bonus catch power if you're catching your partner Pokémon. To set your partner Pokémon do `.partner`.\nYou own {} now.".format(datas[10][8]), inline = True)
    embed.add_field(name = "Premierball `prb`", value = "Adds 10 catch power. Is the only ball you can throw if the Quickball's special effect is triggered.\nYou own {} now.".format(datas[10][9]), inline = True)
    embed.add_field(name = "Fifty-fifty ball `fb`", value = "Put the catch power to 50 no matter what except if a rare razz is activated.\nYou own {} now.".format(datas[10][10]), inline = True)
    await ctx.send(embed = embed)

  @commands.command(aliases = ["quiz"])
  @commands.has_role("Trivia Organizer")
  @commands.cooldown(10, 900, commands.BucketType.user)
  async def trivia(self, ctx):
    if ctx.message.channel.id != 834362605140705291:
      await ctx.send(bot.get_channel(834362605140705291).mention)
    keys = db.prefix("player_data")
    difficulty = choices([0, 1, 2, 3, 4], weights = [700, 200, 140, 50, 1])[0]
    questionset = [trivias1, trivias2, trivias3, trivias4, trivias5][difficulty]
    question = randint(0, len(questionset)-1)
    quiz = await bot.get_channel(834362605140705291).send("Difficulty : {}\n{}".format(difficulty+1, questionset[question][0]))
    def check(m):
      return m.content.lower() in questionset[question][1:] and "player_data"+str(m.author.id) in keys
    try:
      answer = await bot.wait_for("message", check=check, timeout=120)
    except asyncio.TimeoutError:
      return await ctx.send("Timeout. Correct answer was {}.".format(questionset[question][1]))

    id = answer.author.id
    datas = setdata(id, None)
    moneyprize = randint(100*2**(difficulty+1), 500*2**(difficulty+1))
    datas[9] += moneyprize
    datas[14] += moneyprize
    datas[24] += moneyprize
    await quiz.edit(content = "Difficulty : {}\n{}\nCorrect answer was given by {}.".format(difficulty+1, questionset[question][0], datas[0]))


    await bot.get_channel(834362605140705291).send("{} won {} coins as a prize.".format(datas[0], moneyprize))


def add_pokemon(player_id, dex_number, datas, shiny, updateiv = False):
  iv = [randint(0,31) for i in range(6)]
  if sum(iv) > datas[7][dex_number][2]+datas[7][dex_number][3]+datas[7][dex_number][4]+datas[7][dex_number][5]+datas[7][dex_number][6]+datas[7][dex_number][7] and updateiv:
    for i in range(6):
      datas[7][dex_number][i+2] = iv[i]
  datas[7][dex_number][int(shiny)] += 1
  if updateiv: #Real catch
    datas[13+3*int(shiny)][dex_number] += 1
    datas[12] += 1
  return datas

def getrarity(number):
  if number in commonpool:
    return 0
  if number in uncommonpool:
    return 1
  if number in rarepool:
    return 2
  if number in rarerpool:
    return 3
  if number in veryrarepool:
    return 4
  if number in pseudolegendarypool:
    return 5
  if number in legendarypool:
    return 6
  if number in mythicalpool:
    return 7
  if number in ultrabeastpool:
    return 8
  if number in god:
    return 9
  if number in egg:
    return 10
  return 11

places = [["Pallet Town", None], ["Pokémon Laboratory", None], ["Home (Kanto)"], None, ["Route 1 (Kanto)", ]]

places_pic = dict([
  ("Pallet Town", "https://cdn.discordapp.com/attachments/793341791025889310/793713704716992512/Bourg_Palette_HGSS.png"),
  ("Pokémon Laboratory", "https://cdn.discordapp.com/attachments/793341791025889310/793715721443737630/Capture_decran_2020-12-30_a_06.42.47.png"),
  ("Home (Kanto)", "https://cdn.discordapp.com/attachments/793341791025889310/793716267931795486/Capture_decran_2020-12-30_a_06.44.59.png"),
  ("Route 1 (Kanto)",
  "https://cdn.discordapp.com/attachments/793341791025889310/794229694966136832/Kanto_Route_1_HGSS.webp")
  ])

battle_background = ["https://cdn.discordapp.com/attachments/793341791025889310/795158435682582548/Capture_decran_2021-01-03_a_06.15.39.png", #Herbe claire 0
  "https://cdn.discordapp.com/attachments/793341791025889310/795158274243559454/Capture_decran_2021-01-03_a_06.15.01.png", #Route rocheuse 1
  "https://cdn.discordapp.com/attachments/793341791025889310/795158027472863242/Capture_decran_2021-01-03_a_06.14.02.png", #Désert 2
  "https://cdn.discordapp.com/attachments/793341791025889310/795157608800976896/Capture_decran_2021-01-03_a_06.12.20.png", #Plage blanche 3
  "https://cdn.discordapp.com/attachments/793341791025889310/795157698814410792/Capture_decran_2021-01-03_a_06.12.41.png", #Grotte 4
  "https://cdn.discordapp.com/attachments/793341791025889310/795157455822520330/Capture_decran_2021-01-03_a_06.11.42.png", #Endroit sombre 5
  "https://cdn.discordapp.com/attachments/793341791025889310/795157782613196830/Capture_decran_2021-01-03_a_06.13.02.png", #Herbe un peu plus sombre 6
  "https://cdn.discordapp.com/attachments/793341791025889310/795158144329711676/Capture_decran_2021-01-03_a_06.14.30.png", #Mer 7
  "https://cdn.discordapp.com/attachments/793341791025889310/795158515093733417/Capture_decran_2021-01-03_a_06.15.57.png", #Terrain vague 8
  "https://cdn.discordapp.com/attachments/793341791025889310/795158367224070144/Capture_decran_2021-01-03_a_06.15.23.png", #Terrain aménagé sombre 9
  "https://cdn.discordapp.com/attachments/793341791025889310/795158206925373440/Capture_decran_2021-01-03_a_06.14.45.png" #Chemin calme 10
  ]
story = [
  2, #Initialement dans la maison.
  0, #En route pour le laboratoire.
  1, #Choix du starter et début de l"aventure.
  ]


moves = [["pound", 100, None, 35, 0, 40, "physical"], ["karate-chop", 100, None, 25, 0, 50, "physical"], ["double-slap", 85, None, 10, 0, 15, "physical"], ["comet-punch", 85, None, 15, 0, 18, "physical"], ["mega-punch", 85, None, 20, 0, 80, "physical"], ["pay-day", 100, None, 20, 0, 40, "physical"], ["fire-punch", 100, 10, 15, 0, 75, "physical"], ["ice-punch", 100, 10, 15, 0, 75, "physical"], ["thunder-punch", 100, 10, 15, 0, 75, "physical"], ["scratch", 100, None, 35, 0, 40, "physical"], ["vice-grip", 100, None, 30, 0, 55, "physical"], ["guillotine", 30, None, 5, 0, None, "physical"], ["razor-wind", 100, None, 10, 0, 80, "special"], ["swords-dance", None, None, 20, 0, None, "status"], ["cut", 95, None, 30, 0, 50, "physical"], ["gust", 100, None, 35, 0, 40, "special"], ["wing-attack", 100, None, 35, 0, 60, "physical"], ["whirlwind", None, None, 20, -6, None, "status"], ["fly", 95, None, 15, 0, 90, "physical"], ["bind", 85, 100, 20, 0, 15, "physical"], ["slam", 75, None, 20, 0, 80, "physical"], ["vine-whip", 100, None, 25, 0, 45, "physical"], ["stomp", 100, 30, 20, 0, 65, "physical"], ["double-kick", 100, None, 30, 0, 30, "physical"], ["mega-kick", 75, None, 5, 0, 120, "physical"], ["jump-kick", 95, None, 10, 0, 100, "physical"], ["rolling-kick", 85, 30, 15, 0, 60, "physical"], ["sand-attack", 100, None, 15, 0, None, "status"], ["headbutt", 100, 30, 15, 0, 70, "physical"], ["horn-attack", 100, None, 25, 0, 65, "physical"], ["fury-attack", 85, None, 20, 0, 15, "physical"], ["horn-drill", 30, None, 5, 0, None, "physical"], ["tackle", 100, None, 35, 0, 40, "physical"], ["body-slam", 100, 30, 15, 0, 85, "physical"], ["wrap", 90, 100, 20, 0, 15, "physical"], ["take-down", 85, None, 20, 0, 90, "physical"], ["thrash", 100, None, 10, 0, 120, "physical"], ["double-edge", 100, None, 15, 0, 120, "physical"], ["tail-whip", 100, None, 30, 0, None, "status"], ["poison-sting", 100, 30, 35, 0, 15, "physical"], ["twineedle", 100, 20, 20, 0, 25, "physical"], ["pin-missile", 95, None, 20, 0, 25, "physical"], ["leer", 100, 100, 30, 0, None, "status"], ["bite", 100, 30, 25, 0, 60, "physical"], ["growl", 100, None, 40, 0, None, "status"], ["roar", None, None, 20, -6, None, "status"], ["sing", 55, None, 15, 0, None, "status"], ["supersonic", 55, None, 20, 0, None, "status"], ["sonic-boom", 90, None, 20, 0, None, "special"], ["disable", 100, None, 20, 0, None, "status"], ["acid", 100, 10, 30, 0, 40, "special"], ["ember", 100, 10, 25, 0, 40, "special"], ["flamethrower", 100, 10, 15, 0, 90, "special"], ["mist", None, None, 30, 0, None, "status"], ["water-gun", 100, None, 25, 0, 40, "special"], ["hydro-pump", 80, None, 5, 0, 110, "special"], ["surf", 100, None, 15, 0, 90, "special"], ["ice-beam", 100, 10, 10, 0, 90, "special"], ["blizzard", 70, 10, 5, 0, 110, "special"], ["psybeam", 100, 10, 20, 0, 65, "special"], ["bubble-beam", 100, 10, 20, 0, 65, "special"], ["aurora-beam", 100, 10, 20, 0, 65, "special"], ["hyper-beam", 90, None, 5, 0, 150, "special"], ["peck", 100, None, 35, 0, 35, "physical"], ["drill-peck", 100, None, 20, 0, 80, "physical"], ["submission", 80, None, 20, 0, 80, "physical"], ["low-kick", 100, None, 20, 0, None, "physical"], ["counter", 100, None, 20, -5, None, "physical"], ["seismic-toss", 100, None, 20, 0, None, "physical"], ["strength", 100, None, 15, 0, 80, "physical"], ["absorb", 100, None, 25, 0, 20, "special"], ["mega-drain", 100, None, 15, 0, 40, "special"], ["leech-seed", 90, None, 10, 0, None, "status"], ["growth", None, None, 20, 0, None, "status"], ["razor-leaf", 95, None, 25, 0, 55, "physical"], ["solar-beam", 100, None, 10, 0, 120, "special"], ["poison-powder", 75, None, 35, 0, None, "status"], ["stun-spore", 75, None, 30, 0, None, "status"], ["sleep-powder", 75, None, 15, 0, None, "status"], ["petal-dance", 100, None, 10, 0, 120, "special"], ["string-shot", 95, None, 40, 0, None, "status"], ["dragon-rage", 100, None, 10, 0, None, "special"], ["fire-spin", 85, 100, 15, 0, 35, "special"], ["thunder-shock", 100, 10, 30, 0, 40, "special"], ["thunderbolt", 100, 10, 15, 0, 90, "special"], ["thunder-wave", 90, None, 20, 0, None, "status"], ["thunder", 70, 30, 10, 0, 110, "special"], ["rock-throw", 90, None, 15, 0, 50, "physical"], ["earthquake", 100, None, 10, 0, 100, "physical"], ["fissure", 30, None, 5, 0, None, "physical"], ["dig", 100, None, 10, 0, 80, "physical"], ["toxic", 90, None, 10, 0, None, "status"], ["confusion", 100, 10, 25, 0, 50, "special"], ["psychic", 100, 10, 10, 0, 90, "special"], ["hypnosis", 60, None, 20, 0, None, "status"], ["meditate", None, None, 40, 0, None, "status"], ["agility", None, None, 30, 0, None, "status"], ["quick-attack", 100, None, 30, 1, 40, "physical"], ["rage", 100, None, 20, 0, 20, "physical"], ["teleport", None, None, 20, 0, None, "status"], ["night-shade", 100, None, 15, 0, None, "special"], ["mimic", None, None, 10, 0, None, "status"], ["screech", 85, None, 40, 0, None, "status"], ["double-team", None, None, 15, 0, None, "status"], ["recover", None, None, 10, 0, None, "status"], ["harden", None, None, 30, 0, None, "status"], ["minimize", None, None, 10, 0, None, "status"], ["smokescreen", 100, None, 20, 0, None, "status"], ["confuse-ray", 100, None, 10, 0, None, "status"], ["withdraw", None, None, 40, 0, None, "status"], ["defense-curl", None, None, 40, 0, None, "status"], ["barrier", None, None, 20, 0, None, "status"], ["light-screen", None, None, 30, 0, None, "status"], ["haze", None, None, 30, 0, None, "status"], ["reflect", None, None, 20, 0, None, "status"], ["focus-energy", None, None, 30, 0, None, "status"], ["bide", None, None, 10, 1, None, "physical"], ["metronome", None, None, 10, 0, None, "status"], ["mirror-move", None, None, 20, 0, None, "status"], ["self-destruct", 100, None, 5, 0, 200, "physical"], ["egg-bomb", 75, None, 10, 0, 100, "physical"], ["lick", 100, 30, 30, 0, 30, "physical"], ["smog", 70, 40, 20, 0, 30, "special"], ["sludge", 100, 30, 20, 0, 65, "special"], ["bone-club", 85, 10, 20, 0, 65, "physical"], ["fire-blast", 85, 10, 5, 0, 110, "special"], ["waterfall", 100, 20, 15, 0, 80, "physical"], ["clamp", 85, 100, 15, 0, 35, "physical"], ["swift", None, None, 20, 0, 60, "special"], ["skull-bash", 100, 100, 10, 0, 130, "physical"], ["spike-cannon", 100, None, 15, 0, 20, "physical"], ["constrict", 100, 10, 35, 0, 10, "physical"], ["amnesia", None, None, 20, 0, None, "status"], ["kinesis", 80, None, 15, 0, None, "status"], ["soft-boiled", None, None, 10, 0, None, "status"], ["high-jump-kick", 90, None, 10, 0, 130, "physical"], ["glare", 100, None, 30, 0, None, "status"], ["dream-eater", 100, None, 15, 0, 100, "special"], ["poison-gas", 90, None, 40, 0, None, "status"], ["barrage", 85, None, 20, 0, 15, "physical"], ["leech-life", 100, None, 10, 0, 80, "physical"], ["lovely-kiss", 75, None, 10, 0, None, "status"], ["sky-attack", 90, 30, 5, 0, 140, "physical"], ["transform", None, None, 10, 0, None, "status"], ["bubble", 100, 10, 30, 0, 40, "special"], ["dizzy-punch", 100, 20, 10, 0, 70, "physical"], ["spore", 100, None, 15, 0, None, "status"], ["flash", 100, None, 20, 0, None, "status"], ["psywave", 100, None, 15, 0, None, "special"], ["splash", None, None, 40, 0, None, "status"], ["acid-armor", None, None, 20, 0, None, "status"], ["crabhammer", 90, None, 10, 0, 100, "physical"], ["explosion", 100, None, 5, 0, 250, "physical"], ["fury-swipes", 80, None, 15, 0, 18, "physical"], ["bonemerang", 90, None, 10, 0, 50, "physical"], ["rest", None, None, 10, 0, None, "status"], ["rock-slide", 90, 30, 10, 0, 75, "physical"], ["hyper-fang", 90, 10, 15, 0, 80, "physical"], ["sharpen", None, None, 30, 0, None, "status"], ["conversion", None, None, 30, 0, None, "status"], ["tri-attack", 100, 20, 10, 0, 80, "special"], ["super-fang", 90, None, 10, 0, None, "physical"], ["slash", 100, None, 20, 0, 70, "physical"], ["substitute", None, None, 10, 0, None, "status"], ["struggle", None, None, 1, 0, 50, "physical"], ["sketch", None, None, 1, 0, None, "status"], ["triple-kick", 90, None, 10, 0, 10, "physical"], ["thief", 100, None, 25, 0, 60, "physical"], ["spider-web", None, None, 10, 0, None, "status"], ["mind-reader", None, None, 5, 0, None, "status"], ["nightmare", 100, None, 15, 0, None, "status"], ["flame-wheel", 100, 10, 25, 0, 60, "physical"], ["snore", 100, 30, 15, 0, 50, "special"], ["curse", None, None, 10, 0, None, "status"], ["flail", 100, None, 15, 0, None, "physical"], ["conversion-2", None, None, 30, 0, None, "status"], ["aeroblast", 95, None, 5, 0, 100, "special"], ["cotton-spore", 100, None, 40, 0, None, "status"], ["reversal", 100, None, 15, 0, None, "physical"], ["spite", 100, None, 10, 0, None, "status"], ["powder-snow", 100, 10, 25, 0, 40, "special"], ["protect", None, None, 10, 4, None, "status"], ["mach-punch", 100, None, 30, 1, 40, "physical"], ["scary-face", 100, None, 10, 0, None, "status"], ["feint-attack", None, None, 20, 0, 60, "physical"], ["sweet-kiss", 75, None, 10, 0, None, "status"], ["belly-drum", None, None, 10, 0, None, "status"], ["sludge-bomb", 100, 30, 10, 0, 90, "special"], ["mud-slap", 100, 100, 10, 0, 20, "special"], ["octazooka", 85, 50, 10, 0, 65, "special"], ["spikes", None, None, 20, 0, None, "status"], ["zap-cannon", 50, 100, 5, 0, 120, "special"], ["foresight", None, None, 40, 0, None, "status"], ["destiny-bond", None, None, 5, 0, None, "status"], ["perish-song", None, None, 5, 0, None, "status"], ["icy-wind", 95, 100, 15, 0, 55, "special"], ["detect", None, None, 5, 4, None, "status"], ["bone-rush", 90, None, 10, 0, 25, "physical"], ["lock-on", None, None, 5, 0, None, "status"], ["outrage", 100, None, 10, 0, 120, "physical"], ["sandstorm", None, None, 10, 0, None, "status"], ["giga-drain", 100, None, 10, 0, 75, "special"], ["endure", None, None, 10, 4, None, "status"], ["charm", 100, None, 20, 0, None, "status"], ["rollout", 90, None, 20, 0, 30, "physical"], ["false-swipe", 100, None, 40, 0, 40, "physical"], ["swagger", 85, None, 15, 0, None, "status"], ["milk-drink", None, None, 10, 0, None, "status"], ["spark", 100, 30, 20, 0, 65, "physical"], ["fury-cutter", 95, None, 20, 0, 40, "physical"], ["steel-wing", 90, 10, 25, 0, 70, "physical"], ["mean-look", None, None, 5, 0, None, "status"], ["attract", 100, None, 15, 0, None, "status"], ["sleep-talk", None, None, 10, 0, None, "status"], ["heal-bell", None, None, 5, 0, None, "status"], ["return", 100, None, 20, 0, None, "physical"], ["present", 90, None, 15, 0, None, "physical"], ["frustration", 100, None, 20, 0, None, "physical"], ["safeguard", None, None, 25, 0, None, "status"], ["pain-split", None, None, 20, 0, None, "status"], ["sacred-fire", 95, 50, 5, 0, 100, "physical"], ["magnitude", 100, None, 30, 0, None, "physical"], ["dynamic-punch", 50, 100, 5, 0, 100, "physical"], ["megahorn", 85, None, 10, 0, 120, "physical"], ["dragon-breath", 100, 30, 20, 0, 60, "special"], ["baton-pass", None, None, 40, 0, None, "status"], ["encore", 100, None, 5, 0, None, "status"], ["pursuit", 100, None, 20, 0, 40, "physical"], ["rapid-spin", 100, None, 40, 0, 20, "physical"], ["sweet-scent", 100, None, 20, 0, None, "status"], ["iron-tail", 75, 30, 15, 0, 100, "physical"], ["metal-claw", 95, 10, 35, 0, 50, "physical"], ["vital-throw", None, None, 10, -1, 70, "physical"], ["morning-sun", None, None, 5, 0, None, "status"], ["synthesis", None, None, 5, 0, None, "status"], ["moonlight", None, None, 5, 0, None, "status"], ["hidden-power", 100, None, 15, 0, 60, "special"], ["cross-chop", 80, None, 5, 0, 100, "physical"], ["twister", 100, 20, 20, 0, 40, "special"], ["rain-dance", None, None, 5, 0, None, "status"], ["sunny-day", None, None, 5, 0, None, "status"], ["crunch", 100, 20, 15, 0, 80, "physical"], ["mirror-coat", 100, None, 20, -5, None, "special"], ["psych-up", None, None, 10, 0, None, "status"], ["extreme-speed", 100, None, 5, 2, 80, "physical"], ["ancient-power", 100, 10, 5, 0, 60, "special"], ["shadow-ball", 100, 20, 15, 0, 80, "special"], ["future-sight", 100, None, 10, 0, 120, "special"], ["rock-smash", 100, 50, 15, 0, 40, "physical"], ["whirlpool", 85, 100, 15, 0, 35, "special"], ["beat-up", 100, None, 10, 0, None, "physical"], ["fake-out", 100, 100, 10, 3, 40, "physical"], ["uproar", 100, None, 10, 0, 90, "special"], ["stockpile", None, None, 20, 0, None, "status"], ["spit-up", 100, None, 10, 0, None, "special"], ["swallow", None, None, 10, 0, None, "status"], ["heat-wave", 90, 10, 10, 0, 95, "special"], ["hail", None, None, 10, 0, None, "status"], ["torment", 100, None, 15, 0, None, "status"], ["flatter", 100, None, 15, 0, None, "status"], ["will-o-wisp", 85, None, 15, 0, None, "status"], ["memento", 100, None, 10, 0, None, "status"], ["facade", 100, None, 20, 0, 70, "physical"], ["focus-punch", 100, None, 20, -3, 150, "physical"], ["smelling-salts", 100, None, 10, 0, 70, "physical"], ["follow-me", None, None, 20, 2, None, "status"], ["nature-power", None, None, 20, 0, None, "status"], ["charge", None, None, 20, 0, None, "status"], ["taunt", 100, None, 20, 0, None, "status"], ["helping-hand", None, None, 20, 5, None, "status"], ["trick", 100, None, 10, 0, None, "status"], ["role-play", None, None, 10, 0, None, "status"], ["wish", None, None, 10, 0, None, "status"], ["assist", None, None, 20, 0, None, "status"], ["ingrain", None, None, 20, 0, None, "status"], ["superpower", 100, 100, 5, 0, 120, "physical"], ["magic-coat", None, None, 15, 4, None, "status"], ["recycle", None, None, 10, 0, None, "status"], ["revenge", 100, None, 10, -4, 60, "physical"], ["brick-break", 100, None, 15, 0, 75, "physical"], ["yawn", None, None, 10, 0, None, "status"], ["knock-off", 100, None, 20, 0, 65, "physical"], ["endeavor", 100, None, 5, 0, None, "physical"], ["eruption", 100, None, 5, 0, 150, "special"], ["skill-swap", None, None, 10, 0, None, "status"], ["imprison", None, None, 10, 0, None, "status"], ["refresh", None, None, 20, 0, None, "status"], ["grudge", None, None, 5, 0, None, "status"], ["snatch", None, None, 10, 4, None, "status"], ["secret-power", 100, 30, 20, 0, 70, "physical"], ["dive", 100, None, 10, 0, 80, "physical"], ["arm-thrust", 100, None, 20, 0, 15, "physical"], ["camouflage", None, None, 20, 0, None, "status"], ["tail-glow", None, None, 20, 0, None, "status"], ["luster-purge", 100, 50, 5, 0, 70, "special"], ["mist-ball", 100, 50, 5, 0, 70, "special"], ["feather-dance", 100, None, 15, 0, None, "status"], ["teeter-dance", 100, None, 20, 0, None, "status"], ["blaze-kick", 90, 10, 10, 0, 85, "physical"], ["mud-sport", None, None, 15, 0, None, "status"], ["ice-ball", 90, None, 20, 0, 30, "physical"], ["needle-arm", 100, 30, 15, 0, 60, "physical"], ["slack-off", None, None, 10, 0, None, "status"], ["hyper-voice", 100, None, 10, 0, 90, "special"], ["poison-fang", 100, 50, 15, 0, 50, "physical"], ["crush-claw", 95, 50, 10, 0, 75, "physical"], ["blast-burn", 90, None, 5, 0, 150, "special"], ["hydro-cannon", 90, None, 5, 0, 150, "special"], ["meteor-mash", 90, 20, 10, 0, 90, "physical"], ["astonish", 100, 30, 15, 0, 30, "physical"], ["weather-ball", 100, None, 10, 0, 50, "special"], ["aromatherapy", None, None, 5, 0, None, "status"], ["fake-tears", 100, None, 20, 0, None, "status"], ["air-cutter", 95, None, 25, 0, 60, "special"], ["overheat", 90, 100, 5, 0, 130, "special"], ["odor-sleuth", None, None, 40, 0, None, "status"], ["rock-tomb", 95, 100, 15, 0, 60, "physical"], ["silver-wind", 100, 10, 5, 0, 60, "special"], ["metal-sound", 85, None, 40, 0, None, "status"], ["grass-whistle", 55, None, 15, 0, None, "status"], ["tickle", 100, None, 20, 0, None, "status"], ["cosmic-power", None, None, 20, 0, None, "status"], ["water-spout", 100, None, 5, 0, 150, "special"], ["signal-beam", 100, 10, 15, 0, 75, "special"], ["shadow-punch", None, None, 20, 0, 60, "physical"], ["extrasensory", 100, 10, 20, 0, 80, "special"], ["sky-uppercut", 90, None, 15, 0, 85, "physical"], ["sand-tomb", 85, 100, 15, 0, 35, "physical"], ["sheer-cold", 30, None, 5, 0, None, "special"], ["muddy-water", 85, 30, 10, 0, 90, "special"], ["bullet-seed", 100, None, 30, 0, 25, "physical"], ["aerial-ace", None, None, 20, 0, 60, "physical"], ["icicle-spear", 100, None, 30, 0, 25, "physical"], ["iron-defense", None, None, 15, 0, None, "status"], ["block", None, None, 5, 0, None, "status"], ["howl", None, None, 40, 0, None, "status"], ["dragon-claw", 100, None, 15, 0, 80, "physical"], ["frenzy-plant", 90, None, 5, 0, 150, "special"], ["bulk-up", None, None, 20, 0, None, "status"], ["bounce", 85, 30, 5, 0, 85, "physical"], ["mud-shot", 95, 100, 15, 0, 55, "special"], ["poison-tail", 100, 10, 25, 0, 50, "physical"], ["covet", 100, None, 25, 0, 60, "physical"], ["volt-tackle", 100, 10, 15, 0, 120, "physical"], ["magical-leaf", None, None, 20, 0, 60, "special"], ["water-sport", None, None, 15, 0, None, "status"], ["calm-mind", None, None, 20, 0, None, "status"], ["leaf-blade", 100, None, 15, 0, 90, "physical"], ["dragon-dance", None, None, 20, 0, None, "status"], ["rock-blast", 90, None, 10, 0, 25, "physical"], ["shock-wave", None, None, 20, 0, 60, "special"], ["water-pulse", 100, 20, 20, 0, 60, "special"], ["doom-desire", 100, None, 5, 0, 140, "special"], ["psycho-boost", 90, 100, 5, 0, 140, "special"], ["roost", None, None, 10, 0, None, "status"], ["gravity", None, None, 5, 0, None, "status"], ["miracle-eye", None, None, 40, 0, None, "status"], ["wake-up-slap", 100, None, 10, 0, 70, "physical"], ["hammer-arm", 90, 100, 10, 0, 100, "physical"], ["gyro-ball", 100, None, 5, 0, None, "physical"], ["healing-wish", None, None, 10, 0, None, "status"], ["brine", 100, None, 10, 0, 65, "special"], ["natural-gift", 100, None, 15, 0, None, "physical"], ["feint", 100, None, 10, 2, 30, "physical"], ["pluck", 100, None, 20, 0, 60, "physical"], ["tailwind", None, None, 15, 0, None, "status"], ["acupressure", None, None, 30, 0, None, "status"], ["metal-burst", 100, None, 10, 0, None, "physical"], ["u-turn", 100, None, 20, 0, 70, "physical"], ["close-combat", 100, 100, 5, 0, 120, "physical"], ["payback", 100, None, 10, 0, 50, "physical"], ["assurance", 100, None, 10, 0, 60, "physical"], ["embargo", 100, None, 15, 0, None, "status"], ["fling", 100, None, 10, 0, None, "physical"], ["psycho-shift", 100, None, 10, 0, None, "status"], ["trump-card", None, None, 5, 0, None, "special"], ["heal-block", 100, None, 15, 0, None, "status"], ["wring-out", 100, None, 5, 0, None, "special"], ["power-trick", None, None, 10, 0, None, "status"], ["gastro-acid", 100, None, 10, 0, None, "status"], ["lucky-chant", None, None, 30, 0, None, "status"], ["me-first", None, None, 20, 0, None, "status"], ["copycat", None, None, 20, 0, None, "status"], ["power-swap", None, None, 10, 0, None, "status"], ["guard-swap", None, None, 10, 0, None, "status"], ["punishment", 100, None, 5, 0, None, "physical"], ["last-resort", 100, None, 5, 0, 140, "physical"], ["worry-seed", 100, None, 10, 0, None, "status"], ["sucker-punch", 100, None, 5, 1, 70, "physical"], ["toxic-spikes", None, None, 20, 0, None, "status"], ["heart-swap", None, None, 10, 0, None, "status"], ["aqua-ring", None, None, 20, 0, None, "status"], ["magnet-rise", None, None, 10, 0, None, "status"], ["flare-blitz", 100, 10, 15, 0, 120, "physical"], ["force-palm", 100, 30, 10, 0, 60, "physical"], ["aura-sphere", None, None, 20, 0, 80, "special"], ["rock-polish", None, None, 20, 0, None, "status"], ["poison-jab", 100, 30, 20, 0, 80, "physical"], ["dark-pulse", 100, 20, 15, 0, 80, "special"], ["night-slash", 100, None, 15, 0, 70, "physical"], ["aqua-tail", 90, None, 10, 0, 90, "physical"], ["seed-bomb", 100, None, 15, 0, 80, "physical"], ["air-slash", 95, 30, 15, 0, 75, "special"], ["x-scissor", 100, None, 15, 0, 80, "physical"], ["bug-buzz", 100, 10, 10, 0, 90, "special"], ["dragon-pulse", 100, None, 10, 0, 85, "special"], ["dragon-rush", 75, 20, 10, 0, 100, "physical"], ["power-gem", 100, None, 20, 0, 80, "special"], ["drain-punch", 100, None, 10, 0, 75, "physical"], ["vacuum-wave", 100, None, 30, 1, 40, "special"], ["focus-blast", 70, 10, 5, 0, 120, "special"], ["energy-ball", 100, 10, 10, 0, 90, "special"], ["brave-bird", 100, None, 15, 0, 120, "physical"], ["earth-power", 100, 10, 10, 0, 90, "special"], ["switcheroo", 100, None, 10, 0, None, "status"], ["giga-impact", 90, None, 5, 0, 150, "physical"], ["nasty-plot", None, None, 20, 0, None, "status"], ["bullet-punch", 100, None, 30, 1, 40, "physical"], ["avalanche", 100, None, 10, -4, 60, "physical"], ["ice-shard", 100, None, 30, 1, 40, "physical"], ["shadow-claw", 100, None, 15, 0, 70, "physical"], ["thunder-fang", 95, 10, 15, 0, 65, "physical"], ["ice-fang", 95, 10, 15, 0, 65, "physical"], ["fire-fang", 95, 10, 15, 0, 65, "physical"], ["shadow-sneak", 100, None, 30, 1, 40, "physical"], ["mud-bomb", 85, 30, 10, 0, 65, "special"], ["psycho-cut", 100, None, 20, 0, 70, "physical"], ["zen-headbutt", 90, 20, 15, 0, 80, "physical"], ["mirror-shot", 85, 30, 10, 0, 65, "special"], ["flash-cannon", 100, 10, 10, 0, 80, "special"], ["rock-climb", 85, 20, 20, 0, 90, "physical"], ["defog", None, None, 15, 0, None, "status"], ["trick-room", None, None, 5, -7, None, "status"], ["draco-meteor", 90, 100, 5, 0, 130, "special"], ["discharge", 100, 30, 15, 0, 80, "special"], ["lava-plume", 100, 30, 15, 0, 80, "special"], ["leaf-storm", 90, 100, 5, 0, 130, "special"], ["power-whip", 85, None, 10, 0, 120, "physical"], ["rock-wrecker", 90, None, 5, 0, 150, "physical"], ["cross-poison", 100, 10, 20, 0, 70, "physical"], ["gunk-shot", 80, 30, 5, 0, 120, "physical"], ["iron-head", 100, 30, 15, 0, 80, "physical"], ["magnet-bomb", None, None, 20, 0, 60, "physical"], ["stone-edge", 80, None, 5, 0, 100, "physical"], ["captivate", 100, None, 20, 0, None, "status"], ["stealth-rock", None, None, 20, 0, None, "status"], ["grass-knot", 100, None, 20, 0, None, "special"], ["chatter", 100, 100, 20, 0, 65, "special"], ["judgment", 100, None, 10, 0, 100, "special"], ["bug-bite", 100, None, 20, 0, 60, "physical"], ["charge-beam", 90, 70, 10, 0, 50, "special"], ["wood-hammer", 100, None, 15, 0, 120, "physical"], ["aqua-jet", 100, None, 20, 1, 40, "physical"], ["attack-order", 100, None, 15, 0, 90, "physical"], ["defend-order", None, None, 10, 0, None, "status"], ["heal-order", None, None, 10, 0, None, "status"], ["head-smash", 80, None, 5, 0, 150, "physical"], ["double-hit", 90, None, 10, 0, 35, "physical"], ["roar-of-time", 90, None, 5, 0, 150, "special"], ["spacial-rend", 95, None, 5, 0, 100, "special"], ["lunar-dance", None, None, 10, 0, None, "status"], ["crush-grip", 100, None, 5, 0, None, "physical"], ["magma-storm", 75, 100, 5, 0, 100, "special"], ["dark-void", 50, None, 10, 0, None, "status"], ["seed-flare", 85, 40, 5, 0, 120, "special"], ["ominous-wind", 100, 10, 5, 0, 60, "special"], ["shadow-force", 100, None, 5, 0, 120, "physical"], ["hone-claws", None, None, 15, 0, None, "status"], ["wide-guard", None, None, 10, 3, None, "status"], ["guard-split", None, None, 10, 0, None, "status"], ["power-split", None, None, 10, 0, None, "status"], ["wonder-room", None, None, 10, 0, None, "status"], ["psyshock", 100, None, 10, 0, 80, "special"], ["venoshock", 100, None, 10, 0, 65, "special"], ["autotomize", None, None, 15, 0, None, "status"], ["rage-powder", None, None, 20, 2, None, "status"], ["telekinesis", None, None, 15, 0, None, "status"], ["magic-room", None, None, 10, 0, None, "status"], ["smack-down", 100, 100, 15, 0, 50, "physical"], ["storm-throw", 100, None, 10, 0, 60, "physical"], ["flame-burst", 100, None, 15, 0, 70, "special"], ["sludge-wave", 100, 10, 10, 0, 95, "special"], ["quiver-dance", None, None, 20, 0, None, "status"], ["heavy-slam", 100, None, 10, 0, None, "physical"], ["synchronoise", 100, None, 10, 0, 120, "special"], ["electro-ball", 100, None, 10, 0, None, "special"], ["soak", 100, None, 20, 0, None, "status"], ["flame-charge", 100, 100, 20, 0, 50, "physical"], ["coil", None, None, 20, 0, None, "status"], ["low-sweep", 100, 100, 20, 0, 65, "physical"], ["acid-spray", 100, 100, 20, 0, 40, "special"], ["foul-play", 100, None, 15, 0, 95, "physical"], ["simple-beam", 100, None, 15, 0, None, "status"], ["entrainment", 100, None, 15, 0, None, "status"], ["after-you", None, None, 15, 0, None, "status"], ["round", 100, None, 15, 0, 60, "special"], ["echoed-voice", 100, None, 15, 0, 40, "special"], ["chip-away", 100, None, 20, 0, 70, "physical"], ["clear-smog", None, None, 15, 0, 50, "special"], ["stored-power", 100, None, 10, 0, 20, "special"], ["quick-guard", None, None, 15, 3, None, "status"], ["ally-switch", None, None, 15, 2, None, "status"], ["scald", 100, 30, 15, 0, 80, "special"], ["shell-smash", None, None, 15, 0, None, "status"], ["heal-pulse", None, None, 10, 0, None, "status"], ["hex", 100, None, 10, 0, 65, "special"], ["sky-drop", 100, None, 10, 0, 60, "physical"], ["shift-gear", None, None, 10, 0, None, "status"], ["circle-throw", 90, None, 10, -6, 60, "physical"], ["incinerate", 100, None, 15, 0, 60, "special"], ["quash", 100, None, 15, 0, None, "status"], ["acrobatics", 100, None, 15, 0, 55, "physical"], ["reflect-type", None, None, 15, 0, None, "status"], ["retaliate", 100, None, 5, 0, 70, "physical"], ["final-gambit", 100, None, 5, 0, None, "special"], ["bestow", None, None, 15, 0, None, "status"], ["inferno", 50, 100, 5, 0, 100, "special"], ["water-pledge", 100, None, 10, 0, 80, "special"], ["fire-pledge", 100, None, 10, 0, 80, "special"], ["grass-pledge", 100, None, 10, 0, 80, "special"], ["volt-switch", 100, None, 20, 0, 70, "special"], ["struggle-bug", 100, 100, 20, 0, 50, "special"], ["bulldoze", 100, 100, 20, 0, 60, "physical"], ["frost-breath", 90, 100, 10, 0, 60, "special"], ["dragon-tail", 90, None, 10, -6, 60, "physical"], ["work-up", None, None, 30, 0, None, "status"], ["electroweb", 95, 100, 15, 0, 55, "special"], ["wild-charge", 100, None, 15, 0, 90, "physical"], ["drill-run", 95, None, 10, 0, 80, "physical"], ["dual-chop", 90, None, 15, 0, 40, "physical"], ["heart-stamp", 100, 30, 25, 0, 60, "physical"], ["horn-leech", 100, None, 10, 0, 75, "physical"], ["sacred-sword", 100, None, 15, 0, 90, "physical"], ["razor-shell", 95, 50, 10, 0, 75, "physical"], ["heat-crash", 100, None, 10, 0, None, "physical"], ["leaf-tornado", 90, 50, 10, 0, 65, "special"], ["steamroller", 100, 30, 20, 0, 65, "physical"], ["cotton-guard", None, None, 10, 0, None, "status"], ["night-daze", 95, 40, 10, 0, 85, "special"], ["psystrike", 100, None, 10, 0, 100, "special"], ["tail-slap", 85, None, 10, 0, 25, "physical"], ["hurricane", 70, 30, 10, 0, 110, "special"], ["head-charge", 100, None, 15, 0, 120, "physical"], ["gear-grind", 85, None, 15, 0, 50, "physical"], ["searing-shot", 100, 30, 5, 0, 100, "special"], ["techno-blast", 100, None, 5, 0, 120, "special"], ["relic-song", 100, 10, 10, 0, 75, "special"], ["secret-sword", 100, None, 10, 0, 85, "special"], ["glaciate", 95, 100, 10, 0, 65, "special"], ["bolt-strike", 85, 20, 5, 0, 130, "physical"], ["blue-flare", 85, 20, 5, 0, 130, "special"], ["fiery-dance", 100, 50, 10, 0, 80, "special"], ["freeze-shock", 90, 30, 5, 0, 140, "physical"], ["ice-burn", 90, 30, 5, 0, 140, "special"], ["snarl", 95, 100, 15, 0, 55, "special"], ["icicle-crash", 90, 30, 10, 0, 85, "physical"], ["v-create", 95, 100, 5, 0, 180, "physical"], ["fusion-flare", 100, None, 5, 0, 100, "special"], ["fusion-bolt", 100, None, 5, 0, 100, "physical"], ["flying-press", 95, None, 10, 0, 100, "physical"], ["mat-block", None, None, 10, 0, None, "status"], ["belch", 90, None, 10, 0, 120, "special"], ["rototiller", None, 100, 10, 0, None, "status"], ["sticky-web", None, None, 20, 0, None, "status"], ["fell-stinger", 100, None, 25, 0, 50, "physical"], ["phantom-force", 100, None, 10, 0, 90, "physical"], ["trick-or-treat", 100, None, 20, 0, None, "status"], ["noble-roar", 100, 100, 30, 0, None, "status"], ["ion-deluge", None, None, 25, 1, None, "status"], ["parabolic-charge", 100, None, 20, 0, 65, "special"], ["forests-curse", 100, None, 20, 0, None, "status"], ["petal-blizzard", 100, None, 15, 0, 90, "physical"], ["freeze-dry", 100, 10, 20, 0, 70, "special"], ["disarming-voice", None, None, 15, 0, 40, "special"], ["parting-shot", 100, 100, 20, 0, None, "status"], ["topsy-turvy", None, None, 20, 0, None, "status"], ["draining-kiss", 100, None, 10, 0, 50, "special"], ["crafty-shield", None, None, 10, 3, None, "status"], ["flower-shield", None, 100, 10, 0, None, "status"], ["grassy-terrain", None, None, 10, 0, None, "status"], ["misty-terrain", None, None, 10, 0, None, "status"], ["electrify", None, None, 20, 0, None, "status"], ["play-rough", 90, 10, 10, 0, 90, "physical"], ["fairy-wind", 100, None, 30, 0, 40, "special"], ["moonblast", 100, 30, 15, 0, 95, "special"], ["boomburst", 100, None, 10, 0, 140, "special"], ["fairy-lock", None, None, 10, 0, None, "status"], ["kings-shield", None, None, 10, 4, None, "status"], ["play-nice", None, 100, 20, 0, None, "status"], ["confide", None, 100, 20, 0, None, "status"], ["diamond-storm", 95, 50, 5, 0, 100, "physical"], ["steam-eruption", 95, 30, 5, 0, 110, "special"], ["hyperspace-hole", None, None, 5, 0, 80, "special"], ["water-shuriken", 100, None, 20, 1, 15, "special"], ["mystical-fire", 100, 100, 10, 0, 75, "special"], ["spiky-shield", None, None, 10, 4, None, "status"], ["aromatic-mist", None, None, 20, 0, None, "status"], ["eerie-impulse", 100, None, 15, 0, None, "status"], ["venom-drench", 100, 100, 20, 0, None, "status"], ["powder", 100, None, 20, 1, None, "status"], ["geomancy", None, None, 10, 0, None, "status"], ["magnetic-flux", None, None, 20, 0, None, "status"], ["happy-hour", None, None, 30, 0, None, "status"], ["electric-terrain", None, None, 10, 0, None, "status"], ["dazzling-gleam", 100, None, 10, 0, 80, "special"], ["celebrate", None, None, 40, 0, None, "status"], ["hold-hands", None, None, 40, 0, None, "status"], ["baby-doll-eyes", 100, None, 30, 1, None, "status"], ["nuzzle", 100, 100, 20, 0, 20, "physical"], ["hold-back", 100, None, 40, 0, 40, "physical"], ["infestation", 100, 100, 20, 0, 20, "special"], ["power-up-punch", 100, 100, 20, 0, 40, "physical"], ["oblivion-wing", 100, None, 10, 0, 80, "special"], ["thousand-arrows", 100, 100, 10, 0, 90, "physical"], ["thousand-waves", 100, None, 10, 0, 90, "physical"], ["lands-wrath", 100, None, 10, 0, 90, "physical"], ["light-of-ruin", 90, None, 5, 0, 140, "special"], ["origin-pulse", 85, None, 10, 0, 110, "special"], ["precipice-blades", 85, None, 10, 0, 120, "physical"], ["dragon-ascent", 100, 100, 5, 0, 120, "physical"], ["hyperspace-fury", None, 100, 5, 0, 100, "physical"], ["breakneck-blitz--physical", None, None, 1, 0, None, "physical"], ["breakneck-blitz--special", None, None, 1, 0, None, "special"], ["all-out-pummeling--physical", None, None, 1, 0, None, "physical"], ["all-out-pummeling--special", None, None, 1, 0, None, "special"], ["supersonic-skystrike--physical", None, None, 1, 0, None, "physical"], ["supersonic-skystrike--special", None, None, 1, 0, None, "special"], ["acid-downpour--physical", None, None, 1, 0, None, "physical"], ["acid-downpour--special", None, None, 1, 0, None, "special"], ["tectonic-rage--physical", None, None, 1, 0, None, "physical"], ["tectonic-rage--special", None, None, 1, 0, None, "special"], ["continental-crush--physical", None, None, 1, 0, None, "physical"], ["continental-crush--special", None, None, 1, 0, None, "special"], ["savage-spin-out--physical", None, None, 1, 0, None, "physical"], ["savage-spin-out--special", None, None, 1, 0, None, "special"], ["never-ending-nightmare--physical", None, None, 1, 0, None, "physical"], ["never-ending-nightmare--special", None, None, 1, 0, None, "special"], ["corkscrew-crash--physical", None, None, 1, 0, None, "physical"], ["corkscrew-crash--special", None, None, 1, 0, None, "special"], ["inferno-overdrive--physical", None, None, 1, 0, None, "physical"], ["inferno-overdrive--special", None, None, 1, 0, None, "special"], ["hydro-vortex--physical", None, None, 1, 0, None, "physical"], ["hydro-vortex--special", None, None, 1, 0, None, "special"], ["bloom-doom--physical", None, None, 1, 0, None, "physical"], ["bloom-doom--special", None, None, 1, 0, None, "special"], ["gigavolt-havoc--physical", None, None, 1, 0, None, "physical"], ["gigavolt-havoc--special", None, None, 1, 0, None, "special"], ["shattered-psyche--physical", None, None, 1, 0, None, "physical"], ["shattered-psyche--special", None, None, 1, 0, None, "special"], ["subzero-slammer--physical", None, None, 1, 0, None, "physical"], ["subzero-slammer--special", None, None, 1, 0, None, "special"], ["devastating-drake--physical", None, None, 1, 0, None, "physical"], ["devastating-drake--special", None, None, 1, 0, None, "special"], ["black-hole-eclipse--physical", None, None, 1, 0, None, "physical"], ["black-hole-eclipse--special", None, None, 1, 0, None, "special"], ["twinkle-tackle--physical", None, None, 1, 0, None, "physical"], ["twinkle-tackle--special", None, None, 1, 0, None, "special"], ["catastropika", None, None, 1, 0, 210, "physical"], ["shore-up", None, None, 10, 0, None, "status"], ["first-impression", 100, None, 10, 2, 90, "physical"], ["baneful-bunker", None, None, 10, 4, None, "status"], ["spirit-shackle", 100, None, 10, 0, 80, "physical"], ["darkest-lariat", 100, None, 10, 0, 85, "physical"], ["sparkling-aria", 100, None, 10, 0, 90, "special"], ["ice-hammer", 90, 100, 10, 0, 100, "physical"], ["floral-healing", None, None, 10, 0, None, "status"], ["high-horsepower", 95, None, 10, 0, 95, "physical"], ["strength-sap", 100, 100, 10, 0, None, "status"], ["solar-blade", 100, None, 10, 0, 125, "physical"], ["leafage", 100, None, 40, 0, 40, "physical"], ["spotlight", None, None, 15, 3, None, "status"], ["toxic-thread", 100, 100, 20, 0, None, "status"], ["laser-focus", None, None, 30, 0, None, "status"], ["gear-up", None, None, 20, 0, None, "status"], ["throat-chop", 100, 100, 15, 0, 80, "physical"], ["pollen-puff", 100, None, 15, 0, 90, "special"], ["anchor-shot", 100, None, 20, 0, 80, "physical"], ["psychic-terrain", None, None, 10, 0, None, "status"], ["lunge", 100, 100, 15, 0, 80, "physical"], ["fire-lash", 100, 100, 15, 0, 80, "physical"], ["power-trip", 100, None, 10, 0, 20, "physical"], ["burn-up", 100, None, 5, 0, 130, "special"], ["speed-swap", None, None, 10, 0, None, "status"], ["smart-strike", None, None, 10, 0, 70, "physical"], ["purify", None, None, 20, 0, None, "status"], ["revelation-dance", 100, None, 15, 0, 90, "special"], ["core-enforcer", 100, None, 10, 0, 100, "special"], ["trop-kick", 100, 100, 15, 0, 70, "physical"], ["instruct", None, None, 15, 0, None, "status"], ["beak-blast", 100, None, 15, -3, 100, "physical"], ["clanging-scales", 100, 100, 5, 0, 110, "special"], ["dragon-hammer", 100, None, 15, 0, 90, "physical"], ["brutal-swing", 100, None, 20, 0, 60, "physical"], ["aurora-veil", None, None, 20, 0, None, "status"], ["sinister-arrow-raid", None, None, 1, 0, 180, "physical"], ["malicious-moonsault", None, None, 1, 0, 180, "physical"], ["oceanic-operetta", None, None, 1, 0, 195, "special"], ["guardian-of-alola", None, None, 1, 0, None, "special"], ["soul-stealing-7-star-strike", None, None, 1, 0, 195, "physical"], ["stoked-sparksurfer", None, 100, 1, 0, 175, "special"], ["pulverizing-pancake", None, None, 1, 0, 210, "physical"], ["extreme-evoboost", None, 100, 1, 0, None, "status"], ["genesis-supernova", None, None, 1, 0, 185, "special"], ["shell-trap", 100, None, 5, -3, 150, "special"], ["fleur-cannon", 90, 100, 5, 0, 130, "special"], ["psychic-fangs", 100, None, 10, 0, 85, "physical"], ["stomping-tantrum", 100, None, 10, 0, 75, "physical"], ["shadow-bone", 100, 20, 10, 0, 85, "physical"], ["accelerock", 100, None, 20, 1, 40, "physical"], ["liquidation", 100, 20, 10, 0, 85, "physical"], ["prismatic-laser", 100, None, 10, 0, 160, "special"], ["spectral-thief", 100, None, 10, 0, 90, "physical"], ["sunsteel-strike", 100, None, 5, 0, 100, "physical"], ["moongeist-beam", 100, None, 5, 0, 100, "special"], ["tearful-look", None, 100, 20, 0, None, "status"], ["zing-zap", 100, 30, 10, 0, 80, "physical"], ["natures-madness", 90, None, 10, 0, None, "special"], ["multi-attack", 100, None, 10, 0, 90, "physical"], ["10-000-000-volt-thunderbolt", None, None, 1, 0, 195, "special"], ["mind-blown", 100, None, 5, 0, 150, "special"], ["plasma-fists", 100, None, 15, 0, 100, "physical"], ["photon-geyser", 100, None, 5, 0, 100, "special"], ["light-that-burns-the-sky", None, None, 1, 0, 200, "special"], ["searing-sunraze-smash", None, None, 1, 0, 200, "physical"], ["menacing-moonraze-maelstrom", None, None, 1, 0, 200, "special"], ["lets-snuggle-forever", None, None, 1, 0, 190, "physical"], ["splintered-stormshards", None, None, 1, 0, 190, "physical"], ["clangorous-soulblaze", None, 100, 1, 0, 185, "special"], ["zippy-zap", 100, None, 15, 2, 50, "physical"], ["splishy-splash", 100, 30, 15, 0, 90, "special"], ["floaty-fall", 95, 30, 15, 0, 90, "physical"], ["pika-papow", None, None, 20, 0, None, "special"], ["bouncy-bubble", 100, None, 15, 0, 90, "special"], ["buzzy-buzz", 100, 100, 15, 0, 90, "special"], ["sizzly-slide", 100, 100, 15, 0, 90, "physical"], ["glitzy-glow", 100, None, 15, 0, 90, "special"], ["baddy-bad", 100, None, 15, 0, 90, "special"], ["sappy-seed", 100, None, 15, 0, 90, "physical"], ["freezy-frost", 100, None, 15, 0, 90, "special"], ["sparkly-swirl", 100, None, 15, 0, 90, "special"], ["veevee-volley", None, None, 20, 0, None, "physical"], ["double-iron-bash", 100, 30, 5, 0, 60, "physical"], ["max-guard", None, None, None, 4, None, "status"], ["dynamax-cannon", 100, None, 5, 0, 100, "special"], ["snipe-shot", 100, None, 15, 0, 80, "special"], ["jaw-lock", 100, None, 10, 0, 80, "physical"], ["stuff-cheeks", None, None, 10, 0, None, "status"], ["no-retreat", None, None, 5, 0, None, "status"], ["tar-shot", 100, None, 15, 0, None, "status"], ["magic-powder", 100, None, 20, 0, None, "status"], ["dragon-darts", 100, None, 10, 0, 50, "physical"], ["teatime", None, None, 10, 0, None, "status"], ["octolock", 100, None, 15, 0, None, "status"], ["bolt-beak", 100, None, 10, 0, 85, "physical"], ["fishious-rend", 100, None, 10, 0, 85, "physical"], ["court-change", 100, None, 10, 0, None, "status"], ["max-flare", None, None, None, 0, None, None], ["max-flutterby", None, None, None, 0, None, None], ["max-lightning", None, None, None, 0, None, None], ["max-strike", None, None, None, 0, None, None], ["max-knuckle", None, None, None, 0, None, None], ["max-phantasm", None, None, None, 0, None, None], ["max-hailstorm", None, None, None, 0, None, None], ["max-ooze", None, None, None, 0, None, None], ["max-geyser", None, None, None, 0, None, None], ["max-airstream", None, None, None, 0, None, None], ["max-starfall", None, None, None, 0, None, None], ["max-wyrmwind", None, None, None, 0, None, None], ["max-mindstorm", None, None, None, 0, None, None], ["max-rockfall", None, None, None, 0, None, None], ["max-quake", None, None, None, 0, None, None], ["max-darkness", None, None, None, 0, None, None], ["max-overgrowth", None, None, None, 0, None, None], ["max-steelspike", None, None, None, 0, None, None], ["clangorous-soul", 100, None, 5, 0, None, "status"], ["body-press", 100, None, 10, 0, 80, "physical"], ["decorate", None, None, 15, 0, None, "status"], ["drum-beating", 100, None, 10, 0, 80, "physical"], ["snap-trap", 100, None, 15, 0, 35, "physical"], ["pyro-ball", 90, None, 5, 0, 120, "physical"], ["behemoth-blade", 100, None, 5, 0, 100, "physical"], ["behemoth-bash", 100, None, 5, 0, 100, "physical"], ["aura-wheel", 100, None, 10, 0, 110, "physical"], ["breaking-swipe", 100, None, 15, 0, 60, "physical"]]

experience = [64, 142, 236, 62, 142, 240, 63, 142, 239, 39, 72, 178, 39, 72, 178, 50, 122, 216, 51, 145, 52, 155, 58, 157, 112, 218, 60, 158, 55, 128, 227, 55, 128, 227, 113, 217, 60, 177, 95, 196, 49, 159, 64, 138, 221, 57, 142, 61, 158, 53, 149, 58, 154, 64, 175, 61, 159, 70, 194, 60, 135, 230, 62, 140, 225, 61, 142, 227, 60, 137, 221, 67, 180, 60, 137, 223, 82, 175, 63, 172, 65, 163, 132, 62, 165, 65, 166, 65, 175, 61, 184, 62, 142, 225, 77, 66, 169, 65, 166, 66, 172, 65, 186, 64, 149, 159, 159, 77, 68, 172, 69, 170, 395, 87, 172, 59, 154, 64, 158, 68, 182, 161, 100, 159, 172, 173, 175, 172, 40, 189, 187, 101, 65, 184, 184, 184, 79, 71, 173, 71, 173, 180, 189, 261, 261, 261, 60, 147, 270, 306, 270, 64, 142, 236, 62, 142, 240, 63, 142, 239, 43, 145, 52, 158, 53, 137, 50, 140, 241, 66, 161, 41, 44, 42, 49, 142, 64, 165, 56, 128, 230, 221, 88, 189, 144, 225, 50, 119, 207, 72, 36, 149, 78, 42, 151, 184, 184, 81, 172, 87, 118, 142, 159, 58, 163, 145, 86, 179, 60, 158, 88, 175, 177, 175, 86, 66, 175, 50, 151, 50, 158, 144, 60, 168, 116, 170, 163, 66, 175, 243, 66, 175, 180, 163, 88, 42, 159, 61, 72, 73, 172, 608, 261, 261, 261, 60, 144, 270, 306, 306, 270, 62, 142, 239, 62, 142, 239, 62, 142, 241, 56, 147, 56, 147, 56, 72, 178, 72, 173, 44, 119, 216, 44, 119, 216, 54, 159, 54, 154, 40, 97, 233, 54, 159, 59, 161, 56, 154, 252, 53, 160, 83, 48, 126, 221, 47, 166, 38, 75, 52, 140, 133, 133, 66, 151, 239, 56, 144, 59, 166, 142, 142, 151, 151, 140, 60, 163, 61, 161, 80, 175, 61, 161, 165, 66, 165, 126, 58, 119, 234, 67, 166, 62, 172, 160, 160, 161, 161, 58, 164, 62, 164, 60, 175, 71, 173, 71, 173, 40, 189, 147, 154, 59, 159, 59, 159, 161, 159, 163, 52, 60, 168, 58, 144, 239, 69, 170, 170, 170, 116, 60, 147, 270, 60, 147, 270, 261, 261, 261, 270, 270, 302, 302, 306, 270, 270, 64, 142, 236, 62, 142, 240, 63, 142, 239, 49, 119, 218, 50, 144, 39, 134, 53, 127, 235, 56, 232, 70, 173, 70, 173, 45, 148, 148, 49, 166, 142, 66, 173, 55, 158, 65, 166, 169, 70, 174, 70, 168, 173, 177, 62, 158, 57, 66, 168, 60, 175, 58, 62, 110, 144, 170, 60, 144, 270, 78, 57, 184, 66, 184, 66, 175, 60, 172, 159, 66, 161, 69, 67, 173, 179, 241, 180, 241, 187, 243, 243, 245, 180, 184, 184, 179, 239, 241, 233, 184, 236, 168, 154, 261, 261, 261, 306, 306, 270, 302, 306, 270, 216, 270, 270, 270, 324, 270, 62, 145, 238, 62, 146, 238, 62, 145, 238, 51, 147, 55, 130, 225, 56, 156, 63, 174, 63, 174, 63, 174, 58, 170, 53, 125, 220, 59, 174, 56, 137, 232, 65, 149, 66, 178, 390, 61, 142, 227, 59, 134, 229, 163, 163, 62, 133, 225, 52, 126, 218, 56, 168, 56, 168, 161, 58, 123, 234, 63, 168, 161, 65, 170, 70, 171, 172, 61, 169, 71, 173, 71, 177, 66, 166, 66, 179, 60, 165, 58, 137, 221, 58, 130, 221, 61, 166, 61, 138, 241, 67, 166, 150, 63, 173, 59, 162, 67, 168, 165, 64, 165, 61, 171, 60, 154, 234, 55, 142, 232, 67, 170, 55, 130, 234, 64, 144, 243, 61, 177, 180, 61, 173, 165, 70, 179, 170, 61, 169, 68, 172, 172, 70, 179, 74, 179, 169, 169, 60, 147, 270, 72, 248, 261, 261, 261, 261, 261, 306, 306, 270, 297, 261, 270, 270, 63, 142, 239, 61, 143, 240, 63, 142, 239, 47, 148, 56, 134, 175, 40, 75, 185, 74, 177, 61, 130, 248, 70, 186, 70, 173, 165, 71, 163, 65, 157, 234, 68, 162, 68, 168, 58, 169, 61, 175, 64, 173, 66, 100, 58, 168, 72, 182, 72, 104, 184, 175, 151, 100, 60, 158, 270, 165, 62, 166, 67, 173, 61, 180, 49, 187, 306, 306, 270, 270, 270, 270, 64, 147, 239, 64, 147, 239, 64, 147, 239, 53, 124, 218, 51, 146, 60, 140, 225, 68, 167, 167, 61, 162, 56, 170, 61, 61, 173, 77, 175, 54, 159, 50, 168, 57, 142, 64, 168, 68, 175, 42, 102, 230, 170, 172, 172, 46, 186, 64, 168, 144, 107, 257, 154, 168, 170, 152, 167, 166, 170, 181, 60, 147, 270, 257, 257, 257, 257, 40, 140, 306, 306, 257, 257, 257, 257, 257, 257, 257, 270, 270, 270, 189, 243, 257, 257, 270, 135, 270, 62, 147, 265, 62, 147, 265, 62, 147, 265, 55, 161, 49, 128, 248, 36, 117, 253, 49, 159, 50, 161, 122, 172, 57, 170, 54, 172, 48, 144, 255, 52, 170, 170, 63, 179, 166, 56, 172, 48, 176, 61, 184, 62, 168, 62, 178, 53, 130, 255, 53, 130, 255, 260, 154, 179, 177, 182, 169, 54, 173, 165, 152, 37, 168, 165, 165, 166, 153, 66, 175, 177, 177, 177, 177, 187, 54, 144, 300, 335, 335, 345, 77, 275, 300, 290, 290, 290, 290, 250]

dex = [["bulbasaur", "bulbizarre", "bisasam", "妙蛙種子", "이상해씨", "fushigidane", "フシギダネ"], ["ivysaur", "herbizarre", "bisaknosp", "妙蛙草", "이상해풀", "fushigisou", "フシギソウ"], ["venusaur", "florizarre", "bisaflor", "妙蛙花", "이상해꽃", "fushigibana", "フシギバナ"], ["charmander", "salamèche", "glumanda", "小火龍", "파이리", "hitokage", "ヒトカゲ"], ["charmeleon", "reptincel", "glutexo", "火恐龍", "리자드", "lizardo", "リザード"], ["charizard", "dracaufeu", "glurak", "噴火龍", "리자몽", "lizardon", "リザードン"], ["squirtle", "carapuce", "schiggy", "傑尼龜", "꼬부기", "zenigame", "ゼニガメ"], ["wartortle", "carabaffe", "schillok", "卡咪龜", "어니부기", "kameil", "カメール"], ["blastoise", "tortank", "turtok", "水箭龜", "거북왕", "kamex", "カメックス"], ["caterpie", "chenipan", "raupy", "綠毛蟲", "캐터피", "caterpie", "キャタピー"], ["metapod", "chrysacier", "safcon", "鐵甲蛹", "단데기", "trancell", "トランセル"], ["butterfree", "papilusion", "smettbo", "巴大蝶", "버터플", "butterfree", "バタフリー"], ["weedle", "aspicot", "hornliu", "獨角蟲", "뿔충이", "beedle", "ビードル"], ["kakuna", "coconfort", "kokuna", "鐵殼蛹", "딱충이", "cocoon", "コクーン"], ["beedrill", "dardargnan", "bibor", "大針蜂", "독침붕", "spear", "スピアー"], ["pidgey", "roucool", "taubsi", "波波", "구구", "poppo", "ポッポ"], ["pidgeotto", "roucoups", "tauboga", "比比鳥", "피죤", "pigeon", "ピジョン"], ["pidgeot", "roucarnage", "tauboss", "大比鳥", "피죤투", "pigeot", "ピジョット"], ["rattata", "rattata", "rattfratz", "小拉達", "꼬렛", "koratta", "コラッタ"], ["raticate", "rattatac", "rattikarl", "拉達", "레트라", "ratta", "ラッタ"], ["spearow", "piafabec", "habitak", "烈雀", "깨비참", "onisuzume", "オニスズメ"], ["fearow", "rapasdepic", "ibitak", "大嘴雀", "깨비드릴조", "onidrill", "オニドリル"], ["ekans", "abo", "rettan", "阿柏蛇", "아보", "arbo", "アーボ"], ["arbok", "arbok", "arbok", "阿柏怪", "아보크", "arbok", "アーボック"], ["pikachu", "pikachu", "pikachu", "皮卡丘", "피카츄", "pikachu", "ピカチュウ"], ["raichu", "raichu", "raichu", "雷丘", "라이츄", "raichu", "ライチュウ"], ["sandshrew", "sabelette", "sandan", "穿山鼠", "모래두지", "sand", "サンド"], ["sandslash", "sablaireau", "sandamer", "穿山王", "고지", "sandpan", "サンドパン"], ["nidoranf", "nidoran♀", "nidoran♀", "尼多蘭", "니드런♀", "nidoran♀", "ニドラン♀"], ["nidorina", "nidorina", "nidorina", "尼多娜", "니드리나", "nidorina", "ニドリーナ"], ["nidoqueen", "nidoqueen", "nidoqueen", "尼多后", "니드퀸", "nidoqueen", "ニドクイン"], ["nidoranm", "nidoran♂", "nidoran♂", "尼多朗", "니드런♂", "nidoran♂", "ニドラン♂"], ["nidorino", "nidorino", "nidorino", "尼多力諾", "니드리노", "nidorino", "ニドリーノ"], ["nidoking", "nidoking", "nidoking", "尼多王", "니드킹", "nidoking", "ニドキング"], ["clefairy", "mélofée", "piepi", "皮皮", "삐삐", "pippi", "ピッピ"], ["clefable", "mélodelfe", "pixi", "皮可西", "픽시", "pixy", "ピクシー"], ["vulpix", "goupix", "vulpix", "六尾", "식스테일", "rokon", "ロコン"], ["ninetales", "feunard", "vulnona", "九尾", "나인테일", "kyukon", "キュウコン"], ["jigglypuff", "rondoudou", "pummeluff", "胖丁", "푸린", "purin", "プリン"], ["wigglytuff", "grodoudou", "knuddeluff", "胖可丁", "푸크린", "pukurin", "プクリン"], ["zubat", "nosferapti", "zubat", "超音蝠", "주뱃", "zubat", "ズバット"], ["golbat", "nosferalto", "golbat", "大嘴蝠", "골뱃", "golbat", "ゴルバット"], ["oddish", "mystherbe", "myrapla", "走路草", "뚜벅쵸", "nazonokusa", "ナゾノクサ"], ["gloom", "ortide", "duflor", "臭臭花", "냄새꼬", "kusaihana", "クサイハナ"], ["vileplume", "rafflesia", "giflor", "霸王花", "라플레시아", "ruffresia", "ラフレシア"], ["paras", "paras", "paras", "派拉斯", "파라스", "paras", "パラス"], ["parasect", "parasect", "parasek", "派拉斯特", "파라섹트", "parasect", "パラセクト"], ["venonat", "mimitoss", "bluzuk", "毛球", "콘팡", "kongpang", "コンパン"], ["venomoth", "aéromite", "omot", "摩魯蛾", "도나리", "morphon", "モルフォン"], ["diglett", "taupiqueur", "digda", "地鼠", "디그다", "digda", "ディグダ"], ["dugtrio", "triopikeur", "digdri", "三地鼠", "닥트리오", "dugtrio", "ダグトリオ"], ["meowth", "miaouss", "mauzi", "喵喵", "나옹", "nyarth", "ニャース"], ["persian", "persian", "snobilikat", "貓老大", "페르시온", "persian", "ペルシアン"], ["psyduck", "psykokwak", "enton", "可達鴨", "고라파덕", "koduck", "コダック"], ["golduck", "akwakwak", "entoron", "哥達鴨", "골덕", "golduck", "ゴルダック"], ["mankey", "férosinge", "menki", "猴怪", "망키", "mankey", "マンキー"], ["primeape", "colossinge", "rasaff", "火爆猴", "성원숭", "okorizaru", "オコリザル"], ["growlithe", "caninos", "fukano", "卡蒂狗", "가디", "gardie", "ガーディ"], ["arcanine", "arcanin", "arkani", "風速狗", "윈디", "windie", "ウインディ"], ["poliwag", "ptitard", "quapsel", "蚊香蝌蚪", "발챙이", "nyoromo", "ニョロモ"], ["poliwhirl", "têtarte", "quaputzi", "蚊香君", "슈륙챙이", "nyorozo", "ニョロゾ"], ["poliwrath", "tartard", "quappo", "蚊香泳士", "강챙이", "nyorobon", "ニョロボン"], ["abra", "abra", "abra", "凱西", "캐이시", "casey", "ケーシィ"], ["kadabra", "kadabra", "kadabra", "勇基拉", "윤겔라", "yungerer", "ユンゲラー"], ["alakazam", "alakazam", "simsala", "胡地", "후딘", "foodin", "フーディン"], ["machop", "machoc", "machollo", "腕力", "알통몬", "wanriky", "ワンリキー"], ["machoke", "machopeur", "maschock", "豪力", "근육몬", "goriky", "ゴーリキー"], ["machamp", "mackogneur", "machomei", "怪力", "괴력몬", "kairiky", "カイリキー"], ["bellsprout", "chétiflor", "knofensa", "喇叭芽", "모다피", "madatsubomi", "マダツボミ"], ["weepinbell", "boustiflor", "ultrigaria", "口呆花", "우츠동", "utsudon", "ウツドン"], ["victreebel", "empiflor", "sarzenia", "大食花", "우츠보트", "utsubot", "ウツボット"], ["tentacool", "tentacool", "tentacha", "瑪瑙水母", "왕눈해", "menokurage", "メノクラゲ"], ["tentacruel", "tentacruel", "tentoxa", "毒刺水母", "독파리", "dokukurage", "ドククラゲ"], ["geodude", "racaillou", "kleinstein", "小拳石", "꼬마돌", "isitsubute", "イシツブテ"], ["graveler", "gravalanch", "georok", "隆隆石", "데구리", "golone", "ゴローン"], ["golem", "grolem", "geowaz", "隆隆岩", "딱구리", "golonya", "ゴローニャ"], ["ponyta", "ponyta", "ponita", "小火馬", "포니타", "ponyta", "ポニータ"], ["rapidash", "galopa", "gallopa", "烈焰馬", "날쌩마", "gallop", "ギャロップ"], ["slowpoke", "ramoloss", "flegmon", "呆呆獸", "야돈", "yadon", "ヤドン"], ["slowbro", "flagadoss", "lahmus", "呆殼獸", "야도란", "yadoran", "ヤドラン"], ["magnemite", "magnéti", "magnetilo", "小磁怪", "코일", "coil", "コイル"], ["magneton", "magnéton", "magneton", "三合一磁怪", "레어코일", "rarecoil", "レアコイル"], ["farfetch’d", "canarticho", "porenta", "大蔥鴨", "파오리", "kamonegi", "カモネギ"], ["doduo", "doduo", "dodu", "嘟嘟", "두두", "dodo", "ドードー"], ["dodrio", "dodrio", "dodri", "嘟嘟利", "두트리오", "dodorio", "ドードリオ"], ["seel", "otaria", "jurob", "小海獅", "쥬쥬", "pawou", "パウワウ"], ["dewgong", "lamantine", "jugong", "白海獅", "쥬레곤", "jugon", "ジュゴン"], ["grimer", "tadmorv", "sleima", "臭泥", "질퍽이", "betbeter", "ベトベター"], ["muk", "grotadmorv", "sleimok", "臭臭泥", "질뻐기", "betbeton", "ベトベトン"], ["shellder", "kokiyas", "muschas", "大舌貝", "셀러", "shellder", "シェルダー"], ["cloyster", "crustabri", "austos", "刺甲貝", "파르셀", "parshen", "パルシェン"], ["gastly", "fantominus", "nebulak", "鬼斯", "고오스", "ghos", "ゴース"], ["haunter", "spectrum", "alpollo", "鬼斯通", "고우스트", "ghost", "ゴースト"], ["gengar", "ectoplasma", "gengar", "耿鬼", "팬텀", "gangar", "ゲンガー"], ["onix", "onix", "onix", "大岩蛇", "롱스톤", "iwark", "イワーク"], ["drowzee", "soporifik", "traumato", "催眠貘", "슬리프", "sleep", "スリープ"], ["hypno", "hypnomade", "hypno", "引夢貘人", "슬리퍼", "sleeper", "スリーパー"], ["krabby", "krabby", "krabby", "大鉗蟹", "크랩", "crab", "クラブ"], ["kingler", "krabboss", "kingler", "巨鉗蟹", "킹크랩", "kingler", "キングラー"], ["voltorb", "voltorbe", "voltobal", "霹靂電球", "찌리리공", "biriridama", "ビリリダマ"], ["electrode", "électrode", "lektrobal", "頑皮雷彈", "붐볼", "marumine", "マルマイン"], ["exeggcute", "noeunoeuf", "owei", "蛋蛋", "아라리", "tamatama", "タマタマ"], ["exeggutor", "noadkoko", "kokowei", "椰蛋樹", "나시", "nassy", "ナッシー"], ["cubone", "osselait", "tragosso", "卡拉卡拉", "탕구리", "karakara", "カラカラ"], ["marowak", "ossatueur", "knogga", "嘎啦嘎啦", "텅구리", "garagara", "ガラガラ"], ["hitmonlee", "kicklee", "kicklee", "飛腿郎", "시라소몬", "sawamular", "サワムラー"], ["hitmonchan", "tygnon", "nockchan", "快拳郎", "홍수몬", "ebiwalar", "エビワラー"], ["lickitung", "excelangue", "schlurp", "大舌頭", "내루미", "beroringa", "ベロリンガ"], ["koffing", "smogo", "smogon", "瓦斯彈", "또가스", "dogars", "ドガース"], ["weezing", "smogogo", "smogmog", "雙彈瓦斯", "또도가스", "matadogas", "マタドガス"], ["rhyhorn", "rhinocorne", "rihorn", "獨角犀牛", "뿔카노", "sihorn", "サイホーン"], ["rhydon", "rhinoféros", "rizeros", "鑽角犀獸", "코뿌리", "sidon", "サイドン"], ["chansey", "leveinard", "chaneira", "吉利蛋", "럭키", "lucky", "ラッキー"], ["tangela", "saquedeneu", "tangela", "蔓藤怪", "덩쿠리", "monjara", "モンジャラ"], ["kangaskhan", "kangourex", "kangama", "袋獸", "캥카", "garura", "ガルーラ"], ["horsea", "hypotrempe", "seeper", "墨海馬", "쏘드라", "tattu", "タッツー"], ["seadra", "hypocéan", "seemon", "海刺龍", "시드라", "seadra", "シードラ"], ["goldeen", "poissirène", "goldini", "角金魚", "콘치", "tosakinto", "トサキント"], ["seaking", "poissoroy", "golking", "金魚王", "왕콘치", "azumao", "アズマオウ"], ["staryu", "stari", "sterndu", "海星星", "별가사리", "hitodeman", "ヒトデマン"], ["starmie", "staross", "starmie", "寶石海星", "아쿠스타", "starmie", "スターミー"], ["mr. mime", "m. mime", "pantimos", "魔牆人偶", "마임맨", "barrierd", "バリヤード"], ["scyther", "insécateur", "sichlor", "飛天螳螂", "스라크", "strike", "ストライク"], ["jynx", "lippoutou", "rossana", "迷唇姐", "루주라", "rougela", "ルージュラ"], ["electabuzz", "élektek", "elektek", "電擊獸", "에레브", "eleboo", "エレブー"], ["magmar", "magmar", "magmar", "鴨嘴火獸", "마그마", "boober", "ブーバー"], ["pinsir", "scarabrute", "pinsir", "凱羅斯", "쁘사이저", "kailios", "カイロス"], ["tauros", "tauros", "tauros", "肯泰羅", "켄타로스", "kentauros", "ケンタロス"], ["magikarp", "magicarpe", "karpador", "鯉魚王", "잉어킹", "koiking", "コイキング"], ["gyarados", "léviator", "garados", "暴鯉龍", "갸라도스", "gyarados", "ギャラドス"], ["lapras", "lokhlass", "lapras", "拉普拉斯", "라프라스", "laplace", "ラプラス"], ["ditto", "métamorph", "ditto", "百變怪", "메타몽", "metamon", "メタモン"], ["eevee", "évoli", "evoli", "伊布", "이브이", "eievui", "イーブイ"], ["vaporeon", "aquali", "aquana", "水伊布", "샤미드", "showers", "シャワーズ"], ["jolteon", "voltali", "blitza", "雷伊布", "쥬피썬더", "thunders", "サンダース"], ["flareon", "pyroli", "flamara", "火伊布", "부스터", "booster", "ブースター"], ["porygon", "porygon", "porygon", "多邊獸", "폴리곤", "porygon", "ポリゴン"], ["omanyte", "amonita", "amonitas", "菊石獸", "암나이트", "omnite", "オムナイト"], ["omastar", "amonistar", "amoroso", "多刺菊石獸", "암스타", "omstar", "オムスター"], ["kabuto", "kabuto", "kabuto", "化石盔", "투구", "kabuto", "カブト"], ["kabutops", "kabutops", "kabutops", "鐮刀盔", "투구푸스", "kabutops", "カブトプス"], ["aerodactyl", "ptéra", "aerodactyl", "化石翼龍", "프테라", "ptera", "プテラ"], ["snorlax", "ronflex", "relaxo", "卡比獸", "잠만보", "kabigon", "カビゴン"], ["articuno", "artikodin", "arktos", "急凍鳥", "프리져", "freezer", "フリーザー"], ["zapdos", "électhor", "zapdos", "閃電鳥", "썬더", "thunder", "サンダー"], ["moltres", "sulfura", "lavados", "火焰鳥", "파이어", "fire", "ファイヤー"], ["dratini", "minidraco", "dratini", "迷你龍", "미뇽", "miniryu", "ミニリュウ"], ["dragonair", "draco", "dragonir", "哈克龍", "신뇽", "hakuryu", "ハクリュー"], ["dragonite", "dracolosse", "dragoran", "快龍", "망나뇽", "kairyu", "カイリュー"], ["mewtwo", "mewtwo", "mewtu", "超夢", "뮤츠", "mewtwo", "ミュウツー"], ["mew", "mew", "mew", "夢幻", "뮤", "mew", "ミュウ"], ["chikorita", "germignon", "endivie", "菊草葉", "치코리타", "chicorita", "チコリータ"], ["bayleef", "macronium", "lorblatt", "月桂葉", "베이리프", "bayleaf", "ベイリーフ"], ["meganium", "méganium", "meganie", "大竺葵", "메가니움", "meganium", "メガニウム"], ["cyndaquil", "héricendre", "feurigel", "火球鼠", "브케인", "hinoarashi", "ヒノアラシ"], ["quilava", "feurisson", "igelavar", "火岩鼠", "마그케인", "magmarashi", "マグマラシ"], ["typhlosion", "typhlosion", "tornupto", "火爆獸", "블레이범", "bakphoon", "バクフーン"], ["totodile", "kaiminus", "karnimani", "小鋸鱷", "리아코", "waninoko", "ワニノコ"], ["croconaw", "crocrodil", "tyracroc", "藍鱷", "엘리게이", "alligates", "アリゲイツ"], ["feraligatr", "aligatueur", "impergator", "大力鱷", "장크로다일", "ordile", "オーダイル"], ["sentret", "fouinette", "wiesor", "尾立", "꼬리선", "otachi", "オタチ"], ["furret", "fouinar", "wiesenior", "大尾立", "다꼬리", "ootachi", "オオタチ"], ["hoothoot", "hoothoot", "hoothoot", "咕咕", "부우부", "hoho", "ホーホー"], ["noctowl", "noarfang", "noctuh", "貓頭夜鷹", "야부엉", "yorunozuku", "ヨルノズク"], ["ledyba", "coxy", "ledyba", "芭瓢蟲", "레디바", "rediba", "レディバ"], ["ledian", "coxyclaque", "ledian", "安瓢蟲", "레디안", "redian", "レディアン"], ["spinarak", "mimigal", "webarak", "圓絲蛛", "페이검", "itomaru", "イトマル"], ["ariados", "migalos", "ariados", "阿利多斯", "아리아도스", "ariados", "アリアドス"], ["crobat", "nostenfer", "iksbat", "叉字蝠", "크로뱃", "crobat", "クロバット"], ["chinchou", "loupio", "lampi", "燈籠魚", "초라기", "chonchie", "チョンチー"], ["lanturn", "lanturn", "lanturn", "電燈怪", "랜턴", "lantern", "ランターン"], ["pichu", "pichu", "pichu", "皮丘", "피츄", "pichu", "ピチュー"], ["cleffa", "mélo", "pii", "皮寶寶", "삐", "py", "ピィ"], ["igglybuff", "toudoudou", "fluffeluff", "寶寶丁", "푸푸린", "pupurin", "ププリン"], ["togepi", "togepi", "togepi", "波克比", "토게피", "togepy", "トゲピー"], ["togetic", "togetic", "togetic", "波克基古", "토게틱", "togechick", "トゲチック"], ["natu", "natu", "natu", "天然雀", "네이티", "naty", "ネイティ"], ["xatu", "xatu", "xatu", "天然鳥", "네이티오", "natio", "ネイティオ"], ["mareep", "wattouat", "voltilamm", "咩利羊", "메리프", "merriep", "メリープ"], ["flaaffy", "lainergie", "waaty", "茸茸羊", "보송송", "mokoko", "モココ"], ["ampharos", "pharamp", "ampharos", "電龍", "전룡", "denryu", "デンリュウ"], ["bellossom", "joliflor", "blubella", "美麗花", "아르코", "kireihana", "キレイハナ"], ["marill", "marill", "marill", "瑪力露", "마릴", "maril", "マリル"], ["azumarill", "azumarill", "azumarill", "瑪力露麗", "마릴리", "marilli", "マリルリ"], ["sudowoodo", "simularbre", "mogelbaum", "樹才怪", "꼬지모", "usokkie", "ウソッキー"], ["politoed", "tarpaud", "quaxo", "蚊香蛙皇", "왕구리", "nyorotono", "ニョロトノ"], ["hoppip", "granivol", "hoppspross", "毽子草", "통통코", "hanecco", "ハネッコ"], ["skiploom", "floravol", "hubelupf", "毽子花", "두코", "popocco", "ポポッコ"], ["jumpluff", "cotovol", "papungha", "毽子棉", "솜솜코", "watacco", "ワタッコ"], ["aipom", "capumain", "griffel", "長尾怪手", "에이팜", "eipam", "エイパム"], ["sunkern", "tournegrin", "sonnkern", "向日種子", "해너츠", "himanuts", "ヒマナッツ"], ["sunflora", "héliatronc", "sonnflora", "向日花怪", "해루미", "kimawari", "キマワリ"], ["yanma", "yanma", "yanma", "蜻蜻蜓", "왕자리", "yanyanma", "ヤンヤンマ"], ["wooper", "axoloto", "felino", "烏波", "우파", "upah", "ウパー"], ["quagsire", "maraiste", "morlord", "沼王", "누오", "nuoh", "ヌオー"], ["espeon", "mentali", "psiana", "太陽伊布", "에브이", "eifie", "エーフィ"], ["umbreon", "noctali", "nachtara", "月亮伊布", "블래키", "blacky", "ブラッキー"], ["murkrow", "cornèbre", "kramurx", "黑暗鴉", "니로우", "yamikarasu", "ヤミカラス"], ["slowking", "roigada", "laschoking", "呆呆王", "야도킹", "yadoking", "ヤドキング"], ["misdreavus", "feuforêve", "traunfugil", "夢妖", "무우마", "muma", "ムウマ"], ["unown", "zarbi", "icognito", "未知圖騰", "안농", "unknown", "アンノーン"], ["wobbuffet", "qulbutoké", "woingenau", "果然翁", "마자용", "sonans", "ソーナンス"], ["girafarig", "girafarig", "girafarig", "麒麟奇", "키링키", "kirinriki", "キリンリキ"], ["pineco", "pomdepik", "tannza", "榛果球", "피콘", "kunugidama", "クヌギダマ"], ["forretress", "foretress", "forstellka", "佛烈托斯", "쏘콘", "foretos", "フォレトス"], ["dunsparce", "insolourdo", "dummisel", "土龍弟弟", "노고치", "nokocchi", "ノコッチ"], ["gligar", "scorplane", "skorgla", "天蠍", "글라이거", "gliger", "グライガー"], ["steelix", "steelix", "stahlos", "大鋼蛇", "강철톤", "haganeil", "ハガネール"], ["snubbull", "snubbull", "snubbull", "布魯", "블루", "bulu", "ブルー"], ["granbull", "granbull", "granbull", "布魯皇", "그랑블루", "granbulu", "グランブル"], ["qwilfish", "qwilfish", "baldorfish", "千針魚", "침바루", "harysen", "ハリーセン"], ["scizor", "cizayox", "scherox", "巨鉗螳螂", "핫삼", "hassam", "ハッサム"], ["shuckle", "caratroc", "pottrott", "壺壺", "단단지", "tsubotsubo", "ツボツボ"], ["heracross", "scarhino", "skaraborn", "赫拉克羅斯", "헤라크로스", "heracros", "ヘラクロス"], ["sneasel", "farfuret", "sniebel", "狃拉", "포푸니", "nyula", "ニューラ"], ["teddiursa", "teddiursa", "teddiursa", "熊寶寶", "깜지곰", "himeguma", "ヒメグマ"], ["ursaring", "ursaring", "ursaring", "圈圈熊", "링곰", "ringuma", "リングマ"], ["slugma", "limagma", "schneckmag", "熔岩蟲", "마그마그", "magmag", "マグマッグ"], ["magcargo", "volcaropod", "magcargo", "熔岩蝸牛", "마그카르고", "magcargot", "マグカルゴ"], ["swinub", "marcacrin", "quiekel", "小山豬", "꾸꾸리", "urimoo", "ウリムー"], ["piloswine", "cochignon", "keifel", "長毛豬", "메꾸리", "inomoo", "イノムー"], ["corsola", "corayon", "corasonn", "太陽珊瑚", "코산호", "sunnygo", "サニーゴ"], ["remoraid", "rémoraid", "remoraid", "鐵砲魚", "총어", "teppouo", "テッポウオ"], ["octillery", "octillery", "octillery", "章魚桶", "대포무노", "okutank", "オクタン"], ["delibird", "cadoizo", "botogel", "信使鳥", "딜리버드", "delibird", "デリバード"], ["mantine", "démanta", "mantax", "巨翅飛魚", "만타인", "mantain", "マンタイン"], ["skarmory", "airmure", "panzaeron", "盔甲鳥", "무장조", "airmd", "エアームド"], ["houndour", "malosse", "hunduster", "戴魯比", "델빌", "delvil", "デルビル"], ["houndoom", "démolosse", "hundemon", "黑魯加", "헬가", "hellgar", "ヘルガー"], ["kingdra", "hyporoi", "seedraking", "刺龍王", "킹드라", "kingdra", "キングドラ"], ["phanpy", "phanpy", "phanpy", "小小象", "코코리", "gomazou", "ゴマゾウ"], ["donphan", "donphan", "donphan", "頓甲", "코리갑", "donfan", "ドンファン"], ["porygon2", "porygon2", "porygon2", "多邊獸２", "폴리곤2", "porygon2", "ポリゴン２"], ["stantler", "cerfrousse", "damhirplex", "驚角鹿", "노라키", "odoshishi", "オドシシ"], ["smeargle", "queulorior", "farbeagle", "圖圖犬", "루브도", "doble", "ドーブル"], ["tyrogue", "debugant", "rabauz", "無畏小子", "배루키", "balkie", "バルキー"], ["hitmontop", "kapoera", "kapoera", "戰舞郎", "카포에라", "kapoerer", "カポエラー"], ["smoochum", "lippouti", "kussilla", "迷唇娃", "뽀뽀라", "muchul", "ムチュール"], ["elekid", "élekid", "elekid", "電擊怪", "에레키드", "elekid", "エレキッド"], ["magby", "magby", "magby", "鴨嘴寶寶", "마그비", "buby", "ブビィ"], ["miltank", "écrémeuh", "miltank", "大奶罐", "밀탱크", "miltank", "ミルタンク"], ["blissey", "leuphorie", "heiteira", "幸福蛋", "해피너스", "happinas", "ハピナス"], ["raikou", "raikou", "raikou", "雷公", "라이코", "raikou", "ライコウ"], ["entei", "entei", "entei", "炎帝", "앤테이", "entei", "エンテイ"], ["suicune", "suicune", "suicune", "水君", "스이쿤", "suikun", "スイクン"], ["larvitar", "embrylex", "larvitar", "幼基拉斯", "애버라스", "yogiras", "ヨーギラス"], ["pupitar", "ymphect", "pupitar", "沙基拉斯", "데기라스", "sanagiras", "サナギラス"], ["tyranitar", "tyranocif", "despotar", "班基拉斯", "마기라스", "bangiras", "バンギラス"], ["lugia", "lugia", "lugia", "洛奇亞", "루기아", "lugia", "ルギア"], ["ho-oh", "ho-oh", "ho-oh", "鳳王", "칠색조", "houou", "ホウオウ"], ["celebi", "celebi", "celebi", "時拉比", "세레비", "celebi", "セレビィ"], ["treecko", "arcko", "geckarbor", "木守宮", "나무지기", "kimori", "キモリ"], ["grovyle", "massko", "reptain", "森林蜥蜴", "나무돌이", "juptile", "ジュプトル"], ["sceptile", "jungko", "gewaldro", "蜥蜴王", "나무킹", "jukain", "ジュカイン"], ["torchic", "poussifeu", "flemmli", "火稚雞", "아차모", "achamo", "アチャモ"], ["combusken", "galifeu", "jungglut", "力壯雞", "영치코", "wakasyamo", "ワカシャモ"], ["blaziken", "braségali", "lohgock", "火焰雞", "번치코", "bursyamo", "バシャーモ"], ["mudkip", "gobou", "hydropi", "水躍魚", "물짱이", "mizugorou", "ミズゴロウ"], ["marshtomp", "flobio", "moorabbel", "沼躍魚", "늪짱이", "numacraw", "ヌマクロー"], ["swampert", "laggron", "sumpex", "巨沼怪", "대짱이", "laglarge", "ラグラージ"], ["poochyena", "medhyèna", "fiffyen", "土狼犬", "포챠나", "pochiena", "ポチエナ"], ["mightyena", "grahyèna", "magnayen", "大狼犬", "그라에나", "guraena", "グラエナ"], ["zigzagoon", "zigzaton", "zigzachs", "蛇紋熊", "지그제구리", "ziguzaguma", "ジグザグマ"], ["linoone", "linéon", "geradaks", "直衝熊", "직구리", "massuguma", "マッスグマ"], ["wurmple", "chenipotte", "waumpel", "刺尾蟲", "개무소", "kemusso", "ケムッソ"], ["silcoon", "armulys", "schaloko", "甲殼繭", "실쿤", "karasalis", "カラサリス"], ["beautifly", "charmillon", "papinella", "狩獵鳳蝶", "뷰티플라이", "agehunt", "アゲハント"], ["cascoon", "blindalys", "panekon", "盾甲繭", "카스쿤", "mayuld", "マユルド"], ["dustox", "papinox", "pudox", "毒粉蛾", "독케일", "dokucale", "ドクケイル"], ["lotad", "nénupiot", "loturzel", "蓮葉童子", "연꽃몬", "hassboh", "ハスボー"], ["lombre", "lombre", "lombrero", "蓮帽小童", "로토스", "hasubrero", "ハスブレロ"], ["ludicolo", "ludicolo", "kappalores", "樂天河童", "로파파", "runpappa", "ルンパッパ"], ["seedot", "grainipiot", "samurzel", "橡實果", "도토링", "taneboh", "タネボー"], ["nuzleaf", "pifeuil", "blanas", "長鼻葉", "잎새코", "konohana", "コノハナ"], ["shiftry", "tengalice", "tengulist", "狡猾天狗", "다탱구", "dirteng", "ダーテング"], ["taillow", "nirondelle", "schwalbini", "傲骨燕", "테일로", "subame", "スバメ"], ["swellow", "hélédelle", "schwalboss", "大王燕", "스왈로", "ohsubame", "オオスバメ"], ["wingull", "goélise", "wingull", "長翅鷗", "갈모매", "camome", "キャモメ"], ["pelipper", "bekipan", "pelipper", "大嘴鷗", "패리퍼", "pelipper", "ペリッパー"], ["ralts", "tarsal", "trasla", "拉魯拉絲", "랄토스", "ralts", "ラルトス"], ["kirlia", "kirlia", "kirlia", "奇魯莉安", "킬리아", "kirlia", "キルリア"], ["gardevoir", "gardevoir", "guardevoir", "沙奈朵", "가디안", "sirnight", "サーナイト"], ["surskit", "arakdo", "gehweiher", "溜溜糖球", "비구술", "ametama", "アメタマ"], ["masquerain", "maskadra", "maskeregen", "雨翅蛾", "비나방", "amemoth", "アメモース"], ["shroomish", "balignon", "knilz", "蘑蘑菇", "버섯꼬", "kinococo", "キノココ"], ["breloom", "chapignon", "kapilz", "斗笠菇", "버섯모", "kinogassa", "キノガッサ"], ["slakoth", "parecool", "bummelz", "懶人獺", "게을로", "namakero", "ナマケロ"], ["vigoroth", "vigoroth", "muntier", "過動猿", "발바로", "yarukimono", "ヤルキモノ"], ["slaking", "monaflèmit", "letarking", "請假王", "게을킹", "kekking", "ケッキング"], ["nincada", "ningale", "nincada", "土居忍士", "토중몬", "tutinin", "ツチニン"], ["ninjask", "ninjask", "ninjask", "鐵面忍者", "아이스크", "tekkanin", "テッカニン"], ["shedinja", "munja", "ninjatom", "脫殼忍者", "껍질몬", "nukenin", "ヌケニン"], ["whismur", "chuchmur", "flurmel", "咕妞妞", "소곤룡", "gonyonyo", "ゴニョニョ"], ["loudred", "ramboum", "krakeelo", "吼爆彈", "노공룡", "dogohmb", "ドゴーム"], ["exploud", "brouhabam", "krawumms", "爆音怪", "폭음룡", "bakuong", "バクオング"], ["makuhita", "makuhita", "makuhita", "幕下力士", "마크탕", "makunoshita", "マクノシタ"], ["hariyama", "hariyama", "hariyama", "鐵掌力士", "하리뭉", "hariteyama", "ハリテヤマ"], ["azurill", "azurill", "azurill", "露力麗", "루리리", "ruriri", "ルリリ"], ["nosepass", "tarinor", "nasgnet", "朝北鼻", "코코파스", "nosepass", "ノズパス"], ["skitty", "skitty", "eneco", "向尾喵", "에나비", "eneco", "エネコ"], ["delcatty", "delcatty", "enekoro", "優雅貓", "델케티", "enekororo", "エネコロロ"], ["sableye", "ténéfix", "zobiris", "勾魂眼", "깜까미", "yamirami", "ヤミラミ"], ["mawile", "mysdibule", "flunkifer", "大嘴娃", "입치트", "kucheat", "クチート"], ["aron", "galekid", "stollunior", "可可多拉", "가보리", "cokodora", "ココドラ"], ["lairon", "galegon", "stollrak", "可多拉", "갱도라", "kodora", "コドラ"], ["aggron", "galeking", "stolloss", "波士可多拉", "보스로라", "bossgodora", "ボスゴドラ"], ["meditite", "méditikka", "meditie", "瑪沙那", "요가랑", "asanan", "アサナン"], ["medicham", "charmina", "meditalis", "恰雷姆", "요가램", "charem", "チャーレム"], ["electrike", "dynavolt", "frizelbliz", "落雷獸", "썬더라이", "rakurai", "ラクライ"], ["manectric", "élecsprint", "voltenso", "雷電獸", "썬더볼트", "livolt", "ライボルト"], ["plusle", "posipi", "plusle", "正電拍拍", "플러시", "prasle", "プラスル"], ["minun", "négapi", "minun", "負電拍拍", "마이농", "minun", "マイナン"], ["volbeat", "muciole", "volbeat", "電螢蟲", "볼비트", "barubeat", "バルビート"], ["illumise", "lumivole", "illumise", "甜甜螢", "네오비트", "illumise", "イルミーゼ"], ["roselia", "rosélia", "roselia", "毒薔薇", "로젤리아", "roselia", "ロゼリア"], ["gulpin", "gloupti", "schluppuck", "溶食獸", "꼴깍몬", "gokulin", "ゴクリン"], ["swalot", "avaltout", "schlukwech", "吞食獸", "꿀꺽몬", "marunoom", "マルノーム"], ["carvanha", "carvanha", "kanivanha", "利牙魚", "샤프니아", "kibanha", "キバニア"], ["sharpedo", "sharpedo", "tohaido", "巨牙鯊", "샤크니아", "samehader", "サメハダー"], ["wailmer", "wailmer", "wailmer", "吼吼鯨", "고래왕자", "whalko", "ホエルコ"], ["wailord", "wailord", "wailord", "吼鯨王", "고래왕", "whaloh", "ホエルオー"], ["numel", "chamallot", "camaub", "呆火駝", "둔타", "donmel", "ドンメル"], ["camerupt", "camérupt", "camerupt", "噴火駝", "폭타", "bakuuda", "バクーダ"], ["torkoal", "chartor", "qurtel", "煤炭龜", "코터스", "cotoise", "コータス"], ["spoink", "spoink", "spoink", "跳跳豬", "피그점프", "baneboo", "バネブー"], ["grumpig", "groret", "groink", "噗噗豬", "피그킹", "boopig", "ブーピッグ"], ["spinda", "spinda", "pandir", "晃晃斑", "얼루기", "patcheel", "パッチール"], ["trapinch", "kraknoix", "knacklion", "大顎蟻", "톱치", "nuckrar", "ナックラー"], ["vibrava", "vibraninf", "vibrava", "超音波幼蟲", "비브라바", "vibrava", "ビブラーバ"], ["flygon", "libégon", "libelldra", "沙漠蜻蜓", "플라이곤", "frygon", "フライゴン"], ["cacnea", "cacnea", "tuska", "刺球仙人掌", "선인왕", "sabonea", "サボネア"], ["cacturne", "cacturne", "noktuska", "夢歌仙人掌", "밤선인", "noctus", "ノクタス"], ["swablu", "tylton", "wablu", "青綿鳥", "파비코", "tyltto", "チルット"], ["altaria", "altaria", "altaria", "七夕青鳥", "파비코리", "tyltalis", "チルタリス"], ["zangoose", "mangriff", "sengo", "貓鼬斬", "쟝고", "zangoose", "ザングース"], ["seviper", "séviper", "vipitis", "飯匙蛇", "세비퍼", "habunake", "ハブネーク"], ["lunatone", "séléroc", "lunastein", "月石", "루나톤", "lunatone", "ルナトーン"], ["solrock", "solaroc", "sonnfel", "太陽岩", "솔록", "solrock", "ソルロック"], ["barboach", "barloche", "schmerbe", "泥泥鰍", "미꾸리", "dojoach", "ドジョッチ"], ["whiscash", "barbicha", "welsar", "鯰魚王", "메깅", "namazun", "ナマズン"], ["corphish", "écrapince", "krebscorps", "龍蝦小兵", "가재군", "heigani", "ヘイガニ"], ["crawdaunt", "colhomard", "krebutack", "鐵螯龍蝦", "가재장군", "shizariger", "シザリガー"], ["baltoy", "balbuto", "puppance", "天秤偶", "오뚝군", "yajilon", "ヤジロン"], ["claydol", "kaorine", "lepumentas", "念力土偶", "점토도리", "nendoll", "ネンドール"], ["lileep", "lilia", "liliep", "觸手百合", "릴링", "lilyla", "リリーラ"], ["cradily", "vacilys", "wielie", "搖籃百合", "릴리요", "yuradle", "ユレイドル"], ["anorith", "anorith", "anorith", "太古羽蟲", "아노딥스", "anopth", "アノプス"], ["armaldo", "armaldo", "armaldo", "太古盔甲", "아말도", "armaldo", "アーマルド"], ["feebas", "barpau", "barschwa", "醜醜魚", "빈티나", "hinbass", "ヒンバス"], ["milotic", "milobellus", "milotic", "美納斯", "밀로틱", "milokaross", "ミロカロス"], ["castform", "morphéo", "formeo", "飄浮泡泡", "캐스퐁", "powalen", "ポワルン"], ["kecleon", "kecleon", "kecleon", "變隱龍", "켈리몬", "kakureon", "カクレオン"], ["shuppet", "polichombr", "shuppet", "怨影娃娃", "어둠대신", "kagebouzu", "カゲボウズ"], ["banette", "branette", "banette", "詛咒娃娃", "다크펫", "juppeta", "ジュペッタ"], ["duskull", "skelénox", "zwirrlicht", "夜巡靈", "해골몽", "yomawaru", "ヨマワル"], ["dusclops", "téraclope", "zwirrklop", "彷徨夜靈", "미라몽", "samayouru", "サマヨール"], ["tropius", "tropius", "tropius", "熱帶龍", "트로피우스", "tropius", "トロピウス"], ["chimecho", "éoko", "palimpalim", "風鈴鈴", "치렁", "chirean", "チリーン"], ["absol", "absol", "absol", "阿勃梭魯", "앱솔", "absol", "アブソル"], ["wynaut", "okéoké", "isso", "小果然", "마자", "sohnano", "ソーナノ"], ["snorunt", "stalgamin", "schneppke", "雪童子", "눈꼬마", "yukiwarashi", "ユキワラシ"], ["glalie", "oniglali", "firnontor", "冰鬼護", "얼음귀신", "onigohri", "オニゴーリ"], ["spheal", "obalie", "seemops", "海豹球", "대굴레오", "tamazarashi", "タマザラシ"], ["sealeo", "phogleur", "seejong", "海魔獅", "씨레오", "todoggler", "トドグラー"], ["walrein", "kaimorse", "walraisa", "帝牙海獅", "씨카이저", "todoseruga", "トドゼルガ"], ["clamperl", "coquiperl", "perlu", "珍珠貝", "진주몽", "pearlulu", "パールル"], ["huntail", "serpang", "aalabyss", "獵斑魚", "헌테일", "huntail", "ハンテール"], ["gorebyss", "rosabyss", "saganabyss", "櫻花魚", "분홍장이", "sakurabyss", "サクラビス"], ["relicanth", "relicanth", "relicanth", "古空棘魚", "시라칸", "glanth", "ジーランス"], ["luvdisc", "lovdisc", "liebiskus", "愛心魚", "사랑동이", "lovecus", "ラブカス"], ["bagon", "draby", "kindwurm", "寶貝龍", "아공이", "tatsubay", "タツベイ"], ["shelgon", "drackhaus", "draschel", "甲殼龍", "쉘곤", "komoruu", "コモルー"], ["salamence", "drattak", "brutalanda", "暴飛龍", "보만다", "bohmander", "ボーマンダ"], ["beldum", "terhal", "tanhel", "鐵啞鈴", "메탕", "dumbber", "ダンバル"], ["metang", "métang", "metang", "金屬怪", "메탕구", "metang", "メタング"], ["metagross", "métalosse", "metagross", "巨金怪", "메타그로스", "metagross", "メタグロス"], ["regirock", "regirock", "regirock", "雷吉洛克", "레지락", "regirock", "レジロック"], ["regice", "regice", "regice", "雷吉艾斯", "레지아이스", "regice", "レジアイス"], ["registeel", "registeel", "registeel", "雷吉斯奇魯", "레지스틸", "registeel", "レジスチル"], ["latias", "latias", "latias", "拉帝亞斯", "라티아스", "latias", "ラティアス"], ["latios", "latios", "latios", "拉帝歐斯", "라티오스", "latios", "ラティオス"], ["kyogre", "kyogre", "kyogre", "蓋歐卡", "가이오가", "kyogre", "カイオーガ"], ["groudon", "groudon", "groudon", "固拉多", "그란돈", "groudon", "グラードン"], ["rayquaza", "rayquaza", "rayquaza", "烈空坐", "레쿠쟈", "rayquaza", "レックウザ"], ["jirachi", "jirachi", "jirachi", "基拉祈", "지라치", "jirachi", "ジラーチ"], ["deoxys", "deoxys", "deoxys", "代歐奇希斯", "테오키스", "deoxys", "デオキシス"], ["turtwig", "tortipouss", "chelast", "草苗龜", "모부기", "naetle", "ナエトル"], ["grotle", "boskara", "chelcarain", "樹林龜", "수풀부기", "hayashigame", "ハヤシガメ"], ["torterra", "torterra", "chelterrar", "土台龜", "토대부기", "dodaitose", "ドダイトス"], ["chimchar", "ouisticram", "panflam", "小火焰猴", "불꽃숭이", "hikozaru", "ヒコザル"], ["monferno", "chimpenfeu", "panpyro", "猛火猴", "파이숭이", "mōkazaru", "モウカザル"], ["infernape", "simiabraz", "panferno", "烈焰猴", "초염몽", "gōkazaru", "ゴウカザル"], ["piplup", "tiplouf", "plinfa", "波加曼", "팽도리", "pochama", "ポッチャマ"], ["prinplup", "prinplouf", "pliprin", "波皇子", "팽태자", "pottaishi", "ポッタイシ"], ["empoleon", "pingoléon", "impoleon", "帝王拿波", "엠페르트", "emperte", "エンペルト"], ["starly", "étourmi", "staralili", "姆克兒", "찌르꼬", "mukkuru", "ムックル"], ["staravia", "étourvol", "staravia", "姆克鳥", "찌르버드", "mukubird", "ムクバード"], ["staraptor", "étouraptor", "staraptor", "姆克鷹", "찌르호크", "mukuhawk", "ムクホーク"], ["bidoof", "keunotor", "bidiza", "大牙狸", "비버니", "bipper", "ビッパ"], ["bibarel", "castorno", "bidifas", "大尾狸", "비버통", "beadull", "ビーダル"], ["kricketot", "crikzik", "zirpurze", "圓法師", "귀뚤뚜기", "korobohshi", "コロボーシ"], ["kricketune", "mélokrik", "zirpeise", "音箱蟀", "귀뚤톡크", "korotok", "コロトック"], ["shinx", "lixy", "sheinux", "小貓怪", "꼬링크", "kolink", "コリンク"], ["luxio", "luxio", "luxio", "勒克貓", "럭시오", "luxio", "ルクシオ"], ["luxray", "luxray", "luxtra", "倫琴貓", "렌트라", "rentorar", "レントラー"], ["budew", "rozbouton", "knospi", "含羞苞", "꼬몽울", "subomie", "スボミー"], ["roserade", "roserade", "roserade", "羅絲雷朵", "로즈레이드", "roserade", "ロズレイド"], ["cranidos", "kranidos", "koknodon", "頭蓋龍", "두개도스", "zugaidos", "ズガイドス"], ["rampardos", "charkos", "rameidon", "戰槌龍", "램펄드", "rampard", "ラムパルド"], ["shieldon", "dinoclier", "schilterus", "盾甲龍", "방패톱스", "tatetops", "タテトプス"], ["bastiodon", "bastiodon", "bollterus", "護城龍", "바리톱스", "trideps", "トリデプス"], ["burmy", "cheniti", "burmy", "結草兒", "도롱충이", "minomucchi", "ミノムッチ"], ["wormadam", "cheniselle", "burmadame", "結草貴婦", "도롱마담", "minomadam", "ミノマダム"], ["mothim", "papilord", "moterpel", "紳士蛾", "나메일", "garmeil", "ガーメイル"], ["combee", "apitrini", "wadribie", "三蜜蜂", "세꿀버리", "mitsuhoney", "ミツハニー"], ["vespiquen", "apireine", "honweisel", "蜂女王", "비퀸", "beequeen", "ビークイン"], ["pachirisu", "pachirisu", "pachirisu", "帕奇利茲", "파치리스", "pachirisu", "パチリス"], ["buizel", "mustébouée", "bamelin", "泳圈鼬", "브이젤", "buoysel", "ブイゼル"], ["floatzel", "mustéflott", "bojelin", "浮潛鼬", "플로젤", "flowsel", "フローゼル"], ["cherubi", "ceribou", "kikugi", "櫻花寶", "체리버", "cherinbo", "チェリンボ"], ["cherrim", "ceriflor", "kinoso", "櫻花兒", "체리꼬", "cherrim", "チェリム"], ["shellos", "sancoki", "schalellos", "無殼海兔", "깝질무", "karanakushi", "カラナクシ"], ["gastrodon", "tritosor", "gastrodon", "海兔獸", "트리토돈", "toritodon", "トリトドン"], ["ambipom", "capidextre", "ambidiffel", "雙尾怪手", "겟핸보숭", "eteboth", "エテボース"], ["drifloon", "baudrive", "driftlon", "飄飄球", "흔들풍손", "fuwante", "フワンテ"], ["drifblim", "grodrive", "drifzepeli", "隨風球", "둥실라이드", "fuwaride", "フワライド"], ["buneary", "laporeille", "haspiror", "捲捲耳", "이어롤", "mimirol", "ミミロル"], ["lopunny", "lockpin", "schlapor", "長耳兔", "이어롭", "mimilop", "ミミロップ"], ["mismagius", "magirêve", "traunmagil", "夢妖魔", "무우마직", "mumage", "ムウマージ"], ["honchkrow", "corboss", "kramshef", "烏鴉頭頭", "돈크로우", "donkarasu", "ドンカラス"], ["glameow", "chaglam", "charmian", "魅力喵", "나옹마", "nyarmar", "ニャルマー"], ["purugly", "chaffreux", "shnurgarst", "東施喵", "몬냥이", "bunyat", "ブニャット"], ["chingling", "korillon", "klingplim", "鈴鐺響", "랑딸랑", "lisyan", "リーシャン"], ["stunky", "moufouette", "skunkapuh", "臭鼬噗", "스컹뿡", "skunpoo", "スカンプー"], ["skuntank", "moufflair", "skuntank", "坦克臭鼬", "스컹탱크", "skutank", "スカタンク"], ["bronzor", "archéomire", "bronzel", "銅鏡怪", "동미러", "domirror", "ドーミラー"], ["bronzong", "archéodong", "bronzong", "青銅鐘", "동탁군", "dotakun", "ドータクン"], ["bonsly", "manzaï", "mobai", "盆才怪", "꼬지지", "usohachi", "ウソハチ"], ["mime jr.", "mime jr.", "pantimimi", "魔尼尼", "흉내내", "manene", "マネネ"], ["happiny", "ptiravi", "wonneira", "小福蛋", "핑복", "pinpuku", "ピンプク"], ["chatot", "pijako", "plaudagei", "聒噪鳥", "페라페", "perap", "ペラップ"], ["spiritomb", "spiritomb", "kryppuk", "花岩怪", "화강돌", "mikaruge", "ミカルゲ"], ["gible", "griknot", "kaumalat", "圓陸鯊", "딥상어동", "fukamaru", "フカマル"], ["gabite", "carmache", "knarksel", "尖牙陸鯊", "한바이트", "gabite", "ガバイト"], ["garchomp", "carchacrok", "knakrack", "烈咬陸鯊", "한카리아스", "gablias", "ガブリアス"], ["munchlax", "goinfrex", "mampfaxo", "小卡比獸", "먹고자", "gonbe", "ゴンベ"], ["riolu", "riolu", "riolu", "利歐路", "리오르", "riolu", "リオル"], ["lucario", "lucario", "lucario", "路卡利歐", "루카리오", "lucario", "ルカリオ"], ["hippopotas", "hippopotas", "hippopotas", "沙河馬", "히포포타스", "hipopotas", "ヒポポタス"], ["hippowdon", "hippodocus", "hippoterus", "河馬獸", "하마돈", "kabarudon", "カバルドン"], ["skorupi", "rapion", "pionskora", "鉗尾蠍", "스콜피", "scorpi", "スコルピ"], ["drapion", "drascore", "piondragi", "龍王蠍", "드래피온", "dorapion", "ドラピオン"], ["croagunk", "cradopaud", "glibunkel", "不良蛙", "삐딱구리", "gureggru", "グレッグル"], ["toxicroak", "coatox", "toxiquak", "毒骷蛙", "독개굴", "dokurog", "ドクロッグ"], ["carnivine", "vortente", "venuflibis", "尖牙籠", "무스틈니", "muskippa", "マスキッパ"], ["finneon", "écayon", "finneon", "螢光魚", "형광어", "keikouo", "ケイコウオ"], ["lumineon", "luminéon", "lumineon", "霓虹魚", "네오라이트", "neolant", "ネオラント"], ["mantyke", "babimanta", "mantirps", "小球飛魚", "타만타", "tamanta", "タマンタ"], ["snover", "blizzi", "shnebedeck", "雪笠怪", "눈쓰개", "yukikaburi", "ユキカブリ"], ["abomasnow", "blizzaroi", "rexblisar", "暴雪王", "눈설왕", "yukinooh", "ユキノオー"], ["weavile", "dimoret", "snibunna", "瑪狃拉", "포푸니라", "manyula", "マニューラ"], ["magnezone", "magnézone", "magnezone", "自爆磁怪", "자포코일", "jibacoil", "ジバコイル"], ["lickilicky", "coudlangue", "schlurplek", "大舌舔", "내룸벨트", "beroberto", "ベロベルト"], ["rhyperior", "rhinastoc", "rihornior", "超甲狂犀", "거대코뿌리", "dosydon", "ドサイドン"], ["tangrowth", "bouldeneu", "tangoloss", "巨蔓藤", "덩쿠림보", "mojumbo", "モジャンボ"], ["electivire", "élekable", "elevoltek", "電擊魔獸", "에레키블", "elekible", "エレキブル"], ["magmortar", "maganon", "magbrant", "鴨嘴炎獸", "마그마번", "booburn", "ブーバーン"], ["togekiss", "togekiss", "togekiss", "波克基斯", "토게키스", "togekiss", "トゲキッス"], ["yanmega", "yanmega", "yanmega", "遠古巨蜓", "메가자리", "megayanma", "メガヤンマ"], ["leafeon", "phyllali", "folipurba", "葉伊布", "리피아", "leafia", "リーフィア"], ["glaceon", "givrali", "glaziola", "冰伊布", "글레이시아", "glacia", "グレイシア"], ["gliscor", "scorvol", "skorgro", "天蠍王", "글라이온", "glion", "グライオン"], ["mamoswine", "mammochon", "mamutel", "象牙豬", "맘모꾸리", "mammoo", "マンムー"], ["porygon-z", "porygon-z", "porygon-z", "多邊獸ｚ", "폴리곤z", "porygonz", "ポリゴンｚ"], ["gallade", "gallame", "galagladi", "艾路雷朵", "엘레이드", "erlade", "エルレイド"], ["probopass", "tarinorme", "voluminas", "大朝北鼻", "대코파스", "dainose", "ダイノーズ"], ["dusknoir", "noctunoir", "zwirrfinst", "黑夜魔靈", "야느와르몽", "yonoir", "ヨノワール"], ["froslass", "momartik", "frosdedje", "雪妖女", "눈여아", "yukimenoko", "ユキメノコ"], ["rotom", "motisma", "rotom", "洛托姆", "로토무", "rotom", "ロトム"], ["uxie", "créhelf", "selfe", "由克希", "유크시", "yuxie", "ユクシー"], ["mesprit", "créfollet", "vesprit", "艾姆利多", "엠라이트", "emrit", "エムリット"], ["azelf", "créfadet", "tobutz", "亞克諾姆", "아그놈", "agnome", "アグノム"], ["dialga", "dialga", "dialga", "帝牙盧卡", "디아루가", "dialga", "ディアルガ"], ["palkia", "palkia", "palkia", "帕路奇亞", "펄기아", "palkia", "パルキア"], ["heatran", "heatran", "heatran", "席多藍恩", "히드런", "heatran", "ヒードラン"], ["regigigas", "regigigas", "regigigas", "雷吉奇卡斯", "레지기가스", "regigigas", "レジギガス"], ["giratina", "giratina", "giratina", "騎拉帝納", "기라티나", "giratina", "ギラティナ"], ["cresselia", "cresselia", "cresselia", "克雷色利亞", "크레세리아", "crecelia", "クレセリア"], ["phione", "phione", "phione", "霏歐納", "피오네", "phione", "フィオネ"], ["manaphy", "manaphy", "manaphy", "瑪納霏", "마나피", "manaphy", "マナフィ"], ["darkrai", "darkrai", "darkrai", "達克萊伊", "다크라이", "darkrai", "ダークライ"], ["shaymin", "shaymin", "shaymin", "謝米", "쉐이미", "shaymin", "シェイミ"], ["arceus", "arceus", "arceus", "阿爾宙斯", "아르세우스", "arceus", "アルセウス"], ["victini", "victini", "victini", "比克提尼", "비크티니", "bikutini", "ビクティニ"], ["snivy", "vipélierre", "serpifeu", "藤藤蛇", "주리비얀", "tsutaaja", "ツタージャ"], ["servine", "lianaja", "efoserp", "青藤蛇", "샤비", "janobii", "ジャノビー"], ["serperior", "majaspic", "serpiroyal", "君主蛇", "샤로다", "jarooda", "ジャローダ"], ["tepig", "gruikui", "floink", "暖暖豬", "뚜꾸리", "pokabu", "ポカブ"], ["pignite", "grotichon", "ferkokel", "炒炒豬", "차오꿀", "chaobuu", "チャオブー"], ["emboar", "roitiflam", "flambirex", "炎武王", "염무왕", "enbuoo", "エンブオー"], ["oshawott", "moustillon", "ottaro", "水水獺", "수댕이", "mijumaru", "ミジュマル"], ["dewott", "mateloutre", "zwottronin", "雙刃丸", "쌍검자비", "futachimaru", "フタチマル"], ["samurott", "clamiral", "admurai", "大劍鬼", "대검귀", "daikenki", "ダイケンキ"], ["patrat", "ratentif", "nagelotz", "探探鼠", "보르쥐", "minezumi", "ミネズミ"], ["watchog", "miradar", "kukmarda", "步哨鼠", "보르그", "miruhoggu", "ミルホッグ"], ["lillipup", "ponchiot", "yorkleff", "小約克", "요테리", "yooterii", "ヨーテリー"], ["herdier", "ponchien", "terribark", "哈約克", "하데리어", "haaderia", "ハーデリア"], ["stoutland", "mastouffe", "bissbark", "長毛狗", "바랜드", "muurando", "ムーランド"], ["purrloin", "chacripan", "felilou", "扒手貓", "쌔비냥", "choroneko", "チョロネコ"], ["liepard", "léopardus", "kleoparda", "酷豹", "레파르다스", "reparudasu", "レパルダス"], ["pansage", "feuillajou", "vegimak", "花椰猴", "야나프", "yanappu", "ヤナップ"], ["simisage", "feuiloutan", "vegichita", "花椰猿", "야나키", "yanakkii", "ヤナッキー"], ["pansear", "flamajou", "grillmak", "爆香猴", "바오프", "baoppu", "バオップ"], ["simisear", "flamoutan", "grillchita", "爆香猿", "바오키", "baokkii", "バオッキー"], ["panpour", "flotajou", "sodamak", "冷水猴", "앗차프", "hiyappu", "ヒヤップ"], ["simipour", "flotoutan", "sodachita", "冷水猿", "앗차키", "hiyakkii", "ヒヤッキー"], ["munna", "munna", "somniam", "食夢夢", "몽나", "munna", "ムンナ"], ["musharna", "mushana", "somnivora", "夢夢蝕", "몽얌나", "mushaana", "ムシャーナ"], ["pidove", "poichigeon", "dusselgurr", "豆豆鴿", "콩둘기", "mamepato", "マメパト"], ["tranquill", "colombeau", "navitaub", "咕咕鴿", "유토브", "hatooboo", "ハトーボー"], ["unfezant", "déflaisan", "fasasnob", "高傲雉雞", "켄호로우", "kenhorou", "ケンホロウ"], ["blitzle", "zébibron", "elezeba", "斑斑馬", "줄뮤마", "shimama", "シママ"], ["zebstrika", "zéblitz", "zebritz", "雷電斑馬", "제브라이카", "zeburaika", "ゼブライカ"], ["roggenrola", "nodulithe", "kiesling", "石丸子", "단굴", "dangoro", "ダンゴロ"], ["boldore", "géolithe", "sedimantur", "地幔岩", "암트르", "gantoru", "ガントル"], ["gigalith", "gigalithe", "brockoloss", "龐岩怪", "기가이어스", "gigaiasu", "ギガイアス"], ["woobat", "chovsourir", "fleknoil", "滾滾蝙蝠", "또르박쥐", "koromori", "コロモリ"], ["swoobat", "rhinolove", "fletiamo", "心蝙蝠", "맘박쥐", "kokoromori", "ココロモリ"], ["drilbur", "rototaupe", "rotomurf", "螺釘地鼠", "두더류", "moguryuu", "モグリュー"], ["excadrill", "minotaupe", "stalobor", "龍頭地鼠", "몰드류", "doryuuzu", "ドリュウズ"], ["audino", "nanméouïe", "ohrdoch", "差不多娃娃", "다부니", "tabunne", "タブンネ"], ["timburr", "charpenti", "praktibalk", "搬運小匠", "으랏차", "dokkoraa", "ドッコラー"], ["gurdurr", "ouvrifier", "strepoli", "鐵骨土人", "토쇠골", "dotekkotsu", "ドテッコツ"], ["conkeldurr", "bétochef", "meistagrif", "修建老匠", "노보청", "roobushin", "ローブシン"], ["tympole", "tritonde", "schallquap", "圓蝌蚪", "동챙이", "otamaro", "オタマロ"], ["palpitoad", "batracné", "mebrana", "藍蟾蜍", "두까비", "gamagaru", "ガマガル"], ["seismitoad", "crapustule", "branawarz", "蟾蜍王", "두빅굴", "gamageroge", "ガマゲロゲ"], ["throh", "judokrak", "jiutesto", "投摔鬼", "던지미", "nageki", "ナゲキ"], ["sawk", "karaclée", "karadonis", "打擊鬼", "타격귀", "dageki", "ダゲキ"], ["sewaddle", "larveyette", "strawickl", "蟲寶包", "두르보", "kurumiru", "クルミル"], ["swadloon", "couverdure", "folikon", "寶包繭", "두르쿤", "kurumayu", "クルマユ"], ["leavanny", "manternel", "matrifol", "保母蟲", "모아머", "hahakomori", "ハハコモリ"], ["venipede", "venipatte", "toxiped", "百足蜈蚣", "마디네", "fushide", "フシデ"], ["whirlipede", "scobolide", "rollum", "車輪毬", "휠구", "hoiiga", "ホイーガ"], ["scolipede", "brutapode", "cerapendra", "蜈蚣王", "펜드라", "pendoraa", "ペンドラー"], ["cottonee", "doudouvet", "waumboll", "木棉球", "소미안", "monmen", "モンメン"], ["whimsicott", "farfaduvet", "elfun", "風妖精", "엘풍", "erufuun", "エルフーン"], ["petilil", "chlorobule", "lilminip", "百合根娃娃", "치릴리", "churine", "チュリネ"], ["lilligant", "fragilady", "dressella", "裙兒小姐", "드레디어", "doredia", "ドレディア"], ["basculin", "bargantua", "barschuft", "野蠻鱸魚", "배쓰나이", "basurao", "バスラオ"], ["sandile", "mascaïman", "ganovil", "黑眼鱷", "깜눈크", "meguroko", "メグロコ"], ["krokorok", "escroco", "rokkaiman", "混混鱷", "악비르", "warubiru", "ワルビル"], ["krookodile", "crocorible", "rabigator", "流氓鱷", "악비아르", "warubiaru", "ワルビアル"], ["darumaka", "darumarond", "flampion", "火紅不倒翁", "달막화", "darumakka", "ダルマッカ"], ["darmanitan", "darumacho", "flampivian", "達摩狒狒", "불비달마", "hihidaruma", "ヒヒダルマ"], ["maractus", "maracachi", "maracamba", "沙鈴仙人掌", "마라카치", "marakacchi", "マラカッチ"], ["dwebble", "crabicoque", "lithomith", "石居蟹", "돌살이", "ishizumai", "イシズマイ"], ["crustle", "crabaraque", "castellith", "岩殿居蟹", "암팰리스", "iwaparesu", "イワパレス"], ["scraggy", "baggiguane", "zurrokex", "滑滑小子", "곤율랭", "zuruggu", "ズルッグ"], ["scrafty", "baggaïd", "irokex", "頭巾混混", "곤율거니", "zuruzukin", "ズルズキン"], ["sigilyph", "cryptéro", "symvolara", "象徵鳥", "심보러", "shinboraa", "シンボラー"], ["yamask", "tutafeh", "makabaja", "哭哭面具", "데스마스", "desumasu", "デスマス"], ["cofagrigus", "tutankafer", "echnatoll", "死神棺", "데스니칸", "desukaan", "デスカーン"], ["tirtouga", "carapagos", "galapaflos", "原蓋海龜", "프로토가", "purotooga", "プロトーガ"], ["carracosta", "mégapagos", "karippas", "肋骨海龜", "늑골라", "abagoora", "アバゴーラ"], ["archen", "arkéapti", "flapteryx", "始祖小鳥", "아켄", "aaken", "アーケン"], ["archeops", "aéroptéryx", "aeropteryx", "始祖大鳥", "아케오스", "aakeosu", "アーケオス"], ["trubbish", "miamiasme", "unratütox", "破破袋", "깨봉이", "yabukuron", "ヤブクロン"], ["garbodor", "miasmax", "deponitox", "灰塵山", "더스트나", "dasutodasu", "ダストダス"], ["zorua", "zorua", "zorua", "索羅亞", "조로아", "zoroa", "ゾロア"], ["zoroark", "zoroark", "zoroark", "索羅亞克", "조로아크", "zoroaaku", "ゾロアーク"], ["minccino", "chinchidou", "picochilla", "泡沫栗鼠", "치라미", "chiraamy", "チラーミィ"], ["cinccino", "pashmilla", "chillabell", "奇諾栗鼠", "치라치노", "chirachiino", "チラチーノ"], ["gothita", "scrutella", "mollimorba", "哥德寶寶", "고디탱", "gochimu", "ゴチム"], ["gothorita", "mesmérella", "hypnomorba", "哥德小童", "고디보미", "gochimiru", "ゴチミル"], ["gothitelle", "sidérella", "morbitesse", "哥德小姐", "고디모아젤", "gochiruzeru", "ゴチルゼル"], ["solosis", "nucléos", "monozyto", "單卵細胞球", "유니란", "yuniran", "ユニラン"], ["duosion", "méios", "mitodos", "雙卵細胞球", "듀란", "daburan", "ダブラン"], ["reuniclus", "symbios", "zytomega", "人造細胞卵", "란쿨루스", "rankurusu", "ランクルス"], ["ducklett", "couaneton", "piccolente", "鴨寶寶", "꼬지보리", "koaruhii", "コアルヒー"], ["swanna", "lakmécygne", "swaroness", "舞天鵝", "스완나", "suwanna", "スワンナ"], ["vanillite", "sorbébé", "gelatini", "迷你冰", "바닐프티", "banipucchi", "バニプッチ"], ["vanillish", "sorboul", "gelatroppo", "多多冰", "바닐리치", "baniricchi", "バニリッチ"], ["vanilluxe", "sorbouboul", "gelatwino", "雙倍多多冰", "배바닐라", "baibanira", "バイバニラ"], ["deerling", "vivaldaim", "sesokitz", "四季鹿", "사철록", "shikijika", "シキジカ"], ["sawsbuck", "haydaim", "kronjuwild", "萌芽鹿", "바라철록", "mebukijika", "メブキジカ"], ["emolga", "emolga", "emolga", "電飛鼠", "에몽가", "emonga", "エモンガ"], ["karrablast", "carabing", "laukaps", "蓋蓋蟲", "딱정곤", "kaburumo", "カブルモ"], ["escavalier", "lançargot", "cavalanzas", "騎士蝸牛", "슈바르고", "shubarugo", "シュバルゴ"], ["foongus", "trompignon", "tarnpignon", "哎呀球菇", "깜놀버슬", "tamagetake", "タマゲタケ"], ["amoonguss", "gaulet", "hutsassa", "敗露球菇", "뽀록나", "morobareru", "モロバレル"], ["frillish", "viskuse", "quabbel", "輕飄飄", "탱그릴", "pururiru", "プルリル"], ["jellicent", "moyade", "apoquallyp", "胖嘟嘟", "탱탱겔", "burungeru", "ブルンゲル"], ["alomomola", "mamanbo", "mamolida", "保母曼波", "맘복치", "mamanbou", "ママンボウ"], ["joltik", "statitik", "wattzapf", "電電蟲", "파쪼옥", "bachuru", "バチュル"], ["galvantula", "mygavolt", "voltula", "電蜘蛛", "전툴라", "denchura", "デンチュラ"], ["ferroseed", "grindur", "kastadur", "種子鐵球", "철시드", "tesshiido", "テッシード"], ["ferrothorn", "noacier", "tentantel", "堅果啞鈴", "너트령", "nattorei", "ナットレイ"], ["klink", "tic", "klikk", "齒輪兒", "기어르", "giaru", "ギアル"], ["klang", "clic", "kliklak", "齒輪組", "기기어르", "gigiaru", "ギギアル"], ["klinklang", "cliticlic", "klikdiklak", "齒輪怪", "기기기어르", "gigigiaru", "ギギギアル"], ["tynamo", "anchwatt", "zapplardin", "麻麻小魚", "저리어", "shibishirasu", "シビシラス"], ["eelektrik", "lampéroie", "zapplalek", "麻麻鰻", "저리릴", "shibibiiru", "シビビール"], ["eelektross", "ohmassacre", "zapplarang", "麻麻鰻魚王", "저리더프", "shibirudon", "シビルドン"], ["elgyem", "lewsor", "pygraulon", "小灰怪", "리그레", "riguree", "リグレー"], ["beheeyem", "neitram", "megalon", "大宇怪", "벰크", "oobemu", "オーベム"], ["litwick", "funécire", "lichtel", "燭光靈", "불켜미", "hitomoshi", "ヒトモシ"], ["lampent", "mélancolux", "laternecto", "燈火幽靈", "램프라", "ranpuraa", "ランプラー"], ["chandelure", "lugulabre", "skelabra", "水晶燈火靈", "샹델라", "shandera", "シャンデラ"], ["axew", "coupenotte", "milza", "牙牙", "터검니", "kibago", "キバゴ"], ["fraxure", "incisache", "sharfax", "斧牙龍", "액슨도", "onondo", "オノンド"], ["haxorus", "tranchodon", "maxax", "雙斧戰龍", "액스라이즈", "ononokusu", "オノノクス"], ["cubchoo", "polarhume", "petznief", "噴嚏熊", "코고미", "kumashun", "クマシュン"], ["beartic", "polagriffe", "siberio", "凍原熊", "툰베어", "tsunbeaa", "ツンベアー"], ["cryogonal", "hexagel", "frigometri", "幾何雪花", "프리지오", "furiijio", "フリージオ"], ["shelmet", "escargaume", "schnuthelm", "小嘴蝸", "쪼마리", "chobomaki", "チョボマキ"], ["accelgor", "limaspeed", "hydragil", "敏捷蟲", "어지리더", "agirudaa", "アギルダー"], ["stunfisk", "limonde", "flunschlik", "泥巴魚", "메더", "maggyo", "マッギョ"], ["mienfoo", "kungfouine", "lin-fu", "功夫鼬", "비조푸", "kojofuu", "コジョフー"], ["mienshao", "shaofouine", "wie-shu", "師父鼬", "비조도", "kojondo", "コジョンド"], ["druddigon", "drakkarmin", "shardrago", "赤面龍", "크리만", "kurimugan", "クリムガン"], ["golett", "gringolem", "golbit", "泥偶小人", "골비람", "gobitto", "ゴビット"], ["golurk", "golemastoc", "golgantes", "泥偶巨人", "골루그", "goruugu", "ゴルーグ"], ["pawniard", "scalpion", "gladiantri", "駒刀小兵", "자망칼", "komatana", "コマタナ"], ["bisharp", "scalproie", "caesurio", "劈斬司令", "절각참", "kirikizan", "キリキザン"], ["bouffalant", "frison", "bisofank", "爆炸頭水牛", "버프론", "baffuron", "バッフロン"], ["rufflet", "furaiglon", "geronimatz", "毛頭小鷹", "수리둥보", "washibon", "ワシボン"], ["braviary", "gueriaigle", "washakwil", "勇士雄鷹", "워글", "wooguru", "ウォーグル"], ["vullaby", "vostourno", "skallyk", "禿鷹丫頭", "벌차이", "baruchai", "バルチャイ"], ["mandibuzz", "vaututrice", "grypheldis", "禿鷹娜", "버랜지나", "barujiina", "バルジーナ"], ["heatmor", "aflamanoir", "furnifraß", "熔蟻獸", "앤티골", "kuitaran", "クイタラン"], ["durant", "fermite", "fermicula", "鐵蟻", "아이앤트", "aianto", "アイアント"], ["deino", "solochi", "kapuno", "單首龍", "모노두", "monozu", "モノズ"], ["zweilous", "diamat", "duodino", "雙首暴龍", "디헤드", "jiheddo", "ジヘッド"], ["hydreigon", "trioxhydre", "trikephalo", "三首惡龍", "삼삼드래", "sazandora", "サザンドラ"], ["larvesta", "pyronille", "ignivor", "燃燒蟲", "활화르바", "meraruba", "メラルバ"], ["volcarona", "pyrax", "ramoth", "火神蛾", "불카모스", "urugamosu", "ウルガモス"], ["cobalion", "cobaltium", "kobalium", "勾帕路翁", "코바르온", "kobaruon", "コバルオン"], ["terrakion", "terrakium", "terrakium", "代拉基翁", "테라키온", "terakion", "テラキオン"], ["virizion", "viridium", "viridium", "畢力吉翁", "비리디온", "birijion", "ビリジオン"], ["tornadus", "boréas", "boreos", "龍捲雲", "토네로스", "torunerosu", "トルネロス"], ["thundurus", "fulguris", "voltolos", "雷電雲", "볼트로스", "borutorosu", "ボルトロス"], ["reshiram", "reshiram", "reshiram", "萊希拉姆", "레시라무", "reshiramu", "レシラム"], ["zekrom", "zekrom", "zekrom", "捷克羅姆", "제크로무", "zekuromu", "ゼクロム"], ["landorus", "démétéros", "demeteros", "土地雲", "랜드로스", "randorosu", "ランドロス"], ["kyurem", "kyurem", "kyurem", "酋雷姆", "큐레무", "kyuremu", "キュレム"], ["keldeo", "keldeo", "keldeo", "凱路迪歐", "케르디오", "kerudio", "ケルディオ"], ["meloetta", "meloetta", "meloetta", "美洛耶塔", "메로엣타", "meroetta", "メロエッタ"], ["genesect", "genesect", "genesect", "蓋諾賽克特", "게노세크트", "genosekuto", "ゲノセクト"], ["chespin", "marisson", "igamaro", "哈力栗", "도치마론", "harimaron", "ハリマロン"], ["quilladin", "boguérisse", "igastarnish", "胖胖哈力", "도치보구", "hariboogu", "ハリボーグ"], ["chesnaught", "blindépique", "brigaron", "布里卡隆", "브리가론", "burigaron", "ブリガロン"], ["fennekin", "feunnec", "fynx", "火狐狸", "푸호꼬", "fokko", "フォッコ"], ["braixen", "roussil", "rutena", "長尾火狐", "테르나", "teerunaa", "テールナー"], ["delphox", "goupelin", "fennexis", "妖火紅狐", "마폭시", "mafokushii", "マフォクシー"], ["froakie", "grenousse", "froxy", "呱呱泡蛙", "개구마르", "keromatsu", "ケロマツ"], ["frogadier", "croâporal", "amphizel", "呱頭蛙", "개굴반장", "gekogashira", "ゲコガシラ"], ["greninja", "amphinobi", "quajutsu", "甲賀忍蛙", "개굴닌자", "gekkouga", "ゲッコウガ"], ["bunnelby", "sapereau", "scoppel", "掘掘兔", "파르빗", "horubii", "ホルビー"], ["diggersby", "excavarenne", "grebbit", "掘地兔", "파르토", "horuudo", "ホルード"], ["fletchling", "passerouge", "dartiri", "小箭雀", "화살꼬빈", "yayakoma", "ヤヤコマ"], ["fletchinder", "braisillon", "dartignis", "火箭雀", "불화살빈", "hinoyakoma", "ヒノヤコマ"], ["talonflame", "flambusard", "fiaro", "烈箭鷹", "파이어로", "faiaroo", "ファイアロー"], ["scatterbug", "lépidonille", "purmel", "粉蝶蟲", "분이벌레", "kofukimushi", "コフキムシ"], ["spewpa", "pérégrain", "puponcho", "粉蝶蛹", "분떠도리", "kofuurai", "コフーライ"], ["vivillon", "prismillon", "vivillon", "彩粉蝶", "비비용", "bibiyon", "ビビヨン"], ["litleo", "hélionceau", "leufeo", "小獅獅", "레오꼬", "shishiko", "シシコ"], ["pyroar", "némélios", "pyroleo", "火炎獅", "화염레오", "kaenjishi", "カエンジシ"], ["flabébé", "flabébé", "flabébé", "花蓓蓓", "플라베베", "furabebe", "フラベベ"], ["floette", "floette", "floette", "花葉蒂", "플라엣테", "furaette", "フラエッテ"], ["florges", "florges", "florges", "花潔夫人", "플라제스", "furaajesu", "フラージェス"], ["skiddo", "cabriolaine", "mähikel", "坐騎小羊", "메이클", "meeekuru", "メェークル"], ["gogoat", "chevroum", "chevrumm", "坐騎山羊", "고고트", "googooto", "ゴーゴート"], ["pancham", "pandespiègle", "pam-pam", "頑皮熊貓", "판짱", "yanchamu", "ヤンチャム"], ["pangoro", "pandarbare", "pandagro", "流氓熊貓", "부란다", "goronda", "ゴロンダ"], ["furfrou", "couafarel", "coiffwaff", "多麗米亞", "트리미앙", "torimian", "トリミアン"], ["espurr", "psystigri", "psiau", "妙喵", "냐스퍼", "nyasupaa", "ニャスパー"], ["meowstic", "mistigrix", "psiaugon", "超能妙喵", "냐오닉스", "nyaonikusu", "ニャオニクス"], ["honedge", "monorpale", "gramokles", "獨劍鞘", "단칼빙", "hitotsuki", "ヒトツキ"], ["doublade", "dimoclès", "duokles", "雙劍鞘", "쌍검킬", "nidangiru", "ニダンギル"], ["aegislash", "exagide", "durengard", "堅盾劍怪", "킬가르도", "girugarudo", "ギルガルド"], ["spritzee", "fluvetin", "parfi", "粉香香", "슈쁘", "shushupu", "シュシュプ"], ["aromatisse", "cocotine", "parfinesse", "芳香精", "프레프티르", "furefuwan", "フレフワン"], ["swirlix", "sucroquin", "flauschling", "綿綿泡芙", "나룸퍼프", "peroppafu", "ペロッパフ"], ["slurpuff", "cupcanaille", "sabbaione", "胖甜妮", "나루림", "peroriimu", "ペロリーム"], ["inkay", "sepiatop", "iscalar", "好啦魷", "오케이징", "maaiika", "マーイーカ"], ["malamar", "sepiatroce", "calamanero", "烏賊王", "칼라마네로", "karamanero", "カラマネロ"], ["binacle", "opermine", "bithora", "龜腳腳", "거북손손", "kametete", "カメテテ"], ["barbaracle", "golgopathe", "thanathora", "龜足巨鎧", "거북손데스", "gamenodesu", "ガメノデス"], ["skrelp", "venalgue", "algitt", "垃垃藻", "수레기", "kuzumoo", "クズモー"], ["dragalge", "kravarech", "tandrak", "毒藻龍", "드래캄", "doramidoro", "ドラミドロ"], ["clauncher", "flingouste", "scampisto", "鐵臂槍蝦", "완철포", "udeppou", "ウデッポウ"], ["clawitzer", "gamblast", "wummer", "鋼砲臂蝦", "블로스터", "burosutaa", "ブロスター"], ["helioptile", "galvaran", "eguana", "傘電蜥", "목도리키텔", "erikiteru", "エリキテル"], ["heliolisk", "iguolta", "elezard", "光電傘蜥", "일레도리자드", "erezaado", "エレザード"], ["tyrunt", "ptyranidur", "balgoras", "寶寶暴龍", "티고라스", "chigorasu", "チゴラス"], ["tyrantrum", "rexillius", "monargoras", "怪顎龍", "견고라스", "gachigorasu", "ガチゴラス"], ["amaura", "amagara", "amarino", "冰雪龍", "아마루스", "amarusu", "アマルス"], ["aurorus", "dragmara", "amagarga", "冰雪巨龍", "아마루르가", "amaruruga", "アマルルガ"], ["sylveon", "nymphali", "feelinara", "仙子伊布", "님피아", "ninfia", "ニンフィア"], ["hawlucha", "brutalibré", "resladero", "摔角鷹人", "루차불", "ruchaburu", "ルチャブル"], ["dedenne", "dedenne", "dedenne", "咚咚鼠", "데덴네", "dedenne", "デデンネ"], ["carbink", "strassie", "rocara", "小碎鑽", "멜리시", "mereshii", "メレシー"], ["goomy", "mucuscule", "viscora", "黏黏寶", "미끄메라", "numera", "ヌメラ"], ["sliggoo", "colimucus", "viscargot", "黏美兒", "미끄네일", "numeiru", "ヌメイル"], ["goodra", "muplodocus", "viscogon", "黏美龍", "미끄래곤", "numerugon", "ヌメルゴン"], ["klefki", "trousselin", "clavion", "鑰圈兒", "클레피", "kureffi", "クレッフィ"], ["phantump", "brocélôme", "paragoni", "小木靈", "나목령", "bokuree", "ボクレー"], ["trevenant", "desséliande", "trombork", "朽木妖", "대로트", "oorotto", "オーロット"], ["pumpkaboo", "pitrouille", "irrbis", "南瓜精", "호바귀", "bakeccha", "バケッチャ"], ["gourgeist", "banshitrouye", "pumpdjinn", "南瓜怪人", "펌킨인", "panpujin", "パンプジン"], ["bergmite", "grelaçon", "arktip", "冰寶", "꽁어름", "kachikooru", "カチコール"], ["avalugg", "séracrawl", "arktilas", "冰岩怪", "크레베이스", "kurebeesu", "クレベース"], ["noibat", "sonistrelle", "ef-em", "嗡蝠", "음뱃", "onbatto", "オンバット"], ["noivern", "bruyverne", "uhafnir", "音波龍", "음번", "onbaan", "オンバーン"], ["xerneas", "xerneas", "xerneas", "哲爾尼亞斯", "제르네아스", "zeruneasu", "ゼルネアス"], ["yveltal", "yveltal", "yveltal", "伊裴爾塔爾", "이벨타르", "iberutaru", "イベルタル"], ["zygarde", "zygarde", "zygarde", "基格爾德", "지가르데", "jigarude", "ジガルデ"], ["diancie", "diancie", "diancie", "蒂安希", "디안시", "dianshii", "ディアンシー"], ["hoopa", "hoopa", "hoopa", "胡帕", "후파", "fuupa", "フーパ"], ["volcanion", "volcanion", "volcanion", "波爾凱尼恩", "볼케니온", "borukenion", "ボルケニオン"], ["rowlet", "brindibou", "bauz", "木木梟", "나몰빼미", "mokuroo", "モクロー"], ["dartrix", "efflèche", "arboretoss", "投羽梟", "빼미스로우", "fukusuroo", "フクスロー"], ["decidueye", "archéduc", "silvarro", "狙射樹梟", "모크나이퍼", "junaipaa", "ジュナイパー"], ["litten", "flamiaou", "flamiau", "火斑喵", "냐오불", "nyabii", "ニャビー"], ["torracat", "matoufeu", "miezunder", "炎熱喵", "냐오히트", "nyahiito", "ニャヒート"], ["incineroar", "félinferno", "fuegro", "熾焰咆哮虎", "어흥염", "gaogaen", "ガオガエン"], ["popplio", "otaquin", "robball", "球球海獅", "누리공", "ashimari", "アシマリ"], ["brionne", "otarlette", "marikeck", "花漾海獅", "키요공", "oshamari", "オシャマリ"], ["primarina", "oratoria", "primarene", "西獅海壬", "누리레느", "ashireenu", "アシレーヌ"], ["pikipek", "picassaut", "peppeck", "小篤兒", "콕코구리", "tsutsukera", "ツツケラ"], ["trumbeak", "piclairon", "trompeck", "喇叭啄鳥", "크라파", "kerarappa", "ケララッパ"], ["toucannon", "bazoucan", "tukanon", "銃嘴大鳥", "왕큰부리", "dodekabashi", "ドデカバシ"], ["yungoos", "manglouton", "mangunior", "貓鼬少", "영구스", "yanguusu", "ヤングース"], ["gumshoos", "argouste", "manguspektor", "貓鼬探長", "형사구스", "dekaguusu", "デカグース"], ["grubbin", "larvibule", "mabula", "強顎雞母蟲", "턱지충이", "agojimushi", "アゴジムシ"], ["charjabug", "chrysapile", "akkup", "蟲電寶", "전지충이", "denjimushi", "デンヂムシ"], ["vikavolt", "lucanon", "donarion", "鍬農砲蟲", "투구뿌논", "kuwaganon", "クワガノン"], ["crabrawler", "crabagarre", "krabbox", "好勝蟹", "오기지게", "makenkani", "マケンカニ"], ["crabominable", "crabominable", "krawell", "好勝毛蟹", "모단단게", "kekenkani", "ケケンカニ"], ["oricorio", "plumeline", "choreogel", "花舞鳥", "춤추새", "odoridori", "オドリドリ"], ["cutiefly", "bombydou", "wommel", "萌虻", "에블리", "aburii", "アブリー"], ["ribombee", "rubombelle", "bandelby", "蝶結萌虻", "에리본", "aburibon", "アブリボン"], ["rockruff", "rocabot", "wuffels", "岩狗狗", "암멍이", "iwanko", "イワンコ"], ["lycanroc", "lougaroc", "wolwerock", "鬃岩狼人", "루가루암", "rugarugan", "ルガルガン"], ["wishiwashi", "froussardine", "lusardin", "弱丁魚", "약어리", "yowashi", "ヨワシ"], ["mareanie", "vorastérie", "garstella", "好壞星", "시마사리", "hidoide", "ヒドイデ"], ["toxapex", "prédastérie", "aggrostella", "超壞星", "더시마사리", "dohidoide", "ドヒドイデ"], ["mudbray", "tiboudet", "pampuli", "泥驢仔", "머드나기", "dorobanko", "ドロバンコ"], ["mudsdale", "bourrinos", "pampross", "重泥挽馬", "만마드", "banbadoro", "バンバドロ"], ["dewpider", "araqua", "araqua", "滴蛛", "물거미", "shizukumo", "シズクモ"], ["araquanid", "tarenbulle", "aranestro", "滴蛛霸", "깨비물거미", "onishizukumo", "オニシズクモ"], ["fomantis", "mimantis", "imantis", "偽螳草", "짜랑랑", "karikiri", "カリキリ"], ["lurantis", "floramantis", "mantidea", "蘭螳花", "라란티스", "rarantesu", "ラランテス"], ["morelull", "spododo", "bubungus", "睡睡菇", "자마슈", "nemashu", "ネマシュ"], ["shiinotic", "lampignon", "lamellux", "燈罩夜菇", "마셰이드", "masheedo", "マシェード"], ["salandit", "tritox", "molunk", "夜盜火蜥", "야도뇽", "yatoumori", "ヤトウモリ"], ["salazzle", "malamandre", "amfira", "焰后蜥", "염뉴트", "ennyuuto", "エンニュート"], ["stufful", "nounourson", "velursi", "童偶熊", "포곰곰", "nuikoguma", "ヌイコグマ"], ["bewear", "chelours", "kosturso", "穿著熊", "이븐곰", "kiteruguma", "キテルグマ"], ["bounsweet", "croquine", "frubberl", "甜竹竹", "달콤아", "amakaji", "アマカジ"], ["steenee", "candine", "frubaila", "甜舞妮", "달무리나", "amamaiko", "アママイコ"], ["tsareena", "sucreine", "fruyal", "甜冷美后", "달코퀸", "amaajo", "アマージョ"], ["comfey", "guérilande", "curelei", "花療環環", "큐아링", "kyuwawaa", "キュワワー"], ["oranguru", "gouroutan", "kommandutan", "智揮猩", "하랑우탄", "yareyuutan", "ヤレユータン"], ["passimian", "quartermac", "quartermak", "投擲猴", "내던숭이", "nagetsukesaru", "ナゲツケサル"], ["wimpod", "sovkipou", "reißlaus", "膽小蟲", "꼬시레", "kosokumushi", "コソクムシ"], ["golisopod", "sarmuraï", "tectass", "具甲武者", "갑주무사", "gusokumusha", "グソクムシャ"], ["sandygast", "bacabouh", "sankabuh", "沙丘娃", "모래꿍", "sunabaa", "スナバァ"], ["palossand", "trépassable", "colossand", "噬沙堡爺", "모래성이당", "shirodesuna", "シロデスナ"], ["pyukumuku", "concombaffe", "gufa", "拳海參", "해무기", "namakobushi", "ナマコブシ"], ["type: null", "type:0", "typ:null", "屬性：空", "타입:널", "taipu:nuru", "タイプ：ヌル"], ["silvally", "silvallié", "amigento", "銀伴戰獸", "실버디", "shiruvadi", "シルヴァディ"], ["minior", "météno", "meteno", "小隕星", "메테노", "meteno", "メテノ"], ["komala", "dodoala", "koalelu", "樹枕尾熊", "자말라", "nekkoara", "ネッコアラ"], ["turtonator", "boumata", "tortunator", "爆焰龜獸", "폭거북스", "bakugamesu", "バクガメス"], ["togedemaru", "togedemaru", "togedemaru", "托戈德瑪爾", "토게데마루", "togedemaru", "トゲデマル"], ["mimikyu", "mimiqui", "mimigma", "謎擬ｑ", "따라큐", "mimikkyu", "ミミッキュ"], ["bruxish", "denticrisse", "knirfish", "磨牙彩皮魚", "치갈기", "hagigishiri", "ハギギシリ"], ["drampa", "draïeul", "sen-long", "老翁龍", "할비롱", "jijiiron", "ジジーロン"], ["dhelmise", "sinistrail", "moruda", "破破舵輪", "타타륜", "dadarin", "ダダリン"], ["jangmo-o", "bébécaille", "miniras", "心鱗寶", "짜랑꼬", "jarako", "ジャラコ"], ["hakamo-o", "écaïd", "mediras", "鱗甲龍", "짜랑고우", "jarango", "ジャランゴ"], ["kommo-o", "ékaïser", "grandiras", "杖尾鱗甲龍", "짜랑고우거", "jararanga", "ジャラランガ"], ["tapu koko", "tokorico", "kapu-riki", "卡璞・鳴鳴", "카푸꼬꼬꼭", "kapu・kokeko", "カプ・コケコ"], ["tapu lele", "tokopiyon", "kapu-fala", "卡璞・蝶蝶", "카푸나비나", "kapu・tetefu", "カプ・テテフ"], ["tapu bulu", "tokotoro", "kapu-toro", "卡璞・哞哞", "카푸브루루", "kapu・bururu", "カプ・ブルル"], ["tapu fini", "tokopisco", "kapu-kime", "卡璞・鰭鰭", "카푸느지느", "kapu・rehire", "カプ・レヒレ"], ["cosmog", "cosmog", "cosmog", "科斯莫古", "코스모그", "kosumoggu", "コスモッグ"], ["cosmoem", "cosmovum", "cosmovum", "科斯莫姆", "코스모움", "kosumoumu", "コスモウム"], ["solgaleo", "solgaleo", "solgaleo", "索爾迦雷歐", "솔가레오", "sorugareo", "ソルガレオ"], ["lunala", "lunala", "lunala", "露奈雅拉", "루나아라", "runaaara", "ルナアーラ"], ["nihilego", "zéroïd", "anego", "虛吾伊德", "텅비드", "utsuroido", "ウツロイド"], ["buzzwole", "mouscoto", "masskito", "爆肌蚊", "매시붕", "masshibuun", "マッシブーン"], ["pheromosa", "cancrelove", "schabelle", "費洛美螂", "페로코체", "ferooche", "フェローチェ"], ["xurkitree", "câblifère", "voltriant", "電束木", "전수목", "denjumoku", "デンジュモク"], ["celesteela", "bamboiselle", "kaguron", "鐵火輝夜", "철화구야", "tekkaguya", "テッカグヤ"], ["kartana", "katagami", "katagami", "紙御劍", "종이신도", "kamitsurugi", "カミツルギ"], ["guzzlord", "engloutyran", "schlingking", "惡食大王", "악식킹", "akujikingu", "アクジキング"], ["necrozma", "necrozma", "necrozma", "奈克洛茲瑪", "네크로즈마", "nekurozuma", "ネクロズマ"], ["magearna", "magearna", "magearna", "瑪機雅娜", "마기아나", "magiana", "マギアナ"], ["marshadow", "marshadow", "marshadow", "瑪夏多", "마샤도", "maashadoo", "マーシャドー"], ["poipole", "vémini", "venicro", "毒貝比", "베베놈", "bebenomu", "ベベノム"], ["naganadel", "mandrillon", "agoyon", "四顎針龍", "아고용", "aagoyon", "アーゴヨン"], ["stakataka", "ama-ama", "muramura", "壘磊石", "차곡차곡", "tsundetsunde", "ツンデツンデ"], ["blacephalon", "pierroteknik", "kopplosio", "砰頭小丑", "두파팡", "zugadoon", "ズガドーン"], ["zeraora", "zeraora", "zeraora", "捷拉奥拉", "제라오라", "zeraora", "ゼラオラ"], ["meltan", "meltan", "meltan", "美錄坦", "멜탄", "merutan", "メルタン"], ["melmetal", "melmetal", "melmetal", "美錄梅塔", "멜메탈", "merumetaru", "メルメタル"], ["grookey", "ouistempo", "chimpep", "敲音猴", "흥나숭", "sarunori", "サルノリ"], ["thwackey", "badabouin", "chimstix", "啪咚猴", "채키몽", "bachinkii", "バチンキー"], ["rillaboom", "gorythmic", "gortrom", "轟擂金剛猩", "고릴타", "gorirandaa", "ゴリランダー"], ["scorbunny", "flambino", "hopplo", "炎兔兒", "염버니", "hibanii", "ヒバニー"], ["raboot", "lapyro", "kickerlo", "騰蹴小將", "래비풋", "rabifutto", "ラビフット"], ["cinderace", "pyrobut", "liberlo", "閃焰王牌", "에이스번", "eesubaan", "エースバーン"], ["sobble", "larméléon", "memmeon", "淚眼蜥", "울머기", "messon", "メッソン"], ["drizzile", "arrozard", "phlegleon", "變澀蜥", "누겔레온", "jimereon", "ジメレオン"], ["inteleon", "lézargus", "intelleon", "千面避役", "인텔리레온", "intereon", "インテレオン"], ["skwovet", "rongourmand", "raffel", "貪心栗鼠", "탐리스", "hoshigarisu", "ホシガリス"], ["greedent", "rongrigou", "schlaraffel", "藏飽栗鼠", "요씽리스", "yokubarisu", "ヨクバリス"], ["rookidee", "minisange", "meikro", "稚山雀", "파라꼬", "kokogara", "ココガラ"], ["corvisquire", "bleuseille", "kranoviz", "藍鴉", "파크로우","aogarasu", "アオガラス"], ["corviknight", "corvaillus", "krarmor", "鋼鎧鴉", "아머까오", "aamaagaa", "アーマーガア"], ["blipbug", "larvadar", "sensect", "索偵蟲", "두루지벌레", "sacchimushi", "サッチムシ"], ["dottler", "coléodôme", "keradar", "天罩蟲", "레돔벌레", "redoomushi", "レドームシ"], ["orbeetle", "astronelle", "maritellit", "以歐路普", "이올브", "iorubu", "イオルブ"], ["nickit", "goupilou", "kleptifux", "偷兒狐", "훔처우", "kusune", "クスネ"], ["thievul", "roublenard", "gaunux", "狐大盜", "폭슬라이", "fokusurai", "フォクスライ"], ["gossifleur", "tournicoton", "cottini", "幼棉棉", "꼬모카", "himenka", "ヒメンカ"], ["eldegoss", "blancoton", "cottomi", "白蓬蓬", "백솜모카", "watashiraga", "ワタシラガ"], ["wooloo", "moumouton", "wolly", "毛辮羊", "우르", "uuruu", "ウールー"], ["dubwool", "moumouflon", "zwollock", "毛毛角羊", "배우르", "baiuuruu", "バイウールー"], ["chewtle", "khélocrok", "kamehaps", "咬咬龜", "깨물부기", "kamukame", "カムカメ"], ["drednaw", "torgamord", "kamalm", "暴噬龜", "갈가부기", "kajirigame", "カジリガメ"], ["yamper", "voltoutou", "voldi", "來電汪", "멍파치", "wanpachi", "ワンパチ"], ["boltund", "fulgudog", "bellektro", "逐電犬", "펄스멍", "parusuwan", "パルスワン"], ["rolycoly", "charbi", "klonkett", "小炭仔", "탄동", "tandon", "タンドン"], ["carkol", "wagomine", "wagong", "大炭車", "탄차곤", "toroggon", "トロッゴン"], ["coalossal", "monthracite", "montecarbo", "巨炭山", "석탄산", "sekitanzan", "セキタンザン"], ["applin", "verpom", "knapfel", "啃果蟲", "과사삭벌레", "kajicchu", "カジッチュ"], ["flapple", "pomdrapi", "drapfel", "蘋裹龍", "애프룡", "appuryuu", "アップリュー"], ["appletun", "dratatin", "schlapfel", "豐蜜龍", "단지래플", "taruppuru", "タルップル"], ["silicobra", "dunaja", "salanga", "沙包蛇", "모래뱀", "sunahebi", "スナヘビ"], ["sandaconda", "dunaconda", "sanaconda", "沙螺蟒", "사다이사", "sadaija", "サダイジャ"], ["cramorant", "nigosier", "urgl", "古月鳥", "윽우지", "u'u", "ウッウ"], ["arrokuda", "embrochet", "pikuda", "刺梭魚", "찌로꼬치", "sashikamasu", "サシカマス"], ["barraskewda", "hastacuda", "barrakiefa", "戽斗尖梭", "꼬치조", "kamasujoo", "カマスジョー"], ["toxel", "toxizap", "toxel", "毒電嬰", "일레즌", "erezun", "エレズン"], ["toxtricity", "salarsen", "riffex", "顫弦蠑螈", "스트린더", "sutorindaa", "ストリンダー"], ["sizzlipede", "grillepattes", "thermopod", "燒火蚣", "태우지네", "yakude", "ヤクデ"], ["centiskorch", "scolocendre", "infernopod", "焚焰蚣", "다태우지네", "maruyakude", "マルヤクデ"], ["clobbopus", "poulpaf", "klopptopus", "拳拳蛸", "때때무노", "tatakko", "タタッコ"], ["grapploct", "krakos", "kaocto", "八爪武師", "케오퍼스", "otosupasu", "オトスパス"], ["sinistea", "théffroi", "fatalitee", "來悲茶", "데인차", "yabacha", "ヤバチャ"], ["polteageist", "polthégeist", "mortipot", "怖思壺", "포트데스", "pottodesu", "ポットデス"], ["hatenna", "bibichut", "brimova", "迷布莉姆", "몸지브림", "miburimu", "ミブリム"], ["hattrem", "chapotus", "brimano", "提布莉姆", "손지브림", "teburimu", "テブリム"], ["hatterene", "sorcilence", "silembrim", "布莉姆溫", "브리무음", "burimuon", "ブリムオン"], ["impidimp", "grimalin", "bähmon", "搗蛋小妖", "메롱꿍", "berobaa", "ベロバー"], ["morgrem", "fourbelin", "pelzebub", "詐唬魔", "쏘겨모", "gimoo", "ギモー"], ["grimmsnarl", "angoliath", "olangaar", "長毛巨魔", "오롱털", "ooronge", "オーロンゲ"], ["obstagoon", "ixon", "barrikadax", "堵攔熊", "가로막구리", "tachifusaguma", "タチフサグマ"], ["perrserker", "berserkatt", "mauzinger", "喵頭目", "나이킹", "nyaikingu", "ニャイキング"], ["cursola", "corayôme", "gorgasonn", "魔靈珊瑚", "산호르곤", "sanigoon", "サニゴーン"], ["sirfetch’d", "palarticho", "lauchzelot", "蔥遊兵", "창파나이트", "negiganaito", "ネギガナイト"], ["mr. rime", "m. glaquette", "pantifrost", "踏冰人偶", "마임꽁꽁", "barikooru", "バリコオル"], ["runerigus", "tutétékri", "oghnatoll", "死神板", "데스판", "desubaan", "デスバーン"], ["milcery", "crèmy", "hokumil", "小仙奶", "마빌크", "mahomiru", "マホミル"], ["alcremie", "charmilly", "pokusan", "霜奶仙", "마휘핑", "mahoippu", "マホイップ"], ["falinks", "hexadron", "legios", "列陣兵", "대여르", "taireetsu", "タイレーツ"], ["pincurchin", "wattapik", "britzigel", "啪嚓海膽", "찌르성게", "bachin'uni", "バチンウニ"], ["snom", "frissonille", "snomnom", "雪吞蟲", "누니머기", "yukihami", "ユキハミ"], ["frosmoth", "beldeneige", "mottineva", "雪絨蛾", "모스노우", "mosunou", "モスノウ"], ["stonjourner", "dolman", "humanolith", "巨石丁", "돌헨진", "ishihenjin", "イシヘンジン"], ["eiscue", "bekaglaçon", "kubuin", "冰砌鵝", "빙큐보", "koorippo", "コオリッポ"], ["indeedee", "wimessir", "servol", "愛管侍", "에써르", "iessan", "イエッサン"], ["morpeko", "morpeko", "morpeko", "莫魯貝可", "모르페코", "morupeko", "モルペコ"], ["cufant", "charibari", "kupfanti", "銅象", "끼리동", "zoudou", "ゾウドウ"], ["copperajah", "pachyradjah", "patinaraja", "大王銅象", "대왕끼리동", "daioudou", "ダイオウドウ"], ["dracozolt", "galvagon", "lectragon", "雷鳥龍", "파치래곤", "pacchiragon", "パッチラゴン"], ["arctozolt", "galvagla", "lecryodon", "雷鳥海獸", "파치르돈", "pacchirudon", "パッチルドン"], ["dracovish", "hydragon", "pescragon", "鰓魚龍", "어래곤", "uonoragon", "ウオノラゴン"], ["arctovish", "hydragla", "pescryodon", "鰓魚海獸", "어치르돈", "uochirudon", "ウオチルドン"], ["duraludon", "duralugon", "duraludon", "鋁鋼龍", "두랄루돈", "jurarudon", "ジュラルドン"], ["dreepy", "fantyrm", "grolldra", "多龍梅西亞", "드라꼰", "dorameshiya", "ドラメシヤ"], ["drakloak", "dispareptil", "phandra", "多龍奇", "드래런치", "doronchi", "ドロンチ"], ["dragapult", "lanssorien", "katapuldra", "多龍巴魯托", "드래펄트", "doraparuto", "ドラパルト"], ["zacian", "zacian", "zacian", "蒼響", "자시안", "zashian", "ザシアン"], ["zamazenta", "zamazenta", "zamazenta", "藏瑪然特", "자마젠타", "zamazenta", "ザマゼンタ"], ["eternatus", "éthernatos", "endynalos", "無極汰那", "무한다이노", "mugendaina", "ムゲンダイナ"], ["kubfu", "wushours", "dakuma", "熊徒弟", "치고마", "dakuma", "ダクマ"], ["urshifu", "shifours", "wulaosu", "武道熊師", "우라오스", "uuraosu", "ウーラオス"], ["zarude", "zarude", "zarude", "薩戮德", "자루도", "zaruudo", "ザルード"], ["regieleki", "regieleki", "regieleki", "雷吉艾勒奇", "레지에레키", "rejiereki", "レジエレキ"], ["regidrago", "regidrago", "regidrago", "雷吉鐸拉戈", "레지드래고", "rejidorago", "レジドラゴ"], ["glastrier", "blizzeval", "blizzeval", "雪暴馬", "블리자포스", "burizaposu", "ブリザポス"], ["spectrier", "spectreval", "spectreval", "靈幽馬", "레이스포스", "reisuposu", "レイスポス"], ["calyrex", "sylveroy", "sylveroy", "蕾冠王", "버드렉스", "badorekkusu", "バドレックス"]]

type_chart = array([[1,1,1,1,1,0.5,1,0,0.5,1,1,1,1,1,1,1,1,1],[2,1,0.5,0.5,1,2,0.5,0,1,1,1,1,1,0.5,2,1,2,0.5],[1,2,1,1,1,0.5,2,1,0.5,1,1,2,0.5,1,1,1,1,1],[1,1,1,0.5,0.5,0.5,1,0.5,0,1,1,2,1,1,1,1,1,2],[1,1,0,2,1,2,0.5,1,2,2,1,0.5,2,1,1,1,1,1],[1,0.5,2,1,0.5,1,2,1,0.5,2,1,1,1,1,2,1,1,1],[1,0.5,0.5,0.5,1,1,1,0.5,0.5,0.5,1,2,1,2,1,1,2,0.5],[0,1,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,1],[1,1,1,1,1,2,1,1,0.5,0.5,0.5,1,0.5,1,2,1,1,2],[1,1,1,1,1,0.5,2,1,2,0.5,0.5,2,1,1,2,0.5,1,1],[1,1,1,1,2,2,1,1,1,2,0.5,0.5,1,1,1,0.5,1,1],[1,1,0.5,0.5,2,2,0.5,1,0.5,0.5,2,0.5,1,1,1,0.5,1,1],[1,1,2,1,0,1,1,1,1,1,2,0.5,0.5,1,1,0.5,1,1],[1,2,1,2,1,1,1,1,0.5,1,1,1,1,0.5,1,1,0,1],[1,1,2,1,2,1,1,1,0.5,0.5,0.5,2,1,1,0.5,2,1,1],[1,1,1,1,1,1,1,1,0.5,1,1,1,1,1,1,2,1,0],[1,0.5,1,1,1,1,1,2,1,1,1,1,1,2,1,1,0.5,0.5],[1,2,1,0.5,1,1,1,1,0.5,0.5,1,1,1,1,1,2,2,1]])

types_name = [["Normal", "Normal", "Normal", "一般", "노말", "Nōmaru", "ノーマル"], ["Fighting", "Combat", "Kampf", "格斗", "격투", "Kakutō", "かくとう"], ["Flying", "Vol", "Flug", "飞行", "비행", "Hikou", "ひこう"], ["Poison", "Poison", "Gift", "毒", "독", "Doku", "どく"], ["Ground", "Sol", "Boden", "地面", "땅", "Ji men", "じめん"], ["Rock", "Roche", "Gestein", "岩石", "바위", "Iwa", "いわ"], ["Bug", "Insecte", "Käfer", "虫", "벌레", "Mushi", "むし"], ["Ghost", "Spectre", "Geist", "幽灵", "고스트", "Gōsuto", "ゴースト"], ["Steel", "Acier", "Stahl", "钢", "강철", "Hagane", "はがね"], ["Fire", "Feu", "Feuer", "火", "불꽃", "Ho no o", "ほのお"], ["Water", "Eau", "Wasser", "水", "물", "Mizu", "みず"], ["Grass", "Plante", "Pflanze", "草", "풀", "Kusa", "くさ"], ["Electric", "Électrik", "Elektro", "电", "전기", "Den ki", "でんき"], ["Psychic", "Psy", "Psycho", "超能力", "에스퍼", "Esupā", "エスパー"], ["Ice", "Glace", "Eis", "冰", "얼음", "Kōri", "こおり"], ["Dragon", "Dragon", "Drache", "龙", "드래곤", "Doragon", "ドラゴン"], ["Dark", "Ténèbres", "Unlicht", "恶", "악", "Aku", "あく"], ["Fairy", "Fée", "Fee", "妖精", "페어리", "Fearī", "フェアリー"]]

types = [[11, 3], [11, 3], [11, 3], [9], [9], [9, 2], [10], [10], [10], [6], [6], [6, 2], [6, 3], [6, 3], [6, 3], [0, 2], [0, 2], [0, 2], [0], [0], [0, 2], [0, 2], [3], [3], [12], [12], [4], [4], [3], [3], [3, 4], [3], [3], [3, 4], [17], [17], [9], [9], [0, 17], [0, 17], [3, 2], [3, 2], [11, 3], [11, 3], [11, 3], [6, 11], [6, 11], [6, 3], [6, 3], [4], [4], [0], [0], [10], [10], [1], [1], [9], [9], [10], [10], [10, 1], [13], [13], [13], [1], [1], [1], [11, 3], [11, 3], [11, 3], [10, 3], [10, 3], [5, 4], [5, 4], [5, 4], [9], [9], [10, 13], [10, 13], [12, 8], [12, 8], [0, 2], [0, 2], [0, 2], [10], [10, 14], [3], [3], [10], [10, 14], [7, 3], [7, 3], [7, 3], [5, 4], [13], [13], [10], [10], [12], [12], [11, 13], [11, 13], [4], [4], [1], [1], [0], [3], [3], [4, 5], [4, 5], [0], [11], [0], [10], [10], [10], [10], [10], [10, 13], [13, 17], [6, 2], [14, 13], [12], [9], [6], [0], [10], [10, 2], [10, 14], [0], [0], [10], [12], [9], [0], [5, 10], [5, 10], [5, 10], [5, 10], [5, 2], [0], [14, 2], [12, 2], [9, 2], [15], [15], [15, 2], [13], [13], [11], [11], [11], [9], [9], [9], [10], [10], [10], [0], [0], [0, 2], [0, 2], [6, 2], [6, 2], [6, 3], [6, 3], [3, 2], [10, 12], [10, 12], [12], [17], [0, 17], [17], [17, 2], [13, 2], [13, 2], [12], [12], [12], [11], [10, 17], [10, 17], [5], [10], [11, 2], [11, 2], [11, 2], [0], [11], [11], [6, 2], [10, 4], [10, 4], [13], [16], [16, 2], [10, 13], [7], [13], [13], [0, 13], [6], [6, 8], [0], [4, 2], [8, 4], [17], [17], [10, 3], [6, 8], [6, 5], [6, 1], [16, 14], [0], [0], [9], [9, 5], [14, 4], [14, 4], [10, 5], [10], [10], [14, 2], [10, 2], [8, 2], [16, 9], [16, 9], [10, 15], [4], [4], [0], [0], [0], [1], [1], [14, 13], [12], [9], [0], [0], [12], [9], [10], [5, 4], [5, 4], [5, 16], [13, 2], [9, 2], [13, 11], [11], [11], [11], [9], [9, 1], [9, 1], [10], [10, 4], [10, 4], [16], [16], [0], [0], [6], [6], [6, 2], [6], [6, 3], [10, 11], [10, 11], [10, 11], [11], [11, 16], [11, 16], [0, 2], [0, 2], [10, 2], [10, 2], [13, 17], [13, 17], [13, 17], [6, 10], [6, 2], [11], [11, 1], [0], [0], [0], [6, 4], [6, 2], [6, 7], [0], [0], [0], [1], [1], [0, 17], [5], [0], [0], [16, 7], [8, 17], [8, 5], [8, 5], [8, 5], [1, 13], [1, 13], [12], [12], [12], [12], [6], [6], [11, 3], [3], [3], [10, 16], [10, 16], [10], [10], [9, 4], [9, 4], [9], [13], [13], [0], [4], [4, 15], [4, 15], [11], [11, 16], [0, 2], [15, 2], [0], [3], [5, 13], [5, 13], [10, 4], [10, 4], [10], [10, 16], [4, 13], [4, 13], [5, 11], [5, 11], [5, 6], [5, 6], [10], [10], [0], [0], [7], [7], [7], [7], [11, 2], [13], [16], [13], [14], [14], [14, 10], [14, 10], [14, 10], [10], [10], [10], [10, 5], [10], [15], [15], [15, 2], [8, 13], [8, 13], [8, 13], [5], [14], [8], [15, 13], [15, 13], [10], [4], [15, 2], [8, 13], [13], [11], [11], [11, 4], [9], [9, 1], [9, 1], [10], [10], [10, 8], [0, 2], [0, 2], [0, 2], [0], [0, 10], [6], [6], [12], [12], [12], [11, 3], [11, 3], [5], [5], [5, 8], [5, 8], [6], [6, 11], [6, 2], [6, 2], [6, 2], [12], [10], [10], [11], [11], [10], [10, 4], [0], [7, 2], [7, 2], [0], [0], [7], [16, 2], [0], [0], [13], [3, 16], [3, 16], [8, 13], [8, 13], [5], [13, 17], [0], [0, 2], [7, 16], [15, 4], [15, 4], [15, 4], [0], [1], [1, 8], [4], [4], [3, 6], [3, 16], [3, 1], [3, 1], [11], [10], [10], [10, 2], [11, 14], [11, 14], [16, 14], [12, 8], [0], [4, 5], [11], [12], [9], [17, 2], [6, 2], [11], [14], [4, 2], [14, 4], [0], [13, 1], [5, 8], [7], [14, 7], [12, 7], [13], [13], [13], [8, 15], [10, 15], [9, 8], [0], [7, 15], [13], [10], [10], [16], [11], [0], [13, 9], [11], [11], [11], [9], [9, 1], [9, 1], [10], [10], [10], [0], [0], [0], [0], [0], [16], [16], [11], [11], [9], [9], [10], [10], [13], [13], [0, 2], [0, 2], [0, 2], [12], [12], [5], [5], [5], [13, 2], [13, 2], [4], [4, 8], [0], [1], [1], [1], [10], [10, 4], [10, 4], [1], [1], [6, 11], [6, 11], [6, 11], [6, 3], [6, 3], [6, 3], [11, 17], [11, 17], [11], [11], [10], [4, 16], [4, 16], [4, 16], [9], [9], [11], [6, 5], [6, 5], [16, 1], [16, 1], [13, 2], [7], [7], [10, 5], [10, 5], [5, 2], [5, 2], [3], [3], [16], [16], [0], [0], [13], [13], [13], [13], [13], [13], [10, 2], [10, 2], [14], [14], [14], [0, 11], [0, 11], [12, 2], [6], [6, 8], [11, 3], [11, 3], [10, 7], [10, 7], [10], [6, 12], [6, 12], [11, 8], [11, 8], [8], [8], [8], [12], [12], [12], [13], [13], [7, 9], [7, 9], [7, 9], [15], [15], [15], [14], [14], [14], [6], [6], [4, 12], [1], [1], [15], [4, 7], [4, 7], [16, 8], [16, 8], [0], [0, 2], [0, 2], [16, 2], [16, 2], [9], [6, 8], [16, 15], [16, 15], [16, 15], [6, 9], [6, 9], [8, 1], [5, 1], [11, 1], [2], [12, 2], [15, 9], [15, 12], [4, 2], [15, 14], [10, 1], [0, 13], [6, 8], [11], [11], [11, 1], [9], [9], [9, 13], [10], [10], [10, 16], [0], [0, 4], [0, 2], [9, 2], [9, 2], [6], [6], [6, 2], [9, 0], [9, 0], [17], [17], [17], [11], [11], [1], [1, 16], [0], [13], [13], [8, 7], [8, 7], [8, 7], [17], [17], [17], [17], [16, 13], [16, 13], [5, 10], [5, 10], [3, 10], [3, 15], [10], [10], [12, 0], [12, 0], [5, 15], [5, 15], [5, 14], [5, 14], [17], [1, 2], [12, 17], [5, 17], [15], [15], [15], [8, 17], [7, 11], [7, 11], [7, 11], [7, 11], [14], [14], [2, 15], [2, 15], [17], [16, 2], [15, 4], [5, 17], [13, 7], [9, 10], [11, 2], [11, 2], [11, 7], [9], [9], [9, 16], [10], [10], [10, 17], [0, 2], [0, 2], [0, 2], [0], [0], [6], [6, 12], [6, 12], [1], [1, 14], [9, 2], [6, 17], [6, 17], [5], [5], [10], [3, 10], [3, 10], [4], [4], [10, 6], [10, 6], [11], [11], [11, 17], [11, 17], [3, 9], [3, 9], [0, 1], [0, 1], [11], [11], [11], [17], [0, 13], [1], [6, 10], [6, 10], [7, 4], [7, 4], [10], [0], [0], [5, 2], [0], [9, 15], [12, 8], [7, 17], [10, 13], [0, 15], [7, 11], [15], [15, 1], [15, 1], [12, 17], [13, 17], [11, 17], [10, 17], [13], [13], [13, 8], [13, 7], [5, 3], [6, 1], [6, 1], [12], [8, 2], [11, 8], [16, 15], [13], [8, 17], [1, 7], [3], [3, 15], [5, 8], [9, 7], [12], [8], [8], [11], [11], [11], [9], [9], [9], [10], [10], [10], [0], [0], [2], [2], [2, 8], [6], [6, 13], [6, 13], [16], [16], [11], [11], [0], [0], [10], [10, 5], [12], [12], [5], [5, 9], [5, 9], [11, 15], [11, 15], [11, 15], [4], [4], [2, 10], [10], [10], [12, 3], [12, 3], [9, 6], [9, 6], [1], [1], [7], [7], [13], [13], [13, 17], [16, 17], [16, 17], [16, 17], [16, 0], [8], [7], [1], [14, 13], [4, 7], [17], [17], [1], [12], [14, 6], [14, 6], [5], [14], [13, 0], [12, 16], [8], [8], [12, 15], [12, 14], [10, 15], [10, 14], [8, 15], [15, 7], [15, 7], [15, 7], [17], [1], [3, 15], [1], [1, 16], [16, 11], [12], [15], [14], [7], [13, 11]]

base_stats = [[45, 49, 49, 65, 65, 45], [60, 62, 63, 80, 80, 60], [80, 82, 83, 100, 100, 80], [39, 52, 43, 60, 50, 65], [58, 64, 58, 80, 65, 80], [78, 84, 78, 109, 85, 100], [44, 48, 65, 50, 64, 43], [59, 63, 80, 65, 80, 58], [79, 83, 100, 85, 105, 78], [45, 30, 35, 20, 20, 45], [50, 20, 55, 25, 25, 30], [60, 45, 50, 90, 80, 70], [40, 35, 30, 20, 20, 50], [45, 25, 50, 25, 25, 35], [65, 90, 40, 45, 80, 75], [40, 45, 40, 35, 35, 56], [63, 60, 55, 50, 50, 71], [83, 80, 75, 70, 70, 101], [30, 56, 35, 25, 35, 72], [55, 81, 60, 50, 70, 97], [40, 60, 30, 31, 31, 70], [65, 90, 65, 61, 61, 100], [35, 60, 44, 40, 54, 55], [60, 95, 69, 65, 79, 80], [35, 55, 40, 50, 50, 90], [60, 90, 55, 90, 80, 110], [50, 75, 85, 20, 30, 40], [75, 100, 110, 45, 55, 65], [55, 47, 52, 40, 40, 41], [70, 62, 67, 55, 55, 56], [90, 92, 87, 75, 85, 76], [46, 57, 40, 40, 40, 50], [61, 72, 57, 55, 55, 65], [81, 102, 77, 85, 75, 85], [70, 45, 48, 60, 65, 35], [95, 70, 73, 95, 90, 60], [38, 41, 40, 50, 65, 65], [73, 76, 75, 81, 100, 100], [115, 45, 20, 45, 25, 20], [140, 70, 45, 85, 50, 45], [40, 45, 35, 30, 40, 55], [75, 80, 70, 65, 75, 90], [45, 50, 55, 75, 65, 30], [60, 65, 70, 85, 75, 40], [75, 80, 85, 110, 90, 50], [35, 70, 55, 45, 55, 25], [60, 95, 80, 60, 80, 30], [60, 55, 50, 40, 55, 45], [70, 65, 60, 90, 75, 90], [10, 55, 25, 35, 45, 95], [35, 100, 50, 50, 70, 120], [40, 45, 35, 40, 40, 90], [65, 70, 60, 65, 65, 115], [50, 52, 48, 65, 50, 55], [80, 82, 78, 95, 80, 85], [40, 80, 35, 35, 45, 70], [65, 105, 60, 60, 70, 95], [55, 70, 45, 70, 50, 60], [90, 110, 80, 100, 80, 95], [40, 50, 40, 40, 40, 90], [65, 65, 65, 50, 50, 90], [90, 95, 95, 70, 90, 70], [25, 20, 15, 105, 55, 90], [40, 35, 30, 120, 70, 105], [55, 50, 45, 135, 95, 120], [70, 80, 50, 35, 35, 35], [80, 100, 70, 50, 60, 45], [90, 130, 80, 65, 85, 55], [50, 75, 35, 70, 30, 40], [65, 90, 50, 85, 45, 55], [80, 105, 65, 100, 70, 70], [40, 40, 35, 50, 100, 70], [80, 70, 65, 80, 120, 100], [40, 80, 100, 30, 30, 20], [55, 95, 115, 45, 45, 35], [80, 120, 130, 55, 65, 45], [50, 85, 55, 65, 65, 90], [65, 100, 70, 80, 80, 105], [90, 65, 65, 40, 40, 15], [95, 75, 110, 100, 80, 30], [25, 35, 70, 95, 55, 45], [50, 60, 95, 120, 70, 70], [52, 90, 55, 58, 62, 60], [35, 85, 45, 35, 35, 75], [60, 110, 70, 60, 60, 110], [65, 45, 55, 45, 70, 45], [90, 70, 80, 70, 95, 70], [80, 80, 50, 40, 50, 25], [105, 105, 75, 65, 100, 50], [30, 65, 100, 45, 25, 40], [50, 95, 180, 85, 45, 70], [30, 35, 30, 100, 35, 80], [45, 50, 45, 115, 55, 95], [60, 65, 60, 130, 75, 110], [35, 45, 160, 30, 45, 70], [60, 48, 45, 43, 90, 42], [85, 73, 70, 73, 115, 67], [30, 105, 90, 25, 25, 50], [55, 130, 115, 50, 50, 75], [40, 30, 50, 55, 55, 100], [60, 50, 70, 80, 80, 150], [60, 40, 80, 60, 45, 40], [95, 95, 85, 125, 75, 55], [50, 50, 95, 40, 50, 35], [60, 80, 110, 50, 80, 45], [50, 120, 53, 35, 110, 87], [50, 105, 79, 35, 110, 76], [90, 55, 75, 60, 75, 30], [40, 65, 95, 60, 45, 35], [65, 90, 120, 85, 70, 60], [80, 85, 95, 30, 30, 25], [105, 130, 120, 45, 45, 40], [250, 5, 5, 35, 105, 50], [65, 55, 115, 100, 40, 60], [105, 95, 80, 40, 80, 90], [30, 40, 70, 70, 25, 60], [55, 65, 95, 95, 45, 85], [45, 67, 60, 35, 50, 63], [80, 92, 65, 65, 80, 68], [30, 45, 55, 70, 55, 85], [60, 75, 85, 100, 85, 115], [40, 45, 65, 100, 120, 90], [70, 110, 80, 55, 80, 105], [65, 50, 35, 115, 95, 95], [65, 83, 57, 95, 85, 105], [65, 95, 57, 100, 85, 93], [65, 125, 100, 55, 70, 85], [75, 100, 95, 40, 70, 110], [20, 10, 55, 15, 20, 80], [95, 125, 79, 60, 100, 81], [130, 85, 80, 85, 95, 60], [48, 48, 48, 48, 48, 48], [55, 55, 50, 45, 65, 55], [130, 65, 60, 110, 95, 65], [65, 65, 60, 110, 95, 130], [65, 130, 60, 95, 110, 65], [65, 60, 70, 85, 75, 40], [35, 40, 100, 90, 55, 35], [70, 60, 125, 115, 70, 55], [30, 80, 90, 55, 45, 55], [60, 115, 105, 65, 70, 80], [80, 105, 65, 60, 75, 130], [160, 110, 65, 65, 110, 30], [90, 85, 100, 95, 125, 85], [90, 90, 85, 125, 90, 100], [90, 100, 90, 125, 85, 90], [41, 64, 45, 50, 50, 50], [61, 84, 65, 70, 70, 70], [91, 134, 95, 100, 100, 80], [106, 110, 90, 154, 90, 130], [100, 100, 100, 100, 100, 100], [45, 49, 65, 49, 65, 45], [60, 62, 80, 63, 80, 60], [80, 82, 100, 83, 100, 80], [39, 52, 43, 60, 50, 65], [58, 64, 58, 80, 65, 80], [78, 84, 78, 109, 85, 100], [50, 65, 64, 44, 48, 43], [65, 80, 80, 59, 63, 58], [85, 105, 100, 79, 83, 78], [35, 46, 34, 35, 45, 20], [85, 76, 64, 45, 55, 90], [60, 30, 30, 36, 56, 50], [100, 50, 50, 86, 96, 70], [40, 20, 30, 40, 80, 55], [55, 35, 50, 55, 110, 85], [40, 60, 40, 40, 40, 30], [70, 90, 70, 60, 70, 40], [85, 90, 80, 70, 80, 130], [75, 38, 38, 56, 56, 67], [125, 58, 58, 76, 76, 67], [20, 40, 15, 35, 35, 60], [50, 25, 28, 45, 55, 15], [90, 30, 15, 40, 20, 15], [35, 20, 65, 40, 65, 20], [55, 40, 85, 80, 105, 40], [40, 50, 45, 70, 45, 70], [65, 75, 70, 95, 70, 95], [55, 40, 40, 65, 45, 35], [70, 55, 55, 80, 60, 45], [90, 75, 85, 115, 90, 55], [75, 80, 95, 90, 100, 50], [70, 20, 50, 20, 50, 40], [100, 50, 80, 60, 80, 50], [70, 100, 115, 30, 65, 30], [90, 75, 75, 90, 100, 70], [35, 35, 40, 35, 55, 50], [55, 45, 50, 45, 65, 80], [75, 55, 70, 55, 95, 110], [55, 70, 55, 40, 55, 85], [30, 30, 30, 30, 30, 30], [75, 75, 55, 105, 85, 30], [65, 65, 45, 75, 45, 95], [55, 45, 45, 25, 25, 15], [95, 85, 85, 65, 65, 35], [65, 65, 60, 130, 95, 110], [95, 65, 110, 60, 130, 65], [60, 85, 42, 85, 42, 91], [95, 75, 80, 100, 110, 30], [60, 60, 60, 85, 85, 85], [48, 72, 48, 72, 48, 48], [190, 33, 58, 33, 58, 33], [70, 80, 65, 90, 65, 85], [50, 65, 90, 35, 35, 15], [75, 90, 140, 60, 60, 40], [100, 70, 70, 65, 65, 45], [65, 75, 105, 35, 65, 85], [75, 85, 200, 55, 65, 30], [60, 80, 50, 40, 40, 30], [90, 120, 75, 60, 60, 45], [65, 95, 85, 55, 55, 85], [70, 130, 100, 55, 80, 65], [20, 10, 230, 10, 230, 5], [80, 125, 75, 40, 95, 85], [55, 95, 55, 35, 75, 115], [60, 80, 50, 50, 50, 40], [90, 130, 75, 75, 75, 55], [40, 40, 40, 70, 40, 20], [60, 50, 120, 90, 80, 30], [50, 50, 40, 30, 30, 50], [100, 100, 80, 60, 60, 50], [65, 55, 95, 65, 95, 35], [35, 65, 35, 65, 35, 65], [75, 105, 75, 105, 75, 45], [45, 55, 45, 65, 45, 75], [85, 40, 70, 80, 140, 70], [65, 80, 140, 40, 70, 70], [45, 60, 30, 80, 50, 65], [75, 90, 50, 110, 80, 95], [75, 95, 95, 95, 95, 85], [90, 60, 60, 40, 40, 40], [90, 120, 120, 60, 60, 50], [85, 80, 90, 105, 95, 60], [73, 95, 62, 85, 65, 85], [55, 20, 35, 20, 45, 75], [35, 35, 35, 35, 35, 35], [50, 95, 95, 35, 110, 70], [45, 30, 15, 85, 65, 65], [45, 63, 37, 65, 55, 95], [45, 75, 37, 70, 55, 83], [95, 80, 105, 40, 70, 100], [255, 10, 10, 75, 135, 55], [90, 85, 75, 115, 100, 115], [115, 115, 85, 90, 75, 100], [100, 75, 115, 90, 115, 85], [50, 64, 50, 45, 50, 41], [70, 84, 70, 65, 70, 51], [100, 134, 110, 95, 100, 61], [106, 90, 130, 90, 154, 110], [106, 130, 90, 110, 154, 90], [100, 100, 100, 100, 100, 100], [40, 45, 35, 65, 55, 70], [50, 65, 45, 85, 65, 95], [70, 85, 65, 105, 85, 120], [45, 60, 40, 70, 50, 45], [60, 85, 60, 85, 60, 55], [80, 120, 70, 110, 70, 80], [50, 70, 50, 50, 50, 40], [70, 85, 70, 60, 70, 50], [100, 110, 90, 85, 90, 60], [35, 55, 35, 30, 30, 35], [70, 90, 70, 60, 60, 70], [38, 30, 41, 30, 41, 60], [78, 70, 61, 50, 61, 100], [45, 45, 35, 20, 30, 20], [50, 35, 55, 25, 25, 15], [60, 70, 50, 100, 50, 65], [50, 35, 55, 25, 25, 15], [60, 50, 70, 50, 90, 65], [40, 30, 30, 40, 50, 30], [60, 50, 50, 60, 70, 50], [80, 70, 70, 90, 100, 70], [40, 40, 50, 30, 30, 30], [70, 70, 40, 60, 40, 60], [90, 100, 60, 90, 60, 80], [40, 55, 30, 30, 30, 85], [60, 85, 60, 75, 50, 125], [40, 30, 30, 55, 30, 85], [60, 50, 100, 95, 70, 65], [28, 25, 25, 45, 35, 40], [38, 35, 35, 65, 55, 50], [68, 65, 65, 125, 115, 80], [40, 30, 32, 50, 52, 65], [70, 60, 62, 100, 82, 80], [60, 40, 60, 40, 60, 35], [60, 130, 80, 60, 60, 70], [60, 60, 60, 35, 35, 30], [80, 80, 80, 55, 55, 90], [150, 160, 100, 95, 65, 100], [31, 45, 90, 30, 30, 40], [61, 90, 45, 50, 50, 160], [1, 90, 45, 30, 30, 40], [64, 51, 23, 51, 23, 28], [84, 71, 43, 71, 43, 48], [104, 91, 63, 91, 73, 68], [72, 60, 30, 20, 30, 25], [144, 120, 60, 40, 60, 50], [50, 20, 40, 20, 40, 20], [30, 45, 135, 45, 90, 30], [50, 45, 45, 35, 35, 50], [70, 65, 65, 55, 55, 90], [50, 75, 75, 65, 65, 50], [50, 85, 85, 55, 55, 50], [50, 70, 100, 40, 40, 30], [60, 90, 140, 50, 50, 40], [70, 110, 180, 60, 60, 50], [30, 40, 55, 40, 55, 60], [60, 60, 75, 60, 75, 80], [40, 45, 40, 65, 40, 65], [70, 75, 60, 105, 60, 105], [60, 50, 40, 85, 75, 95], [60, 40, 50, 75, 85, 95], [65, 73, 75, 47, 85, 85], [65, 47, 75, 73, 85, 85], [50, 60, 45, 100, 80, 65], [70, 43, 53, 43, 53, 40], [100, 73, 83, 73, 83, 55], [45, 90, 20, 65, 20, 65], [70, 120, 40, 95, 40, 95], [130, 70, 35, 70, 35, 60], [170, 90, 45, 90, 45, 60], [60, 60, 40, 65, 45, 35], [70, 100, 70, 105, 75, 40], [70, 85, 140, 85, 70, 20], [60, 25, 35, 70, 80, 60], [80, 45, 65, 90, 110, 80], [60, 60, 60, 60, 60, 60], [45, 100, 45, 45, 45, 10], [50, 70, 50, 50, 50, 70], [80, 100, 80, 80, 80, 100], [50, 85, 40, 85, 40, 35], [70, 115, 60, 115, 60, 55], [45, 40, 60, 40, 75, 50], [75, 70, 90, 70, 105, 80], [73, 115, 60, 60, 60, 90], [73, 100, 60, 100, 60, 65], [90, 55, 65, 95, 85, 70], [90, 95, 85, 55, 65, 70], [50, 48, 43, 46, 41, 60], [110, 78, 73, 76, 71, 60], [43, 80, 65, 50, 35, 35], [63, 120, 85, 90, 55, 55], [40, 40, 55, 40, 70, 55], [60, 70, 105, 70, 120, 75], [66, 41, 77, 61, 87, 23], [86, 81, 97, 81, 107, 43], [45, 95, 50, 40, 50, 75], [75, 125, 100, 70, 80, 45], [20, 15, 20, 10, 55, 80], [95, 60, 79, 100, 125, 81], [70, 70, 70, 70, 70, 70], [60, 90, 70, 60, 120, 40], [44, 75, 35, 63, 33, 45], [64, 115, 65, 83, 63, 65], [20, 40, 90, 30, 90, 25], [40, 70, 130, 60, 130, 25], [99, 68, 83, 72, 87, 51], [75, 50, 80, 95, 90, 65], [65, 130, 60, 75, 60, 75], [95, 23, 48, 23, 48, 23], [50, 50, 50, 50, 50, 50], [80, 80, 80, 80, 80, 80], [70, 40, 50, 55, 50, 25], [90, 60, 70, 75, 70, 45], [110, 80, 90, 95, 90, 65], [35, 64, 85, 74, 55, 32], [55, 104, 105, 94, 75, 52], [55, 84, 105, 114, 75, 52], [100, 90, 130, 45, 65, 55], [43, 30, 55, 40, 65, 97], [45, 75, 60, 40, 30, 50], [65, 95, 100, 60, 50, 50], [95, 135, 80, 110, 80, 100], [40, 55, 80, 35, 60, 30], [60, 75, 100, 55, 80, 50], [80, 135, 130, 95, 90, 70], [80, 100, 200, 50, 100, 50], [80, 50, 100, 100, 200, 50], [80, 75, 150, 75, 150, 50], [80, 80, 90, 110, 130, 110], [80, 90, 80, 130, 110, 110], [100, 100, 90, 150, 140, 90], [100, 150, 140, 100, 90, 90], [105, 150, 90, 150, 90, 95], [100, 100, 100, 100, 100, 100], [50, 150, 50, 150, 50, 150], [55, 68, 64, 45, 55, 31], [75, 89, 85, 55, 65, 36], [95, 109, 105, 75, 85, 56], [44, 58, 44, 58, 44, 61], [64, 78, 52, 78, 52, 81], [76, 104, 71, 104, 71, 108], [53, 51, 53, 61, 56, 40], [64, 66, 68, 81, 76, 50], [84, 86, 88, 111, 101, 60], [40, 55, 30, 30, 30, 60], [55, 75, 50, 40, 40, 80], [85, 120, 70, 50, 60, 100], [59, 45, 40, 35, 40, 31], [79, 85, 60, 55, 60, 71], [37, 25, 41, 25, 41, 25], [77, 85, 51, 55, 51, 65], [45, 65, 34, 40, 34, 45], [60, 85, 49, 60, 49, 60], [80, 120, 79, 95, 79, 70], [40, 30, 35, 50, 70, 55], [60, 70, 65, 125, 105, 90], [67, 125, 40, 30, 30, 58], [97, 165, 60, 65, 50, 58], [30, 42, 118, 42, 88, 30], [60, 52, 168, 47, 138, 30], [40, 29, 45, 29, 45, 36], [60, 59, 85, 79, 105, 36], [70, 94, 50, 94, 50, 66], [30, 30, 42, 30, 42, 70], [70, 80, 102, 80, 102, 40], [60, 45, 70, 45, 90, 95], [55, 65, 35, 60, 30, 85], [85, 105, 55, 85, 50, 115], [45, 35, 45, 62, 53, 35], [70, 60, 70, 87, 78, 85], [76, 48, 48, 57, 62, 34], [111, 83, 68, 92, 82, 39], [75, 100, 66, 60, 66, 115], [90, 50, 34, 60, 44, 70], [150, 80, 44, 90, 54, 80], [55, 66, 44, 44, 56, 85], [65, 76, 84, 54, 96, 105], [60, 60, 60, 105, 105, 105], [100, 125, 52, 105, 52, 71], [49, 55, 42, 42, 37, 85], [71, 82, 64, 64, 59, 112], [45, 30, 50, 65, 50, 45], [63, 63, 47, 41, 41, 74], [103, 93, 67, 71, 61, 84], [57, 24, 86, 24, 86, 23], [67, 89, 116, 79, 116, 33], [50, 80, 95, 10, 45, 10], [20, 25, 45, 70, 90, 60], [100, 5, 5, 15, 65, 30], [76, 65, 45, 92, 42, 91], [50, 92, 108, 92, 108, 35], [58, 70, 45, 40, 45, 42], [68, 90, 65, 50, 55, 82], [108, 130, 95, 80, 85, 102], [135, 85, 40, 40, 85, 5], [40, 70, 40, 35, 40, 60], [70, 110, 70, 115, 70, 90], [68, 72, 78, 38, 42, 32], [108, 112, 118, 68, 72, 47], [40, 50, 90, 30, 55, 65], [70, 90, 110, 60, 75, 95], [48, 61, 40, 61, 40, 50], [83, 106, 65, 86, 65, 85], [74, 100, 72, 90, 72, 46], [49, 49, 56, 49, 61, 66], [69, 69, 76, 69, 86, 91], [45, 20, 50, 60, 120, 50], [60, 62, 50, 62, 60, 40], [90, 92, 75, 92, 85, 60], [70, 120, 65, 45, 85, 125], [70, 70, 115, 130, 90, 60], [110, 85, 95, 80, 95, 50], [115, 140, 130, 55, 55, 40], [100, 100, 125, 110, 50, 50], [75, 123, 67, 95, 85, 95], [75, 95, 67, 125, 95, 83], [85, 50, 95, 120, 115, 80], [86, 76, 86, 116, 56, 95], [65, 110, 130, 60, 65, 95], [65, 60, 110, 130, 95, 65], [75, 95, 125, 45, 75, 95], [110, 130, 80, 70, 60, 80], [85, 80, 70, 135, 75, 90], [68, 125, 65, 65, 115, 80], [60, 55, 145, 75, 150, 40], [45, 100, 135, 65, 135, 45], [70, 80, 70, 80, 70, 110], [50, 50, 77, 95, 77, 91], [75, 75, 130, 75, 130, 95], [80, 105, 105, 105, 105, 80], [75, 125, 70, 125, 70, 115], [100, 120, 120, 150, 100, 90], [90, 120, 100, 150, 120, 100], [91, 90, 106, 130, 106, 77], [110, 160, 110, 80, 110, 100], [150, 100, 120, 100, 120, 90], [120, 70, 120, 75, 130, 85], [80, 80, 80, 80, 80, 80], [100, 100, 100, 100, 100, 100], [70, 90, 90, 135, 90, 125], [100, 100, 100, 100, 100, 100], [120, 120, 120, 120, 120, 120], [100, 100, 100, 100, 100, 100], [45, 45, 55, 45, 55, 63], [60, 60, 75, 60, 75, 83], [75, 75, 95, 75, 95, 113], [65, 63, 45, 45, 45, 45], [90, 93, 55, 70, 55, 55], [110, 123, 65, 100, 65, 65], [55, 55, 45, 63, 45, 45], [75, 75, 60, 83, 60, 60], [95, 100, 85, 108, 70, 70], [45, 55, 39, 35, 39, 42], [60, 85, 69, 60, 69, 77], [45, 60, 45, 25, 45, 55], [65, 80, 65, 35, 65, 60], [85, 110, 90, 45, 90, 80], [41, 50, 37, 50, 37, 66], [64, 88, 50, 88, 50, 106], [50, 53, 48, 53, 48, 64], [75, 98, 63, 98, 63, 101], [50, 53, 48, 53, 48, 64], [75, 98, 63, 98, 63, 101], [50, 53, 48, 53, 48, 64], [75, 98, 63, 98, 63, 101], [76, 25, 45, 67, 55, 24], [116, 55, 85, 107, 95, 29], [50, 55, 50, 36, 30, 43], [62, 77, 62, 50, 42, 65], [80, 115, 80, 65, 55, 93], [45, 60, 32, 50, 32, 76], [75, 100, 63, 80, 63, 116], [55, 75, 85, 25, 25, 15], [70, 105, 105, 50, 40, 20], [85, 135, 130, 60, 80, 25], [65, 45, 43, 55, 43, 72], [67, 57, 55, 77, 55, 114], [60, 85, 40, 30, 45, 68], [110, 135, 60, 50, 65, 88], [103, 60, 86, 60, 86, 50], [75, 80, 55, 25, 35, 35], [85, 105, 85, 40, 50, 40], [105, 140, 95, 55, 65, 45], [50, 50, 40, 50, 40, 64], [75, 65, 55, 65, 55, 69], [105, 95, 75, 85, 75, 74], [120, 100, 85, 30, 85, 45], [75, 125, 75, 30, 75, 85], [45, 53, 70, 40, 60, 42], [55, 63, 90, 50, 80, 42], [75, 103, 80, 70, 80, 92], [30, 45, 59, 30, 39, 57], [40, 55, 99, 40, 79, 47], [60, 100, 89, 55, 69, 112], [40, 27, 60, 37, 50, 66], [60, 67, 85, 77, 75, 116], [45, 35, 50, 70, 50, 30], [70, 60, 75, 110, 75, 90], [70, 92, 65, 80, 55, 98], [50, 72, 35, 35, 35, 65], [60, 82, 45, 45, 45, 74], [95, 117, 80, 65, 70, 92], [70, 90, 45, 15, 45, 50], [105, 140, 55, 30, 55, 95], [75, 86, 67, 106, 67, 60], [50, 65, 85, 35, 35, 55], [70, 105, 125, 65, 75, 45], [50, 75, 70, 35, 70, 48], [65, 90, 115, 45, 115, 58], [72, 58, 80, 103, 80, 97], [38, 30, 85, 55, 65, 30], [58, 50, 145, 95, 105, 30], [54, 78, 103, 53, 45, 22], [74, 108, 133, 83, 65, 32], [55, 112, 45, 74, 45, 70], [75, 140, 65, 112, 65, 110], [50, 50, 62, 40, 62, 65], [80, 95, 82, 60, 82, 75], [40, 65, 40, 80, 40, 65], [60, 105, 60, 120, 60, 105], [55, 50, 40, 40, 40, 75], [75, 95, 60, 65, 60, 115], [45, 30, 50, 55, 65, 45], [60, 45, 70, 75, 85, 55], [70, 55, 95, 95, 110, 65], [45, 30, 40, 105, 50, 20], [65, 40, 50, 125, 60, 30], [110, 65, 75, 125, 85, 30], [62, 44, 50, 44, 50, 55], [75, 87, 63, 87, 63, 98], [36, 50, 50, 65, 60, 44], [51, 65, 65, 80, 75, 59], [71, 95, 85, 110, 95, 79], [60, 60, 50, 40, 50, 75], [80, 100, 70, 60, 70, 95], [55, 75, 60, 75, 60, 103], [50, 75, 45, 40, 45, 60], [70, 135, 105, 60, 105, 20], [69, 55, 45, 55, 55, 15], [114, 85, 70, 85, 80, 30], [55, 40, 50, 65, 85, 40], [100, 60, 70, 85, 105, 60], [165, 75, 80, 40, 45, 65], [50, 47, 50, 57, 50, 65], [70, 77, 60, 97, 60, 108], [44, 50, 91, 24, 86, 10], [74, 94, 131, 54, 116, 20], [40, 55, 70, 45, 60, 30], [60, 80, 95, 70, 85, 50], [60, 100, 115, 70, 85, 90], [35, 55, 40, 45, 40, 60], [65, 85, 70, 75, 70, 40], [85, 115, 80, 105, 80, 50], [55, 55, 55, 85, 55, 30], [75, 75, 75, 125, 95, 40], [50, 30, 55, 65, 55, 20], [60, 40, 60, 95, 60, 55], [60, 55, 90, 145, 90, 80], [46, 87, 60, 30, 40, 57], [66, 117, 70, 40, 50, 67], [76, 147, 90, 60, 70, 97], [55, 70, 40, 60, 40, 40], [95, 130, 80, 70, 80, 50], [80, 50, 50, 95, 135, 105], [50, 40, 85, 40, 65, 25], [80, 70, 40, 100, 60, 145], [109, 66, 84, 81, 99, 32], [45, 85, 50, 55, 50, 65], [65, 125, 60, 95, 60, 105], [77, 120, 90, 60, 90, 48], [59, 74, 50, 35, 50, 35], [89, 124, 80, 55, 80, 55], [45, 85, 70, 40, 40, 60], [65, 125, 100, 60, 70, 70], [95, 110, 95, 40, 95, 55], [70, 83, 50, 37, 50, 60], [100, 123, 75, 57, 75, 80], [70, 55, 75, 45, 65, 60], [110, 65, 105, 55, 95, 80], [85, 97, 66, 105, 66, 65], [58, 109, 112, 48, 48, 109], [52, 65, 50, 45, 50, 38], [72, 85, 70, 65, 70, 58], [92, 105, 90, 125, 90, 98], [55, 85, 55, 50, 55, 60], [85, 60, 65, 135, 105, 100], [91, 90, 129, 90, 72, 108], [91, 129, 90, 72, 90, 108], [91, 90, 72, 90, 129, 108], [79, 115, 70, 125, 80, 111], [79, 115, 70, 125, 80, 111], [100, 120, 100, 150, 120, 90], [100, 150, 120, 120, 100, 90], [89, 125, 90, 115, 80, 101], [125, 130, 90, 130, 90, 95], [91, 72, 90, 129, 90, 108], [100, 77, 77, 128, 128, 90], [71, 120, 95, 120, 95, 99], [56, 61, 65, 48, 45, 38], [61, 78, 95, 56, 58, 57], [88, 107, 122, 74, 75, 64], [40, 45, 40, 62, 60, 60], [59, 59, 58, 90, 70, 73], [75, 69, 72, 114, 100, 104], [41, 56, 40, 62, 44, 71], [54, 63, 52, 83, 56, 97], [72, 95, 67, 103, 71, 122], [38, 36, 38, 32, 36, 57], [85, 56, 77, 50, 77, 78], [45, 50, 43, 40, 38, 62], [62, 73, 55, 56, 52, 84], [78, 81, 71, 74, 69, 126], [38, 35, 40, 27, 25, 35], [45, 22, 60, 27, 30, 29], [80, 52, 50, 90, 50, 89], [62, 50, 58, 73, 54, 72], [86, 68, 72, 109, 66, 106], [44, 38, 39, 61, 79, 42], [54, 45, 47, 75, 98, 52], [78, 65, 68, 112, 154, 75], [66, 65, 48, 62, 57, 52], [123, 100, 62, 97, 81, 68], [67, 82, 62, 46, 48, 43], [95, 124, 78, 69, 71, 58], [75, 80, 60, 65, 90, 102], [62, 48, 54, 63, 60, 68], [74, 48, 76, 83, 81, 104], [45, 80, 100, 35, 37, 28], [59, 110, 150, 45, 49, 35], [60, 50, 150, 50, 150, 60], [78, 52, 60, 63, 65, 23], [101, 72, 72, 99, 89, 29], [62, 48, 66, 59, 57, 49], [82, 80, 86, 85, 75, 72], [53, 54, 53, 37, 46, 45], [86, 92, 88, 68, 75, 73], [42, 52, 67, 39, 56, 50], [72, 105, 115, 54, 86, 68], [50, 60, 60, 60, 60, 30], [65, 75, 90, 97, 123, 44], [50, 53, 62, 58, 63, 44], [71, 73, 88, 120, 89, 59], [44, 38, 33, 61, 43, 70], [62, 55, 52, 109, 94, 109], [58, 89, 77, 45, 45, 48], [82, 121, 119, 69, 59, 71], [77, 59, 50, 67, 63, 46], [123, 77, 72, 99, 92, 58], [95, 65, 65, 110, 130, 60], [78, 92, 75, 74, 63, 118], [67, 58, 57, 81, 67, 101], [50, 50, 150, 50, 150, 50], [45, 50, 35, 55, 75, 40], [68, 75, 53, 83, 113, 60], [90, 100, 70, 110, 150, 80], [57, 80, 91, 80, 87, 75], [43, 70, 48, 50, 60, 38], [85, 110, 76, 65, 82, 56], [49, 66, 70, 44, 55, 51], [65, 90, 122, 58, 75, 84], [55, 69, 85, 32, 35, 28], [95, 117, 184, 44, 46, 28], [40, 30, 35, 45, 40, 55], [85, 70, 80, 97, 80, 123], [126, 131, 95, 131, 98, 99], [126, 131, 95, 131, 98, 99], [108, 100, 121, 81, 95, 95], [50, 100, 150, 100, 150, 50], [80, 110, 60, 150, 130, 70], [80, 110, 120, 130, 90, 70], [68, 55, 55, 50, 50, 42], [78, 75, 75, 70, 70, 52], [78, 107, 75, 100, 100, 70], [45, 65, 40, 60, 40, 70], [65, 85, 50, 80, 50, 90], [95, 115, 90, 80, 90, 60], [50, 54, 54, 66, 56, 40], [60, 69, 69, 91, 81, 50], [80, 74, 74, 126, 116, 60], [35, 75, 30, 30, 30, 65], [55, 85, 50, 40, 50, 75], [80, 120, 75, 75, 75, 60], [48, 70, 30, 30, 30, 45], [88, 110, 60, 55, 60, 45], [47, 62, 45, 55, 45, 46], [57, 82, 95, 55, 75, 36], [77, 70, 90, 145, 75, 43], [47, 82, 57, 42, 47, 63], [97, 132, 77, 62, 67, 43], [75, 70, 70, 98, 70, 93], [40, 45, 40, 55, 40, 84], [60, 55, 60, 95, 70, 124], [45, 65, 40, 30, 40, 60], [75, 115, 65, 55, 65, 112], [45, 20, 20, 25, 25, 40], [50, 53, 62, 43, 52, 45], [50, 63, 152, 53, 142, 35], [70, 100, 70, 45, 55, 45], [100, 125, 100, 55, 85, 35], [38, 40, 52, 40, 72, 27], [68, 70, 92, 50, 132, 42], [40, 55, 35, 50, 35, 35], [70, 105, 90, 80, 90, 45], [40, 35, 55, 65, 75, 15], [60, 45, 80, 90, 100, 30], [48, 44, 40, 71, 40, 77], [68, 64, 60, 111, 60, 117], [70, 75, 50, 45, 50, 50], [120, 125, 80, 55, 60, 60], [42, 30, 38, 30, 38, 32], [52, 40, 48, 40, 48, 62], [72, 120, 98, 50, 98, 72], [51, 52, 90, 82, 110, 100], [90, 60, 80, 90, 110, 60], [100, 120, 90, 40, 60, 80], [25, 35, 40, 20, 30, 80], [75, 125, 140, 60, 90, 40], [55, 55, 80, 70, 45, 15], [85, 75, 110, 100, 75, 35], [55, 60, 130, 30, 130, 5], [95, 95, 95, 95, 95, 59], [95, 95, 95, 95, 95, 95], [60, 60, 100, 60, 100, 60], [65, 115, 65, 75, 95, 65], [60, 78, 135, 91, 85, 36], [65, 98, 63, 40, 73, 96], [55, 90, 80, 50, 105, 96], [68, 105, 70, 70, 70, 92], [78, 60, 85, 135, 91, 36], [70, 131, 100, 86, 90, 40], [45, 55, 65, 45, 45, 45], [55, 75, 90, 65, 70, 65], [75, 110, 125, 100, 105, 85], [70, 115, 85, 95, 75, 130], [70, 85, 75, 130, 115, 95], [70, 130, 115, 85, 95, 75], [70, 75, 115, 95, 130, 85], [43, 29, 31, 29, 31, 37], [43, 29, 131, 29, 131, 37], [137, 137, 107, 113, 89, 97], [137, 113, 89, 137, 107, 97], [109, 53, 47, 127, 131, 103], [107, 139, 139, 53, 53, 79], [71, 137, 37, 137, 37, 151], [83, 89, 71, 173, 71, 83], [97, 101, 103, 107, 101, 61], [59, 181, 131, 59, 31, 109], [223, 101, 53, 97, 53, 43], [97, 107, 101, 127, 89, 79], [80, 95, 115, 130, 115, 65], [90, 125, 80, 90, 90, 125], [67, 73, 67, 73, 67, 73], [73, 73, 73, 127, 73, 121], [61, 131, 211, 53, 101, 13], [53, 127, 53, 151, 79, 107], [88, 112, 75, 102, 80, 143], [46, 65, 65, 55, 35, 34], [135, 143, 143, 80, 65, 34], [50, 65, 50, 40, 40, 65], [70, 85, 70, 55, 60, 80], [100, 125, 90, 60, 70, 85], [50, 71, 40, 40, 40, 69], [65, 86, 60, 55, 60, 94], [80, 116, 75, 65, 75, 119], [50, 40, 40, 70, 40, 70], [65, 60, 55, 95, 55, 90], [70, 85, 65, 125, 65, 120], [70, 55, 55, 35, 35, 25], [120, 95, 95, 55, 75, 20], [38, 47, 35, 33, 35, 57], [68, 67, 55, 43, 55, 77], [98, 87, 105, 53, 85, 67], [25, 20, 20, 25, 45, 45], [50, 35, 80, 50, 90, 30], [60, 45, 110, 80, 120, 90], [40, 28, 28, 47, 52, 50], [70, 58, 58, 87, 92, 90], [40, 40, 60, 40, 60, 10], [60, 50, 90, 80, 120, 60], [42, 40, 55, 40, 45, 48], [72, 80, 100, 60, 90, 88], [50, 64, 50, 38, 38, 44], [90, 115, 90, 48, 68, 74], [59, 45, 50, 40, 50, 26], [69, 90, 60, 90, 60, 121], [30, 40, 50, 40, 50, 30], [80, 60, 90, 60, 70, 50], [110, 80, 120, 80, 90, 30], [40, 40, 80, 40, 40, 20], [70, 110, 80, 95, 60, 70], [110, 85, 80, 100, 80, 30], [52, 57, 75, 35, 50, 46], [72, 107, 125, 65, 70, 71], [70, 85, 55, 85, 95, 85], [41, 63, 40, 40, 30, 66], [61, 123, 60, 60, 50, 136], [40, 38, 35, 54, 35, 40], [75, 98, 70, 114, 70, 75], [50, 65, 45, 50, 50, 45], [100, 115, 65, 90, 90, 65], [50, 68, 60, 50, 50, 32], [80, 118, 90, 70, 80, 42], [40, 45, 45, 74, 54, 50], [60, 65, 65, 134, 114, 70], [42, 30, 45, 56, 53, 39], [57, 40, 65, 86, 73, 49], [57, 90, 95, 136, 103, 29], [45, 45, 30, 55, 40, 50], [65, 60, 45, 75, 55, 70], [95, 120, 65, 95, 75, 60], [93, 90, 101, 60, 81, 95], [70, 110, 100, 50, 60, 50], [60, 95, 50, 145, 130, 30], [62, 135, 95, 68, 82, 65], [80, 85, 75, 110, 100, 70], [58, 95, 145, 50, 105, 30], [45, 40, 40, 50, 61, 34], [65, 60, 75, 110, 121, 64], [65, 100, 100, 70, 60, 75], [48, 101, 95, 91, 85, 15], [30, 25, 35, 45, 30, 20], [70, 65, 60, 125, 90, 65], [100, 125, 135, 20, 20, 70], [75, 80, 110, 65, 90, 50], [60, 65, 55, 105, 95, 95], [58, 95, 58, 70, 58, 97], [72, 80, 49, 40, 49, 40], [122, 130, 69, 80, 69, 30], [90, 100, 90, 80, 70, 75], [90, 100, 90, 90, 80, 55], [90, 90, 100, 70, 80, 75], [90, 90, 100, 80, 90, 55], [70, 95, 115, 120, 50, 85], [28, 60, 30, 40, 30, 82], [68, 80, 50, 60, 50, 102], [88, 120, 75, 100, 75, 142], [92, 130, 115, 80, 115, 138], [92, 130, 115, 80, 115, 138], [140, 85, 95, 145, 95, 130], [60, 90, 60, 53, 50, 72], [100, 130, 100, 63, 60, 97], [105, 120, 105, 70, 95, 105], [80, 100, 50, 100, 50, 200], [200, 100, 50, 100, 50, 80], [100, 145, 130, 65, 110, 30], [100, 65, 60, 145, 80, 130], [100, 80, 80, 80, 80, 80]]

dex_forms = [["Cosplay Pikachu", "Pikachu Cosplayeur", "Cosplay-Pikachu", "换装皮卡丘", "옷갈아입기 피카츄", "Okigae Pikachu", "おきがえピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-cosplay.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-cosplay.gif"],
["Pikachu Rock Star", "Pikachu Rockeur", "Rocker-Pikachu", "重搖滾皮卡丘", "하드록 피카츄", "Hard Rock Pikachu", "ハードロック・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-rockstar.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-rockstar.gif"],
["Pikachu Belle", "Pikachu Lady", "Damen-Pikachu", "貴婦皮卡丘", "마담 피카츄", "Madame Pikachu", "マダム・ピカチュウ", 24, [12], base_stats[24] ,"https://play.pokemonshowdown.com/sprites/ani/pikachu-belle.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-belle.gif"],
["Pikachu Pop Star", "Pikachu Star", "Star-Pikachu", "偶像皮卡丘", "아이돌 피카츄", "Idol Pikachu", "アイドル・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-popstar.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-popstar.gif"],
["Pikachu, Ph.D.", "Pikachu Docteur", "Professoren-Pikachu", "博士皮卡丘", "닥터 피카츄", "Doctor Pikachu", "ドクター・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-phd.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-phd.gif"],
["Pikachu Libre", "Pikachu Catcheur", "Wrestler-Pikachu", "蒙面皮卡丘", "마스크드 피카츄", "Masked Pikachu", "マスクド・ピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-libre.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-libre.gif"],
["Original Cap Pikachu", "Pikachu Casquette Originale", "Original-Kappe Pikachu", "初始帽子皮卡丘", "오리지널캡 피카츄", "Original Cap Pikachu", "オリジナルキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-original.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-kantocap.gif"],
["Hoenn Cap Pikachu", "Pikachu Casquette de Hoenn", "Hoenn-Kappe Pikachu", "豐緣帽子皮卡丘", "칼로스캡 피카츄", "Kalos Cap Pikachu", "カロスキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-hoenn.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-hoenncap.gif"],
["Sinnoh Cap Pikachu", "Pikachu Casquette de Sinnoh", "Sinnoh-Kappe Pikachu", "神奧帽子皮卡丘", "신오캡 피카츄", "Sinnoh Cap Pikachu", "シンオウキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-sinnoh.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-sinnohcap.gif"],
["Unova Cap Pikachu", "Pikachu Casquette d'Unys", "Einall-Kappe Pikachu", "合眾帽子皮卡丘", "하나캡 피카츄", "Isshu Cap Pikachu", "イッシュキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-unova.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-unovacap.gif"],
["Kalos Cap Pikachu", "Pikachu Casquette de Kalos", "Kalos-Kappe Pikachu", "卡洛斯帽子皮卡丘", "칼로스캡 피카츄", "Kalos Cap Pikachu", "カロスキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-kalos.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-kaloscap.gif"],
["Alola Cap Pikachu", "Pikachu Casquette d'Alola", "Alola-Kappe Pikachu", "阿羅拉帽子皮卡丘", "알로라캡 피카츄", "Alola Cap Pikachu", "アローラキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-alola.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-alolacap.gif"],
["Partner Cap Pikachu", "Pikachu Casquette Partenaire", "Partnerkappe Pikachu", "就決定是你了帽子皮卡丘", "너로정했다캡 피카츄", "I Choose You Cap Pikachu", "キミにきめたキャップピカチュウ", 24, [12], base_stats[24], "https://play.pokemonshowdown.com/sprites/ani/pikachu-partner.gif", "https://play.pokemonshowdown.com/sprites/ani-shiny/pikachu-partner.gif"],
["World Cap Pikachu", "Pikachu Casquette Monde", "Weltreise-Kappe Pikachu", "世界帽子皮卡丘", "월드캡 피카츄", "World Cap Pikachu", "ワールドキャップピカチュウ", 24, [12], base_stats[24], "https://media.tenor.com/images/31e4cf180a51406e2944a79bc5e7f660/tenor.gif", "https://media.tenor.com/images/31e4cf180a51406e2944a79bc5e7f660/tenor.gif"]
]

trivias1 = [
  ["Which ball can be upgraded ? (One word)", "rb", "recoilball"],
  ["Tell the complete name of this Pokémon : -a-u-i-a", "makuhita"],
  ["Tell the complete name of this Pokémon : -a-i-a-a", "hariyama"],
  ["I'm a famous glitch Pokémon from the 1st generation. What's my name ?", "missingno.", "missingno"],
  ["Who is the 151th Pokémon in the national dex ?", "mew"],
  ["In which year did the first Pokémon video games came out on the Game Boy in Japan ?", "1996"]
]

trivias2 = [
  ["Tell the complete name of this Pokémon : -a-i-s", "latios"],
  ["Tell the complete name of this Pokémon : -a-i-s", "latias"],
  ["In what region could we collect Zygarde's cells and get 10% and 100% form Zygarde ?", "alola"],
  ["Whith what object can you fuse Kyurem with either Reshiram or Zekrom ?", 'dna splicers'],
  ["During which year did the live-action film __Detective Pikachu__ got released ?", "2019"]
]

trivias3 = [
  ["How many forms (excluding shiny) does Zygarde have ?", "3"]
]

trivias4 = [
  ["In the Pokémon anime, how many times does Jessie talk during the Team Rocket motto ?", "5"]
]

trivias5 = [
  ["During which year did the live-action film __Detective Pikachu__ got revealed ?", "2016"]
]


@bot.event
async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Don't send messages too quick ! Try again in {error.retry_after:.2f}s.")

optionupdater()
dataupdater()
keep_alive()
updata.start()
bot.add_cog(Owner(bot))
bot.add_cog(Main(bot))
bot.add_cog(Miscellaneous(bot))
bot.add_cog(Game(bot))
bot.run(os.getenv("token"))
