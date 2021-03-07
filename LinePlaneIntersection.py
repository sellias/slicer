#!/bin/python
# ----------------------------------------------------------------
#	implement line plane intersection function
#
#	THIS SCRIPT IS FOR THE INCLUSION OF NON-ORIGINAL WORK
#	the work represented here can be found at these URLs
#
#   https://bit.ly/3v4dBdA
#	https://bit.ly/3v1raKz
# ----------------------------------------------------------------
from __future__ import print_function
import numpy as np
 
def LinePlaneIntersection(planeNormal, planePoint, rayDirection, rayPoint, epsilon=1e-6):
 
	ndotu = planeNormal.dot(rayDirection)
	if abs(ndotu) < epsilon:
		raise RuntimeError("no intersection or line is within plane")
 
	w = rayPoint - planePoint
	si = -planeNormal.dot(w) / ndotu
	Psi = w + si * rayDirection + planePoint
	return Psi


if __name__=="__main__":
	#Define plane
	planeNormal = np.array([0, 0, 1])
	planePoint = np.array([0, 0, 5]) #Any point on the plane
 
	#Define ray
	rayDirection = np.array([0, -1, -1])
	rayPoint = np.array([0, 0, 10]) #Any point along the ray

    #Calculate Collision Point
	Psi = LinePlaneIntersection(planeNormal, planePoint, rayDirection, rayPoint)
	print ("intersection at", Psi)