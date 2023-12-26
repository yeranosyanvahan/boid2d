# Boids Simulation

## Introduction
This Python-based project offers a dynamic and interactive simulation of bird-like entities, known as "boids", in a virtual atmospheric environment. The simulation showcases the behavior of individual boids as well as their interactions in a group.

## Forces
In this project, three fundamental forces are simulated to mimic the realistic movement of boids. Those equations are:

  $$ F_{\text{drag}} = \frac{1}{2} \rho v^2 A_{\text{drag}} $$

  $$ F_{\text{lift}} = R_{\text{LTD}} F_{\text{drag}}  $$
  
  $$ F_{\text{gravity}} = m \cdot g $$

  where:
  - $F_{\text{drag}}$ is the resistance force experienced by a boid moving through the air.
  - $\rho$ is the air density.
  - $v$ is the velocity of the boid.
  - $A_{\text{drag}}$ is the drag area.
  - $F_{\text{lift}}$ is the upward force enabling the boid to counteract gravity.
  - $R_{\text{LTD}}$ is the Lift-to-Drag Ratio, which amplifies the drag force to determine the lift force.
  - $F_{\text{gravity}}$ is the gravitational force acting downwards on the boid. This force is a product of the boid's mass and the gravitational acceleration, pulling the boid towards the earth.
  - $m$ is the mass of the boid, which plays a crucial role in determining both the gravitational force acting on the boid and its inertia.
  - $g$ is the acceleration due to gravity, a constant value that represents the strength of the gravitational pull exerted by the earth.


### **Flap**
Instead of traditional thrust, the simulation uses a flap mechanism to propel the boids. Each flap provides an energy boost to the boid, increasing its kinetic energy and thus influencing its movement and trajectory in the simulation. The energy dynamics during a flap are described by the following equation:

  $$ E_{\text{before}} = E_{\text{after}} + E_{\text{flap}} $$

  where:
  - $E_{\text{before}}$ is the kinetic energy of the boid before executing a flap.
  - $E_{\text{after}}$ is the kinetic energy of the boid after executing a flap.
  - $E_{\text{flap}}$ represents the additional kinetic energy imparted to the boid as a result of the flap.


## Demonstrations
NOTE: In the simulation:
- The drag force and the velocity of the boid is represented in  <span style="color:red;">red</span>.
- The lift force is represented in  <span style="color:green;">green</span>.
- The gravity force is represented in <span style="color:gray;">black</span>.


**[Single Boid Simulation](./amt/singleboid.mp4)**: Observe the behavior of a single boid navigating through the atmosphere.  
 
https://github.com/yeranosyanvahan/boid2d/assets/69711561/910e1a0d-60fd-41d7-9a07-444a43422b20

**[Many Boids Simulation](./amt/manyboids.mp4)**: Here each boid has a specific Vx starting velocity. This video shows the one that goes the furthest.
  
https://github.com/yeranosyanvahan/boid2d/assets/69711561/e6296b19-b755-449a-ac65-f3a09d81ecdf

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

