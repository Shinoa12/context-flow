import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"
UNUSUAL_ARTICLES_URL = "https://en.wikipedia.org/wiki/Wikipedia:Unusual_articles"

def get_unusual_articles_urls():
    try:
        # Realizar la solicitud HTTP a la página de Wikipedia
        response = requests.get(UNUSUAL_ARTICLES_URL)
        response.raise_for_status()

        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar todas las tablas con la clase 'wikitable'
        tables = soup.find_all("table", class_="wikitable")

        # Extraer URLs solo de los enlaces en estas tablas
        urls = []
        for table in tables:
            links = table.select("a[href^='/wiki/']")
            for link in links:
                href = link.get("href")
                # Excluir enlaces internos o especiales
                if not any(x in href for x in [":", "#"]):  
                    full_url = BASE_URL + href
                    urls.append(full_url)
                
                if len(urls) == 50:
                    break
        
        # Eliminar duplicados manteniendo el orden
        urls = list(dict.fromkeys(urls))
        
        print(f"✅ Se han recopilado {len(urls)} URLs de artículos inusuales.")
        return urls
    except requests.RequestException as e:
        print(f"❌ Error al solicitar la página: {e}")
        return []

def get_article_content(url):
    try:
        # Realizar la solicitud HTTP a la página de Wikipedia
        response = requests.get(url)
        response.raise_for_status()

        # Parsear el HTML con BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Encontrar el título y el contenido del artículo
        title = soup.find("h1", {"id": "firstHeading"}).text
        content_div = soup.find("div", {"class": "mw-body-content"})
        paragraphs = content_div.find_all("p")
        print(paragraphs)
        content = " ".join([p.text for p in paragraphs if p.text.strip()])
        return {
            "title": title, 
            "content": content, 
            "url": url
            }
    
    except requests.RequestException as e:
        print(f"❌ Error al solicitar la página: {e}")