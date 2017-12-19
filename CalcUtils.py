#!/usr/bin/python

"""

Riple-drive Project

Helper functions

"""
import math

def dist( a, b ):
    return math.sqrt( ( a * a ) + ( b * b ) )

def get_y_angle( x, y, z ):
    radians = math.atan2( x, dist( y, z ) )
    return -math.degrees( radians )

def get_x_angle( x, y, z ):
    radians = math.atan2( y, dist( x,z ) )
    return math.degrees( radians )

def transform_data( high, low, little-endian=True, twos_complement=True ):
    """
    This functino concatenates two 8-bit register values: high and low.
    The output is a decimal in little-endian
    """
    # if big-endian, swaps bytes
    if little-endian:
        val = ( high << 8 ) | low
    else:
        val = ( low << 8 ) | high
    if twos_complement:
        if ( val >= 1 << 15 ):
            # 2's complement
            return -( ( (1 << 16) - 1 - val) + 1)
    return val
