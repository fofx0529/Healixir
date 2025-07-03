from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from typing import Any, Dict

# �Ыذ�¦��
Base = declarative_base()

class BaseModel(Base):
    """
    �Ҧ��ҫ�����¦��
    ���Ѧ@�P����k�A���]�t�B�~���
    �]���{����Ʈw���c�w�g�T�w
    """
    __abstract__ = True
    
    def to_dict(self) -> Dict[str, Any]:
        """
        �N�ҫ��ഫ���r��
        ��K�ǦC�ƩMAPI�^��
        """
        result = {}
        for column in self.__table__.columns:
            value = getattr(self, column.name)
            # �B�z����ɶ��榡
            if isinstance(value, datetime):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
        return result
    
    def update_from_dict(self, data: Dict[str, Any]) -> None:
        """
        �q�r���s�ҫ��ݩ�
        �Ω��s�ާ@
        """
        for key, value in data.items():
            if hasattr(self, key) and key != 'email':  # �����\��s�D��email
                setattr(self, key, value)
    
    def __repr__(self) -> str:
        """
        �ҫ����r����
        ��K����
        """
        class_name = self.__class__.__name__
        # �ϥ�email�@���ѧO�š]�]�����O�D��^
        email = getattr(self, 'email', 'unknown')
        return f"<{class_name}(email={email})>"