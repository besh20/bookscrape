import requests
import time
from bs4 import BeautifulSoup

bot_token = '6969736991:AAEZX4HB2Jv_fMVlt12A7cpRQWdduft2qQc'
Channel_username = '@projectpy'
url = 'https://www.ethiobookreview.com/amharic'

def scrape():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    books = []
    items = soup.find_all("div", class_="product")
    for item in items:

        image = item.find("img")["src"] if item.find("img") else "Image not found" 
        author_tag = item.find("h5")
        author = author_tag.text.strip() if author_tag else "Author not found"  
        genre_tag = item.find("h6")
        genre = genre_tag.text.strip() if genre_tag else "genre not found" 
        price_tag = item.find("h5", style="color:red; padding-top:5px;")
        price = price_tag.text.strip() if price_tag else "Price not found"

        books.append({
            "Image": image,
            "Author": author,
            "genre": genre,
            "Price": price
        })  
    return books
    
def tele(message):
    send_message_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": Channel_username,
        "text": message,
        "parse_mode": "HTML"
    }
    response = requests.post(send_message_url, data=data)
    if response.status_code != 200:
        print("Failed to send message to Telegram channel.")

in_books = scrape()
for book in in_books:
    mess = f"<b>Author:</b> {book['Author']}\n"
    mess += f"<b>Genre:</b> {book['genre']}\n"
    mess += f"<b>Price:</b> {book['Price']}\n"
    mess += f"<b>Image:</b> {book['Image']}"
    tele(mess)
    time.sleep(10)


# A function used to Choose which information to send to the Telegram channel
# for book in in_books:
#     info_to_send = 'Author'  # Change this to 'genre' or 'Price' or 'image' as needed
#     if info_to_send not in book:
#         print(f"Error: Key '{info_to_send}' not found in book dictionary.")
#         continue
#     mess = f"<b>{info_to_send}:</b> {book[info_to_send]}"
#     tele()
#     time.sleep(10)



