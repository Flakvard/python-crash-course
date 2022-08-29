alien_0 = {'color':'red','points':5}
print (alien_0)

print(alien_0['color'])

print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print (alien_0)

alien_1 = {}

alien_1['color'] = "yellow"
alien_1['points'] = 8
alien_1['x_position'] = 5
alien_1['y_position'] = 5

print (alien_1)

alien_0['speed'] = "medium"

if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position']+x_increment
print(f"New position: {alien_0['x_position']}")

alien_3 = {'color':'red','speed':'slow'} #'points':5 - Use get() when there is no value assigned
point_value = alien_3.get('points','No point value assigned.')
print (point_value)