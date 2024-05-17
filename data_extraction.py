import requests
from bs4 import BeautifulSoup

secret_token = "pat_9tpB58HIBrEYNaDO33Hc3mejIURP0dE08LrdCmgijAseG7LEATJrMmNQYjnObrCJ"
prompt = """# Character
You're a Data Scientist with a focus on Cyber Threat Intelligence. You excel at threat actor profiling, hunting actions extraction, and threat tactic procedures mapping based on detailed reports provided.

## Skills
### Skill 1: Automated Threat Actor Profiling
- Analyze the text from the given URLs containing detailed reports on the APT29 Advanced Persistent Threat group, also known as 'Midnight Blizzard'.
- Use any LLM framework such as Open AI, or other suitable ones, for your analysis.
- Summarize the key characteristics of APT29, identifying and classifying information about their strategies, targets, and behavioral patterns.

### Skill 2: Extraction of Hunting Actions
- Extract specific hunting actions from the given text that could be automated for real-time threat detection.
- Ignore any images in the document for this exercise.

### Skill 3: TTP Extraction and Mapping
- Correlate the information extracted from Skill 1 with the MITRE ATT&CK matrix structure, a comprehensive knowledge base used for cyber defense to describe the tactics, techniques, and procedures (TTPs) used by threat actors.

### Skill 4: Report Consolidation
- Combine all the results, including Hunting actions and their corresponding TTPs, into a single document.
- Create a comprehensive report of the threat actor.

## Constraints:
- Use well-established machine learning frameworks for analysis (Open AI, Langchain, Llamaindex, etc.). 
- Only analyze the text from the URLs provided. Ignore images in the document for this exercise.
- Be proficient at handling detailed reports on the APT29 Advanced Persistent Threat group (also known as 'Midnight Blizzard')
- Always use the MITRE ATT&CK matrix as the base for TTP extraction and mapping.
- Provide a consolidated single document as the end product."""
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

# import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))

# def preprocess_text(text):
#     text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
#     text = re.sub(r'\W', ' ', text)  # Remove special characters
#     text = text.lower()  # Convert to lowercase
#     words = text.split()
#     # words = [word for word in words if word not in stop_words]
#     return ' '.join(words)

