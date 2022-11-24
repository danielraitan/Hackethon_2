import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  '123456789'
DATABASE =  'Hackethon_2'

connection = psycopg2.connect(host = HOSTNAME, user = USERNAME, password = PASSWORD, dbname = DATABASE)
cursor = connection.cursor()
     
class Menu:

    def __init__(self,player_name, date_of_birth, country_of_birth, team,matches_played, goals,trophies):
        self.player_name = player_name
        self.date_of_birth = date_of_birth
        self.country_of_birth = country_of_birth
        self.team = team
        self.matches_played = matches_played
        self.goals = goals
        self.trophies = trophies

    def add(self):
        add = input("enter order with comas and semicolon:")
        q1 = f"INSERT INTO football(player_name, date_of_birth, country_of_birth, team, matches_played, goals, trophies) values ({add});" 
        cursor.execute(q1) 
        connection.commit() 
        connection.close()
        print(f'{add} has been added!')

    def remove(self):
        remove = input("enter name of player you want to remove:")
        q2 = f"DELETE FROM football WHERE player_name like '{remove}';"
        cursor.execute(q2) 
        connection.commit() 
        connection.close()
        print(f'{remove} has been removed!')

    def edit(self):
        edit = input("enter your edit:")
        edit2 = input("enter what you want to edit:")
        q3 = f"UPDATE football SET {edit} WHERE {edit2};"
        cursor.execute(q3) 
        connection.commit() 
        connection.close()
        print(f'{edit} has been edited!')

    def list(self):
          q4 = "SELECT * from football;" 
          cursor.execute(q4) 
          results = cursor.fetchall() 
          print(f'here you have all the list:{results}')
          connection.close()

    def search(self):
          search = input("enter your search:")
          q5 = f"SELECT player_name, team from football WHERE player_name ilike '%{search}%'; ;" 
          cursor.execute(q5) 
          results = cursor.fetchall() 
          if results == []:
            again = input('sorry no result would you like to try again?')
            if again == 'yes':
                item.search()
            else:
                print('goodbye')
          else:
            print(results)
            connection.close()

    def pick(self):
        answer = input('choose what you want to do:\n 1.search\n 2.add\n 3.edit\n 4.remove\n 5.list\n enter:')
        if answer == 'search':
            item.search()
        if answer == 'add':
             item.add()
        if answer == 'edit':
            item.edit()
        if answer == 'remove':
            item.remove()
        if answer == 'list':
            item.list()
        else:
            print('goodbye')

item = Menu('harry kane','1993-07-28','england','tottenham',409,261,0)
item.pick()
