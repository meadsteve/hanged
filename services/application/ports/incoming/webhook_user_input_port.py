# Standard Python Libraries
import json

# Third-Party Libraries
from reactivex import Observable, of
from reactivex import operators as ops

# RG Libraries
from services.application.domain.models.user import User
from services.application.ports.incoming.i_user_input_port import IUserInputPort
from services.application.ports.outgoing.i_user_output_port import IUserOutputPort
from services.application.shared.status import Status
from services.application.shared.utils import date_time_str_to_iso_format


class ApiGatewayUserInputPort(IUserInputPort):

    def __init__(self, user_output_port: IUserOutputPort):
        self.__user_output_port = user_output_port

    def create_user(self, event, contex) -> Observable[Status]:
        return of(event).pipe(
            ops.map(lambda event_data: self.get_body_data(event_data)),
            ops.map(lambda body_data: json.loads(body_data)),
            ops.map(lambda user_data: self.data_to_user_instance(user_data)),
            ops.map(lambda user: self.__user_output_port.save(user)),
            ops.map(lambda save_response: self.generate_status(save_response)),
        )

    def user_list(self, event, contex) -> list:
        return self.__user_output_port.list()

    @staticmethod
    def get_body_data(event_payload: dict) -> dict:
        return event_payload["body"]

    @staticmethod
    def get_users_raw_data(body_data: dict) -> dict:
        return body_data["response"]["data"]["users"]

    @staticmethod
    def data_to_user_instance(body_data: dict) -> User:
        users_raw_data = ApiGatewayUserInputPort.get_users_raw_data(body_data)
        return User(
            user_id=users_raw_data["id"],
            creation_date=date_time_str_to_iso_format(users_raw_data["created_at"]),
            update_date=date_time_str_to_iso_format(users_raw_data["update_at"]),
            first_name=users_raw_data["first_name"],
            last_name=users_raw_data["last_name"],
            email=users_raw_data["email"],
            count_win=users_raw_data["count_win"],
            count_lose=users_raw_data["count_lose"],
            current_game_id=users_raw_data["current_game_id"],
            last_game_id=users_raw_data["last_game_id"],
        )

    @staticmethod
    def generate_status(save_response: bool) -> Status:
        if save_response:
            status = Status(200, "User created.")
        else:
            status = Status(500, "User not created.")
        return status
