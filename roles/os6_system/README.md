System role
===========

This role facilitates the configuration of global system attributes, and is abstracted for os6. It specifically enables configuration of hostname and enable password for os6.

The os6_system role requires an SSH connection for connectivity to a Dell EMC Networking device. You can use any of the built-in OS connection variables .


Role variables
--------------

- Role is abstracted using the *ansible_network_os* variable that can take dellemc.os6.os6 as a value
- If *os6_cfg_generate* is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os6_system keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``hostname`` | string | Configures a hostname to the device (no negate command) | os6 |
| ``enable_password`` | string              | Configures the enable password | os6 |
| ``mtu`` | integer | Configures the maximum transmission unit (MTU) for all interfaces | os6  |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified. 

Connection variables
********************

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

The *os6_system* role is built on modules included in the core Ansible code. These modules were added in Ansible version 2.2.0.

Example playbook
----------------

This example uses the *os6_system role* to completely set the NTP server, hostname, enable password, management route, hash alogrithm, clock, line terminal, banner and reload type. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the *ansible_network_os* variable with corresponding Dell EMC networking OS name. 

When *os6_cfg_generate* is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. The system role writes a simple playbook that only references the *os6_system* role. By including the role, you automatically get access to all of the tasks to configure system features. 

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
	  
    os6_system:
      hostname: host1
      unique_hostname: True
      enable_password: dell
      service_passwd_encryption: true
      banner:
        exec: t hai t
        login:
          ack_enable: true
          ack_prompt: testbanner
          keyboard_interactive: true
          banner_text: cloginbannerc
        motd: t ansibletest t
      hash_algo:
        algo:
          - name: lag
            mode: xor1
            stack_unit: 0
            port_set: 0
            state: present
          - name: ecmp
            mode: xor1
            stack_unit: 0
            port_set: 0
            state: present
        seed:
          - value: 3
            stack_unit: 0
            port_set: 0
            state: present
          - value: 2
            state: present
      load_balance:
        ingress_port: true
        ip_selection: 
           - field: vlan dest-ip
             state: present
        ipv6_selection: 
           - field: dest-ipv6 vlan
             state: present
        tunnel:
          hash_field:
            - name: mac-in-mac
              header: tunnel-header-mac
              state: present
      clock:
        summer_time:
          timezone_name: PST
          type: date
          start_datetime: 2 jan 1993 22:33
          end_datetime: 3 jan 2017 22:33
          offset_mins: 20
        timezone:
          name: IST
          offset_hours: -5
          offset_mins: 20
      reload_type:
        auto_save: true
        boot_type: normal-reload
        boot_type_state: absent
        config_scr_download: true
        dhcp_timeout: 5
        retry_count: 3
        relay: true
        relay_remote_id: ho
        vendor_class_identifier: aa
      management_rt:
        - ip: 10.16.148.254
          state: present
          ipv4: True
      line_terminal:
        vty 0:
          exec_timeout: 40
          exec_banner: true
        vty 1:
          exec_timeout: 40 200
          motd_banner: true
 
**Simple playbook to setup system - switch1.yaml**

    - hosts: switch1
      roles:
         - dellemc.os6.os6_system

**Run**

    ansible-playbook -i hosts switch1.yaml

(c) 2020 Dell Inc. or its subsidiaries.  All Rights Reserved.
