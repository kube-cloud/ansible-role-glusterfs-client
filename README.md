# Ansible Linux based Server Initialization Role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-initserver.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-initserver.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-initserver)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/41894.svg?style=flat)](https://galaxy.ansible.com/jetune/initserver)

Ansible role for custom KubeCloud Server Initialization 

<a href="https://www.kube-cloud.com/"><img width="250" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="300" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Xenial/Bionic

# Usage

* Install Role ``` ansible-galaxy install jetune.initserver ```
* use in your playbook
```
---
- hosts: all

  roles:
   
   - role: jetune.initserver
     vars:
      server_app_code: "kis"
      server_password_auth: true
      server_app_description: "KubeCloud Application description"
      server_app_home: "/kubecloud/myapp/"
      server_user_name: "admin"
      server_user_comment: "KIS Application Administrator"
      server_user_password: "admin123"
      server_user_groups: ["kis", "sudo", "adm", "exploit"]
      server_user_create_home: true
      server_user_shell: "/usr/bin/bash"
      server_user_ssh_private_key: "security/admin_rsa"
      server_user_autorized_keys: ["security/admin_rsa.pub"]

```
