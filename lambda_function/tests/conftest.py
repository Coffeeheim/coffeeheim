from dataclasses import dataclass

import pytest


@pytest.fixture
def lambda_context():
    @dataclass
    class LambdaContext:
        function_name: str = 'test'
        memory_limit_in_mb: int = 128
        invoked_function_arn: str = (
            'arn:aws:lambda:eu-west-1:123456789012:function:test'
        )
        aws_request_id: str = 'da658bd3-2d6f-4e7b-8ec2-937234644fdc'

    return LambdaContext()
