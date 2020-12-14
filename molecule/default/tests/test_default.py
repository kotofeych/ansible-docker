import testinfra

host = testinfra.get_hosts('all')


# Check distribution
def test_distribution(host):
    assert host.system_info.distribution.lower() in [
        'ubuntu',
        'centos'
    ]


# Check exists dockerd file
def test_availability_of_important_files(host):
    important_files = [
        "/usr/bin/dockerd",
        "/tmp/install_docker.sh",
        "/lib/systemd/system/docker.service"
    ]
    for file in important_files:
        assert host.file(file).exists


# Check start service Docker
def test_docker_service(host):
    assert host.package("docker-ce").is_installed
    assert host.package("docker-ce-cli").is_installed
