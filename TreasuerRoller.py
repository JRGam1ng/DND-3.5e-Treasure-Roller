from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random
# import sqlite3
from tkinter import ttk
from pathlib import Path

path = Path(__file__).resolve().parent


gem1 = ["Banded Agate", "Eye Agate", "Moss Agate", "Azurite", "Blue Quartz", "Hematite", "Lapis Lazuli", "Malachite", "Obsidian", "Rhodochrosite", "Tiger Eye Turquoise", "Freshwater (irregular) Pearl"]
gem2 = ["Bloodstone", "Carnelian", "Chalcedony", "Chrysoprase", "Citrine", "Iolite", "Jasper", "Moonstone", "Onyx", "Peridot", "Rock Crystal (clear quartz)", "Sard", "Sardonyx", "Rose Quartz", "Smoky Quartz", "Star Rose Quartz", "Zircon"]
gem3 = ["Amber", "Amethyst", "Chrysoprase", "Coral", "Red Garnet", "Brown-Green Garnet", "Jade", "Jet", "White Pearl", "Golden Pearl", "Pink Pearl", "Silver Pearl", "Red Spinel", "Red-Brown Spinel", "Deep Green Spinel", "Tourmaline"]
gem4 = ["Alexandrite", "Aquamarine", "Violet Garnet", "Black Pearl", "Deep Blue Spinel", "Golden Yellow Topaz", "Emerald"]
gem5 = ["White Opal", "Black Opal", "Fire Opal", "Blue Sapphire", "Fiery Yellow Corundum", "Rich Puprle Corundum", "Blue Star Sapphire", "Black Star Sapphire", "Star Ruby", "Ruby"]
gem6 = ["Blue-White Diamond", "Canary Diamond", "Pink Diamond", "Brown Diamond", "Blue Diamond", "Clear Diamond", "Jacinth"]

art1 = ["Silver Ewer", "Carved Bone", "Ivory Statuette", "Finely Wrought Small Gold Bracelet"]
art2 = ["Cloth of Gold Vestments", "Black Velvet Mask with Numerous Citrines", "Silver Chalice with Lapis Lazuli Gems"]
art3 = ["Large Well-done Wool Tapestry", "Brass Mug with Jade Inlays"]
art4 = ["Silver Comb with Moonstones", "Silver-Plated Steel Longsword with Jet Jewels in Hilt"]
art5 = ["Carved Harp of Exotic Wood with Ivory Inlay and Zircon Gems", "Solid Gold Idol (10 lb.)"]
art6 = ["Gold Dragon Comb with Red Garnet Eye", "Gold and Topaz Bottle Stopper Cork", "Ceremonial Electrum Dagger with a Star Ruby in the Pommel"]
art7 = ["Eyepatch with Mock Eye of Sapphire and Moonstone", "Fire Opal Pendant on a Fine Gold Chain", "Old Masterpiece Painting"]
art8 = ["Embroidered Silk and Velvet Mantle with Numberous Moonstones", "Sapphire Pendant on Gold Chain"]
art9 = ["Embroidered and Bejeweled Glove", "Jeweled Anklet", "Gold Music Box"]
art10 = ["Golden Circlet with Four Aquamarines", "A String of Small Pink Pearls (necklace)"]
art11 = ["Jeweled Gold Crown", "Jeweled Electrum Ring"]
art12 = ["Gold and Ruby Ring", "Gold Cup Set with Emeralds"]


gem_tot_name = []
gem_worth_tot = []
art_tot_name = []
art_worth_tot = []
total_item_type = []
itemtypelis = []
total_item_worth = [] 
itemworthlis = []
total_item_number = [] 
numofitemlis = []
total_item_name = []
itemlis = []


lvl = ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5", "Level 6", "Level 7", "Level 8", "Level 9", "Level 10", "Level 11", "Level 12", "Level 13", "Level 14", "Level 15", "Level 16", "Level 17", "Level 18", "Level 19", "Level 20"]



root = Tk()
root.title('Treasure Picker')
img = PhotoImage(file=str(path) + "\\" + 'JRLogo.png')
root.tk.call('wm', 'iconphoto', root._w, img)
root.geometry("1200x800")
root.configure(bg="black")

