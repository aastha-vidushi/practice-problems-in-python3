'''
Consider a string '11155422211788888' and group them in such a way the output is ['111','55', '4','222', '11', '7', '88888']
'''

ip ="192.168.225.134"
print("Given IP : ", ip)

# Spliting the given string into a list in order to swap the position of 2nd & 3rd octet
ipList = ip.split(".")
# Output : ['192', '168', '225', '134']
print(ipList)

# swaping the value at 2nd position with the value at 3rd position
ipList[1], ipList[2] = ipList[2], ipList[1]
# Output : ['192', '225', '168', '134']
print(ipList)

# Converting the list into final output
finalIp = ".".join(ipList)
print("Final IP : ", finalIp)

print("===================================")
print("Using tuple")
fetchOctet = ipList[1], ipList[2]
ipList[2],ipList[1] = fetchOctet
print(ipList)
