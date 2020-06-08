Users role
==========

This role facilitates the configuration of global system user attributes. It supports the configuration of CLI users, and is abstracted for os6.

The users role requires an SSH connection for connectivity to a Dell EMC Networking device. You can use any of the built-in OS connection variables .


Role variables
--------------

- Role is abstracted using the *ansible_network_os* variable that can take dellemc.os6.os6 as a value
- If *os6_cfg_generate* is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os6_users list keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``username`` | string (required)         | Configures the username which must adhere to specific format guidelines (valid usernames begin with A-Z, a-z, or 0-9 and can also contain `@#$%^&*-_= +;<>,.~` characters) | os6 |
| ``password`` | string                    | Configures the password set for the username; password length must be at least eight characters in os6 devices | os6 |
| ``privilege`` | int                | Configures the privilege level for the user; either 0, 1, or 15 for os6 devices; if this key is ommitted, the default privilege is 1 for os6 | os6 |
| ``state`` | string: absent,present\*     | Deletes a user account if set to absent  | os6 |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified. 

Connection variables
--------------------

Ansible Dell EMC Networking roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories, or inventory or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_PORT option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_USER environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device.  |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the ANSIBLE_BECOME environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the ANSIBLE_BECOME_METHOD environment variable value is used. |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable. |
| ``ansible_network_os`` | yes      | os6, null\*  | This value is used to load the correct terminal and cliconf plugins to communicate with the remote device. |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Dependencies
------------

The *os6_users* role is built on modules included in the core Ansible code. These modules were added in Ansible version 2.2.0.

Example playbook
----------------

This role is abstracted using the *ansible_network_os* variable that can take dellemc.os6.os6 values. If *os6_cfg_generate* is set to true, the variable generates the role configuration commands in a file. It writes a simple playbook that only references the *os6-users* role. By including the role, you automatically get access to all of the tasks to configure user features. 

**Sample hosts file**
 
    switch1 ansible_host= <ip_address> 

**Sample host_vars/switch1**

    hostname: switch1
    ansible_become: yes
    ansible_become_method: xxxxx
    ansible_become_pass: xxxxx
    ansible_ssh_user: xxxxx
    ansible_ssh_pass: xxxxx
    ansible_network_os: dellemc.os6.os6
    build_dir: ../temp/temp_os6
	  
    os6_users:
       - userrole: role1
         userrole_state: present
       - username: u1
         password: test
         role: sysadmin
         privilege: 0
         state: absent
       - username: u1
         password: false
         privilege: 1
         access_class: a1
         role: netadmin
         state: present
       - username: u2
         secret: test1
         secret_key : 0
         access_class: a2
         privilege: 3
         role: sysadmin
         state: present

**Simple playbook to setup users - switch1.yaml**

    - hosts: switch1
      roles:
         - dellemc.os6.os6_users

**Run**

    ansible-playbook -i hosts switch1.yaml

(c) 2020 Dell Inc. or its subsidiaries.  All Rights Reserved.
