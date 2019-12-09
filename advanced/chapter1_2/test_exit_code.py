from pathlib import Path

import pytest
from py._path.local import LocalPath
from pytest import ExitCode


def test_exitCode():
    print([(e.name, e.value) for e in ExitCode])
    assert len([(e.name, e.value) for e in ExitCode]) == 6


def test_temp_dir(tmpdir):
    assert isinstance(tmpdir, LocalPath)
    assert tmpdir.exists()
    tmpdir.remove()
    assert not tmpdir.exists()


def test_temp_path(tmp_path):
    assert isinstance(tmp_path, Path)
    assert tmp_path.exists()
    tmp_path.rmdir()
    assert not tmp_path.exists()


@pytest.fixture
def error_fixture():
    a = 0
    assert a


def test_error(error_fixture):
    pass


@pytest.mark.xfail(reason="xfailing this test")
def test_xfail():
    assert 0


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass


def test_skip():
    pytest.skip("skipping this test")
    assert 0

def test_failed():
    assert 0