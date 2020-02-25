target = "Candva, demult, acum 1000 de ani traia o printesa intr-un castel. Si printesa intr-o zi auzi cum aparuse pe meleagurile sale un cufar fermecat din care iesea grai omenesc. Printesa curioasa strabatu 7 ulite si 7 piete; ajunse la cufar si vazu ca toti stateau la 100 metri distanta de el si se mirau. Din cufar intr-adevar se auzeau vorbe nedeslusite. Printesa curajoasa se duse sa-i vorbeasca. Il intreba cine e si ce dorinte are. Raspunsul fu: \"Sunt Ion am cazut in cufar si m-am ferecat din gresala. As dori sa ies.\". Printesa deschise cufarul si-l elibera pe Ion. \"Multumesc\" spuse Ion. Si astfel, povestea cufarului fermecat a fost deslusita."


def nonAN(target):
    return set([ x for x in list(target) if x.isalpha() == False and x.isdigit() == False]) - set("-")

def masculin(target):
    return [word for word in target if word.endswith("le")]

def get_clean(target, to_exclude):
    return "".join([x for x in target if not(x in to_exclude) or x == " "]).split(" ")
    

def findAll(target, what):
    return [x for x in target if what in x]

# print(len(target))
print(nonAN(target))
filtered = get_clean(target, nonAN(target))
print(filtered)
print(masculin(filtered))
print(findAll(filtered, "-"))