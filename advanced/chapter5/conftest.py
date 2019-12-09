import pytest


@pytest.fixture
def smtp_connection():
    class SMTP:
        def ehlo(self):
            return 250, 'hello'
    return SMTP()

