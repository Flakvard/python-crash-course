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

aliens=[]

#Make a list of 30 aliesn
for alien_number in range (30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points']='10'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points']='15'

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("....")
#show how many aliesn have been created.
print(f"Total number of aliens: {len(aliens)}")