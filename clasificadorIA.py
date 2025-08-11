import argparse
import requests
import os

def clasificar_servicio_cloud_openrouter(texto):
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("ERROR: La variable de entorno OPENROUTER_API_KEY no está definida.")

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Cloud Model Classifier"
    }

    prompt = f"""
Clasifica el siguiente texto en una de estas categorías de servicio en la nube:
IaaS, PaaS, SaaS o FaaS.

Texto: "{texto}"

Responde solo con la categoría.
"""

    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [
            {"role": "system", "content": "Eres un experto en computación en la nube."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print("❌ Error:", response.status_code, response.text)
        response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Clasificador IaaS/PaaS/SaaS/FaaS usando modelo free de OpenRouter.")
    parser.add_argument('--texto', type=str, required=True, help='Texto a clasificar')
    args = parser.parse_args()

    result = clasificar_servicio_cloud_openrouter(args.texto)
    print(f"Clasificación: {result}")