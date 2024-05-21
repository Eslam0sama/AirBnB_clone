from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self, *args, **kwargs) -> None:
        
        if kwargs:
            for key , value in kwargs.item():
                if key  != "__class__":
                    setattr(self, key, value)        
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        if hasattr(self, 'created_at'):
            self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        if hasattr(self, 'updated_at'):
            self.updated_at = datetime.strptime(self.updated_at, '%Y-%m-%dT%H:%M:%S.%f')


    def __str__(self) -> str:

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        
        self.updated_at = datetime.isoformat(datetime.now())


    def to_dict(self):

        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = datetime.isoformat(self.created_at)
        self.__dict__['updated_at'] = datetime.isoformat(self.updated_at)
        return self.__dict__
