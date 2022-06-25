import requests
from bs4 import BeautifulSoup

def contents_to_title(contents):
    return [txt.strip() for txt in contents]

def main():
    resp = requests.get("https://www.bloomberg.co.jp/")
    soup = BeautifulSoup(resp.text, 'html.parser')
    titles = []
    for tag in soup.find_all("a"):
        if "class" in tag.attrs.keys():
            if("hero-module__related-story-link" in tag["class"] or "hero-module__headline-link" in tag["class"] or "story-list-story__info__headline-link" in tag["class"]):
                titles.extend(contents_to_title(tag.contents))
    print(titles)


if __name__ == "__main__":
    main()
