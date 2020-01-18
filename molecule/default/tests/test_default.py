import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_glusterfs_installed(host):

    # Glusterfs client command path
    command_path = 'glusterfs'

    # Execute command and get result
    command_run = host.run(command_path + ' --version')

    # Assert that run is OK
    assert command_run.rc == 0
