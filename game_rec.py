from data import genres

def display_games(genre_name):
    genres_dict = genres()
    
    if genre_name not in genres_dict:
        return None, f"Genre '{genre_name}' not found."
    
    games_list = genres_dict[genre_name]()
    
    if not games_list:
        return None, f"No games found in '{genre_name}' genre."
    
    return games_list, None

def get_game_details(genre_name, game_name):
    genres_dict = genres()
    
    genre_function = genres_dict.get(genre_name)
    if not genre_function:
        return None
    
    games_list = genre_function()
    
    for game in games_list:
        if game["name"].lower() == game_name.lower():
            return game
    
    return None

def main():
    def back():
        print("\nGoing back to the previous menu...\n")
        return True

    print("Welcome to the Game-Rec App!")

    while True:
        genre_input = input("Please enter a genre of your choosing to begin the program (or type 'exit' to quit): ").strip().lower()
        
        if genre_input == 'exit':
            print("Farewell!")
            break
        
        games, error = display_games(genre_input)
        
        if error:
            print(error)
            continue

        print(f"Top 5 games as per IGN and Steam rankings available in the {genre_input} genre:")
        for idx, game in enumerate(games, start=1):
            print(f"{idx}. {game['name']}")
        
        while True:
            game_choice = input("Please enter the name of the game you want more information about (or type 'back' to go back to the genre selection): ").strip().lower()
            
            if game_choice == 'back':
                if back():
                    break
            
            game_details = get_game_details(genre_input, game_choice)
            
            if game_details:
                print("\nGame Details:")
                print(f"Name: {game_details['name']}")
                print(f"Developer: {game_details['developer']}")
                print(f"Publisher: {game_details['publisher']}")
                print(f"Price: ${game_details['price']:.2f}")
            else:
                print(f"Game '{game_choice}' not found in genre '{genre_input}'.")

if __name__ == "__main__":
    main()