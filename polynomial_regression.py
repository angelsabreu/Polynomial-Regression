# When a car doubles its speed, its braking distance doesn't just double, it quadruples 
# because kinetic energy grows with the square of speed (v^2).
# Here are the test results for a car

# Speed (x in 10s of mph) | Braking Distance (y in feet)
# 1 (10 mph)              | 2
# 2 (20 mph)              | 8
# 3 (30 mph)              | 18
# 4 (40 mph)              | 32

# speed = [1, 2, 3, 4]
# braking_distance = [2, 8, 18, 32]

# def braking_distance(speed):
#     return 2 * (speed ** 2)

# for x in range(1, 11):
#     mph = x * 10
#     print(f"Speed: {mph} mph | Braking Distance: {braking_distance(x)} feet.")


# speeds = [1, 2, 3, 4]
# actual_distances = [2, 8, 18, 32]
# speeds_squared = [s**2 for s in speeds]
# print("Squared speeds (x^2):", speeds_squared)

# weight = 2.0
# predictions = [weight *s2 for s2 in speeds_squared]
# print("Predicted Distances: ", predictions)
# new_speed = 5
# new_prediction = weight * (new_speed ** 2)

# print(f"Braking distance for speed {new_speed}: {new_prediction} feet")


# When you drop a ball from a tower, it accelerates due to gravity. 
# The distance it falls doesn't increase by a fixed number each second—it 
# scales with the square of time (t2). 

# Time (t in seconds) | Distance Fallen (y in meters)
# 1                   | 5
# 2                   | 20
# 3                   | 45
# 4                   | 80

# The Pattern: Distance = 5.0 * (t ** 2)
# Task: Create the t2 feature and predict how far the ball falls after 6 seconds.

time = [1, 2, 3, 4]
distance_fallen = [5, 20, 45, 80]
times_squared = [t**2 for t in time]
print("Squared times (t^2):", times_squared)

weight = 5.0
predictions = [weight *t2 for t2 in times_squared]
print("Predicted Distances: ", predictions)

new_time = 6
new_prediction = weight * (new_time ** 2)
print(f"Distance fallen after {new_time} seconds: {new_prediction} meters")