import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
import os

MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = os.environ.get('PASSWORD')
AMAZON_URL = "https://www.amazon.in/ASUS-Vivobook-Windows-Backlit-M1603QA-MB712WS/dp/B0BH6QPVVF/ref=asc_df_B0BH6QPVVF/?tag=googleshopdes-21&linkCode=df0&hvadid=619722637671&hvpos=&hvnetw=g&hvrand=18231354447265701744&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007788&hvtargid=pla-1915864937426&psc=1"

response = requests.get(url=AMAZON_URL)
print(response.status_code)

soup = BeautifulSoup(response.text, parser="lxml")

price_whole = soup.find("span", class_="a-price-whole").get_text().split(",")
digit1 = price_whole[0]
digit1 += price_whole[1].split(".")[0]

final_price = int("".join(digit1))
print(final_price)

if final_price < 57000:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="abhishekbiradar0207@gmail.com",
            msg=f"Subject:Price Alert for 'Asus Vivobook 16X'\n\n"
                f"The current price of product is {final_price}."
                f"{AMAZON_URL}"
        )



