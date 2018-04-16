# create your lists and change the index, e.g. Ext_temp_01 - Ext_temp_02 - ... - Ext_temp_24
# Some random lists of external temperatures were created below for the purpose of testing the algorithm
Ext_temp_01 = [22.6, 22.5, 21.7, 24.2, 22.9, 23.1, 21.8, 22.0, 21.5, 20.3, 22.1, 24.0,
            22.2, 22.1, 21.0, 24.6, 22.7, 23.8, 21.4, 22.6, 21.2, 20.6, 22.9, 24.5]
Ext_temp_02 = [22.6, 22.5, 21.7, 24.2, 22.9, 23.1, 21.8, 22.0, 21.5, 20.3, 22.1, 24.0,
            22.2, 22.1, 21.0, 24.6, 22.7, 23.8, 21.4, 22.6, 21.2, 20.6, 22.9, 24.5]

# Below, is the name_list of all the lists introduced above, list them all here:
Ext_temp_list = [Ext_temp_01, Ext_temp_02]

# Change the constant values below:
HEAT_TRANSFER = 0.5
AIR_MASS = 11
AIR_CAP = 22
WATER_CAP = 33
WATER_VAP = 44
T_out = []


def Q_trans_calculator(ext_list, init_temp):
    """This method generates the corresponding Q of your initially introduced temperature
    and it'll sum 'em all up to generate the total_Q; the total_Q will be sent to temp_output method
    to re-generate the next initial temperature.
    """
    Q_Trans = []
    for temperature in ext_list:
        Q_Trans.append(HEAT_TRANSFER*(temperature - init_temp))
    return temp_output(sum(Q_Trans))


def temp_output(total_q):
    """This method receives the total_Q value from the Q_trans_calculator method and it 
    re-generates the next initial temperature; the total_Q and the initial temperature
    used for the current iteration will be printed as well.
    """
    print("Sum of Q_trans--> {}\nInitial Temprature--> {} C\n". format(total_q, T_out[-1]))
    print((total_q / (AIR_MASS * (AIR_CAP + WATER_CAP * WATER_VAP))) - T_out[-1])
    return (total_q / (AIR_MASS * (AIR_CAP + WATER_CAP * WATER_VAP))) - T_out[-1]


def main():
    """This main method counts the lists within the Ext_temp_list that you've already
     generated and it'll go through every external temperatures that you have introduced
    in them; each iteration will be initialized with T_out = 18 and after each cycle is done,
    it will be reset to 18 for the next cycle."""
    for idx, lists in enumerate(Ext_temp_list):
        T_out.append(18)  # define your initial temperature here
        for idy, _ in enumerate(lists):
            print("Iteration {} from the list #{}:".format(idy+1, idx+1))
            T_out.append(Q_trans_calculator(lists, T_out[-1]))
        print("|##########################################|")


if __name__ == '__main__':
    main()
