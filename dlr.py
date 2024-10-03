import requests

def download_game_page():
    # URL to download
    url = 'https://funhtml5games.com/mariofps/index.html'
    
    # Spoofed referer URL
    headers = {
        'Referer': 'https://funhtml5games.com/mariofps'
    }
    
    try:
        # Make the request with the spoofed referer
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Save the content to a file
            with open('donkeykong.html', 'w', encoding='utf-8') as file:
                file.write(response.text)
            print("Page downloaded successfully!")
        else:
            print(f"Failed to download the page. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    download_game_page()
