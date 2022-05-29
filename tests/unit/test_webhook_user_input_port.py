# Third-Party Libraries
from services.adapters.persistence import dynamo_user_adapter
from services.adapters.persistence.dynamo_user_adapter import DynamoDBUserAdapter
from services.application.ports.incoming.webhook_user_input_port import ApiGatewayUserInputPort
from services.application.ports.outgoing.user_output_port import UserOutputPort
import boto3
from dotenv import dotenv_values
from moto import mock_dynamodb

post_event = {
    "body": '{"response":{"data":{"users": { "id": 1, "created_at": "2022-05-21", "update_at": "2022-05-21", '
            '"first_name": "Alexis", "last_name": "Poveda", "email": "test@gmail.com", "count_win": 0, "count_lose": '
            '0, "current_game_id": 1, "last_game_id": 1}}}}',
    "resource": "/{proxy+}",
    "path": "/path/to/resource",
    "httpMethod": "POST",
    "queryStringParameters": {"foo": "bar"},
    "pathParameters": {"proxy": "path/to/resource"},
    "stageVariables": {"baz": "qux"},
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "max-age=0",
        "CloudFront-Forwarded-Proto": "https",
        "CloudFront-Is-Desktop-Viewer": "true",
        "CloudFront-Is-Mobile-Viewer": "false",
        "CloudFront-Is-SmartTV-Viewer": "false",
        "CloudFront-Is-Tablet-Viewer": "false",
        "CloudFront-Viewer-Country": "US",
        "Host": "1234567890.execute-api.{dns_suffix}",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Custom User Agent String",
        "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
        "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https",
    },
    "requestContext": {
        "accountId": "123456789012",
        "resourceId": "123456",
        "stage": "prod",
        "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
        "identity": {
            "cognitoIdentityPoolId": None,
            "accountId": None,
            "cognitoIdentityId": None,
            "caller": None,
            "apiKey": None,
            "sourceIp": "127.0.0.1",
            "cognitoAuthenticationType": None,
            "cognitoAuthenticationProvider": None,
            "userArn": None,
            "userAgent": "Custom User Agent String",
            "user": None,
        },
        "resourcePath": "/{proxy+}",
        "httpMethod": "POST",
        "apiId": "1234567890",
    },
}


@mock_dynamodb
def test_user_output_port(dynamodb_schema, monkeypatch):
    devenv = dotenv_values(".env.dev")
    monkeypatch.setattr(dynamo_user_adapter, "table_name", devenv["USERS_TABLE_NAME"])
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        TableName=devenv["USERS_TABLE_NAME"],
        **dynamodb_schema,
    )
    user_input_port = ApiGatewayUserInputPort(UserOutputPort(DynamoDBUserAdapter()))
    result = user_input_port.create_user(post_event, {})
    result.subscribe()
    assert True


@mock_dynamodb
def test_500_user_output_port(dynamodb_schema, monkeypatch):
    devenv = dotenv_values(".env.dev")
    monkeypatch.setattr(dynamo_user_adapter, "table_name", devenv["USERS_TABLE_NAME"])
    dynamodb = boto3.resource("dynamodb")
    dynamodb.create_table(
        TableName=devenv["USERS_TABLE_NAME"],
        **dynamodb_schema,
    )
    user_input_port = ApiGatewayUserInputPort(UserOutputPort(DynamoDBUserAdapter()))
    user_input_port.create_user({}, {})
    assert True
