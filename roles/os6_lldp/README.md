LLDP role
=========

This role facilitates the configuration of link layer discovery protocol (LLDP) attributes at a global and interface level. It supports the configuration of hello, mode, multiplier, advertise tlvs, management interface, FCoE, ISCSI at global and interface level.

The LLDP role requires an SSH connection for connectivity to a Dell EMC Networking device. You can use any of the built-in OS connection variables .

Role variables
--------------

- If *os6_cfg_generate* is set to true, the variable generates the role configuration commands in a file
- Any role variable with a corresponding state variable set to absent negates the configuration of that variable
- Setting an empty value for any variable negates the corresponding configuration
- Variables and values are case-sensitive

**os6_lldp keys**

| Key        | Type                      | Description                                             | Support               |
|------------|---------------------------|---------------------------------------------------------|-----------------------|
| ``interval`` | integer | The interval in seconds to transmit local LLDP data (5 to 32768) | os6 |
| ``hold`` | integer | The interval multiplier to set local LLDP data TTL (2 to 10) | os6 |
| ``notification_interval`` | integer | Configure minimum interval to send remote data change notifications (5 - 3600) | os6 |
| ``reinit`` | integer | Configures the reinit value (1-10) | os6 |
| ``timers`` | dictionary | Configures the LLDP global timer value | os6 |
| ``advertise`` | dictionary     | Configures LLDP-MED and TLV advertisement at the global level (see ``advertise.*``) | os6 |
| ``advertise.med`` | dictionary     | Configures MED TLVs advertisement (see ``med_tlv.*``) | os6 |
| ``med.global_med`` | boolean     | Configures global MED TLVs advertisement | os6 |
| ``med.fast_start_repeat_count`` | integer | Configures med fast start repeat count value (1 to 10) | os6 |
| ``med.config_notification`` | boolean | Configure all the ports to send the topology change notification | os6 | 
| ``local_interface`` | dictionary     | Configures LLDP at the interface level (see ``local_interface.*``) | os6 |
| ``local_interface.<interface name>`` | dictionary     | Configures LLDP at the interface level (see ``<interface name>.*``)     | os6 |
| ``<interface name>.mode``  | dictionary: rx,tx   | Configures LLDP mode configuration at the interface level | os6 |
| ``<interface name>.mode.tx``  | boolean | Enable/Disable LLDP transmit capability at interface level | os6 |
| ``<interface name>.mode.rx``  | boolean | Enable/Disable LLDP receive capability at interface level | os6 |
| ``<interface name>.notification``  | boolean | Enable/Disable LLDP remote data change notifications at interface level | os6 |
| ``<interface name>.advertise`` | dictionary     | Configures LLDP-MED TLV advertisement at the interface level (see ``advertise.*``)     | os6 |
| ``advertise.med`` | dictionary     | Configures MED TLVs advertisement at the interface level (see ``med_tlv.*``) | os6 |
| ``med.enable`` | boolean     | Enables interface level MED capabilities | os6 |
| ``med.config_notification`` | boolean     | Configure sending the topology change notification |os6 |


Connection variables
--------------------

Ansible Dell EMC Networking roles require connection information to establish communication with the nodes in your inventory. This information can exist in the Ansible *group_vars* or *host_vars* directories or inventory, or in the playbook itself.

