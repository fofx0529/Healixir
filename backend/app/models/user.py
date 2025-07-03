from sqlalchemy import Column, String, Date, Enum as SQLEnum
from sqlalchemy.orm import relationship
import enum

# �`�N�G�o�̤��A�~�� BaseModel�A�]���ڭ̨ϥ� email �@���D��
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenderEnum(str, enum.Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"  # �i��G�K�[��L�ʧO�ﶵ

class User(Base):
    __tablename__ = "users"
    
    # email �@���D��
    email = Column(String, primary_key=True, index=True, nullable=False)
    password = Column(String, nullable=False)  # �אּ password
    name = Column(String, nullable=True)
    gender = Column(SQLEnum(GenderEnum), nullable=True)
    birth_date = Column(Date, nullable=True)
    phone = Column(String, nullable=True)  # �s�W phone ���
    
    # �����o�����G
    # hashed_password (�אּ password)
    # is_active (�w�R��)
    # is_verified (�w�R��)
    # id (email �{�b�O�D��)
    # created_at (�w�R��)
    # updated_at (�w�R��)
    
    # ���p���Y�]�p�G�ݭn���ܡ^
    # orders = relationship("Order", back_populates="user")
    # reviews = relationship("Review", back_populates="user")
    
    def __repr__(self):
        return f"<User(email='{self.email}', name='{self.name}')>"