from sqlalchemy import Column, ForeignKey, Float, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True)
    symbol = Column(String(5), nullable=False)
    currency = Column(String(3), nullable=False)
    name = Column(String(50), nullable=True)
    country = Column(String(20), nullable=True)


class PriceMinute(Base):
    __tablename__ = "priceminute"
    time = Column(DateTime, nullable=False, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship(Stock)
    open = Column(Float(precision=16))
    close = Column(Float(precision=16))
    high = Column(Float(precision=16))
    low = Column(Float(precision=16))
    volume = Column(Float(precision=16))


class PriceDay(Base):
    __tablename__ = "priceday"
    time = Column(DateTime, nullable=False, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship(Stock)
    open = Column(Float(precision=16))
    close = Column(Float(precision=16))
    high = Column(Float(precision=16))
    low = Column(Float(precision=16))
    volume = Column(Float(precision=16))


# def create_tables():
#     engine = create_engine(
#         "postgresql://a001080:@localhost/finalyze"
#         , echo=True, future=True
#     )
#     Base.metadata.create_all(engine)
