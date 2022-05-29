# Third-Party Libraries
from services.adapters.persistence import dynamo_user_adapter
from services.adapters.persistence.dynamo_user_adapter import DynamoDBUserAdapter
import boto3
from dotenv import dotenv_values
from moto import mock_dynamodb


@mock_dynamodb
def test_success_save(make_new_user, dynamodb_schema, monkeypatch):
    devenv = dotenv_values(".env.dev")
    monkeypatch.setattr(dynamo_user_adapter, "table_name", devenv["USERS_TABLE_NAME"])
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        TableName=devenv["USERS_TABLE_NAME"],
        **dynamodb_schema,
    )
    dynamodb_adapter = DynamoDBUserAdapter()
    user = make_new_user()
    result = dynamodb_adapter.save(user)
    assert result


@mock_dynamodb
def test_client_error_on_save(make_new_user, monkeypatch):
    devenv = dotenv_values(".env.dev")
    monkeypatch.setattr(dynamo_user_adapter, "table_name", devenv["USERS_TABLE_NAME"])
    user = make_new_user()
    dynamodb_adapter = DynamoDBUserAdapter()
    result = dynamodb_adapter.save(user)
    assert not result
