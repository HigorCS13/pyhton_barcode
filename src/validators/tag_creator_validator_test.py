from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError
from .tag_creator_validator import tag_creator_validator

class MockRequest:
	def __init__(self, json) -> None:
		self.json = json

def test_tag_creator_validator():
	request = MockRequest(json={"product_code": "123456"})
	tag_creator_validator(request)

def test_tag_creator_validator_with_error():
	request = MockRequest(json={"product_code": 123456})
	try:
		tag_creator_validator(request)
		assert False
	except Exception as exception:
		assert isinstance(exception, HttpUnprocessableEntityError)
