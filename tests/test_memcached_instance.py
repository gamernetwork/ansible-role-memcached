def test_memache_process_ownership(Process, File):
    pid = File("/run/memcached/memcached.pid").content
    proc = Process.get(pid=pid)
    assert proc.user == "nobody"
    assert proc.group == "nogroup"


def test_memache_pid_file_ownership(File):
    pid_file = File("/run/memcached/memcached.pid")
    assert pid_file.user == "nobody"
    assert pid_file.group == "nogroup"
    assert pid_file.mode == 0o644


def test_memcached_service_running(Service):
    assert Service('memcached').is_running


def test_memcached_service_enable(Service):
    assert Service('memcached').is_enabled


def test_memcached_listener_tcp(Socket):
    assert Socket("tcp://127.0.0.2:11212").is_listening


def test_memcached_listener_udp(Socket):
    assert Socket("udp://127.0.0.2:11212").is_listening
