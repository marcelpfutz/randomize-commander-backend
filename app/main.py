from .services import scryfall_service as scryfall
from .services import ehdrec_service as ehdrec
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Configurar origens permitidas baseado no ambiente
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
if ENVIRONMENT == "production":
    # Em produção, permitir apenas o domínio do frontend
    # Você pode definir isso via variável de ambiente ALLOWED_ORIGINS
    allowed_origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
else:
    # Em desenvolvimento, permitir localhost
    allowed_origins = ["http://localhost:4200", "http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "API rodando"}

@app.get("/api/commander")
async def get_commander():
    tags = []
    commander = scryfall.randomize_commander()
    ehdrec_data = ehdrec.get_edh_data(commander.get('formated-name'))

    for item in ehdrec_data:
        tags.append({"label": item[0], "link": item[1]})

    
    return {
        "image": commander.get('scryfall')['image_uris']['normal'],
        "title": commander.get('scryfall')['name'],
        "description": commander.get('scryfall')['oracle_text'],
        "tags": tags
    }







