import bs4, requests

def getAmazonPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    return elems[0].text.strip()





price = getAmazonPrice('http://www.amazon.co.uk/gp/product/B00XRFB9PA?colid=1OP7SGZK1ODJS&coliid=I28LECOJQYWJ1T&redirect=true&ref_=s9_wish_gw_d36_g201_i1')
print('The Price is ' + price)
