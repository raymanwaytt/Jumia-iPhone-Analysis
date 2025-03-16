from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pandas as pd
import osZZZZZS

# Ensure the data folder exists
os.makedirs("data", exist_ok=True)

base_url = "https://www.jumia.com.ng/"
current_page = 'ios-phones/apple/#catalog-listing'

iphone_data = []

while current_page:
    url = base_url + current_page  # Full URL of the page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all phone details on the current page
    phone_catalog = soup.find_all('article', {'class': 'prd'})

    # Extract phone details
    for phone in phone_catalog:
        name = phone.find('h3').text.strip()
        price = phone.find('div', {'class':'prc'}).text.strip()
        link = phone.find("a", class_="core")["href"]
        link = base_url + link
        image = phone.find('img').get('data-src')

        # Store the extracted data
        iphone_data.append({
            "Name": name,
            "Price": price,
            "Link": link,
            "Image": image,
            "Date": datetime.now().strftime("%Y-%m-%d")
        })

    print(f'Extracted {len(iphone_data)} phones so far...')

    # Find next page, if it exists
    next_page = soup.find('a', {'aria-label': 'Next Page'})
    current_page = next_page.get('href') if next_page else None

print(f'Final extracted total: {len(iphone_data)} phones')

file_path = 'data/iphone_data.csv'
df = pd.DataFrame(iphone_data)
df.to_csv(file_path, index=False)

# # append to csv file
# existing_df = pd.read_csv('data/iphone_data.csv')
# df = pd.DataFrame(iphone_data)
# df = pd.concat([existing_df, df])
# df.to_csv('data/iphone_data.csv', index=False)

# file_path = 'data/iphone_data.csv'
# df = pd.DataFrame(iphone_data)
# try:
#     existing_df = pd.read_csv(file_path)
#     df = pd.concat([existing_df, df])
# except FileNotFoundError:
#     print("No existing CSV—creating new one")
# df.to_csv(file_path, index=False)


print(f'Data saved to {file_path}')