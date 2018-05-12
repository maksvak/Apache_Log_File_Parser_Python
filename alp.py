#Apache Log Parser
#2/15/2018
#Created by: Maksim Vakulenko
##########################################################
###############################Import Libraries
import csv #import csv library
import re #import regex
from collections import defaultdict #imports default dict for better info handling

###############################Step 1: Import the CSV file.
#absolute path required but can be made an input for automation
path = r'C:\Users\maksi\Desktop\ALP\weblog.csv'
with open(path, 'r') as f:#read in the CSV file
	reader=csv.reader(f)
	your_list=list(reader) #puts each line into a string as a part of a list

#############################Step 2: Sort & Separate Information

#Idea here is to use regex in order to break this apart into
#the desired pieces.
length=len(your_list) #length of list, needed for sort & loops
i=0 #counter
ip_list=[]#create a list for IPs
client_list=[]#create a list of clients
ip_by_clients = {}
for i in range(length):
	xline=your_list[i] #pull line item from csv
	xline_str=''.join(xline)#convert to string for regex process
	breakdown=re.findall('\[[^\]]*\]|\([^\)]*\)|\"[^\"]*\"|\S+',xline_str) #split string by spaces
	ip_temp=breakdown[0]#select origin IP
	client_temp=breakdown[8]#client name
	ip_list.append(ip_temp)#add all IPs to list
	client_list.append(client_temp)#add all clients to list
	if client_temp in ip_by_clients:
		ip_by_clients[client_temp].append(ip_temp)
		#if the client is already in the dictionary append the ip list
	else:
		ip_by_clients[client_temp] = [ip_temp]
		#create a new pair for the client name
	i+=1#increment counter

#now we have a list of individual IP's' and clients

def unique(list1): #function for removing duplicates

  # intilize a list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return (unique_list)

#############################Step 3: Print Desired Information
#Print Unique IP List
uniqueip=unique(ip_list)
for x in uniqueip:
	print(x)

#print unique clients and associated IP's
for client in sorted(ip_by_clients.keys()): #sorts the hosts and post the IP's
	print(client)
	for ip_addr in  unique(ip_by_clients[client]):
		print("    " + ip_addr)
