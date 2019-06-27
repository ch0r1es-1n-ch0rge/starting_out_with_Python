# In physics, an object that is in motion is said to have kinetic energy. The following formula can be used to determine
# a moving object's kinetic energy:
#                                       KE = 1/2mv^2
# The variables in the formula ae as follows: KE is the kinetic energy, m is the object's mass in kilograms, and v is
# the object's velocity in meters per second.
# Write a functions named kinetic_energy that accepts an object's mass (in kilograms) and velocity (in meters per
# second) as arguments. The function should return the amount of kinetic energy that the object has. Write a program
# that asks the user to enter values for mass and velocity, then calls the kinetic_energy function to get the object's
# kinetic energy.


# Create Main Function
def main():
    user_mass = float(input('Enter the mass (in kilograms) of the moving object: '))
    user_velocity = float(input('Enter the velocity (in meters per second) of the moving object: '))
    ke = kinetic_energy(user_mass, user_velocity)
    print('With a mass of:', format(user_mass, ',.2f'), 'kilograms', 'and a velocity of:', user_velocity,
          'meters per second.')
    print('The kinetic energy of the object is:', ke)


def kinetic_energy(mass, velocity):
    ke = (1 / 2) * mass * (velocity ** 2)
    return format(ke, ',.2f')


main()
