import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ssh_port(host):
    memcached = host.addr("127.0.0.1")
    memcached.port(22).is_reachable


def test_revoked_keys(host):
    revoked_keys = host.file("/etc/ssh/revoked_keys")
    revoked_keys.exists
    oct(revoked_keys.mode) == '0600'
    revoked_keys.user == 'root'
    revoked_keys.group == 'root'


def test_sshd_config(host):
    sshd_config = host.file("/etc/ssh/sshd_config")
    sshd_config.exists
    oct(sshd_config.mode) == '0600'
    sshd_config.user == 'root'
    sshd_config.group == 'root'


def test_ssh_config(host):
    ssh_config = host.file("/etc/ssh/ssh_config")
    ssh_config.exists
    oct(ssh_config.mode) == '0644'
    ssh_config.user == 'root'
    ssh_config.group == 'root'
