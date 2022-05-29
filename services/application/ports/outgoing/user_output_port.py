# RG Libraries
from services.adapters.user.i_user_adapter import IUserAdapter
from services.application.domain.models.user import User
from services.application.ports.outgoing.i_user_output_port import IUserOutputPort


class UserOutputPort(IUserOutputPort):
    def __init__(self, adapter: IUserAdapter):
        self.__adapter = adapter

    def save(self, user: User) -> bool:
        return self.__adapter.save(user)
