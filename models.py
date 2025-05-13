from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from typing import Optional

class Distribuidores(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    direccion: str = Field(..., min_length=2, max_length=50)
    class Config:
        orm_mode = True
        from_attributes = True
    
class Componente(BaseModel):
    nombre: str = Field(..., min_length=2, max_length=50)
    tipo: str = Field(..., min_length=2, max_length=30)
    marca: str = Field(..., min_length=2, max_length=30)
    modelo: str = Field(..., min_length=2, max_length=30)
    class Config:
        orm_mode = True
        from_attributes = True

class ComponenteConId(Componente):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class DistriConId(Distribuidores):
    id: int
    class Config:
        orm_mode = True
        from_attributes = True

class ComponenteActualizado(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    tipo: Optional[str] = Field(None, min_length=2, max_length=30)
    marca: Optional[str] = Field(None, min_length=2, max_length=30)
    modelo: Optional[str] = Field(None, min_length=2, max_length=30)
    class Config:
        orm_mode = True
        from_attributes = True

class DistriActualizado(BaseModel):
    nombre: Optional[str] = Field(None, min_length=2, max_length=50)
    direccion: Optional[str] = Field(None, min_length=2, max_length=30)
    class Config:
        orm_mode = True
        from_attributes = True

