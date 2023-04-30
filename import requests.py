import requests
from bs4 import BeautifulSoup

url = "https://medium.com/free-code-camp/the-rise-of-the-data-engineer-91be18f1e603"

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the article heading
heading = soup.find('h1').text.strip()

# Find all the paragraphs in the article
paragraphs = soup.find_all('p')

# Loop through each paragraph and print its text
for paragraph in paragraphs:
    print(paragraph.text)
