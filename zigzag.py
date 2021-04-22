#This problem was asked by PayPal.
#
#Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.
#
#For example, given the sentence "thisisazigzag" and k = 4, you should print:
#
#t     a     g
# h   s z   a
#  i i   i z
#   s     g

def makeZigZag(string, k, spaced = False):
    finalZigZag = "\n"
    if spaced is False:
        string = string.replace(" ","")
    elif spaced is True:
        pass
    elif isinstance(spaced, str) and len(spaced) == 1:
        string = string.replace(" ",spaced)
    
    for i in range(k):
        linestring = " "*i
        j = i
        going_up = i 

        if i==0:
                going_up= False
        elif i == k -1:
            going_up= True
        else:
            going_up = not bool(going_up)
        while j < len(string):
            linestring += string[j]

            if going_up:
                valleySize = 2*i-1
            else:
                valleySize = 2*(k-i-1)-1
            
            linestring += (" "*valleySize)
            j+=valleySize+1
            if i==0:
                going_up= False
            elif i == k -1:
                going_up= True
            else:
                going_up = not bool(going_up)
        #print(linestring)
        finalZigZag += str(linestring + "\n")

    return finalZigZag[1:-1]






print(f'thisisazigzag: \n{makeZigZag("thisisazigzag",4)}')

print(f'Not spaced: \n{makeZigZag("Construction of each of the line is the key part of this problem",4,spaced = "#")}')
print(f'Spaced: \n{makeZigZag("Construction of each of the line is the key part of this problem",4,spaced = "$")}')


print(f'8 Rows: \n{makeZigZag("Construction of each of the line is the key part of this problem",8)}')
print(f'8 Rows Spaced: \n{makeZigZag("Construction of each of the line is the key part of this problem",8,spaced = True)}')

