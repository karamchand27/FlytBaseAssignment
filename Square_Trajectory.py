#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # Create a Flyt drone navigation instance

time.sleep(3)

print('Mission Objective - Takeoff at 5m, move in a square trajectory ABCD of side length 6.5m at a height of 5m, and land once the entire mission is over')
print('-- UAV initating takeoff to a height of 5m --')
drone.take_off(5.0)
print('Current position: Point A of square ABCD')

print('Moving in a square trajectory of side length 6.5m at a height of 5m')

print('-- Moving to Point B of square ABCD...')
drone.position_set(6.5, 0, 0, yaw=1.0472, relative=True)

print('-- Moving to Point C of square ABCD...')
drone.position_set(0, 6.5, 0, relative=True)

print('-- Moving to point D of square ABCD...')
drone.position_set(-6.5, 0, 0, relative=True)

print('-- Returning to Point A of square ABCD...')
drone.position_set(0, -6.5, 0, relative=True)

print('Landing Initiated')
drone.land(async=False)

# Disconnect from the Flyt navigation API
drone.disconnect()

