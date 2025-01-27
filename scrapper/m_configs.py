GET_NEXT_BUTTON_SCRIPT = "return document.querySelector('[data-testid=pagination-next-button] > button')"

# ask for a keyword input (default is nintendo) with error checking

while True:
    keyword = input("Introducir palabra clave a buscar (ej.: nintendo): ")
    if keyword == "":
        keyword = "nintendo"
        break
    else:
        break

# assign the keyword to MERCAIR_IT_BOOK_URL

MERCARI_IT_BOOK_URL = "https://jp.mercari.com/search?keyword=" + keyword

# get a number input of quantity of products with error checks and default value of 10

QUANTITY = 10

while True:
    try:
        QUANTITY = int(input("Cuántos productos quieres obtener? (ej.: 10): "))
        if QUANTITY < 1:
            print("Por favor, introducir un número mayor a 0!!!")
            continue
    except ValueError:
        print("Por favor, introducir un número y no letra!!!")
        continue
    else:
        break

PRODUCT_CATEGORY = ''

# ask for a product category input (default is Consolas y videojuegos>Consolas y videojuegos) with error checking

while True:
    PRODUCT_CATEGORY = input("Introducir categoría de producto (ej.: Consolas y videojuegos>Nintendo): ")
    if PRODUCT_CATEGORY == "":
        PRODUCT_CATEGORY = 'Consolas y videojuegos>Nintendo'
        break
    else:
        break

# ask for a translation dest language input (default is en) with error checking

while True:
    trans_lang = input("Introducir lenguaje de destino de traducción (ej.: en, es, de, ...): ")
    if trans_lang == "":
        trans_lang = 'en'
        break
    else:
        break


MERCARI_DEFAULT_URL = "https://jp.mercari.com"

GET_ITEM_NAME = "return document.querySelector('#item-info > section:nth-child(1) > div > mer-heading').shadowRoot.querySelector('div > div > h1').textContent"
GET_ITEM_NAMEV2 = "return document.querySelector('div[data-testid=\"name\"] h1').innerText.trim()"

GET_ITEM_PRICE = "return document.querySelector('mer-price').shadowRoot.querySelector('span:nth-of-type(2)').textContent"
GET_ITEM_PRICEV2 = "return document.querySelector('div[data-testid=\"price\"] span:not(.currency)').innerText"


"""
xpath=//div[@id='item-info']/section[2]
"""
GET_ITEM_DESCRIPTION = "return document.querySelector('#item-info > section:nth-child(2)').textContent"
GET_ITEM_DESCRIPTIONV2 = "document.querySelector('mer-text[data-testid=\"description\"]').innerText.trim()"

#xpath=//main[@id='main']/article/div/section/div/div/div/div/div/div/div/div/div/div/div/div/mer-item-thumbnail (check if mer-item-thumbnail has sticker="sold" attribute)
GET_ITEM_SOLD = "return document.querySelector('#main > article > div:nth-child(1) > section > div > div > div > div > div > div > div > div > div > div > div > div > mer-item-thumbnail').getAttribute('sticker')"
#GET_ITEM_SOLD = "document.querySelector('div[role=\"img\"] mer-item-thumbnail[sticker=\"sold\"]')"

