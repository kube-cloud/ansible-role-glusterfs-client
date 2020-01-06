import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_heketi_installed(host):

    # Application code
    server_app_code = 'kis'

    # System Release
    server_app_home = '/kubecloud/myapp/' + server_app_code

    # App Logs Dir
    server_app_logs = server_app_home + '/logs'

    # App Config dir
    server_app_configuration = server_app_home + '/configuration'

    # App Security dir
    server_app_security = server_app_home + '/security'

    # App Script dir
    server_app_sccipts = server_app_home + '/scripts'

    # App Delivery dir
    server_app_delivery = server_app_home + '/delivery'

    # App Datas dir
    server_app_datas = server_app_home + '/datas'

    # App Username dir
    server_user_name = 'admin'

    # Private key
    server_user_ssh_private_key = '/home/' + server_user_name + '/.ssh/id_rsa'

    # Check home dir
    assert host.file(server_app_home).exists
    assert host.file(server_app_home).is_directory
    assert host.file(server_app_home).user == server_user_name

    # Check conf dir
    assert host.file(server_app_configuration).exists
    assert host.file(server_app_configuration).is_directory
    assert host.file(server_app_configuration).user == server_user_name

    # Check logs dir
    assert host.file(server_app_logs).exists
    assert host.file(server_app_logs).is_directory
    assert host.file(server_app_logs).user == server_user_name

    # Check security dir
    assert host.file(server_app_security).exists
    assert host.file(server_app_security).is_directory
    assert host.file(server_app_security).user == server_user_name

    # Check script dir
    assert host.file(server_app_sccipts).exists
    assert host.file(server_app_sccipts).is_directory
    assert host.file(server_app_sccipts).user == server_user_name

    # Check delivery dir
    assert host.file(server_app_delivery).exists
    assert host.file(server_app_delivery).is_directory
    assert host.file(server_app_delivery).user == server_user_name

    # Check delivery dir
    assert host.file(server_app_datas).exists
    assert host.file(server_app_datas).is_directory
    assert host.file(server_app_datas).user == server_user_name

    # Check private key
    assert host.file(server_user_ssh_private_key).exists
    assert host.file(server_user_ssh_private_key).is_file
    assert host.file(server_user_ssh_private_key).user == server_user_name

    # Check user exists
    assert host.user(server_user_name).exists
    assert server_user_name in host.user(server_user_name).groups
    assert 'sudo' in host.user(server_user_name).groups
