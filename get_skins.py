import os
import requests
from bs4 import BeautifulSoup
import sys


def get_skin_images(champion_name):
    # Create folder if it doesn't exist
    folder_path = f"skins/{champion_name}"
    os.makedirs(folder_path, exist_ok=True)

    # URL of the champion's cosmetics page
    url = f"https://leagueoflegends.fandom.com/wiki/{champion_name}/LoL/Cosmetics"

    # Send a GET request to the URL
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image elements
        img_elements = soup.find_all('div', class_='skin-icon')

        for img_elem in img_elements:
            link = img_elem.a['href']
            name = img_elem.a.img['data-image-name']
            # print('href: ' + link)
            # print('skin-name: ' + name)
            if link.startswith('https://'):
                img_path = f"{folder_path}/{name}"
                with open(img_path, 'wb') as f:
                    f.write(requests.get(link).content)
                print(f"Downloaded: {name}")
            else:
                print(f"Skipping: {name}")
    else:
        print("Failed to retrieve data.")


if __name__ == "__main__":
    champ_name = str(sys.argv[1])
    get_skin_images(champ_name)
