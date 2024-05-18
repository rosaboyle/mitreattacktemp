import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url):
    if url == "https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/":
        with open("link1.html", "r") as f:
            text = f.read()
            
    elif url == "https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/":
        with open("link2.html", "r") as f:
            text = f.read()
    else:
        response = requests.get(url)
        text = response.content
    soup = BeautifulSoup(text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])
    return text
#  Might potentially use Javascript Engine to run if required. If prerendered then not required.
urls = [
    "https://www.microsoft.com/en-us/security/blog/2023/08/02/midnight-blizzard-conducts-targeted-social-engineering-over-microsoft-teams/",
    "https://www.microsoft.com/en-us/security/blog/2024/01/25/midnight-blizzard-guidance-for-responders-on-nation-state-attack/",
    "https://www.fortinet.com/blog/threat-research/teamcity-intrusion-saga-apt29-suspected-exploiting-cve-2023-42793",
    "https://www.mandiant.com/resources/blog/apt29-wineloader-german-political-parties",
    "https://cloud.google.com/blog/topics/threat-intelligence/apt29-evolving-diplomatic-phishing/"
]

texts = [extract_text_from_url(url) for url in urls]
print(texts)

