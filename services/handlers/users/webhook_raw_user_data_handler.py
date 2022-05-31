# Standard Python Libraries
import asyncio

# RG Libraries
from services.application.shared.decorators import process_response_to_json
from services.handlers.users.async_handlers import user_webhook_async_handler, user_list_webhook_async_handler


@process_response_to_json
def create_lambda_handler(event, contex):
    return asyncio.get_event_loop().run_until_complete(
        user_webhook_async_handler(event, contex)
    )


@process_response_to_json
def list_lambda_handler(event, contex):
    return asyncio.get_event_loop().run_until_complete(
        user_list_webhook_async_handler(event, contex)
    )
