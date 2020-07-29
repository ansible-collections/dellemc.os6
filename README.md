# The Ansible Network Collection for Dell EMC OS6

This collection includes the Ansible modules, plugins and roles required to work on the Dell EMC PowerSwitch platforms running Dell EMC OS6. Sample playbooks and documentation are also included to show how the collection can be used.

### Ansible modules

- **os6_command.py** — Run commands on remote devices running Dell EMC OS6

- **os6_config.py** — Manage configuration sections on remote devices running Dell EMC OS6

- **os6_facts.py** — Collect facts from remote devices running Dell EMC OS6

### Ansible roles

Roles facilitate provisioning of device running Dell EMC OS6. These roles explain how to use OS9 and include os6_aaa, os6_bgp, os6_xstp, and so on. There are over 15 roles available. The documentation for each role is at [OS6 roles](https://github.com/ansible-collections/dellemc.os6/blob/master/docs/roles.rst).

### Playbooks

Sample playbooks are included for provisioning device running Dell EMC OS6.

- [iBGP](https://github.com/ansible-collections/dellemc.os6/blob/master/playbooks/README.md) — Example playbook to configure iBGP between two routers with Dell EMC OS6 switches

## Installation

Use this command to install the latest version of the OS6 collection from Ansible Galaxy.

```
ansible-galaxy collection install dellemc.os6

```

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0.

```
ansible-galaxy collection install 'dellemc.os6:>=1.0.0,<2.0.0'

```

## Version compatibility
Ansible version 2.10 or later.

> **NOTE**: For Ansible version lower than 2.10, use [dellos6 modules](https://ansible-dellos-docs.readthedocs.io/en/latest/modules.html#os6-modules) and [dellos roles](https://ansible-dellos-docs.readthedocs.io/en/latest/roles.html).

## Sample playbook

```

- hosts: os6switches
  connection: network_cli
  collections:
    - dellemc.os6
  roles:
    - os6_vlan

```

**Sample host_vars/os6_sw1.yaml**

```

hostname: os6switches
# parameters for connection type network_cli
ansible_ssh_user: xxxx
ansible_ssh_pass: xxxx
ansible_become: yes
ansible_become_method: enable
ansible_network_os: dellemc.os6.os6

```

**Sample inventory.yaml**

```
[os6switches]
switch1 ansible_host= 100.94.51.40
switch2 ansible_host= 100.94.52.38

```

(c) 2017-2020 Dell Inc. or its subsidiaries. All rights reserved.
