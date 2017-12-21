def normalize(name):
    # def change(index, val):
    #     if(index == 0):
    #         return val.upper()
    #     else:
    #         val.lower()        
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)