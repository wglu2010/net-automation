# net-automation
Will post my work done in the "Building Network Automation Solutions" course (ipspace.net) here.

## Initial Lab Setup
The initial lab consists of five CSR1000v virtual routers running on an ESXI whitebox. Using one virtual switch and four port groups, they are arranged in this topology:

![lab topology](net_auto_lab_1.png)

The plan is to provision/deprovision MPLS VPNs between the CE nodes, such as the VPN called 'RED' in the topology above.

Will do automation from an Ubuntu VM running in Virtualbox on my workstation. There is also a small Ubuntu VM running ser2net for console switch duties.
