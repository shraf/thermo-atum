import math
import utils.main as utils
import numpy as np
import scipy.constants as constants
IDEAL_GAS = 8.3143
PLANCK = constants.Planck
BOLTZMANN = constants.Boltzmann
temp_rate = 10

def calculate_sheet_data(sheet, start=0, end=-1):
    if end == -1:
        end = len(sheet.index)
    initial_row = sheet.iloc[start]
    final_row = sheet.iloc[end]
    new_data = []
    x_values = []
    y_values = []
    for indx, row in sheet.iloc[start:end].iterrows():
        row_data = calculate_row_data(row, initial_row, final_row)
        if row_data['y_axis'] is not None and row_data['x_axis'] is not None:
            y_values.append(row_data['y_axis'])
            x_values.append(row_data['x_axis'])
        new_data.append(row_data)
    linear_fit = calculate_linear_fit(x_values, y_values)
    for row in new_data:
        row['y_fitted'] = calculate_y(row['x_axis'], linear_fit['slope'], linear_fit['intercept'])
    activation_energy = calculate_activation_energy(linear_fit['slope'])
    final_temp = utils.convert_from_celsius_to_kelvin(final_row[0])
    enthalapy = calculate_enthalapy(activation_energy, final_temp)
    gibbs_free_energy = calculate_gibbs_free_energy(activation_energy, final_temp, linear_fit['intercept'], temp_rate)
    entropy = calculate_entropy(enthalapy, gibbs_free_energy, final_temp)
    new_data[0]['activation_energy'] = activation_energy
    new_data[0]['entropy'] = entropy
    new_data[0]['enthalapy'] = enthalapy
    new_data[0]['gibs_free_energy'] = gibbs_free_energy
    return new_data
                         

def calculate_row_data(row, initial_row, final_row):
    temp = row[0]
    temp_kel = utils.convert_from_celsius_to_kelvin(temp)
    x_axis = get_x_axis(temp_kel)
    y_axis = get_y_axis(temp, initial_row[0], final_row[0])
    return {
        "x_axis":x_axis,
        "y_axis": y_axis
    }

def calculate_entropy(enthalapy, gibbs, temp_final):
    return (enthalapy-gibbs)/temp_final

def calculate_enthalapy(activation_energy, avg_temp):
    return activation_energy- IDEAL_GAS * avg_temp

def calculate_gibbs_free_energy(activation_energy, temp_final, intercept, temp_rate):
    bks = utils.convert_from_celsius_to_kelvin(temp_rate)/60
    a = (math.e**intercept)*(bks*activation_energy/IDEAL_GAS)
    return activation_energy + (IDEAL_GAS*temp_final* math.log(BOLTZMANN*temp_final/(PLANCK*a)))

def calculate_axis_linear_fit(row ,slope, intercept):
    return calculate_y(row[0], slope, intercept) 

def get_x_axis(temp: int):
    return 1000/temp

def get_y_axis(temp, temp_initial, temp_final):
    alpha = get_alpha(temp, temp_initial, temp_final)
    if alpha >= 1:
        return None
    beta = math.log(1-alpha)/temp**2
    if beta*-1 <=0:
        return None
    return math.log(beta * -1)

def get_alpha(val, valInitial, valFinal):
    return (valInitial - val)/(valInitial - valFinal)

def calculate_linear_fit(x_values, y_values):
    x = np.array(x_values)
    y = np.array(y_values)
    [slope, intercept] =np.linalg.lstsq(np.column_stack([x, np.ones(len(x))]), y, rcond=None)[0]
    return {"slope":slope, "intercept":intercept}

def calculate_y(x, slope, intercept):
    return intercept + slope*x


def calculate_activation_energy(slope):
    return slope * IDEAL_GAS * 1000*-1