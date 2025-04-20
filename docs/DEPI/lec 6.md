* securing Amazon S3 buckets and objects

- AWS Compliance program
- AWS Artifact 
---
- Networking basics
---
# what is IP ?
- internet protocol --> unique identifier that identifies somethings , allow the device to communicate with each other
- IP = network part + host part
- network part --> nic card (network interface card)
- host part --> device 

# types of IP ?
- ipv4 --> 32bit 192.0.2.0
- ipv6 --> 128bit (####)

# private vs Public IP
- public : any ip for public service
	- ex: google 8.8.8.8
- private : used for private data application to not connect to the public internet 
- NAT --> translate private IP to public IP in order to make private IP connects the internet 

# special IPs
- loopback address -->used to test the software on the local machine 
- link local address 

# subnet
- sub divisions of the network 
- we need to pass an IP to access the internet 
- if public its okey , if its private --> we use NAT to access the internet (through internet getway)
- subnet have range of IPs that access it 
- if the subnet access an IP that is out of the range --> firewall prevent the access 

# CIDR
- network routing (routing prefix) + host identifier 
- routing prefix --> must be fixed

# OSI model

# amazon vpc

- virtual private control , logically isolated  

# Elastic IP address
- associated with AWS account 
- can be allocated and remapped 
- additional costs might apply 

# route table




