import pandas as pd
import datetime as dt
import math
'''
python script based on python code in juupyter notebook in 
order to run it using flask 
'''

def docking_days():
    #grab flight plan
    flight_plan = pd.read_csv(r'/Users/eliza/Desktop/iss_flight_plan_20220101-20251231.csv')

    #query to only use dates where the event is dock and convert it to a list
    dock_days_list = flight_plan[flight_plan['event'] == 'Dock']['datedim'].to_list()

    #convert list of date strings into a list of datetime objects
    dates_list = [dt.datetime.strptime(date, '%m/%d/%Y').date() for date in dock_days_list]

    #print the days difference between each date
    num_days = pd.Series(dates_list).diff().dt.days.iloc[1:].astype(int).tolist()
    print("number of daays til next dock\n",num_days)
    return dock_days_list, num_days


#return tuple with dock days list and num days list ------------------------------------------------

def crew_per_docking(dock_days_list):
    #grab crew members per dock
    crewF = pd.read_csv(r'/Users/eliza/Desktop/iss_flight_plan_crew_20220101-20251321.csv')

    crew_per_dock = []
    #the_tuple = docking_days()
    #dock_days_list = the_tuple[0]
    for i, date in enumerate(dock_days_list):
        crewNum = crewF[crewF['datedim'] == date]['crew_count'].tolist()
        Amount = sum(crewNum)
        crew_per_dock.append(Amount)

    #number of crew members on board during each dock
    print("number of crew per docking\n",crew_per_dock)     
    return crew_per_dock

# return crew per dock --------------------------------------


def consumption_rates(consumable): 
    #grab rates
    rater = pd.read_csv(r'/Users/eliza/Desktop/rates_definition.csv')

    #consumable must match a consumable on the rates csv. case sensitive.
    #consumable = 'Pretreat Tanks'
    #consumable = 'Air'
    #consumable = 'Water'

    #sum of generated
    sum_generated = sum(rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'generation')]['rate'].to_list())

    #grabs the usage rate of consumable and sums it up
    sum_usage = sum(rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'usage')]['rate'].to_list())

    #if units contains 'crew'
    crew_check = rater[rater['affected_consumable'] == consumable]['units'].tolist()
    combine =  '\t'.join(crew_check)

    print(crew_check)
    if 'Crew' in combine:
        per_crew = True
    else:
        per_crew = False

    print(per_crew)

    #prints
    print("Consumable used = ", sum_usage)
    print("Consumable generated = ", sum_generated)
    #net_consumable = sum_generated - sum_usage
    #print("net consumable per day= ", net_consumable)
    return per_crew, sum_usage, sum_generated
# return per_crew sum usage sum generated --------------------------------



#consumables to send 
#import math
def consumables_to_send(num_days, sum_usage, dock_days_list, per_crew, sum_generated, crew_per_dock):  #requires num_days sum_usage
    #create a list of base rates 
    listofrates = [sum_usage] * len(dock_days_list)
    consumable_to_send = []
    current_sum = 0
    res_list = []
    #call function to get crew_per_dock
    #crew_per_dock = crew_per_docking(dock_days_list)
    if(per_crew): #if percrew true change the list of rates
        for i in range(0, len(listofrates)):
            res_list.append(listofrates[i] * crew_per_dock[i])
    else:
        res_list = listofrates

    #match length and subtract the amount generated to get proper list of rates   
    res_list.pop()
    res_list = [x - sum_generated for x in res_list]

    intermediate = []
   
    #the_tuple = docking_days()
    #num_days = the_tuple[1]
    for i in range(0, len(res_list)):
        intermediate.append(res_list[i] * num_days[i])
    print (intermediate)

    #rounding
    for i, value in enumerate(intermediate):
        current_sum+=value
        consumable_to_send.append(math.trunc(current_sum))
        current_sum = current_sum - math.trunc(current_sum)
    print(consumable_to_send)
    return consumable_to_send
    #return consumable to send 

#--------------------------------------------------------
def create_table(consumable): #will be user selection / button
    #create table 
    #note to self
    #call all function in order o create varibles to inpuut into each 
    result_tup = docking_days()
    dock_days_list = result_tup[0]
    num_days = result_tup[1]
    crew_per_dock = crew_per_docking(dock_days_list)
    cons_tuple = consumption_rates(consumable)
    per_crew = cons_tuple[0]
    sum_usage = cons_tuple[1]
    sum_generated = cons_tuple[2]
    consumable_to_send = consumables_to_send(num_days, sum_usage,
                         dock_days_list, per_crew, sum_generated,
                         crew_per_dock)
#debuging will delete later
   #print("result tup", result_tup)
   #print("dock days ls", dock_days_list)
   #print("num days", num_days)
   #print("crew_per_dock", crew_per_dock)
   #print ("consumable tup", cons_tuple)
   #print ("per crew", per_crew,)
   #print ("sum use ", sum_usage)
   #print("sum gen", sum_generated)        
   #print("consumables to send", consumable_to_send)
    ##RUN ALL or this wont work
    dock_days_list.pop()

    readable = pd.DataFrame(
        {'Docking Days': dock_days_list,
         'Amount of Consumable to Send': consumable_to_send
        })
    print(readable)
    
#display(readable) - only works for jupyter notebook 
#testing
consumable = 'Water'
consumable = 'Air'
consumable = 'Pretreat Tanks'

create_table(consumable)