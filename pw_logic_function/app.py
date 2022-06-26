import json
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths, Logger
from aws_lambda_powertools.event_handler.api_gateway import Response
from aws_lambda_powertools.event_handler import content_types

tracer = Tracer()
logger = Logger()
app = APIGatewayRestResolver()


def build_response(status_code, body):
    return Response(
        status_code=status_code,
        content_type=content_types.APPLICATION_JSON,
        body=json.dumps(body),
    )


@app.get("/logic/health")
@tracer.capture_method
def get_health():

    return build_response(
        200, {"message": "This is the Logic Function and i just edited it."}
    )


@app.get("/logic/password/<user_id>/<account_id>")
@tracer.capture_method
def get_password(user_id, account_id):
    return


@app.put("/logic/password/<user_id>/<account_id>")
@tracer.capture_method
def update_password(user_id, account_id):
    return


@app.post("/logic/password/<user_id>")
@tracer.capture_method
def create_account(user_id):
    return


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
