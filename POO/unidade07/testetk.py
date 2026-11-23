import urllib.request
import json

cnpj = "08241739000105"
url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj}"

req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"}
)

with urllib.request.urlopen(req, timeout=10) as r:
    dados = json.loads(r.read().decode("utf-8"))

print(dados["razao_social"])
print(dados["nome_fantasia"])
print(dados["municipio"], dados["uf"])