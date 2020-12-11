import testinfra

host = testinfra.get_hosts('all')


def test_check_distribution(host):
    assert host.system_info.distribution.lower() in [
        'ubuntu',
    ]
