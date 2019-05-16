#!/usr/bin/env python

import numpy as np
import os
import sys

def getXYZdata(xyzFname):
    
    xyz = xyzFname
    print(xyz)

    xyzData = np.genfromtxt(fname=xyz, skip_header=2, dtype='unicode')

    return xyzData

def getElems(xyzData):
    
    elements = xyzData[:,0]

    return elements

def getCoords(xyzData):

    coordinates = xyzData[:,1:].astype(np.float)

    return coordinates

def calculateDistance(atom1, atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1: list
        A list of coordinates [x, y, z]
    atom2: list
        A list of coordinates [x, y, z]
    
    Returns
    -------
    distance: float
        The distance between atoms.

    Examples
    --------
    >>> calculateDistance([0,0,0], [0,0,1])
    1.0
    """
    
    x = atom1[0] - atom2[0]
    y = atom1[1] - atom2[1]
    z = atom1[2] - atom2[2]
    distance = np.sqrt(x**2 + y**2 + z**2)
    
    return distance

def bondCheck(bondDistance, minDist=0.0, maxDist=1.5):
    """
    Check if distance isa bond.

    Parameters
    ----------
    bondDistance: float
        The distance between atoms.
    minDist: float
        The minimum distance for a bond.
    maxDist: float
        The maximum distance for a bond.

    Returns
    -------
    boolean
        True if it is a bond.
        False if it is not a bond.
    """
    
    # Check that bondDistance is a float.
    if not isinstance(bondDistance, float):
        raise TypeError(F'bondDistance must be a type float. At the moment its type is {type(bondDistance)}')
    
    if (bondDistance > minDist) and (bondDistance < maxDist):
        return True
    
    else:
        return False

def getDistStrings(elements, coordinates):
    
    string = ""
    
    for idx1, atom1 in enumerate(coordinates):

        for idx2, atom2 in enumerate(coordinates):
            
            if (idx1 > idx2):
                dist = calculateDistance(atom1, atom2)
                
                if bondCheck(dist, maxDist=1.5):   # Specifying only one default value.
                    string += F'{elements[idx1]} to {elements[idx2]}: {dist:.3f}\n'

    return string[:-1]

if __name__ == "__main__":

    if (len(sys.argv) < 2):
        raise IndexError("No file name given. Script requires an xyz file.")
    
    xyzData = getXYZdata(sys.argv[1])
    
    elements = getElems(xyzData)
    coordinates = getCoords(xyzData)
    
    string = getDistStrings(elements, coordinates)
    print(string)
