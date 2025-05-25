from tools.welcome_libs import welcome_message
from games.goa_main_game import main_game_struture, exit_program
from games.warungmini import warung_mini_main

def options():
    user_option = input(f'Pilih Permainan\n1.Games Cuy \n2.Warung Mini\n: ')
    return user_option

def options_game ():
    user_option = int (options())
    if user_option == 1:
            main_game_struture()
    elif user_option == 2:
            warung_mini_main()
    else:
        print("Hanya boleh tersedia di program ")
        exit_program()

def main () :
    welcome_message()
    print('\n')
    options_game()
    main_game_struture()
    exit_program()

if __name__ == '__main__':
    main() 