| Key         | Required | Choices    | Description                                         |
|-------------|----------|------------|-----------------------------------------------------|
| ``ansible_host`` | yes      |            | Specifies the hostname or address for connecting to the remote device over the specified transport |
| ``ansible_port`` | no       |            | Specifies the port used to build the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_PORT option is used; it defaults to 22 |
| ``ansible_ssh_user`` | no       |            | Specifies the username that authenticates the CLI login for the connection to the remote device; if value is unspecified, the ANSIBLE_REMOTE_USER environment variable value is used  |
| ``ansible_ssh_pass`` | no       |            | Specifies the password that authenticates the connection to the remote device. |
| ``ansible_become`` | no       | yes, no\*   | Instructs the module to enter privileged mode on the remote device before sending any commands; if value is unspecified, the ANSIBLE_BECOME environment variable value is used, and the device attempts to execute all commands in non-privileged mode |
| ``ansible_become_method`` | no       | enable, sudo\*   | Instructs the module to allow the become method to be specified for handling privilege escalation; if value is unspecified, the ANSIBLE_BECOME_METHOD environment variable value is used. |
| ``ansible_become_pass`` | no       |            | Specifies the password to use if required to enter privileged mode on the remote device; if ``ansible_become`` is set to no this key is not applicable. |
| ``ansible_network_os`` | yes      | os6, null\*  | This value is used to load the correct terminal and cliconf plugins to communicate with the remote device. |

> **NOTE**: Asterisk (\*) denotes the default value if none is specified.

Dependencies
------------

The *os6_lldp* role is built on modules included in the core Ansible code. These modules were added in Ansible version 2.2.0.

Example playbook
----------------

This example uses the *os6_lldp* role to configure protocol lldp. It creates a *hosts* file with the switch details and corresponding variables. The hosts file should define the *ansible_network_os* variable with corresponding Dell EMC networking OS name. When *os6_cfg_generate* is set to true, the variable generates the configuration commands as a .part file in *build_dir* path. By default, the variable is set to false. It writes a simple playbook that only references the *os6_lldp* role.
 
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
    build_dir: ../temp/os6
    os6_lldp:
       global_lldp_state: present
       enable: false
        mode: rx
       multiplier: 3
       fcoe_priority_bits: 3
       iscsi_priority_bits: 3
       hello: 6
       dcbx:
         version: auto
       management_interface:
         hello: 7
         multiplier: 3
         mode: tx
         enable: true
         advertise:
           port_descriptor: false
           management_tlv: management-address system-capabilities
           management_tlv_state: absent
       advertise:
         dcbx_tlv: pfc
         dcbx_tlv_state: absent
         dcbx_appln_tlv: fcoe
         dcbx_appln_tlv_state:
         dot1_tlv:
           port_tlv:
              protocol_vlan_id: true
              port_vlan_id: true
           vlan_tlv:
              vlan_range: 2-4
         dot3_tlv:
           max_frame_size: false
         port_descriptor: false
         management_tlv: management-address system-capabilities
         management_tlv_state: absent
         med:
           global_med: true
           application:
             - name: "guest-voice"
               vlan_id: 2
               l2_priority: 3
               code_point_value: 4
             - name: voice
               priority_tagged: true
               l2_priority: 3
               code_point_value: 4
           location_identification:
             - loc_info: ecs-elin
               value: 12345678911
               state: present
       local_interface:
         fortyGigE 1/3:
           lldp_state: present
           enable: false
           mode: rx
           multiplier: 3
           hello: 8
           dcbx:
             version: auto
             port_role: auto-upstream
           advertise:
             dcbx_tlv: pfc
             dcbx_tlv_state: present
             dcbx_appln_tlv: fcoe
             dcbx_appln_tlv_state: absent
             dot1_tlv:
               port_tlv:
                 protocol_vlan_id: true
                 port_vlan_id: true
               vlan_tlv:
                 vlan_range: 2-4
                 state: present
             dot3_tlv:
               max_frame_size: true
             port_descriptor: true
             management_tlv: management-address system-capabilities
             management_tlv_state: absent
             med:
               application:
                 - name: guest-voice
                   vlan_id: 2
                   l2_priority: 3
                   code_point_value: 4
                 - name: voice
                   priority_tagged: true
                   l2_priority: 3
                   code_point_value: 4
               location_identification:
                 - loc_info: ecs-elin
                   value: 12345678911

**Simple playbook to setup system - switch1.yaml**

    - hosts: switch1
      roles:
         - dellemc.os6.os6_lldp

**Run**

    ansible-playbook -i hosts switch1.yaml

(c) 2017-2020 Dell Inc. or its subsidiaries. All Rights Reserved.
