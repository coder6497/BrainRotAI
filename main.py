from fastapi import FastAPI
from fusion_brain import FusionBrainApi
import os

app = FastAPI()

@app.get('/')
async def root():
    return {"message": 'BrainRotAI'}

@app.get('/generate/{prompt}')
async def generate(prompt: str):
    fusionbrainapi = FusionBrainApi("https://api-key.fusionbrain.ai/", os.getenv("API_KEY"), os.getenv("SECRET_KEY"))
    pipeline_id = fusionbrainapi.get_pipeline()
    uuid = fusionbrainapi.generate(prompt, pipeline_id)
    files = fusionbrainapi.check_generation(uuid)
    return {"result": files}