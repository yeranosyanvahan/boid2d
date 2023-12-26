# Boids Simulation

## Introduction
This Python-based project offers a dynamic and interactive simulation of bird-like entities, known as "boids", in a virtual atmospheric environment. The simulation showcases the behavior of individual boids as well as their interactions in a group.

## Table of Contents
- [Introduction](#introduction)
- [Demonstrations](#demonstrations)
- [Forces](#forces)
  - [Flap](#flap)
- [Atmosphere](#atmosphere)
- [Constants and Properties](#constants-and-properties-in-the-simulation)
- [Assumptions of the Model](#assumptions-of-the-model)
- [Contributing](#contributing)
- [Bug Reporting](#bug-reporting)
- [License](#license)

## Demonstrations
NOTE: In the simulation:
- The drag force and the velocity of the boid is represented in  <span style="color:red;">red</span>.
- The lift force is represented in  <span style="color:green;">green</span>.
- The gravity force is represented in <span style="color:gray;">black</span>.
- A change in the boid's color indicates that it has executed a flap.


**[Single Boid Simulation](./amt/singleboid.mp4)**: Observe the behavior of a single boid navigating through the atmosphere.  
 
https://github.com/yeranosyanvahan/boid2d/assets/69711561/910e1a0d-60fd-41d7-9a07-444a43422b20

**[Many Boids Simulation](./amt/manyboids.mp4)**: Here each boid has a specific Vx starting velocity. This video shows the one that goes the furthest.
  
https://github.com/yeranosyanvahan/boid2d/assets/69711561/e6296b19-b755-449a-ac65-f3a09d81ecdf

## Forces
In this project, three fundamental forces are simulated to mimic the realistic movement of boids. Those equations are:

  $$ F_{\text{drag}} = \frac{1}{2} \rho v^2 A_{\text{drag}} $$

  $$ F_{\text{lift}} = R_{\text{LTD}} \cdot F_{\text{drag}}  $$
  
  $$ F_{\text{gravity}} = m g $$

  where:
  - $F_{\text{drag}}$ is the drag force,
  - $F_{\text{lift}}$ is the lift force,
  - $F_{\text{gravity}}$ is the gravitational force,
  - $\rho$ is the mass density of the air,
  - $v$ is the flow velocity relative to the boid,
  - $A_{\text{drag}}$ is the drag area,
  - $R_{\text{LTD}}$ is the Lift-to-Drag Ratio,
  - $m$ is the mass of the boid, and
  - $g$ is the acceleration due to gravity on Earth.


### **Flap**
Instead of traditional thrust, the simulation uses a flap mechanism to propel the boids. Each flap provides an energy boost to the boid, increasing its kinetic energy and thus influencing its movement and trajectory in the simulation. The energy dynamics during a flap are described by the following equation:

  $$ E_{\text{before}} = E_{\text{after}} + E_{\text{flap}} $$

  where:
  - $E_{\text{before}}$ is the kinetic energy of the boid before doing one flap,
  - $E_{\text{after}}$ is the kinetic energy of the boid after doing one flap, and
  - $E_{\text{flap}}$ represents the additional kinetic energy added to the boid as a result of the flap.

## Atmosphere

In studying the behavior of the atmosphere at different altitudes, several key equations come into play. These equations help in understanding how temperature, pressure, and density vary with altitude. This ensures that the boids won't fly as high as they can limiting their ability to the limits of the atmosphere.


$$ T(h) = T_0 \left(1 - \frac{h}{h_0}\right) $$
$$ P(h) = P_0 \left(1 - \frac{h}{h_0}\right)^{\frac{\gamma}{\gamma - 1}} $$
$$ \rho(h) = \rho_0 \left(1 - \frac{h}{h_0}\right)^{\frac{1}{\gamma - 1}} $$

where:
- $T(h)$ is the temperature at height $h$,
- $P(h)$ is the pressure at height $h$,
- $\rho(h)$ is the mass density at height $h$,
- $T_0$ is the sea level air temperature,
- $P_0$ is the sea level air pressure,
- $\rho_0$ is the sea level air mass density,
- $h$ is the altitude,
- $h_0$ is the height of the atmosphere, and
- $\gamma$ is the adiabatic index.


## Constants and Properties in the Simulation

- ### Boid properties
  - LTDRatio [ $R_{\text{LTD}}$ ] = 15
  - DragArea [ $A_{\text{drag}}$ ] = 50 cm²
  - Mass [ $m$ ] = 1 kg
  - FlapEnergy [ $E_{\text{flap}}$ ] = 10 J
  - MaxFlapsPerSecond = 3 

- ### Atmosphere properties
  - SeaLevelAirDensity [ $\rho_0$ ] = 1.225 kg/m³
  - SeaLevelAirPressure [ $P_0$ ] = 101.325 kPa
  - SeaLevelAirTemperature [ $T_0$ ] = 15 °C
  - AirAdiabaticIndex [ $\gamma$ ] = 1.4
  - AtmosphereHeight [ $h_0$ ] = 30 km
  - AirMolarMass [ $M_\text{air}$ ] = 28.97 g/mol
  - GravitationalPull [ $g$ ] = 9.81 m/s²


## Assumptions of the Model

### 1. Dry Atmosphere
The model closely follows the dry adiabatic lapse rate for temperature, hence the pressure, and density are calculated accordingly. It assumes an atmosphere comprised solely of air, without water vapor. Although this assumption slightly deviates from reality, it generally maintains the correct order of magnitude for these parameters.

### 2. Subsonic Speeds Within Specific Range
Air speeds ranging from 3 to 50 meters per second are assumed, falling within the subsonic category. Within this range, Lift-Induced drag is predominant, while parasite drag is less significant. The primary way for lift generation relies on adjusting the angle of attack.

### 3. No Inter-Boid Interaction
In this simulation, boids operate independently without any interaction or influence from other boids.


## Assumptions of the model

1. Dry atmosphere
 When the temperature lapse rate is calculated, it will closely follow the dry adiabatic lapse rate. This holds true for temperature, pressure and density. It assumes that the atmosphere consists only with air, no water molecules. This assumption does deviate from the actual numbers, but the order of magniute is generally preserved.

2. Relatively slow subsonic speeds
 This model assumes air speed from 3 to 50 meters per second. This is in the range, where Lift-Induced drag is the most significant drag and the parasite drag is not significant. The main way to generate lift is through correcting the angle of attack

3. No interaction
 The boids do not interact with each other at all.

## Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Bug Reporting
If you encounter any bugs or issues, please report them on the [Issues page](https://github.com/yeranosyanvahan/boid2d/issues). Include as much detail as possible, such as the steps to reproduce the bug and any error messages.

## License
Distributed under the MIT License. See `LICENSE` for more information.