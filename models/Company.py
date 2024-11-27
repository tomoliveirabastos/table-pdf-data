from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, Column, String

class Base(DeclarativeBase):
    pass

class Company(Base):
    __tablename__ = "Company"
    id = Column(Integer, primary_key=True)
    razao_social = Column(String(255), nullable=True)
    nm_fantasia = Column(String(255), nullable=True)
    cd_cnpj = Column(String(255), nullable=True, index=True)
    cidade = Column(String(255), nullable=True)
    bairro = Column(String(255), nullable=True)
    cep = Column(String(255), nullable=True)
    uf = Column(String(255), nullable=True)
    numero = Column(String(255), nullable=True)

    def __init__(self, setor_amigavel, cd_ativ_econ_primaria, visible, logo, razao_social, cd_cnpj, nm_fantasia, cep, logradouro, numero, bairro, cidade, uf, nm_ativ_econ_primaria):
        self.logo = logo
        self.visible = visible
        self.cd_ativ_econ_primaria = cd_ativ_econ_primaria
        self.setor_amigavel = setor_amigavel
        self.razao_social = razao_social
        self.cd_cnpj = cd_cnpj
        self.nm_fantasia = nm_fantasia
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.uf = uf
        self.nm_ativ_econ_primaria = nm_ativ_econ_primaria