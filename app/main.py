from .services import scryfall_service as scryfall
from .services import ehdrec_service as ehdrec
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],  # Portas frontend/backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/item")
async def get_item():
    # Exemplo: use serviço para dados (retorne dict simulado ou real)
    commander = scryfall.randomize_commander()
    ehdrec_data = ehdrec.get_edh_data(commander.get('formated-name'))
    print(ehdrec_data)
    # print(commander.get('scryfall')['image_uris']['normal'])
    return {
        "image": commander.get('scryfall')['image_uris']['normal'],
        "title": commander.get('scryfall')['name'],
        "description": commander.get('scryfall')['oracle_text'],
    }

# commander = scryfall.randomize_commander()
# print(f'Randomized commander: {commander.get('Original-Name')}\n')
# data = ehdrec.get_edh_data(commander.get('Formated-Name'))

# print('Tags e Links:')
# for item in data:
#     print(f'{item[0]}: {item[1]}')
#     print('-----')  






