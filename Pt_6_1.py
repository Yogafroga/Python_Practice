from bs4 import BeautifulSoup as Soup
import requests
import csv
url = input("Enter a link to your favourite artist on Genius.com: ")
try:
    response = requests.get(url)
    print(response)
    bs = Soup(response.text, "lxml")
    popular_songs = bs.findAll('div', 'mini_card-title')

    with open('popular_songs.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Popular Songs'])

        for song in popular_songs:
            writer.writerow([song.text])
            print(song.text)

except requests.exceptions.HTTPError:
    print("HTTP Error occurred. Please check the URL.")

except requests.exceptions.ConnectionError:
    print("Connection Error. Please check your internet connection.")

except requests.exceptions.Timeout:
    print("Timeout Error occurred. The request took too long to respond.")

except requests.exceptions.RequestException:
    print("An error occurred while making the request.")
