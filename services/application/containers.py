# Third-Party Libraries
from lagom import Container

# RG Libraries
from services.adapters.user.i_user_adapter import IUserAdapter
from services.adapters.persistence.dynamo_user_adapter import DynamoDBUserAdapter
from services.application.ports.incoming.i_user_input_port import IUserInputPort
from services.application.ports.incoming.webhook_user_input_port import (
    ApiGatewayUserInputPort,
)
from services.application.ports.outgoing.i_user_output_port import IUserOutputPort
from services.application.ports.outgoing.user_output_port import UserOutputPort

container = Container()
container[IUserAdapter] = container[DynamoDBUserAdapter]
container[IUserOutputPort] = container[UserOutputPort]
container[IUserInputPort] = container[ApiGatewayUserInputPort]
