import requests
from bs4 import BeautifulSoup as bs


def scrape_image():
    github_user = input("Enter User Handle:")
    github_url = "https://github.com/"
    full_url = f"{github_url}{github_user}"

    print("one:", github_url)
    print("two:", full_url)

    request = requests.get(full_url)
    soup = bs(request.content, "html.parser")
    profile_image = soup.find("img")["src"]
    print(profile_image)


if __name__ == "__main__":
    scrape_image()
