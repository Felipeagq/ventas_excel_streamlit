# importar las librerias
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Crear el modelo de mi tabla 
Base = declarative_base()

# creando la tabla
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    
    def __repr__(self):
        return f" username:{self.username} - password:{self.password}"

# motor de base de datos
engine = create_engine(
    "sqlite:///database.db", # Postgrest, mysql, mariadb
    echo=True
)
# sessiones a base de datos
SessionLocal = sessionmaker(bind=engine)

# Crear la base de datos como tal "fisicamente"
Base.metadata.create_all(engine)


def crear_user(user:str , passw:int):
    """
    Es una función para crear un registro en la base de datos 
    
    Args:
    - user : str = es el usuario 
    - passw : str = es la contraseña
    """
    session = SessionLocal()
    usuario = Usuario(
        username=user,
        password=passw
    )
    session.add(usuario)
    session.commit()
    session.close()
    return usuario

def obtener_usuario():
    session = SessionLocal()
    usuarios = session.query(Usuario).all()
    session.close()
    return usuarios

def obtener_usuario_id(id_usuario):
    session = SessionLocal()
    usuario = session.query(Usuario).filter_by(id=id_usuario).first()
    session.close()
    return usuario

def actualizar_usuario(id_usuario,nuevo_nombre,nueva_password):
    session = SessionLocal()
    usuarios = session.query(Usuario).filter_by(id=id_usuario).first()
    if usuarios:
        usuarios.username = nuevo_nombre
        usuarios.password = nueva_password
        session.commit()
    session.close()
    return usuarios

def eliminar_usuario(id_usuario):
    session = SessionLocal()
    usuarios = session.query(Usuario).filter_by(id=id_usuario).first()
    if usuarios:
        session.delete(usuarios)
        session.commit()
    session.close()
    return usuarios