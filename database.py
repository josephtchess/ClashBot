import sqlite3
from PIL import Image
import os

champions = ['archer queen', 'golden knight', 'mighty miner', 'monk', 'skeleton king', 'little prince']
clash_royale_cards = {
    "archer queen": [5, "ArcherQueenCard.png"],
    "archers": [3, "ArchersCard.png"],
    "arrows": [3, "ArrowsCard.png"],
    "baby dragon": [4, "BabyDragonCard.png"],
    "balloon": [5, "BalloonCard.png"],
    "bandit": [3, "BanditCard.png"],
    "barbarian barrel": [2, "BarbarianBarrelCard.png"],
    "barbarian hut": [7, "BarbarianHutCard.png"],
    "barbarians": [5, "BarbariansCard.png"],
    "bats": [2, "BatsCard.png"],
    "battle healer": [4, "BattleHealerCard.png"],
    "battle ram": [4, "BattleRamCard.png"],
    "bomb tower": [4, "BombTowerCard.png"],
    "bomber": [2, "BomberCard.png"],
    "bowler": [5, "BowlerCard.png"],
    "cannon": [3, "CannonCard.png"],
    "cannon cart": [5, "CannonCartCard.png"],
    "clone": [3, "CloneCard.png"],
    "dark prince": [4, "DarkPrinceCard.png"],
    "dart goblin": [3, "DartGoblinCard.png"],
    "earthquake": [3, "EarthquakeCard.png"],
    "elixir collector": [6, "ElixirCollectorCard.png"],
    "elixir golem": [3, "ElixirGolemCard.png"],
    "elite barbarians": [6, "EliteBarbariansCard.png"],
    "electro dragon": [5, "ElectroDragonCard.png"],
    "electro giant": [7, "ElectroGiantCard.png"],
    "electro spirit": [1, "ElectroSpiritCard.png"],
    "electro wizard": [4, "ElectroWizardCard.png"],
    "executioner": [5, "ExecutionerCard.png"],
    "fire spirit": [1, "FireSpiritCard.png"],
    "fireball": [4, "FireballCard.png"],
    "firecracker": [3, "FirecrackerCard.png"],
    "fisherman": [4, "FishermanCard.png"],
    "flying machine": [4, "FlyingMachineCard.png"],
    "freeze": [4, "FreezeCard.png"],
    "furnace": [4, "FurnaceCard.png"],
    "giant": [5, "GiantCard.png"],
    "giant snowball": [2, "GiantSnowballCard.png"],
    "giant skeleton": [6, "GiantSkeletonCard.png"],
    "goblin barrel": [3, "GoblinBarrelCard.png"],
    "goblin cage": [4, "GoblinCageCard.png"],
    "goblin gang": [3, "GoblinGangCard.png"],
    "goblin giant": [6, "GoblinGiantCard.png"],
    "goblin hut": [5, "GoblinHutCard.png"],
    "goblin drill": [4, "GoblinDrillCard.png"],
    "goblins": [2, "GoblinsCard.png"],
    "golden knight": [4, "GoldenKnightCard.png"],
    "golem": [8, "GolemCard.png"],
    "graveyard": [5, "GraveyardCard.png"],
    "guards": [3, "GuardsCard.png"],
    "heal spirit": [1, "HealSpiritCard.png"],
    "hog rider": [4, "HogRiderCard.png"],
    "hunter": [4, "HunterCard.png"],
    "ice golem": [2, "IceGolemCard.png"],
    "ice spirit": [1, "IceSpiritCard.png"],
    "ice wizard": [3, "IceWizardCard.png"],
    "inferno dragon": [4, "InfernoDragonCard.png"],
    "inferno tower": [5, "InfernoTowerCard.png"],
    "knight": [3, "KnightCard.png"],
    "lava hound": [7, "LavaHoundCard.png"],
    "lightning": [6, "LightningCard.png"],
    "little prince": [3, "LittlePrinceCard.png"],
    "lumberjack": [4, "LumberjackCard.png"],
    "mega knight": [7, "MegaKnightCard.png"],
    "mega minion": [3, "MegaMinionCard.png"],
    "mighty miner": [4, "MightyMinerCard.png"],
    "miner": [3, "MinerCard.png"],
    "mini pekka": [4, "MiniPekkaCard.png"],
    "minion horde": [5, "MinionHordeCard.png"],
    "minions": [3, "MinionsCard.png"],
    "mirror": [1, "MirrorCard.png"],
    "monk": [5, "MonkCard.png"],
    "mother witch": [4, "MotherWitchCard.png"],
    "musketeer": [4, "MusketeerCard.png"],
    "night witch": [4, "NightWitchCard.png"],
    "pekka": [7, "PekkaCard.png"],
    "phoenix": [4, "PhoenixCard.png"],
    "poison": [4, "PoisonCard.png"],
    "prince": [5, "PrinceCard.png"],
    "princess": [3, "PrincessCard.png"],
    "rage": [2, "RageCard.png"],
    "ram rider": [5, "RamRiderCard.png"],
    "rascals": [5, "RascalsCard.png"],
    "rocket": [6, "RocketCard.png"],
    "royal delivery": [3, "RoyalDeliveryCard.png"],
    "royal ghost": [3, "RoyalGhostCard.png"],
    "royal giant": [6, "RoyalGiantCard.png"],
    "royal hogs": [5, "RoyalHogsCard.png"],
    "royal recruits": [7, "RoyalRecruitsCard.png"],
    "skeleton army": [3, "SkeletonArmyCard.png"],
    "skeleton barrel": [3, "SkeletonBarrelCard.png"],
    "skeleton dragons": [4, "SkeletonDragonsCard.png"],
    "skeleton king": [4, "SkeletonKingCard.png"],
    "skeletons": [1, "SkeletonsCard.png"],
    "sparky": [6, "SparkyCard.png"],
    "spear goblins": [2, "SpearGoblinsCard.png"],
    "tesla": [4, "TeslaCard.png"],
    "the log": [2, "TheLogCard.png"],
    "three musketeers": [9, "ThreeMusketeersCard.png"],
    "tombstone": [3, "TombstoneCard.png"],
    "tornado": [3, "TornadoCard.png"],
    "valkyrie": [4, "ValkyrieCard.png"],
    "wall breakers": [2, "WallBreakersCard.png"],
    "witch": [5, "WitchCard.png"],
    "wizard": [5, "WizardCard.png"],
    "xbow": [6, "XbowCard.png"],
    "zappies": [4, "ZappiesCard.png"],
    "zap": [2, "ZapCard.png"],
}

