# Standard Python Libraries
import os

# Third-Party Libraries
import boto3
from botocore.exceptions import ClientError

# RG Libraries
from services.adapters.user.i_user_adapter import IUserAdapter
from services.application.domain.models.user import User

table_name = os.getenv("USERS_TABLE_NAME", None)
PK_PREFIX = "user#"


class DynamoDBUserAdapter(IUserAdapter):

    def __init__(self):
        dynamodb = boto3.resource("dynamodb")
        self.__table = dynamodb.Table(table_name)

    def save(self, user: User) -> bool:
        try:
            item = {
                "pk": PK_PREFIX + user.user_id,
                "user_id": user.user_id,
                "creation_date": str(user.creation_date),
                "update_date": str(user.update_date),
                "first_name": user.first_name,
                "last_name": user.last_name,
                "count_win": user.count_win,
                "count_lose": user.count_lose,
                "current_game_id": user.current_game_id,
                "last_game_id": user.last_game_id
            }
            self.__table.put_item(Item=item)
            return True
        except ClientError as error:
            print(error)
            return False

    def list(self) -> list:
        try:
            result = self.__table.scan()
            return result['Items']
        except ClientError as error:
            print(error)
            return None
