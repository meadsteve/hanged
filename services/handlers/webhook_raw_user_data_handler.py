# Standard Python Libraries
import asyncio

# RG Libraries
from services.application.shared.decorators import process_response_to_json
from services.handlers.async_handlers import user_webhook_async_handler


@process_response_to_json
def lambda_handler(event, contex):
    return asyncio.get_event_loop().run_until_complete(
        user_webhook_async_handler(event, contex)
    )