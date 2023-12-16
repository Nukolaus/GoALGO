from abc import ABC, abstractclassmethod, abstractmethod
from pydantic import BaseModel


class AbstractRepository(ABC):
    @abstractmethod
    def add(self, obj: BaseModel) -> BaseModel:
        ...

    @abstractmethod
    def get(self, **kwargs) -> BaseModel:
        ...

    @abstractmethod
    def delete(self, obj: BaseModel) -> None:
        ...

    @abstractmethod
    def update(self, obj: BaseModel) -> BaseModel:
        ...

    @abstractmethod
    def get_all(self, **kwargs) -> list:
        ...
