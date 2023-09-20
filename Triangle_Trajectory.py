#!/usr/bin/env python
import time
from flyt_python import api

# Connect to the drone
drone = api.navigation(timeout=120000)

# Wait for the drone interface to initialize properly
time.sleep(3)

print('--- Initiating Takeoff Till 10m')
drone.take_off(10.0)

print('--- Move in a triangular trajectory of side length 10m at a height of 10m')

print('--- Moving from Point X to Y of triangle XYZ')
drone.position_set(10.0, 0.0, 0.0, relative=True)

print('--- Moving from Point Y to Z of triangle XYZ')
drone.position_set(-5.0, 8.66, 0.0, relative=True)

print('--- Moving back to home position from Point Z to X of triangle XYZ')
drone.position_set(-5.0, -8.66, 0.0, relative=True)

print('--- Landing Initiated')
drone.land(async=False)

# Shutdown the instance
drone.disconnect()
