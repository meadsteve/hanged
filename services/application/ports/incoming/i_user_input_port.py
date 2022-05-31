# Standard Python Libraries
from abc import ABCMeta, abstractmethod

# Third-Party Libraries
from reactivex import Observable

# RG Libraries
from services.application.domain.models.user import User
from services.application.shared.status import Status


class IUserInputPort(metaclass=ABCMeta):
    @abstractmethod
    def create_user(self, event, contex) -> Observable[Status]:
        raise NotImplementedError()

    @abstractmethod
    def user_list(self, event, contex) -> list:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_body_data(event_payload: dict) -> dict:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_users_raw_data(body_data: dict) -> dict:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def data_to_user_instance(body_data: dict) -> User:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def generate_status(save_response: bool) -> Status:
        raise NotImplementedError()
