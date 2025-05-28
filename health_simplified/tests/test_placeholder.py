# tests/test_user.py
from models import User

def test_user_creation():
    user = User(name="test")
    assert user.name == "test"
