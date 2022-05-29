# Standard Python Libraries
from datetime import datetime, timedelta
from decimal import Decimal
from random import randint
from uuid import uuid4

# Third-Party Libraries
from services.application.domain.models.user import User
import mimesis
import pytest

MIMESIS_LOCALE = mimesis.locales.Locale.ES_MX


@pytest.fixture(scope="module")
def dynamodb_schema():
    """Return a schema for table creation."""
    return {
        "AttributeDefinitions": [
            {"AttributeName": "user_id", "AttributeType": "S"},
        ],
        "KeySchema": [
            {"AttributeName": "user_id", "KeyType": "HASH"},
        ],
        "ProvisionedThroughput": {
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5,
        },
    }


@pytest.fixture(scope="module")
def make_new_user():
    """Return a new factory for making users."""
    def _make_new_user():
        creation_random_datetime = mimesis.Datetime(locale=MIMESIS_LOCALE).datetime(
            start=datetime.now().year - 1, end=datetime.now().year
        )
        update_date_random_datetime = creation_random_datetime + timedelta(
            days=randint(0, 5)  # nosec
        )
        person = mimesis.Person(MIMESIS_LOCALE)
        return User(
            user_id=str(uuid4()),
            creation_date=creation_random_datetime,
            update_date=update_date_random_datetime,
            first_name=person.first_name(),
            last_name=person.last_name(),
            email=person.email(),
            count_win=0,
            count_lose=0,
            current_game_id=str(int(uuid4())),
            last_game_id=str(int(uuid4())),
        )

    return _make_new_user
