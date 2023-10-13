"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(num_cof, price_cof):
    num_free_coffee = num_cof//9
    num_paid_coffee = num_cof - num_free_coffee
    return num_paid_coffee*price_cof

