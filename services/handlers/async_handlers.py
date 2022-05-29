# Third-Party Libraries
from lagom import magic_bind_to_container

# RG Libraries
from services.application.containers import container
from services.application.ports.incoming.i_user_input_port import IUserInputPort


@magic_bind_to_container(container)
async def user_webhook_async_handler(
    event, context, user_input_port: IUserInputPort
):
    return await user_input_port.create_user(event, context)
