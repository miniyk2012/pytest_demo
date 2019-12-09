import json
import os

import pytest

from utils import here

HERE = here(__name__)

config = {"1": "123", "2": "456", "3": 345, '9': [2, 34]}


def dump_config(config):
    path = os.path.join(HERE, '.conf.json')
    with open(path, 'w', encoding='utf-8') as wr:
        json.dump(config, wr, indent=4)


@pytest.mark.skip(reason="不应该修改真实环境的数据")
def test_config():
    dump_config(config)
    path = os.path.join(HERE, '.conf.json')
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config


@pytest.mark.run(order=3)
def test_after():
    """All modifications will be undone after the requesting
    test function or fixture has finished."""
    path = os.path.join(HERE, '.conf.json')
    assert path == here(__name__) + os.path.sep + '.conf.json'


@pytest.mark.run(order=1)
def test_patch_config(tmpdir, monkeypatch):
    fake_path = tmpdir.mkdir('home')
    monkeypatch.setattr(os.path, 'join', lambda *args: str(fake_path.join('.conf.json')))

    dump_config(config)
    path = os.path.join(HERE, '.conf.json')  # 这时候已经被monkeypatch了
    assert path != here(__name__) + os.path.sep + '.conf.json'
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config


@pytest.fixture
def patch_fixture(tmpdir, monkeypatch):
    fake_path = tmpdir.mkdir('fixture')
    monkeypatch.setattr(os.path, 'join', lambda *args: str(fake_path.join('.conf.json')))
    path = os.path.join(HERE, '.conf.json')
    return path


@pytest.mark.run(order=2)
def test_fixture_patch(patch_fixture):
    dump_config(config)
    path = os.path.join(HERE, '.conf.json')
    assert path == patch_fixture  # 这时候fixture的patch仍然有效
    assert path != here(__name__) + os.path.sep + '.conf.json'
    expected = json.load(open(path, 'r', encoding='utf-8'))
    assert expected == config
