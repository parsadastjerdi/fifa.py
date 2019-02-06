from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# Returns the title of a webpage, returns None if the title doesn't exist
def get_title(url):
    # If HTTP 404 Error occurs
    try:
        html = urlopen(url)

        # If the server is not found or the url is mistyped
        if html is None:
            print("Server not found or URL mistyped: " + url)
            return None

    except HTTPError:
        print("HTTP Error for URL: " + url)
        return None
    
    # If trying to access a tag that does not exist
    try:
        soup = BeautifulSoup(html.read())
        title = soup.body.h1
    except AttributeError:
        print("Attribute Error for url: " + url)
        return None 

    return title


def get_names(url):
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
    soup = BeautifulSoup(html)
    nameList = soup.findAll("span", {"class" : "green"}) 
    for name in nameList:
        print(name.get_text())


if __name__ == "__main__":
    title = get_title("http://pythonscraping.com/pages/page1.html")

    # If the server was not found, urlopen returns a None object
    if title is None:
        print("Title could not be found")
    else:
        print(title)
