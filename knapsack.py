"""
Given weights and values of n items, put these items in a knapsack of capacity W to get 
the maximum total value in the knapsack. 

You cannot break an item, either pick the complete item or don’t pick it (0-1 property).
"""

class item:
    def __init__(self,name,weight,value):
        self.name=name
        self.weight=weight
        self.value=value

class carried:
    def __init__(self,items=[]):
        self.items=items
        self.value = 0
        self.weight = 0
        
        self.setValue()
        self.setWeigth()

    def setValue(self):
        v = 0
        for i in self.items:
            v += i.value
        self.value=v
    
    def setWeigth(self):
        w = 0
        for i in self.items:
            w += i.weight
        self.weight=w

    @property
    def describe(self):
        print("Total items:",len(self.items))
        print("Total weight:",round(self.weight,2))
        print("Total value:",round(self.value,2))
        print("Items to carry:")
        
        print(countItems(self.items))
        print()

def countItems(items):
    names = []
    for i in items:
        names.append(i.name)
    n = {i:names.count(i) for i in names}
    return n

def visited(n,weight,memo):
    
    for alreadyVisited in range(len(memo)):
        if n == memo[alreadyVisited][0] and weight == memo[alreadyVisited][1]:
            return memo[alreadyVisited][2]
    return False

def maximizeValue(items,weight,n,memo=[]) -> carried:

    # Base case
    if n == 0 or weight==0:
        packed = carried()
        return packed

    # If already visited
    memoized = visited(n,weight,memo)
    if memoized is not False:
        return memoized 
    

    # Main
    currentItem = items[n-1]
    if currentItem.weight <= weight:

        attemp =  carried(maximizeValue(items[:n],weight-currentItem.weight,n-1,memo).items+[currentItem]) # maximizeValue + currenty item

        secondAttemp = maximizeValue(items[:n],weight,n-1,memo) # maximizeValue

        if attemp.value > secondAttemp.value: # maximizeValue + currenty item > maximizeValue
            packed = attemp
        else:
            packed = secondAttemp
        memo.append([n,weight,packed])
    elif currentItem.weight > weight:
        packed = maximizeValue(items[:n],weight,n-1,memo)
        memo.append([n,weight,packed])
    
    return packed

def maximizeValue2(items,weight) -> carried:
    
    # Funciona a veces
    concepcionOptima = [0 for _ in range(len(items))]
    for i in range(len(items)):
        concepcionOptima[i] = (items[i].value/items[i].weight)

    zipped_lists = zip(concepcionOptima, items)

    sorted_zipped_lists = sorted(zipped_lists,reverse=True)

    sorted_list = [element for _, element in sorted_zipped_lists]
    e = 0
    optimal= []
    while e < len(sorted_list) and weight > 0:
        currentItem = sorted_list[e]
        if currentItem.weight <= weight:
            optimal.append(currentItem)
            weight-=currentItem.weight
        e+=1
    
    return carried(optimal)


if __name__ == '__main__':
    apple = item("Apple",1,3.4)
    GoldApple = item("Golden Apple",3,5.6)
    mustard = item("Mustard",9,7.88)
    diamond = item("Diamond",10,15)
    stick = item("Stick",0.8,0.8)
    blackhole = item("Black Hole",25,20)
    heavyRock = item("Heavy Rock",30,50)
    shit = item("Shit",1,3.4)

    maxWeigth = 30

#    Total items: 13
#    Total weight: 29.6
#    Total value: 59.4
#    Items to carry:
#    {'Apple': 6, 'Diamond': 1, 'Golden Apple': 4, 'Stick': 2}

    m = [apple,
        apple, blackhole,
        apple,
        apple,
        apple, heavyRock,
        GoldApple, apple, blackhole, 
        GoldApple,
        blackhole,
        GoldApple, stick, stick, stick, stick, stick, stick, 
        GoldApple, 
        diamond]

    x = maximizeValue(m,maxWeigth,len(m),memo=[])
    
    x.describe

#    Total items: 1
#    Total weight: 30
#    Total value: 50
#    Items to carry:
#    {'Heavy Rock': 1}

    n = [stick,
        stick,
        apple,
        apple,
        apple,
        apple,
        GoldApple, heavyRock,
        mustard,
        diamond,
        stick]

    y = maximizeValue(n,maxWeigth,len(n),memo=[])

    y.describe

#   Total items: 13
#   Total weight: 29.8
#   Total value: 62.0
#   Items to carry:
#   {'Apple': 4, 'Shit': 3, 'Golden Apple': 4, 'Stick': 1, 'Diamond': 1}

    l = [apple,
        shit, blackhole,
        apple, apple,
        shit,
        apple, heavyRock,
        GoldApple, shit, blackhole, 
        GoldApple,
        blackhole,
        GoldApple, stick, stick, stick, stick, stick, stick, 
        GoldApple, 
        diamond]

    z = maximizeValue(l,maxWeigth,len(l),memo=[])
    
    z.describe