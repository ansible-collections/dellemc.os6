# Provision OS6 switch stack using the Ansible Network Collection for Dell EMC OS6

This example describes how to use Ansible to configure OS6 switches. The sample topology contains two OS6 switches connected with each other. This example configures iBGP between two routers using the same AS.

## Create a simple Ansible playbook**

**Step 1**
Create an inventory file `inventory.yaml`, then specify the device IP addresses under use in the inventory.

**Step 2** 
Create a group variable file `group_vars/all`and define credentials common to all hosts.

**Step 3**
Create a host variable file  `host_vars/switch1.yaml`, then define credentials, hostname for switch1.

**Step 4**
Create a host variable file  `host_vars/switch2.yaml`, then define credentials, hostname for switch2

**Step 5** 
Create a playbook `os6switch.yaml`.

**Step 6** 
Run the playbook.

`ansible-playbook  -i  inventory.yaml  os6switch.yaml`
