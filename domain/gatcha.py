from core.sheet import open_sheet
import random


element = open_sheet('element_gatcha')
parts = open_sheet('parts_gatcha')

# 축적되는 가중치 가챠
def weighted_gatcha():
    element_name = []
    element_weight = []

    for name, weight in element:
        element_name.append(name)
        element_weight.append(int(weight))
    result = random.choices(element_name, cum_weights=element_weight, k=1)

    return result


# 확률 가챠
def rated_gatcha(): 
    parts_name = []
    parts_rate = []

    for name, rate in parts:
        parts_name.append(name)
        parts_rate.append(int(rate))
    result = random.choices(parts_name, weights=parts_rate, k=1)

    return result
