from ansible.errors import AnsibleError, AnsibleFilterError

def vlan_parser(vlan_list):
    """
    Input: Unsorted list of vlan integers
    Output: Sorted string list of integers according to OS6-like vlan list rules
    1. Vlans are listed in ascending order
    2. Runs of 2 or more consecutive vlans are listed with a dash
    """

    # Sort and remove duplicates
    sorted_list = sorted(set(vlan_list))

    if sorted_list[0] < 1 or sorted_list[-1] > 4094:
        raise AnsibleFilterError("Valid VLAN range is 1-4094")

    parse_list = []
    idx = 0
    while idx < len(sorted_list):
        start = idx
        end = start
        while end < len(sorted_list) - 1:
            if sorted_list[end + 1] - sorted_list[end] == 1:
                end += 1
            else:
                break

        if start == end:
            # Single VLAN
            parse_list.append(str(sorted_list[idx]))
        else:
            # Run of 2 or more VLANs VLANs
            parse_list.append(
                str(sorted_list[start]) + "-" + str(sorted_list[end])
            )
        idx = end + 1

    result = [""]
    for vlans in parse_list:
        # Line (" switchport trunk allowed vlan ")
        result.append("")
        result[0] += vlans + ","

    # Remove trailing orphan commas
    for idx in range(0, len(result)):
        result[idx] = result[idx].rstrip(",")

    # Sometimes text wraps to next line, but there are no remaining VLANs
    if "" in result:
        result.remove("")

    return result


class FilterModule(object):
    """Filters for working with output from network devices"""

    def filters(self):
        return { 'vlan_parser': vlan_parser }