def clear_deck(user, deck_num):
    conn, c = get_conn()
    c.execute("SELECT * FROM players WHERE username=?", (user,))
    user_exists = c.fetchone()[0]

    if not user_exists:
        conn.close()
        return "Please make a deck first"

    deck_column = f"deck{deck_num}"
    deck_count_column = f"{deck_column}count"
    c.execute(f"SELECT {deck_column}, {deck_count_column} FROM players WHERE username=?", (user,))
    result = c.fetchone()

    if result[0] is None or result[1] is None:
        conn.close()
        return "This deck slot is already empty"

    c.execute(f"UPDATE players SET {deck_column}=?, {deck_count_column}=? WHERE username=?",
              ("", 0, user))
    conn.commit()
    conn.close()
    return f"{user} cleared deck slot {deck_num}"


def get_conn():
    conn = sqlite3.connect('all_decks.db')
    return [conn, conn.cursor()]

def print_all(user):
    conn, c = get_conn()
    c.execute("SELECT * FROM players WHERE username=?", (user,))
    user_exists = c.fetchone()[0]

    if not user_exists:
        conn.close()
        return [0, "Please make a deck first"]

    png_dict = {}
    for i in range(1,9):
        deck_column = f"deck{i}"
        c.execute(f"SELECT {deck_column} FROM players WHERE username=?", (user,))
        current_deck = c.fetchone()[0]
        if current_deck and len(current_deck) > 0:
            deck_array = current_deck.split(',')
            png_array = []
            elixertotal = 0
            for card in deck_array:
                png_array.append(clash_royale_cards[card][1])
                elixertotal += clash_royale_cards[card][0]
            elixer_avg = round(elixertotal / len(deck_array), 1)
            first_image = Image.open(os.path.join('clash_cards', png_array[0]))
            width, height = first_image.size
            new_image = Image.new('RGB', (width * len(png_array), height), 'white')
            for j, png_file in enumerate(png_array):
                image = Image.open(os.path.join('clash_cards', png_file))
                new_image.paste(image, (j * width, 0))
            new_image.save(f'D:/CS/ClashBot/tempImage{i}.png')
            png_dict[i] = [f"Deckslot {i}: ", f'D:/CS/ClashBot/tempImage{i}.png', f"Elixer Average is {elixer_avg}"]
    conn.close()
    return png_dict

def print_deck(user, deck_num):
    conn, c = get_conn()
    c.execute("SELECT * FROM players WHERE username=?", (user,))
    user_exists = c.fetchone()[0]

    if not user_exists:
        conn.close()
        return [0, "Please make a deck first"]

    deck_column = f"deck{deck_num}"
    c.execute(f"SELECT {deck_column} FROM players WHERE username=?", (user,))
    current_deck = c.fetchone()[0]
    if current_deck and len(current_deck) > 0:
        deck_array = current_deck.split(',')
        png_array = []
        elixertotal = 0
        for card in deck_array:
            png_array.append(clash_royale_cards[card][1])
            elixertotal += clash_royale_cards[card][0]
        elixer_avg = round(elixertotal/len(deck_array), 1)
        first_image = Image.open(os.path.join('clash_cards', png_array[0]))
        width, height = first_image.size
        new_image = Image.new('RGB', (width * len(png_array), height), 'white')
        for i, png_file in enumerate(png_array):
            image = Image.open(os.path.join('clash_cards', png_file))
            new_image.paste(image, (i * width, 0))
        new_image.save(f'D:/CS/ClashBot/tempImage{deck_num}.png')
        conn.close()
        return [1,f'D:/CS/ClashBot/tempImage{deck_num}.png', elixer_avg]
    conn.close()
    return [0, f"{user} does not have any cards in deck {deck_num}"]

