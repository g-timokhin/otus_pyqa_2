""" This module contains functions for triangles geometry"""
import math


def inequality(side_a: float, side_b: float, side_c: float):
    if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
        return True


def tri_area(side_a: float, side_b: float, side_c: float):
    semi_per = (side_a + side_b + side_c)*0.5
    product = (semi_per - side_a) * (semi_per - side_b) * (semi_per - side_c) * semi_per
    return math.sqrt(product)

