#importamos desde fastAPI, la clases FastAPI y Response
from typing import Union
from pydantic import BaseModel

# Modelo para la inserción de nuevos nombres
class Persona(BaseModel):
