# Third-Party Libraries
from services.adapters.persistence import dynamo_user_adapter
from services.adapters.persistence.dynamo_user_adapter import DynamoDBUserAdapter
from services.application.ports.outgoing.user_output_port import UserOutputPort
import boto3
from dotenv import dotenv_values
from moto import mock_dynamodb


@mock_dynamodb
def test_user_output_port(make_new_user, dynamodb_schema, monkeypatch):
    devenv = dotenv_values(".env.dev")
    monkeypatch.setattr(dynamo_user_adapter, "table_name", devenv["USERS_TABLE_NAME"])
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        TableName=devenv["USERS_TABLE_NAME"],
        **dynamodb_schema,
    )
    user_output_port = UserOutputPort(DynamoDBUserAdapter())
    user = make_new_user()
    result = user_output_port.save(user)
    assert result
