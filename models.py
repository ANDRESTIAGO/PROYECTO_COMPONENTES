
from typing import Optional
from pydantic import BaseModel, Field

class Distribuidores(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    direccion: str = Field(..., min_length=2, max_length=50)
    
class Componente(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    tipo: str = Field(..., min_length=2, max_length=30)
    marca: str = Field(..., min_length=2, max_length=30)
    modelo: str = Field(..., min_length=2, max_length=30)

class ComponenteConId(Componente):
    id: int

class DistriConId(Distribuidores):
    id: int

class ComponenteActualizado(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    tipo: Optional[str] = Field(None, min_length=2, max_length=30)
    marca: Optional[str] = Field(None, min_length=2, max_length=30)
    modelo: Optional[str] = Field(None, min_length=2, max_length=30)

class DistriActualizado(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    direccion: Optional[str] = Field(None, min_length=2, max_length=30)