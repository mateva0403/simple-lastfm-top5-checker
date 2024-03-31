import requests

API_KEY = 'INSERTAPIKEYHERE'

def get_top_artists(username, period='1month', limit=5):
    url = f'http://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user={username}&api_key={API_KEY}&format=json&period={period}&limit={limit}'
    response = requests.get(url)
    data = response.json()
    return [artist['name'] for artist in data['topartists']['artist']]

def check_artists(top_artists, index_artists):
    found_artists = [artist for artist in top_artists if artist in index_artists]
    return found_artists, bool(found_artists)

def read_file_lines(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

def main():
    index_artists = set(read_file_lines('index.txt'))
    users = read_file_lines('users.txt')
    results = []

    for user in users:
        top_artists = get_top_artists(user)
        found_artists, has_artist = check_artists(top_artists, index_artists)
        artist_string = ', '.join(found_artists) if found_artists else 'None'
        result = f"{user}, {has_artist}, {artist_string}"
        results.append(result)
    
    with open('output.txt', 'w') as file:
        for result in results:
            file.write(result + '\n')

if __name__ == "__main__":
    main()
