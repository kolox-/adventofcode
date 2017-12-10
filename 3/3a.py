import sys
from math import fabs
test_input = 312051


# def get_side(num, layer, edge_len):
#     #min_ = (layer-1) * (layer-1)
#     max_ = edge_len * edge_len
#     # (0, bottom), (1, left), (2, top), (3, right)
#     side = (max_ - num) / (edge_len-1)
#     return side


def sq(x):
    return x * x

def gen_odd_num():
    for i in range(1,999999,2):
        yield i

def get_layer(num):
    for i, odd in enumerate(gen_odd_num()):
        if (odd*odd) >= num:
            return i, odd

def get_middle_of_edge(edge_len):
    # Even number allocated to each edge
    nums_per_edge = edge_len - 1
    # Because each edge starts one square in
    mid_num = (nums_per_edge/2) - 1
    return mid_num

def get_pos_on_edge(input_, edge_len):
    # Remove the number of squares in all previous layers
    total_position = input_ - sq(edge_len - 2)
    # Remove 1 to index from 0
    total_position -= 1
    # Mod to get position on just the relevant edge
    nums_per_edge = edge_len - 1
    return (total_position % (nums_per_edge))

input_ = test_input
layer, edge_len = get_layer(input_)

mid = get_middle_of_edge(edge_len)
pos = get_pos_on_edge(input_, edge_len)
dist_to_mid = fabs(pos - mid)
print dist_to_mid + layer
