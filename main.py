import requests
import json
import math

url = "https://employability-portal.gupy.io/api/v1/jobs?"

params = {"jobName": "dados"}
response = requests.get(url, params = params)

data = response.json()

print("data:", data)

pagination = data.get("pagination", {})

total = pagination.get("total", 0)
limit = pagination.get("limit", 0)
offset = pagination.get("offset", 0)

total_posicoes = total / limit
# if total_posicoes % 1 != 0:
#     total_posicoes = int(total_posicoes) + 1

total_offset = math.ceil(total_posicoes)

print("total:", total)
print("limit:", limit)
print("offset:", offset)
print("total_posicoes:", total_posicoes)
print("total_offset:", total_offset)

resultados_offsets = []

for offset_atual in range(0, total_offset):
    params["offset"] = offset_atual

    response = requests.get(url, params=params)
    data_offset = response.json()
    print("data_offset:", data_offset)
    resultados_offsets.append(data_offset)


with open("resultado_api_docker.json", "w", encoding="utf-8") as arquivo:
    json.dump(
        resultados_offsets,
        arquivo,
        ensure_ascii=False,
        indent=4
    )