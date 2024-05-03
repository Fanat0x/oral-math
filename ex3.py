import matplotlib.pyplot as plt

gravity = 9.8
mass = 12
force = 200
drag_coef = 0.4
reference_area = 98.17

speed = 0
accel = 0

step_time = 1
total_time = 10

masse_volumique_eau = 997
volume_eau_deplace = 14335

def scalaire(xU, xV, yU, yV):
    return xU * xV + yU * yV

def gravity_with_mass():
    g = mass * gravity
    return (0, g)

def archimede(p, V, g):
    return p * V * g

X = [0]
Y = [0]

def canFloat(p, V, g):
    if abs(archimede(p, V, g)) > abs(gravity_with_mass()[1]):
        return False
    else:
        return True
    
def frottements(speed):
    return 0.5*masse_volumique_eau * reference_area * drag_coef * speed**2

def acceleration(force, frottements):
    return 0

for i in range(1, total_time-1):
    accel = force/mass
    speed = speed + accel #- (frottements(speed+accel))
    X.append(X[i-1] + speed * step_time)
    
    if not canFloat(masse_volumique_eau, volume_eau_deplace, gravity_with_mass()[1]):
        Y.append(Y[i-1] - step_time * gravity_with_mass()[1])
    else:
        Y.append(Y[i-1])

plt.plot(X, Y)
plt.xlabel('Distance (m)')
plt.ylabel('Depth (m)')
plt.title('Neptune')
plt.show()