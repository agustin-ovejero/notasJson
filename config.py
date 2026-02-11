# Usamos una clase para tener todas la uris mas ordenadas
class Config:
   SQLALCHEMY_DATABASE_URI = "sqlite:///notasjson.db" # Las config tienen que estar todas en mayusculas y cumpliendo el estandar de flask