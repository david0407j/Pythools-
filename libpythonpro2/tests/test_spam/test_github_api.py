from unittest.mock import Mock

import pytest

from libpythonpro2 import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/5424655?v=4'
    resp_mock.json.return_value = {
        'login': 'davidson', 'id': 5424655,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libpythonpro2.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('davidson')
    assert avatar_url == url




def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('david0407j')
    assert 'https://avatars.githubusercontent.com/u/109997933?v=4' == url
