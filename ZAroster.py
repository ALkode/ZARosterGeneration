
import random
#random character generation

#role

def Gen_ZA_roster():
    roles = ('tank', 'healer', 'dps', 'dps')
    tank_classes = ('paladin', 'druid', 'warrior')
    healer_classes = ('shaman', 'paladin', 'druid', 'priest')
    dps_classes = ('shaman', 'paladin', 'druid', 'priest', 'warrior', 'rogue', 'hunter', 'warlock')
    priority = ('main', 'alt')

    raiders_count = random.randint(15,25)

    raider_roster = []
    random_raider = ''

    for raider in range(raiders_count):
        random_role = random.randint(0,3)
        random_raider = []
        random_raider.append(roles[random_role])
        match random_role:
            case 0:
                random_class = random.randint(0,2)
                random_raider.append(tank_classes[random_class])
            case 1:
                random_class = random.randint(0,2)
                random_raider.append(healer_classes[random_class])
            case 2:
                random_class = random.randint(0,7)
                random_raider.append(dps_classes[random_class])
            case 3:
                random_class = random.randint(0,7)
                random_raider.append(dps_classes[random_class])
            
        random_raider.append(priority[random.randint(0,1)])
        raider_roster.append(random_raider)                                
    return raider_roster
    
#print(Gen_ZA_roster())


def select_ZA_roster(raid_roster):
    roster = []
    available_tanks = []
    available_healers = []
    available_dps = []
    for raider in raid_roster:
        match raider[0]:
            case 'tank':
                available_tanks.append(raider)
            case 'healer':
                available_healers.append(raider)
            case 'dps':
                available_dps.append(raider)

    #print(available_dps)
    #print(available_healers)
    #print(available_tanks)

    available_dps.sort(key = lambda x: x[2])
    available_healers.sort(key = lambda x: x[2])
    available_tanks.sort(key = lambda x: x[2])
    
    available_dps.reverse()
    available_healers.reverse()
    available_tanks.reverse()
    print(available_dps)
    tanks_added = 0
    iteration = 0

    #for i in range(available_tanks.len()):
     #   print(i)


select_ZA_roster(Gen_ZA_roster())
