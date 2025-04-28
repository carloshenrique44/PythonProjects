from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String(25), unique=True)
    email=Column(String(80), unique=True)
    password=Column(Text, nullable=True)
    is_staff=Column(Boolean, default=False)
    is_active=Column(Boolean, default=False)
    
    orders = relationship('Order', back_populates='user')
    
    def __repr__(self):
        return f"<User {self.username}>"
    
class Order(Base):
    
    ORDER__STATUSES = (
        ('Pendente', 'Pendente'),
        ('Em-Transito', 'Em-Transito'),
        ('Aprovado', 'Aprovado'),
        ('Entregue', 'Entregue'),
        ('Cancelado', 'Cancelado')
        
    )
    
    PIZZA_SIZES = (
        ('Pequena', 'pequena'),
        ('Media', 'media'),
        ('Grande', 'grande'),
        ('Extra-Grande', 'extra-grande')
    )
    __tablename__ = 'orders'
    
    id=Column(Integer, primary_key=True, index=True)
    quantity=Column(Integer, nullable=False)
    
    order_status=Column(ChoiceType(choices=ORDER__STATUSES), default='Pendente')
    pizza_size=Column(ChoiceType(choices=PIZZA_SIZES), default='Pequena')
    
    user_id=Column(Integer, ForeignKey('user.id'))
    user=relationship('User', back_populates='orders')
    
    def __repr__(self):
        return f"<Order {self.id}>"

    