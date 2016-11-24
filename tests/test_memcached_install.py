import pytest


def test_memcached_package(Package):
    assert Package('memcached').is_installed


@pytest.mark.parametrize("path", [
    "/etc/init.d/memcached",
    "/etc/default/memcached",
    "/etc/memcached.conf"])
def test_default_file_absence(File, path):
    assert not File(path).exists
