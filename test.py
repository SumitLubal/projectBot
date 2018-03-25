# format is [leg][min,max,center]
leg_limits  = [[100,500,250],[100,550,340],[110,580,350],[110,580,350],[100,500,250],[100,500,330],[110,570,300],[120,580,280],[210,550,330],[120,550,330],[120,510,270],[170,570,300],[130,570,350],[130,540,280],[130,550,350],[140,540,350]]
ancle_right = [0,4,7]
knee_right = [1,5,8]
pelvic_right = [2,3,6]
ancle_left = [13,10]
knee_left = [14,9]
pelvic_left = [15,12,11]
#bring all to center
#bring ancle righ to center
for x in ancle_right:
    val = leg_limits[x][2]
