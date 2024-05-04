import requests
from bs4 import BeautifulSoup as bs


def scrape_image():
    # prompt user for github username
    github_user = input("Enter Username:")
    #
    github_url = "https://github.com/"
    # construct url to fetch from
    full_url = f"{github_url}{github_user}"

    # print("one:", github_url)
    # print("two:", full_url)

    request = requests.get(full_url)
    soup = bs(request.content, "html.parser")
    profile_image = soup.find("img")["src"]
    print(profile_image)


if __name__ == "__main__":
    scrape_image()
