from sqlalchemy import Column, Integer, String, Float, Date
from application.database.base import Base

class Cessao_Fundo(Base):
    __tablename__ = 'cessao_fundo'

    ID_CESSAO = Column(Integer, primary_key=True)
    ORIGINADOR = Column(String(250))
    DOC_ORIGINADOR = Column(String(50))
    CEDENTE = Column(String(250))
    DOC_CEDENTE = Column(String(50))
    CCB = Column(Integer)
    ID_EXTERNO = Column(Integer)
    CLIENTE = Column(String(250))
    CPF_CNPJ = Column(String(50))
    ENDERECO = Column(String(250))
    CEP = Column(String(250))
    CIDADE = Column(String(250))
    UF = Column(String(50))
    VALOR_DO_EMPRESTIMO = Column(Float)
    VALOR_PARCELA = Column(Float)
    TOTAL_PARCELAS = Column(Float)
    PARCELA = Column(Integer)
    DATA_DE_EMISSAO = Column(Date)
    DATA_DE_VENCIMENTO = Column(Date)
    PRECO_DE_AQUISICAO = Column(Float)

    def __repr__(self):
        return f'cessao_fundo {self.id_cessao}'

    def create(engine):
        Base.metadata.create_all(engine)