
def get_all_names():
    with open('pokemon.txt',newline=None) as f:
        l=f.read()
        return l.split('\n')

def get_the_pokemon(clue,names):
    matches=[]
    for name in names:
        for i in clue:
            if i in ['_', name[clue.index(i)]]:
                break
        else:
            matches.append(name)
    return names


class Finder:
    def __init__(self):
        self.names=get_all_names()
        self.currentmatches=[]

    def find(self,clue:str):
        clue=clue.lower()
        for i in self.names:
            if len(clue)==len(i):
                self.currentmatches.append(i)  
        return get_the_pokemon(clue,self.currentmatches)

finder=Finder()
clue=input("Enter clue(the blanks should be marked by an underscore, for example:pi_ka_c__): ")
a=finder.find(clue)
print(a)