def add_card(user, deck_num, card_name):
    ischamp = 0
    if card_name in champions:
        ischamp = 1
    if card_name not in clash_royale_cards:
        return f'{card_name} does not not exist'
    conn, c = get_conn()
    c.execute("SELECT * FROM players WHERE username=?", (user,))
    user_exists = c.fetchone()
    m = ''

    if not user_exists:
        # If the user does not exist, create a new user with default values
        c.execute("INSERT INTO players (username) VALUES (?)", (user,))
        conn.commit()

    # Construct the deck column name (e.g., 'deck1', 'deck2', etc.)
    deck_column = f"deck{deck_num}"
    deck_count_column = f"{deck_column}count"

    # Retrieve the current deck value
    print("getting column")
    c.execute(f"SELECT {deck_column}, {deck_count_column} FROM players WHERE username=?", (user,))
    result = c.fetchone()
    if result[0] == None:
        current_deck = ""
    else:
        current_deck = result[0]
    if result[1] == None:
        deck_count = 0
    else:
        deck_count = result[1]
    print(result[1])

    if card_name in current_deck.split(','):
        conn.close()
        return f"Card '{card_name}' is already in {deck_column} for user '{user}'"

    if deck_count < 8:
        # Concatenate the new card to the existing deck value
        if ischamp:
            for champ in champions:
                if champ in current_deck.split(','):
                    conn.close()
                    return f"Cannot have more than one Champion per deck\nCurrent Champion: {champ}"
        new_deck = f"{current_deck},{card_name}" if current_deck else card_name

        # Update the deck and increment the deckcount in the players table
        c.execute(f"UPDATE players SET {deck_column}=?, {deck_count_column}=? WHERE username=?",
                  (new_deck, deck_count + 1, user))

        m = f"Card '{card_name}' added to {deck_column} for user '{user}'"

        # Commit changes and close the connection
        conn.commit()
    else:
        m = f"Cannot add card to {deck_column} for user '{user}'. Deck count is already 8."

    conn.close()
    return m

def remove_card(user, deck_num, card_name):
    name = card_name.lower()
    print(user, name, deck_num)
    conn, c = get_conn()
    c.execute("SELECT * FROM players WHERE username=?", (user,))
    user_exists = c.fetchone()[0]
    if not user_exists:
        conn.close()
        return "Please make a deck first"

    deck_column = f"deck{deck_num}"
    deck_count_column = f"{deck_column}count"
    c.execute(f"SELECT {deck_column}, {deck_count_column} FROM players WHERE username=?", (user,))
    result = c.fetchone()
    if result[0] and result[1]:
        current_deck = result[0]
        num_cards = result[1]
        print(current_deck, num_cards)
        deck_array = current_deck.split(',')
        if name in deck_array:
            deck_array.remove(name)
            new_deck = ','.join(deck_array)
            c.execute(f"UPDATE players SET {deck_column}=?, {deck_count_column}=? WHERE username=?",
                      (new_deck, num_cards - 1, user))
            conn.commit()
            conn.close()
            return f"{user} removed {card_name} from deckslot {deck_num}"
        conn.close()
        return f"{user} does not have {card_name} in deckslot {deck_num}"
    conn.close()
    return f"{user} deck {deck_num} is empty"

def create_database_and_table():
    conn, c = get_conn()

    c.execute("""CREATE TABLE IF NOT EXISTS players (
    username TEXT PRIMARY KEY,
    deck1 TEXT,
    deck1count INTEGER,
    deck2 TEXT,
    deck2count INTEGER,
    deck3 TEXT,
    deck3count INTEGER,
    deck4 TEXT,
    deck4count INTEGER,
    deck5 TEXT,
    deck5count INTEGER,
    deck6 TEXT,
    deck6count INTEGER,
    deck7 TEXT,
    deck7count INTEGER,
    deck8 TEXT,
    deck8count INTEGER
    )""")
    conn.commit()
    conn.close()

def see_cards():
    smaller_dict = {}
    for key in clash_royale_cards:
        smaller_dict[key] = [f"Card Name:{key} Elixir {clash_royale_cards[key][0]}"]
    return smaller_dict