# Standard Python Libraries
import json

# Third-Party Libraries
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator


@lambda_handler_decorator
def process_response_to_json(handler, event, context):
    status = handler(event, context)
    return {
        "statusCode": status.status_code,
        "body": json.dumps({"message": status.message}),
    }
