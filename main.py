# Define classes for system, bodies and maybe natural satellites
# Prototype 3D simulation for 2 body system

def gravitational_force(mass1, mass2, distance):
    """Calcuates the gravitational force between two bodies"""

    G = 6.67 * 10 ** (-11)
    return (G * mass1 * mass2) / (distance ** 2)


def acceleration(force, mass):
    """Calculates acceleration due to gravity of an object towards """

    return force / mass


class SolarSystem:
    """"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"Solar system: {self.name}"


class CelestialBody:
    """"""


if __name__ == "__main__":
    mass_earth = 5.97 * 10 ** 24
    mass_moon = 7.35 * 10 ** 22
    distance = 3.844 * 10 ** 8

    g_force = gravitational_force(mass_earth, mass_moon, distance)
    accel_moon = acceleration(g_force, mass_moon)
    accel_earth = acceleration(g_force, mass_earth)

    print(f"Gravitational force between Earth and Moon: {g_force}")
    print(f"Earth acceleration towards Moon: {accel_earth} \nMoon acceleration towards Earth: {accel_moon}")
    # print(SolarSystem("Mike"))
