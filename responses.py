import sqlite3
from typing import List

import database


def handle_response(user, message):
    p_message = message.lower()
    p_message = p_message.split()

    if p_message[0] == 'remove' and 1 <= int(p_message[len(p_message) - 1]) <= 8:
        if len(p_message) == 4:
            p_message = [p_message[0], p_message[1] + ' ' + p_message[2], p_message[3]]
        return [0, database.remove_card(user, p_message[2], p_message[1])]

    if p_message[0] == 'clear' and 1 <= int(p_message[1]) <= 8:
        return [0, database.clear_deck(user, p_message[1])]

    if p_message[0] == 'add' and 1 <= int(p_message[len(p_message) - 1]) <= 8:
        if len(p_message) == 4:
            p_message = [p_message[0], p_message[1] + ' ' + p_message[2], p_message[3]]
        return [0, database.add_card(user, p_message[2], p_message[1])]

    if p_message[0] == 'view' and p_message[1] == 'all':
        png_dict = database.print_all(user)
        return [2, png_dict]

    if p_message[0] == 'view' and 1 <= int(p_message[1]) <= 8:
        return database.print_deck(user, p_message[1])

    if p_message[0] == 'see' and p_message[1] == 'cards':
        return [3, database.see_cards()]

    if p_message[0] == 'help':
        return [0, "`"
                   "To add a card to your deck, use !add card_name deckslot. You have 8 slots and can fit 8 cards per slot\n"
                   "To remove a card from your deck, use !remove card_name deckslot\n"
                   "To remove all cards from your deck, use !clear deckslot\n"
                   "To view a deck, use !view deckslot\n"
                   "To view all your decks, use !view all"
                   "`"]

    return [0, "Use !help for valid commands!"]
