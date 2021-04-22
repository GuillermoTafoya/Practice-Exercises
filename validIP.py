import pprint

def validIPAddresses(string):
    validIPs = []
    for i in range(1,min(len(string),4)):
        currentParts = ["","","",""]
        
        currentParts[0] = string[:i]
        if not isValid(currentParts[0]):
            continue
            
        for j in range(i+1,i+min(len(string)-i,4)):
            currentParts[1]=string[i:j]
            if not isValid(currentParts[1]):
                continue
            for k in range(j+1,j+min(len(string)-j,4)):
                currentParts[2] = string[j:k]
                currentParts[3] = string[k:]
                
                if isValid(currentParts[2]) and isValid(currentParts[3]):
                    validIPs.append(".".join(currentParts))
            
            
    
    return validIPs

def isValid(string_sub):
    stringInt = int(string_sub)
    if stringInt > 255:
        return False
    return len(str(stringInt)) == len(string_sub)

pprint.pprint(validIPAddresses("1921680"))

pprint.pprint(validIPAddresses("3700100"))

pprint.pprint(validIPAddresses("99999999"))

pprint.pprint(validIPAddresses("100100"))

pprint.pprint(validIPAddresses("111"))