lvllabel = Label(root, text="Select this encounter's level:", bg="black", fg="#00ffff")
lvllabel.grid(row=0, column=0, columnspan=2)

selectlvl = ttk.Combobox(root, value=lvl)
selectlvl.current(0)
selectlvl.grid(row=1, column=0)

gold_img = str(path) + "\gold.png"
item_img = str(path) + "\items.png"
goods_img = str(path) + "\goods.png"

goldimg = ImageTk.PhotoImage(Image.open(gold_img))
itemimg = ImageTk.PhotoImage(Image.open(item_img))
goodsimg = ImageTk.PhotoImage(Image.open(goods_img))

show_gold = Label(root, image=goldimg, bg="black")
show_gold.grid(row = 3, column=4)

show_item = Label(root, image=itemimg, bg="black")
show_item.grid(row = 5, column=4)

show_goods = Label(root, image=goodsimg, bg="black")
show_goods.grid(row = 7, column=4)

goldoutput = Label(root, text="", bg="black", fg="#00ffff")
goldoutput.grid(row=3, column=5)

itemoutput = Label(root, text="", bg="black", fg="#00ffff")
itemoutput.grid(row=5, column=5)

goodsoutput = Label(root, text="", bg="black", wraplength=800, fg="#00ffff")
goodsoutput.grid(row=7, column=5)

#Level 1 Rolls
def lvl1gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 14:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 15 and percentile <= 29:
        money = randint(1, 6) * 1000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 30 and percentile <= 52:
        money = randint(1, 8) * 100
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 53 and percentile <= 95:
        money = (randint(1, 8) + randint(1, 8)) * 10
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = randint(1, 4) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl1goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 90:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 91 and percentile <= 95:
        x = 0
        gems = 1
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 96:
        x = 0
        art_roll = randint(1, 100)
        art = 1
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl1items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 71:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 72 and itemroll <= 95:
        zz = 0
        item_roll = 1
        while zz != item_roll:
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 84:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            zz += 1
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 96:
        minor = 1
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

#Level 2 Rolls
def lvl2gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 13:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 14 and percentile <= 23:
        money = randint(1, 10) * 1000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 24 and percentile <= 43:
        money = (randint(1, 10) + randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 44 and percentile <= 95:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)) * 10
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = (randint(1, 8) + randint(1, 8)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl2goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 81:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 82 and percentile <= 95:
        x = 0
        gems = randint(1, 3)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 96:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 3)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl2items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 49:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 50 and itemroll <= 85:
        zz = 0
        item_roll = 1
        while zz != item_roll:
            zz += 1
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 84:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 86:
        minor = 1
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

