from vpython import *
#Web VPython 3.2
# PROJ1-Q3
# Author: MAHEEN & VALERIE
# Class: PHYS1454

#creating the objects:
rocket = cylinder(pos = vec(0, 0, 0), axis = vec(0, 20, 0), radius = 100, color = color.yellow, make_trail = True, trail_color = color.cyan)
earthSur = sphere (pos=vector(0, 0, 0), size = vector (1000, 1000, 1000),color = color.blue)

#initial velocity before the launch
rocket.velocity = vec(0, 0, 0)
#values provided in the table:
#subtracting total mass 433,100 - propellant_mass 321,600 in order to get mass of the rocket = 111,500 kgs
rocket.mass = 111500
#propellant_mass provided in the Q
rocket.propellant_mass = 321600
#exhaust_velocity provided in the Q- (velocity at which gases leaves the nozzle)- keeping it -ive or it goes -y direction 
exhaust_velocity = vec(0, -2766, 0)
#keeping it -ive or it goes -y direction- thrust/exhaust = rocket_burn 
rocket_burn = -2750.18
#thrust(Force) provided in the Q
thrust = 7607000
# create time variable, t, and time step, dt
t = 0
dt = 0.01
#since mass of rocket is changing so its equal to dt * rocket_burn// as rocket_burn is dm/dt
changeinmass = rocket_burn * dt 

#graph plots for pos vs t, vel vs t, acc vs t
gra1= graph(xtitle = "time", ytitle=" Pos")
gra2= graph (xtitle = "time", ytitle=" Vel")
gra3= graph (xtitle = "time", ytitle = "Acc")
    
#creating a new variable by using the variable gra and gcurve function
gra1_Pos= gcurve(color=color.black,graph=gra1) 
gra2_Vel= gcurve(color=color.black,graph=gra2) 
gra3_Acc= gcurve(color= color.black,graph=gra3) 
#setting the camera to only focus on the motion of rocket
scene.camera.follow(rocket)
# loop to animate the fly
while (rocket.propellant_mass > 0):
    #could use 1000 to increase the speed
    rate(500)   
    #update rocket's position, velocity, and acceleration
    #dividing the change in mass that we got from the rocket_burn and dt and divide it by the total mass of rocket and prop mass and multiplied by the exhaust velcoity in order to get the new velocity
    rocket.velocity = rocket.velocity + (changeinmass  / (rocket.mass + rocket.propellant_mass)) * (exhaust_velocity)
    #rocket.velocity = rocket.velocity + log (rocket.mass/(rocket.mass + rocket.propellant_mass)) * exhaust_velocity
    #updating the inital pos by adding velocity and time multiplied ; pos = vel * t
    rocket.pos = rocket.pos + rocket.velocity * dt
    #update the propellant mass 
    rocket.propellant_mass = rocket.propellant_mass + changeinmass
    #acc = force/total mass of rocket and propellent 
    rocket.acceleration = (thrust/(rocket.mass + rocket.propellant_mass))
    
    # update time variable 
    t = t + dt
    
    #inorder to plot a vector component, we add .y to pos vector and velocity vector but not to acceleration bc we used the scalar values to find the acceleration
    gra1_Pos.plot(t,rocket.pos.y)
    gra2_Vel.plot(t,rocket.velocity.y)
    gra3_Acc.plot(t,rocket.acceleration)
 #output  
print("Final velocity of the rocket =  " + rocket.velocity + " m/s and the rocket takes = " + t + " seconds to burn through the fuel\n")