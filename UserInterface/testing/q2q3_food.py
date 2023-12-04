#python code to run food algorithm and be able to output to html 
import pandas as pd
import datetime as dt
import math


def docking_days():
    flight_plan = pd.read_csv(r'/Users/eliza/Desktop/iss_flight_plan_20220101-20251231.csv')

    dock_days_list = flight_plan[flight_plan['event'] == 'Dock']['datedim'].to_list()

    dates_list = [dt.datetime.strptime(date, '%m/%d/%Y').date() for date in dock_days_list]


    num_days = pd.Series(dates_list).diff().dt.days.iloc[1:].astype(int).tolist()
    print("number of daays til next dock\n",num_days)

    flight_plan['datedim'] = pd.to_datetime(flight_plan['datedim'])

    dock_days_list_next2years = flight_plan[
        (flight_plan['datedim'].dt.year >= 2024) & 
        (flight_plan['datedim'].dt.year <= 2025) & 
        (flight_plan['event'] == 'Dock')
    ]['datedim'].to_list()

    return dock_days_list, num_days


#---------------------------------------------------------------------------
def crew_per_docking(dock_days_list):
    crewF = pd.read_csv(r'/Users/eliza/Desktop/iss_flight_plan_crew_20220101-20251321.csv')

    crew_per_dock = []

    for i, date in enumerate(dock_days_list):
        crewNum = crewF[crewF['datedim'] == date]['crew_count'].tolist()
        Amount = sum(crewNum)
        crew_per_dock.append(Amount)

    print("number of crew per docking\n",crew_per_dock)
    return crew_per_dock
#-----------------------------------------------------------------------------

def consumption_rates(consumable): 
    rater = pd.read_csv(r'/Users/eliza/Desktop/rates_definition.csv')


    #consumable must match a consumable on the rates csv. case sensitive.
    #consumable = 'Pretreat Tanks'
    #consumable = 'Air'
    #consumable = 'US Food BOBs'
    crew_used = 2.7

    sum_generated = sum(rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'generation')]['rate'].to_list())

    sum_usage = sum(rater[(rater['affected_consumable'] == consumable) & (rater['type'] == 'usage')]['rate'].to_list())

    crew_check = rater[rater['affected_consumable'] == consumable]['units'].tolist()
    combine =  '\t'.join(crew_check)

    if 'Crew' in combine:
        per_crew = True
    else:
        per_crew = False


    #prints
    print("Consumable used = ", sum_usage)
    print("Consumable generated = ", sum_generated)
    return per_crew, sum_usage, sum_generated

#--------------------------------------------------------------------------------

def consumables_to_send(num_days, sum_usage, dock_days_list, per_crew, sum_generated, crew_per_dock):
    listofrates = [sum_usage] * len(dock_days_list)
    consumable_to_send = []
    consumable_water_to_send = []
    consumable_water_to_send_new = []
    consumable_to_send_water = []
    current_sum = 0
    current_sum1 = 0
    current_sum2 = 0
    current_sum3 = 0
    res_list = []

    if(per_crew): #if percrew true change the list of rates
        for i in range(0, len(listofrates)):
            res_list.append(listofrates[i] * crew_per_dock[i])
    else:
        res_list = listofrates

    res_list.pop()
    res_list = [x - sum_generated for x in res_list]

    intermediate = []
    for i in range(0, len(res_list)):
        intermediate.append(res_list[i] * num_days[i])
    print ("amount of food need to send = ",intermediate)

    multiplied_crew_numbers = []

    for i in range(len(crew_per_dock)):
        multiplied_crew_numbers.append(crew_per_dock[i] * 2.7)

    for i, value in enumerate(intermediate):
        current_sum+=value
        consumable_to_send.append(math.trunc(current_sum))
        current_sum = current_sum - math.trunc(current_sum)


    for i, value in enumerate(multiplied_crew_numbers):
        current_sum1+=value
        consumable_water_to_send.append(math.trunc(current_sum1))
        current_sum1 = current_sum1 - math.trunc(current_sum1)

    need_to_send_list = []

    for i in range(len(intermediate)):
        x = 0.027 * num_days[i] * crew_per_dock[i]
        need_to_send_list.append(x)


    for i, value in enumerate(need_to_send_list):
        current_sum3+=value
        consumable_to_send_water.append(math.trunc(current_sum3))
        current_sum3 = current_sum3 - math.trunc(current_sum3)




    greatest_number = max(intermediate[26:63])
    print("The greatest number in the array is:", greatest_number)

    index_of_greatest_number = intermediate.index(greatest_number)
    print("The index of the greatest number is:", index_of_greatest_number)
    return need_to_send_list, index_of_greatest_number, greatest_number



#-----------------------------------------------------------------------------------

def create_table_food(consumable):
    ##RUN ALL or this wont work
    dock_days_tuple = docking_days()
    dock_days_list = dock_days_tuple[0]
    num_days = dock_days_tuple[1]
    crew_per_dock = crew_per_docking(dock_days_list)
    consumable_rates_tuple = consumption_rates(consumable)
    per_crew = consumable_rates_tuple[0]
    sum_usage = consumable_rates_tuple[1]
    sum_generated = consumable_rates_tuple[2]
    cts_tuple = consumables_to_send(num_days, sum_usage,
                                            dock_days_list, per_crew,
                                            sum_generated, crew_per_dock)
    need_to_send_list = cts_tuple[0]
    index_of_greatest_number = cts_tuple[1]
    g_qty = cts_tuple[2]
    dock_days_list.pop()
    #print(len(dock_days_list))
    readable = pd.DataFrame(
        {'Docking Days': dock_days_list,
         'Amount of Consumable to Send': need_to_send_list
        })
    #print(len(dock_days_list))
    #print(len(need_to_send_list))
    #print(dock_days_list[51])
    #table_data = readable.to_html(index=False)
    #print(table_data)
    #return table_data
    #testing 
    date = dock_days_list[index_of_greatest_number]
   
    return readable, date, g_qty, dock_days_list, need_to_send_list

#consumable = 'US Food BOBs'
#create_table_food(consumable)