# The Ansible Network collection for Dell EMC OS6

## Collection contents

The OS6 Ansible Network collection includes the Ansible modules, plugins and roles required to work on the Dell EMC Power Switch platforms running Dell EMC OS6. It also includes sample playbooks and documents that illustrates how the collection can be used.

### Ansible modules

The following modules are part of this collection

- **os6_command.py** - Run commands on remote devices running Dell EMC OS6

- **os6_config.py** - Manage configuration sections on remote devices running Dell EMC OS6

- **os6_facts.py** - Collect facts from remote devices running Dell EMC OS6

### Ansible Roles

The roles facilitate provisioning of device running Dell EMC OS6. Some of the roles included in the collection are os6_aaa, os6_bgp, os6_xstp and so on. The docs directory in the collection includes documentation for each of the roles part of the collection.

### Playbooks

The playbooks directory includes sample playbooks that illustrate the usage of OS6 collections for provisioning device running Dell EMC OS6.

## Installation

Use this command to install the latest version of the OS6 collection from Ansible Galaxy:

```
ansible-galaxy collection install dellemc.os6

```

To install a specific version, a version range identifier must be specified. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0:

```
ansible-galaxy collection install 'dellemc.os6:>=1.0.0,<2.0.0'

```

## Dependency
Ansible version 2.10 or later

## Sample Playbook

```

- hosts: os6switches
  connection: network_cli
  collections:
    - dellemc.os6
  roles:
    - os6_vlan

```

## Sample host_vars/os6_sw1.yaml

```

hostname: os6switches
# parameters for connection type network_cli
ansible_ssh_user: xxxx
ansible_ssh_pass: xxxx
ansible_become: yes
ansible_become_method: enable
ansible_network_os: dellemc.os6.os6

```

## Sample inventory.yaml

```
[os6switches]
switch1 ansible_host= 100.94.51.40
switch2 ansible_host= 100.94.52.38

```

