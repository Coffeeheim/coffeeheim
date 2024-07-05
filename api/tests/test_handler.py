import json
import uuid

import handler as app

sample_event = {
    'rawPath': '/',
    'requestContext': {
        'http': {
            'method': 'POST',
        },
        'stage': '$default',
    },
}


def test_post_succ(lambda_context):
    minimal_event = sample_event | {
        'body': json.dumps(
            {'steamid': 'https://steamcommunity.com/id/sergiors'}
        )
    }

    ret = app.lambda_handler(minimal_event, lambda_context)
    assert ret['statusCode'] == 201


def test_post_not_found(lambda_context):
    minimal_event = sample_event | {
        'body': json.dumps({'steamid': str(uuid.uuid4())}),
    }

    ret = app.lambda_handler(minimal_event, lambda_context)
    assert ret['statusCode'] == 404


def test_post_invalid(lambda_context):
    minimal_event = sample_event | {
        'body': json.dumps({}),
    }

    ret = app.lambda_handler(minimal_event, lambda_context)
    assert ret['statusCode'] == 422
