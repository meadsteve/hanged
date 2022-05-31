# Standard Python Libraries
from abc import ABCMeta, abstractmethod

# RG Libraries
from services.application.domain.models.user import User


class IUserAdapter(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def list(self) -> list:
        raise NotImplementedError()
