import pytest

from SoftLife.app import create_app

@pytest.fixture(scope='module')
def app():
    '''Instance of main flask app'''
    return create_app()