#Level 3 Rolls
def lvl3gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 11:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 12 and percentile <= 21:
        money = (randint(1, 10) + randint(1, 10)) * 1000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 22 and percentile <= 41:
        money = (randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)) * 100
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 42 and percentile <= 95:
        money = (randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = (randint(1, 10)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl3goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 77:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 78 and percentile <= 95:
        x = 0
        gems = randint(1, 3)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 96:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 3)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl3items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 49:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 50 and itemroll <= 79:
        zz = 0
        item_roll = randint(1, 3)
        while zz != item_roll:
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 80:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            zz += 1
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 80:
        minor = 1
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

#Level 4 Rolls
def lvl4gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 11:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 12 and percentile <= 21:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10)) * 1000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 22 and percentile <= 41:
        money = (randint(1, 12) + randint(1, 12) + randint(1, 12) + randint(1, 12)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 42 and percentile <= 95:
        money = (randint(1, 6)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = (randint(1, 8)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl4goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 70:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 71 and percentile <= 95:
        x = 0
        gems = randint(1, 4)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 96:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 3)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl4items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 42:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 43 and itemroll <= 62:
        zz = 0
        item_roll = randint(1, 4)
        while zz != item_roll:
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 80:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            zz += 1
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 63:
        minor = 1
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

#Level 5 Rolls
def lvl5gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 10:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 11 and percentile <= 19:
        money = (randint(1, 4)) * 10000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 20 and percentile <= 38:
        money = (randint(1, 6)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 39 and percentile <= 95:
        money = (randint(1, 8)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = (randint(1, 10)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl5goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 60:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 61 and percentile <= 95:
        x = 0
        gems = randint(1, 4)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 96:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 4)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl5items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 57:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 58 and itemroll <= 67:
        zz = 0
        item_roll = randint(1, 4)
        while zz != item_roll:
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 80:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            zz += 1
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 68:
        minor = randint(1, 3)
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

#Level 6 Rolls
def lvl6gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 10:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 11 and percentile <= 18:
        money = (randint(1, 6)) * 10000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 19 and percentile <= 37:
        money = (randint(1, 8)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 38 and percentile <= 95:
        money = (randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 96:
        money = (randint(1, 12)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl6goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 56:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 57 and percentile <= 92:
        x = 0
        gems = randint(1, 4)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 93:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 4)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl6items():
    total_item_type = []
    itemtypelis = []
    total_item_worth = [] 
    itemworthlis = []
    total_item_number = [] 
    numofitemlis = []
    total_item_name = []
    itemlis = []
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 54:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 55 and itemroll <= 59:
        zz = 0
        item_roll = randint(1, 4)
        while zz != item_roll:
            itemtype = random.randint(1, 100)
            if itemtype >= 1 and itemtype <= 17:
                item_type = "Alchemy Agent"
                alchemy_agent = random.randint(1, 100)
                if alchemy_agent >= 1 and alchemy_agent <= 12:
                    name = "Alchemist's Fire"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 13 and alchemy_agent <= 24:
                    name = "Acid"
                    worth = "10gp each"
                    number = random.randint(1, 4) + random.randint(1, 4)
                if alchemy_agent >= 25 and alchemy_agent <= 36:
                    name = "Smokesticks"
                    worth = "20gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 37 and alchemy_agent <= 48:
                    name = "Holy Water"
                    worth = "25gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 49 and alchemy_agent <= 62:
                    name = "Antitoxin"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 63 and alchemy_agent <= 74:
                    name = "Everburning Torch"
                    worth = "N/A"
                    number = 1
                if alchemy_agent >= 75 and alchemy_agent <= 88:
                    name = "Tanglefoot bags"
                    worth = "50gp each"
                    number = random.randint(1, 4)
                if alchemy_agent >= 89:
                    name = "Thunderstones"
                    worth = "30gp each"
                    number = random.randint(1, 4)
            if itemtype >= 18 and itemtype <= 50:
                armor_roll = random.randint(1, 100)
                size_roll = random.randint(1, 100)
                number = 1
                if size_roll >= 1 and size_roll <= 10:
                    size = "Small"
                if size_roll >= 11:
                    size = "Medium"
                item_type = size + " Armor"
                if armor_roll >= 1 and armor_roll <= 12:
                    name = "Chain Shirt"
                    worth = "100gp"
                if armor_roll >= 13 and armor_roll <= 18:
                    name = "Masterwork studded leather"
                    worth = "175gp"
                if armor_roll >= 19 and armor_roll <= 26:
                    name = "Breastplate"
                    worth = "200gp"
                if armor_roll >= 27 and armor_roll <= 34:
                    name = "Banded mail"
                    worth = "250gp"
                if armor_roll >= 35 and armor_roll <= 54:
                    name = "Half-plate"
                    worth = "600gp"
                if armor_roll >= 55 and armor_roll <= 80:
                    name = "Full plate"
                    worth = "1500gp"
                if armor_roll >= 81 and armor_roll <= 90:
                    prefix = "Darkwood"
                    actitem = random.randint(1, 100)
                    if actitem <= 50:
                        name = prefix + " buckler"
                        worth = "205gp"
                    if actitem >= 51:
                        name = prefix + " shield"
                        worth = "257gp"
                if armor_roll >= 91:
                    prefix = "Masterwork"
                    actitem = random.randint(1, 100)
                    if actitem >= 1 and actitem <= 17:
                        name = prefix + " buckler"
                        worth = "165gp"
                    if actitem >= 18 and actitem <= 40:
                        name = prefix + " light wooden shield"
                        worth = "153gp"
                    if actitem >= 41 and actitem <= 60:
                        name = prefix + " light steel shield"
                        worth = "159gp"
                    if actitem >= 61 and actitem <= 83:
                        name = prefix + " heavy wooden shield"
                        worth = "157gp"
                    if actitem >= 84:
                        name = prefix + " heavy steel shield"
                        worth = "170gp"
            if itemtype >= 51 and itemtype <= 83:
                number = 1
                item_type = "Weapon"
                weapon_roll = random.randint(1, 100)
                if weapon_roll >= 1 and weapon_roll <= 50:
                    name = "Masterwork Common Melee Weapon"
                    worth = "N/A"
                if weapon_roll >= 51 and weapon_roll <= 70:
                    name = "Masterwork Uncommon Weapon"
                    worth = "N/A"
                if weapon_roll >= 71:
                    name = "Masterwork Common Ranged Weapon"
                    worth = "N/A"
            if itemtype >= 80:
                number = 1
                item_type = "Tools and Gear"
                tool_roll = random.randint(1, 100)
                if tool_roll >= 1 and tool_roll <= 3:
                    name = "Empty Backpack"
                    worth = "2gp"
                if tool_roll >= 4 and tool_roll <= 6:
                    name = "Crowbar"
                    worth = "2gp"
                if tool_roll >= 7 and tool_roll <= 11:
                    name = "Bullseye Lantern"
                    worth = "12gp"
                if tool_roll >= 12 and tool_roll <= 16:
                    name = "Simple Lock"
                    worth = "20gp"
                if tool_roll >= 17 and tool_roll <= 21:
                    name = "Average Lock"
                    worth = "40gp"
                if tool_roll >= 22 and tool_roll <= 28:
                    name = "Good Lock"
                    worth = "80gp"
                if tool_roll >= 29 and tool_roll <= 35:
                    name = "Superior Lock"
                    worth = "150gp"
                if tool_roll >= 36 and tool_roll <= 40:
                    name = "Masterwork Manacles"
                    worth = "50gp"
                if tool_roll >= 41 and tool_roll <= 43:
                    name = "Small Steel Mirror"
                    worth = "10gp"
                if tool_roll >= 44 and tool_roll <= 46:
                    name = "Silk Rope (50 ft)"
                    worth = "10gp"
                if tool_roll >= 47 and tool_roll <= 53:
                    name = "Spyglass"
                    worth = "1000gp"
                if tool_roll >= 54 and tool_roll <= 58:
                    name = "Masterwork Artisan's Tools"
                    worth = "55gp"
                if tool_roll >= 59 and tool_roll <= 63:
                    name = "Climber's Kit"
                    worth = "80gp"
                if tool_roll >= 64 and tool_roll <= 68:
                    name = "Disguise Kit"
                    worth = "50gp"
                if tool_roll >= 69 and tool_roll <= 73:
                    name = "Healer's Kit"
                    worth = "50gp"
                if tool_roll >= 74 and tool_roll <= 77:
                    name = "Silver Holy Symbol"
                    worth = "25gp"
                if tool_roll >= 78 and tool_roll <= 81:
                    name = "Hourglass"
                    worth = "25gp"
                if tool_roll >= 82 and tool_roll <= 88:
                    name = "Magnifying Glass"
                    worth = "100gp"
                if tool_roll >= 89 and tool_roll <= 95:
                    name = "Masterwork Musical Instrument"
                    worth = "100gp"
                if tool_roll >= 96:
                    name = "Masterwork Thieves' Tools"
                    worth = "50gp"
            zz += 1
            itemtypelis.append(item_type)
            itemlis.append(name)
            numofitemlis.append(str(number))
            itemworthlis.append(worth)
        total_item_type = ', '.join(itemtypelis)
        total_item_worth = ', '.join(itemworthlis)
        total_item_number = ', '.join(numofitemlis)
        total_item_name = ', '.join(itemlis)
        itemoutput.config(text="You got these types of items: " + total_item_type + ".  There are " + total_item_number + " of " + total_item_name + ", which are worth " + total_item_worth + ".")

    if itemroll >= 60 and itemroll <= 97:
        minor = randint(1, 3)
        itemoutput.config(text='You found ' + str(minor) + ' minor item(s)!')

    if itemroll >= 98:
        medium = 1
        itemoutput.config(text='You found ' + str(medium) + ' medium item(s)!')

#Level 7 Rolls
def lvl7gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 11:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 12 and percentile <= 18:
        money = (randint(1, 10)) * 10000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 19 and percentile <= 35:
        money = (randint(1, 12)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 36 and percentile <= 93:
        money = (randint(1, 6) + randint(1, 6)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 94:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl7goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 48:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 49 and percentile <= 88:
        x = 0
        gems = randint(1, 4)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 89:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 4)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl7items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 51:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 52 and itemroll <= 97:
        minor = randint(1, 3)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 98:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")

#Level 8 Rolls
def lvl8gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 10:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 11 and percentile <= 15:
        money = (randint(1, 12)) * 10000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 16 and percentile <= 29:
        money = (randint(1, 6) + randint(1, 6)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 30 and percentile <= 87:
        money = (randint(1, 8) + randint(1, 8)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 88:
        money = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl8goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 45:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 46 and percentile <= 85:
        x = 0
        gems = randint(1, 8)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 86:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 4)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl8items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 48:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 49 and itemroll <= 96:
        minor = randint(1, 4)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 97:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")

#Level 9 Rolls
def lvl9gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 10:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 11 and percentile <= 15:
        money = (randint(1, 6) + randint(1, 6)) * 10000
        goldoutput.config(text="You found " + str(money) + " copper pieces!")
    if percentile >= 16 and percentile <= 29:
        money = (randint(1, 8) + randint(1, 8)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 30 and percentile <= 85:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 86:
        money = (randint(1, 12) + randint(1, 12)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl9goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 40:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 41 and percentile <= 80:
        x = 0
        gems = randint(1, 8)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 81:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 4)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl9items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 43:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 44 and itemroll <= 91:
        minor = randint(1, 4)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 92:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")

#Level 10 Rolls
def lvl10gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 10:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 11 and percentile <= 24:
        money = (randint(1, 10) + randint(1, 10)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 25 and percentile <= 79:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 80:
        money = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl10goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 35:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 36 and percentile <= 79:
        x = 0
        gems = randint(1, 8)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 80:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 6)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl10items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 40:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 41 and itemroll <= 88:
        minor = randint(1, 4)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 89 and itemroll <= 99:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll == 100:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 11 Rolls
def lvl11gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 8:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 9 and percentile <= 14:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 15 and percentile <= 75:
        money = (randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)) * 100
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 76:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)) * 10
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl11goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 24:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 25 and percentile <= 74:
        x = 0
        gems = randint(1, 10)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 75:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 6)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl11items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 31:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 32 and itemroll <= 84:
        minor = randint(1, 4)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 85 and itemroll <= 98:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 99:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 12 Rolls
def lvl12gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 8:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 9 and percentile <= 14:
        money = (randint(1, 12) + randint(1, 12) + randint(1, 12)) * 1000
        goldoutput.config(text="You found " + str(money) + " silver pieces!")
    if percentile >= 15 and percentile <= 75:
        money = (randint(1, 4)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 76:
        money = (randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl12goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 17:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 18 and percentile <= 70:
        x = 0
        gems = randint(1, 10)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 71:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 8)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl12items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 27:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 28 and itemroll <= 82:
        minor = randint(1, 6)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 83 and itemroll <= 97:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 98:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 13 Rolls
def lvl13gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 8:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 9 and percentile <= 75:
        money = (randint(1, 4)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 76:
        money = (randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl13goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 11:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 12 and percentile <= 66:
        x = 0
        gems = randint(1, 12)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 67:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 10)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl13items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 19:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 20 and itemroll <= 73:
        minor = randint(1, 6)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 74 and itemroll <= 95:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 96:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 14 Rolls
def lvl14gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 8:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 9 and percentile <= 75:
        money = (randint(1, 6)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 76:
        money = (randint(1, 12)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl14goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 11:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 12 and percentile <= 66:
        x = 0
        gems = randint(1, 8) + randint(1, 8)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 67:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 6) + randint(1, 6)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl14items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 19:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 20 and itemroll <= 58:
        minor = randint(1, 6)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 59 and itemroll <= 92:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 93:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 15 Rolls
def lvl15gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 3:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 4 and percentile <= 74:
        money = (randint(1, 8)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 75:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl15goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 9:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 10 and percentile <= 65:
        x = 0
        gems = randint(1, 10) + randint(1, 10)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 66:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 8) + randint(1, 8)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl15items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 11:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 12 and itemroll <= 46:
        minor = randint(1, 10)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 47 and itemroll <= 90:
        medium = 1
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 91:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 16 Rolls
def lvl16gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 3:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 4 and percentile <= 74:
        money = (randint(1, 12)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 75:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl16goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 7:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 8 and percentile <= 64:
        x = 0
        gems = randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 65:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 10) + randint(1, 10)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl16items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 40:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 41 and itemroll <= 46:
        minor = randint(1, 10)
        itemoutput.config(text="You got " + str(minor) + " minor magical item(s)!")
    if itemroll >= 47 and itemroll <= 90:
        medium = randint(1, 3)
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 91:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 17 Rolls
def lvl17gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 3:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 4 and percentile <= 68:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 69:
        money = (randint(1, 10) + randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl17goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 4:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 5 and percentile <= 63:
        x = 0
        gems = randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 64:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 8) + randint(1, 8) + randint(1, 8)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl17items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 33:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 34 and itemroll <= 83:
        medium = randint(1, 3)
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 84:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 18 Rolls
def lvl18gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 2:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 3 and percentile <= 65:
        money = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 66:
        money = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl18goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 4:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 5 and percentile <= 54:
        x = 0
        gems = randint(1, 12) + randint(1, 12) + randint(1, 12)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 55:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 10) + randint(1, 10) + randint(1, 10)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl18items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 24:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 25 and itemroll <= 80:
        medium = randint(1, 4)
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 81:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")

#Level 19 Rolls
def lvl19gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 2:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 3 and percentile <= 65:
        money = (randint(1, 8) + randint(1, 8) + randint(1, 8)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 66:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl19goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 3:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 4 and percentile <= 50:
        x = 0
        gems = randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 51:
        x = 0
        art_roll = randint(1, 100)
        art = randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl19items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 4:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 5 and itemroll <= 70:
        medium = randint(1, 4)
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 71:
        major = 1
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")


#Level 20 Rolls
def lvl20gold():
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 2:
        goldoutput.config(text="You didn't find any gold!")
    if percentile >= 3 and percentile <= 65:
        money = (randint(1, 8) + randint(1, 8) + randint(1, 8) + randint(1, 8)) * 1000
        goldoutput.config(text="You found " + str(money) + " gold pieces!")
    if percentile >= 66:
        money = (randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)) * 100
        goldoutput.config(text="You found " + str(money) + " platinum pieces!")

def lvl20goods():
    gem_tot_name = []
    gem_worth_tot = []
    art_tot_name = []
    art_worth_tot = []
    percentile = randint(1, 100)
    if percentile >= 1 and percentile <= 2:
        goodsoutput.config(text="You didn't find any goods.")
    if percentile >= 3 and percentile <= 38:
        x = 0
        gems = randint(1, 10) + randint(1, 10) + randint(1, 10) + randint(1, 10)
        while x != gems:
            gem_roll = randint(1, 100)
            if gem_roll >= 1 and gem_roll <= 25:
                gem_pick = random.choice(gem1)
                gem_tot_name.append(gem_pick)
                gem_worth = randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 26 and gem_roll <= 50:
                gem_pick = random.choice(gem2)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 51 and gem_roll <= 70:
                gem_pick = random.choice(gem3)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 10
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 71 and gem_roll <= 90:
                gem_pick = random.choice(gem4)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 91 and gem_roll <= 99:
                gem_pick = random.choice(gem5)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4)) * 100
                gem_worth_tot.append(str(gem_worth))
            if gem_roll >= 100:
                gem_pick = random.choice(gem6)
                gem_tot_name.append(gem_pick)
                gem_worth = (randint(1, 4) + randint(1, 4)) * 1000
                gem_worth_tot.append(str(gem_worth))
            x += 1
        total_gem_name = ', '.join(gem_tot_name)
        total_gem_worth = ', '.join(gem_worth_tot)
        goodsoutput.config(text='You found ' + str(gems) + ' gem(s)!  They are: ' + total_gem_name + ", worth " + total_gem_worth + " gold respectively.")
    if percentile >= 39:
        x = 0
        art_roll = randint(1, 100)
        art = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6))
        while x != art:
            if art_roll >= 1 and art_roll <= 10:
                art_pick = random.choice(art1)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 11 and art_roll <= 25:
                art_pick = random.choice(art2)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 10
                art_worth_tot.append(str(art_worth))
            if art_roll >= 26 and art_roll <= 40:
                art_pick = random.choice(art3)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 41 and art_roll <= 50:
                art_pick = random.choice(art4)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 10) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 51 and art_roll <= 60:
                art_pick = random.choice(art5)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 61 and art_roll <= 70:
                art_pick = random.choice(art6)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 71 and art_roll <= 80:
                art_pick = random.choice(art7)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 81 and art_roll <= 85:
                art_pick = random.choice(art8)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6) + randint(1, 6)) * 100
                art_worth_tot.append(str(art_worth))
            if art_roll >= 86 and art_roll <= 90:
                art_pick = random.choice(art9)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 4) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 91 and art_roll <= 95:
                art_pick = random.choice(art10)
                art_tot_name.append(art_pick)
                art_worth = randint(1, 6) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll >= 96 and art_roll <= 99:
                art_pick = random.choice(art11)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 4) + randint(1, 4)) * 1000
                art_worth_tot.append(str(art_worth))
            if art_roll == 100:
                art_pick = random.choice(art12)
                art_tot_name.append(art_pick)
                art_worth = (randint(1, 6) + randint(1, 6)) * 1000
                art_worth_tot.append(str(art_worth))
            x += 1
        total_art_name = ', '.join(art_tot_name)
        total_art_worth = ', '.join(art_worth_tot)
        goodsoutput.config(text='You found ' + str(art) + ' art piece(s)!  They are: ' + total_art_name + ", worth " + total_art_worth + " gold respectively.")

