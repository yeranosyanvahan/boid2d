import numpy as np
import time
import math

class Conversion:
    KilometerToMeter = 1000
    KilopascalToPascal = 1000
    KelvinToCelcius = 273.15
    CelciusToKelvin = -273.15
    CentimeterToMeter = 1e-2

class Atmosphere:
    SeaLevelAirDensity = 1.225 # kg/m^3
    SeaLevelAirPressure = 101.325 # kPa
    SeaLevelAirTemperature = 15 # °C

    AirAdiabaticIndex = 1.4
    AtmosphereHeight = 30 # km
    AirMolarMass = 28.97 # g/mol
    GravitationalPull =  9.81 # m/s^2

    def __init__(self, height):
        """
        height of the point in meters
        """
        self.height = height
        self.relheight = height / (Atmosphere.AtmosphereHeight * Conversion.KilometerToMeter)


    @property
    def temperature(self):
        _temperature_in_kelvin = (Atmosphere.SeaLevelAirTemperature + Conversion.KelvinToCelcius) * ( 1 - self.relheight)
        return _temperature_in_kelvin + Conversion.CelciusToKelvin
    
    @property
    def pressure(self):
        powerindex = Atmosphere.AirAdiabaticIndex / ( Atmosphere.AirAdiabaticIndex - 1 )
        return Atmosphere.SeaLevelAirPressure * ( ( 1 - self.relheight) ** powerindex )
    
    @property
    def density(self):
        powerindex = 1 / ( Atmosphere.AirAdiabaticIndex - 1 )
        return Atmosphere.SeaLevelAirDensity * ( ( 1 - self.relheight) ** powerindex )


class Boid2D:
    LTDRatio = 15
    DragArea = 50 # cm^2
    Mass = 1 # kg
    FlapEnergy = 10 # J
    MaxFlapsPerSecond = 3 # Maximum flap per second

    def __init__(self, Vx = 0, Vy = 0, X = 0, Y = 0):
        self.Vx = Vx
        self.Vy = Vy
        self.X = X
        self.Y = Y
        self.last_flap_time = 0
        self.atmosphere = Atmosphere(height = Y)
    
    def can_flap(self):
            time_since_last_flap = time.time() - self.last_flap_time
            return time_since_last_flap >= (1 / Boid2D.MaxFlapsPerSecond)

    @property
    def drag(self):
        absFx = self.atmosphere.density * Boid2D.DragArea * (Conversion.CentimeterToMeter **2 ) * (self.Vx ** 2) / 2
        absFy = self.atmosphere.density * Boid2D.DragArea * (Conversion.CentimeterToMeter **2 ) * (self.Vy ** 2) / 2
        dirVx = 2 * (self.Vx > 0) - 1
        dirVy = 2 * (self.Vy > 0) - 1
        return (-dirVx * absFx , -dirVy * absFy)

    @property    
    def lift(self):
        absFy = Boid2D.LTDRatio * self.atmosphere.density * Boid2D.DragArea * (Conversion.CentimeterToMeter **2 ) * (self.Vx ** 2) / 2
        absFx = Boid2D.LTDRatio * self.atmosphere.density * Boid2D.DragArea * (Conversion.CentimeterToMeter **2 ) * (self.Vy ** 2) / 2
        
        dirVx = 2 * (self.Vx > 0) - 1
        dirVy = 2 * (self.Vy > 0) - 1

        return (-dirVy * absFx, dirVx * absFy)
    
    @property
    def gravity(self):
        return ( 0, - self.Mass * self.atmosphere.GravitationalPull )

    @property
    def energy(self):
        return self.kinetic_energy + self.potential_energy
    
    @property
    def potential_energy(self):
        return self.Mass * self.atmosphere.GravitationalPull * self.Y 

    @property
    def kinetic_energy(self):
        return self.Mass * ((self.Vx**2 + self.Vy**2 ) / 2)

    @property
    def V(self):
        return np.sqrt(self.Vx**2 + self.Vy **2)

    def flap(self):
        if self.can_flap():
            current_ke = self.kinetic_energy

            new_ke = current_ke + Boid2D.FlapEnergy

            new_velocity_magnitude = math.sqrt(2 * new_ke / self.Mass)

            current_velocity_direction = math.atan2(self.Vy, self.Vx)

            self.Vx = new_velocity_magnitude * math.cos(current_velocity_direction)
            self.Vy = new_velocity_magnitude * math.sin(current_velocity_direction)            

            self.last_flap_time = time.time()
            return True
        
        return False