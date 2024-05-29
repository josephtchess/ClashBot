import bot
import database
if __name__ == '__main__':
    database.create_database_and_table()
    bot.run_bot()