def lvl20items():
    itemroll = randint(1, 100)
    if itemroll >= 1 and itemroll <= 25:
        itemoutput.config(text="Awww dang, you didn't find any items.")
    if itemroll >= 26 and itemroll <= 65:
        medium = randint(1, 4)
        itemoutput.config(text="You got " + str(medium) + " medium magical item(s)!")
    if itemroll >= 66:
        major = randint(1, 3)
        itemoutput.config(text="You got " + str(major) + " major magical item(s)!")


def selectedlvl():
    level = selectlvl.get()
    if level == "Level 1":
        lvl1gold()
        lvl1goods()
        lvl1items()
    if level == "Level 2":
        lvl2gold()
        lvl2goods()
        lvl2items()
    if level == "Level 3":
        lvl3gold()
        lvl3goods()
        lvl3items()
    if level == "Level 4":
        lvl4gold()
        lvl4goods()
        lvl4items()
    if level == "Level 5":
        lvl5gold()
        lvl5goods()
        lvl5items()
    if level == "Level 6":
        lvl6gold()
        lvl6goods()
        lvl6items()
    if level == "Level 7":
        lvl7gold()
        lvl7goods()
        lvl7items()
    if level == "Level 8":
        lvl8gold()
        lvl8goods()
        lvl8items()
    if level == "Level 9":
        lvl9gold()
        lvl9goods()
        lvl9items()
    if level == "Level 10":
        lvl10gold()
        lvl10goods()
        lvl10items()
    if level == "Level 11":
        lvl11gold()
        lvl11goods()
        lvl11items()
    if level == "Level 12":
        lvl12gold()
        lvl12goods()
        lvl12items()
    if level == "Level 13":
        lvl13gold()
        lvl13goods()
        lvl13items()
    if level == "Level 14":
        lvl14gold()
        lvl14goods()
        lvl14items()
    if level == "Level 15":
        lvl15gold()
        lvl15goods()
        lvl15items()
    if level == "Level 16":
        lvl16gold()
        lvl16goods()
        lvl16items()
    if level == "Level 17":
        lvl17gold()
        lvl17goods()
        lvl17items()
    if level == "Level 18":
        lvl18gold()
        lvl18goods()
        lvl18items()
    if level == "Level 19":
        lvl19gold()
        lvl19goods()
        lvl19items()
    if level == "Level 20":
        lvl20gold()
        lvl20goods()
        lvl20items()


lvlbutton = Button(root, text="Submit", command=selectedlvl, bg="#00ffff", fg="black")
lvlbutton.grid(row=1, column=1)


root.mainloop()