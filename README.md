# Ansible Linux based glusterfs-client role

![Python](https://img.shields.io/pypi/pyversions/testinfra.svg?style=flat)
![Licence](https://img.shields.io/github/license/kube-cloud/ansible-role-glusterfs-client.svg?style=flat)
[![Travis Build](https://img.shields.io/travis/kube-cloud/ansible-role-glusterfs-client.svg?style=flat)](https://travis-ci.com/kube-cloud/ansible-role-glusterfs-client)
[![Galaxy Role Downloads](https://img.shields.io/ansible/role/d/45449.svg?style=flat)](https://galaxy.ansible.com/jetune/glusterfs-client)

Ansible role used to install glusterfs-client on Linux based Operating System.

<a href="https://www.kube-cloud.com/"><img width="200" src="https://kube-cloud.com/images/branding/logo/kubecloud-logo-single_writing_horizontal_color_300x112px.png" /></a>
<a href="https://www.redhat.com/fr/technologies/management/ansible"><img width="150" src="https://getvectorlogo.com/wp-content/uploads/2019/01/red-hat-ansible-vector-logo.png" /></a>
<a href="https://www.gluster.org/"><img width="150" src="https://www.gluster.org/wp-content/uploads/2016/03/gluster-ant.png" /></a>

# Supported Version

* glusterfs-client 3.12+

# Supported OS

* CentOS 6/7
* RedHat 6/7
* Ubuntu Xenial/Bionic

# Usage

* Install Role ``` ansible-galaxy install jetune.glusterfs-client ```
* use in your playbook
```
---
- hosts: all

  roles:
   
   - role: jetune.glusterfs-client
```
