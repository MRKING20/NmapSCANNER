import nmap

# initialize the port scanner
scanner = nmap.PortScanner()
target = input("Please Enter An IP Address :")
# scan target for ports in range 1-1024
scanner.scan(target,"1-1024",'-sV')

#output the host name
print("This Host Name Is:" + scanner[target].hostname())
#output the host status up/no
print("The Host Status Is:" + scanner[target].state())

#output all open ports 
keys = scanner[target]['tcp'].keys()
#output all opens ports with informations
for i in keys:
    print('----------------------------')
    print('the port' + str(i) + " : ")
    #this line for information of ports 
    res = scanner[target]['tcp'][i]
    for re in res:
        print(re + " : " + res[re])