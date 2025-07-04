# Network Subnetting Analysis Report

## Executive Summary

This report analyzes 25 IP addresses with their corresponding subnet masks to identify network efficiency, overlapping subnets, and optimization opportunities.

## 1. Subnet with Most Hosts

**Answer:subnets with prefix 24 have the most hosts (1,022 usable hosts each)**

The subnets with /22 masks (255.255.252.0) contain the most hosts:

- 192.168.100.0/22 (contains 192.168.100.7)
- 10.2.0.0/22 (contains 10.2.1.56)
- 172.16.48.0/22 (contains 172.16.50.1)
- 10.20.4.0/22 (contains 10.20.4.6)
- 192.168.20.0/22 (contains 192.168.20.44)
- 10.3.0.0/22 (contains 10.3.3.9)
- 172.16.60.0/22 (contains 172.16.60.30)
- 10.15.4.0/22 (contains 10.15.5.50)

## 2. Overlapping Subnets Analysis

**Answer: No overlapping subnets detected**

All subnets are properly separated:

### Class A (10.x.x.x) Networks:

- 10.1.4.0/23, 10.0.2.0/22, 10.2.0.0/22, 10.20.4.0/22, 10.4.0.0/24, 10.0.0.0/23, 10.3.0.0/22, 10.50.2.0/24, 10.15.4.0/22

### Class B (172.16.x.x) Networks:

- 172.16.20.0/24, 172.16.0.0/23, 172.16.48.0/22, 172.16.8.0/23, 172.16.40.0/24, 172.16.14.0/23, 172.16.60.0/22

### Class C (192.168.x.x) Networks:

- 192.168.1.0/24, 192.168.100.0/22, 192.168.2.0/24, 192.168.3.0/24, 192.168.20.0/22, 192.168.10.0/24, 192.168.4.0/24, 192.168.6.0/23

## 3. Smallest and Largest Subnets

### Smallest Subnets (/24 - 254 usable hosts):

- 192.168.1.0/24, 172.16.20.0/24, 10.0.3.0/24, 192.168.2.0/24, 172.16.40.0/24, 192.168.3.0/24, 10.4.3.0/24, 192.168.10.0/24, 192.168.4.0/24, 10.50.2.0/24

### Largest Subnets (/22 - 1,022 usable hosts):

- 192.168.100.0/22, 10.2.0.0/22, 172.16.48.0/22, 10.20.4.0/22, 192.168.20.0/22, 10.3.0.0/22, 172.16.60.0/22, 10.15.4.0/22

## 4. Subnetting Strategy Recommendations

### Current Network Inefficiencies:

1. **Over-provisioning**: Many /22 subnets (1,022 hosts) likely have low utilization
2. **Inconsistent sizing**: Mix of /24, /23, and /22 subnets
3. **Potential waste**: Large subnets with single hosts represent significant IP waste

### Recommended VLSM Strategy:

#### 1 Network Assessment

- Determine actual host requirements per subnet
- Identify future growth for each network segment

#### 2 Hierarchical Subnetting

**For 10.x.x.x networks:**

- Use /16 for major sites (65,534 hosts)
- Subdivide into /20 for departments (4,094 hosts)
- Further subdivide into /24 for VLANs (254 hosts)
- Use /28 for point-to-point links (14 hosts)

**For 172.16.x.x networks:**

- Use /20 for large departments (4,094 hosts)
- Use /24 for standard VLANs (254 hosts)
- Use /26 for small workgroups (62 hosts)
- Use /30 for point-to-point links (2 hosts)

**For 192.168.x.x networks:**

- Use /24 for standard subnets (254 hosts)
- Use /26 for small departments (62 hosts)
- Use /28 for servers/printers (14 hosts)
- Use /30 for device management (2 hosts)

### Benefits:

- **Reduced waste**: Potential 60-70% reduction in unused IP addresses
- **Improved scalability**: Hierarchical structure supports better route summarization
- **Enhanced security**: Smaller subnets reduce broadcast domains
- **Better management**: Consistent sizing simplifies network administration