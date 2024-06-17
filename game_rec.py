from data import genres

def search_games(genre_name, game_name):
    genres_dict = genres()

    if genre_name not in genres_dict:
        return f"Genre '{genre_name}' not found."

    games_list = genres_dict[genre_name]()
    
    for game in games_list:
        if game["name"].lower() == game_name.lower():
            return f"Game found: {game}"

    return f"Game '{game_name}' not found in genre '{genre_name}'."

if __name__ == "__main__":
    genre_input = input("Enter genre: ").strip().lower()
    game_input = input("Enter game name: ").strip().lower()

    result = search_games(genre_input, game_input)
    print(result)