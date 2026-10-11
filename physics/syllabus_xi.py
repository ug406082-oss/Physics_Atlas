"""The AKU-EB Physics HSSC Syllabus 2025, Part I (Grade XI), verbatim.

This module is the single source of truth for the 185 student learning
outcomes of Grade XI. Every chapter data file must match it exactly, and the
test suite enforces that. The wording is the published wording, including the
syllabus's own capitalisation and punctuation, so that a learner holding the
book and a learner using this app are reading the same list.

Twelve outcomes lost their text when the source PDF was extracted. Those are
reconstructed in ``REVIEWED`` and must be checked against the PDF by hand.
"""

from __future__ import annotations

__all__ = ["OUTCOMES", "CHAPTERS", "REVIEWED", "topics", "outcome", "chapter_ids"]

#: The outcomes whose wording had to be reconstructed, with what was used.
REVIEWED = {
    "1.1.4": ("Discuss derived units as products or quotients of the SI base units.", "*"),
    "10.11.1": ("Explain 'entropy'.", "*"),
    "10.11.5": ("Discuss environmental crisis as an entropy crisis.", "*"),
    "10.2.1": ("State Boyle's law and Charles's law.", "*"),
    "10.2.2": ("Describe that a gas obeying PV proportional to T is an ideal gas.", "*"),
    "10.4.2": ("Explain that internal energy is function of 'state' and is independent of paths.", "*"),
    "10.5.3": ("Calculate the following on the basis of the first law of thermodynamics: a. change in internal energy, b. work done, c. change in heat.", "*"),
    "10.6.2": ("Explain that Cp is greater than Cv.", "*"),
    "10.6.3": ("Show that Cp - Cv = R by using first law of thermodynamics.", "*"),
    "3.2.1": ("Describe law of conservation of linear momentum.", "*"),
    "3.2.2": ("Exemplify the law of conservation of momentum in: a. karate chops to break a pile of bricks, b. car crashes, c. ball and bat, d. motion under thrust of a rocket in a straight line.", "*"),
    "5.4.2": ("Interpret force extension graph for a deformed material.", "*"),
    "5.4.3": ("Solve word problems related to Young modulus.", "*"),
    "5.5.1": ("Determine the elastic potential energy of a material by using E = Fx = (1/2) k x^2.", "*"),
    "6.1.2": ("Solve word problems using Upthrust = rho g V.", "*"),
    "6.1.4": ("State Archimedes' principle of floatation.", "*"),
    "6.2.1": ("Define the following terms: a. streamline flow (laminar flow), b. turbulent flow, c. incompressible flow.", "*"),
    "6.4.1": ("Derive Bernoulli's equation.", "*"),
    "7.2.3": ("Derive expression for instantaneous displacement, velocity and acceleration in terms of angular velocity (omega).", "*"),
    "7.5.2": ("Solve word problems related to given expression.", "*"),
    "8.1.4": ("Solve word problems using V = f lambda.", "*"),
    "8.3.3": ("Calculate the phase difference between two waves.", "*"),
    "8.5.1": ("Describe Doppler's effect.", "*"),
    "8.5.2": ("Derive the relation between the original frequency of source of sound and the apparent frequency detected by the listener in following conditions: a. when the source is at rest and the listener is moving towards or away from the source, b. when the listener is at rest and the source is moving towards or away from the listener, c. when both source and listener are moving towards each other, d. when both source and listener are moving away from each other.", "*"),
    "8.5.3": ("Solve word problems using the above relations mentioned in the SLO # 8.5.2.", "*"),
    "8.5.4": ("Explain the application of Doppler's effect in electromagnetic waves.", "*"),
    "8.5.5": ("Apply Doppler's effect to understand the working of radar, sonar, satellites and red and blue shifts.", "*"),
    "9.4.3": ("Describe diffraction in a narrow slit.", "*"),
    "9.4.4": ("Solve word problems related to diffraction of light.", "*"),
    "9.5.1": ("State Bragg's law.", "*"),
    "9.5.3": ("Derive the equation 2 d sin theta = m lambda.", "*"),
    "9.5.4": ("Solve word problems related to the given equation.", "*"),
    "9.6.5": ("State Malus's law.", "*"),
    "9.6.6": ("Solve word problems related to the Malus's law.", "*"),
}

OUTCOMES = [
    {"id": "1.1.1", "text": "Discuss that all physical quantities consist of a numerical magnitude and a unit", "cognitive": "E", "formative": False, "topic": "Physical Quantities"},
    {"id": "1.1.2", "text": "Determine appropriate values of physical quantities", "cognitive": "A", "formative": False, "topic": "Physical Quantities"},
    {"id": "1.1.3", "text": "Identify the SI base quantities and their units", "cognitive": "*", "formative": False, "topic": "Physical Quantities"},
    {"id": "1.1.4", "text": "Significant Figures and Uncertainty", "cognitive": "*", "formative": False, "topic": "Physical Quantities"},
    {"id": "1.1.5", "text": "Use SI base units to check the homogeneity of physical equations", "cognitive": "A", "formative": False, "topic": "Physical Quantities"},
    {"id": "1.2.1", "text": "Describe the concept of dimensions", "cognitive": "*", "formative": False, "topic": "Dimensions"},
    {"id": "1.2.2", "text": "Discuss various physical quantities in terms of their dimensions", "cognitive": "E", "formative": False, "topic": "Dimensions"},
    {"id": "1.2.3", "text": "Show the homogeneity of physical equations by using dimensions", "cognitive": "A", "formative": False, "topic": "Dimensions"},
    {"id": "1.2.4", "text": "Derive the formula for physical quantities by using dimensions", "cognitive": "A", "formative": False, "topic": "Dimensions"},
    {"id": "1.3.1", "text": "Differentiate between precision and accuracy", "cognitive": "*", "formative": False, "topic": "Precision and Accuracy"},
    {"id": "1.3.2", "text": "Analyse the accuracy and precision of data collected using different measuring instruments", "cognitive": "An", "formative": False, "topic": "Precision and Accuracy"},
    {"id": "1.4.1", "text": "Solve word problems related to uncertainty in derived quantity with correct number of significant figures", "cognitive": "A", "formative": False, "topic": ""},
    {"id": "1.4.2", "text": "Justify that all measurements contain uncertainty. E 2. Scalars and Vectors Students should be able to:", "cognitive": "*", "formative": False, "topic": ""},
    {"id": "2.1.1", "text": "Differentiate between scalar and vector quantities", "cognitive": "*", "formative": False, "topic": "Introduction to Vectors"},
    {"id": "2.2.1", "text": "Analyse a vector into its rectangular components", "cognitive": "An", "formative": False, "topic": "Addition of Vectors by Rectangular Component Method"},
    {"id": "2.2.2", "text": "Explain the sum of vectors using perpendicular components", "cognitive": "*", "formative": False, "topic": "Addition of Vectors by Rectangular Component Method"},
    {"id": "2.2.3", "text": "Calculate the resultant of two vectors by rectangular component method", "cognitive": "A", "formative": False, "topic": "Addition of Vectors by Rectangular Component Method"},
    {"id": "2.3.1", "text": "Define scalar product of two vectors", "cognitive": "*", "formative": False, "topic": "Scalar Product of Two Vectors"},
    {"id": "2.3.2", "text": "Exemplify scalar product of two vectors in terms of angle between them", "cognitive": "*", "formative": False, "topic": "Scalar Product of Two Vectors"},
    {"id": "2.3.3", "text": "Describe properties of scalar product of two vectors", "cognitive": "*", "formative": False, "topic": "Scalar Product of Two Vectors"},
    {"id": "2.4.1", "text": "Define vector product of two vectors", "cognitive": "*", "formative": False, "topic": "Vector Product of Two Vectors"},
    {"id": "2.4.2", "text": "Exemplify vector product of two vectors in terms of angle between them", "cognitive": "*", "formative": False, "topic": "Vector Product of Two Vectors"},
    {"id": "2.4.3", "text": "Describe properties of vector product of two vectors. * 3. Motion in One Dimension Students should be able to:", "cognitive": "*", "formative": False, "topic": "Vector Product of Two Vectors"},
    {"id": "3.1.1", "text": "Derive equations of motion for a body moving with a uniform acceleration in a straight line", "cognitive": "A", "formative": False, "topic": "Equations of Motion"},
    {"id": "3.1.2", "text": "Solve word problems related to uniformly accelerated motion including free fall using appropriate equations", "cognitive": "A", "formative": False, "topic": "Equations of Motion"},
    {"id": "3.2.1", "text": "State the law of conservation of linear momentum", "cognitive": "A", "formative": False, "topic": "Law of Conservation of Momentum"},
    {"id": "3.2.2", "text": "Describe law of conservation of linear momentum; exemplify the law of conservation of momentum in: a. karate chops to break a pile of bricks, b. car crashes, c. ball and bat, d. motion under thrust of a rocket in a straight line", "cognitive": "*", "formative": False, "topic": "Law of Conservation of Momentum"},
    {"id": "3.2.3", "text": "Define elastic and inelastic collision", "cognitive": "*", "formative": False, "topic": "Law of Conservation of Momentum"},
    {"id": "3.2.4", "text": "Apply law of conservation of momentum to study the special cases of elastic collision between two bodies in one dimension", "cognitive": "A", "formative": False, "topic": "Law of Conservation of Momentum"},
    {"id": "3.2.5", "text": "Apply law of conservation of momentum in one and two dimensions in solving word problems", "cognitive": "A", "formative": False, "topic": "Law of Conservation of Momentum"},
    {"id": "3.3.1", "text": "Describe work as the dot product of force and displacement", "cognitive": "*", "formative": False, "topic": "Work"},
    {"id": "3.3.2", "text": "Deduce the work done from the force displacement graphs", "cognitive": "E", "formative": False, "topic": "Work"},
    {"id": "3.4.1", "text": "Differentiate between conservative and non-conservative field", "cognitive": "*", "formative": False, "topic": "Conservative and Non- Conservative Fields"},
    {"id": "3.5.1", "text": "Deduce the work-energy theorem in non-resistive and resistive medium", "cognitive": "E", "formative": False, "topic": "Work-Energy Theorem"},
    {"id": "3.5.2", "text": "Solve word problems related to the work-energy theorem. A 4. Motion in Two Dimensions Students should be able to:", "cognitive": "*", "formative": False, "topic": "Work-Energy Theorem"},
    {"id": "4.1.1", "text": "Explain projectile motion", "cognitive": "*", "formative": False, "topic": "Projectile"},
    {"id": "4.1.2", "text": "Derive the relation for: a. time of flight, b. maximum height, c. horizontal range of a projectile, d. maximum horizontal range of a projectile", "cognitive": "A", "formative": False, "topic": "Projectile"},
    {"id": "4.1.3", "text": "Solve word problems related to the given relations a, b, c and d", "cognitive": "A", "formative": False, "topic": "Projectile"},
    {"id": "4.1.4", "text": "Predict qualitatively the effect of air resistance on the motion of a projectile", "cognitive": "E", "formative": False, "topic": "Projectile"},
    {"id": "4.2.1", "text": "Describe angular displacement, angular velocity and angular acceleration", "cognitive": "*", "formative": False, "topic": "Angular Motion"},
    {"id": "4.2.2", "text": "Derive the relationship between linear and angular displacement, velocity and acceleration", "cognitive": "A", "formative": False, "topic": "Angular Motion"},
    {"id": "4.2.3", "text": "Solve word problems related to the rotational motion", "cognitive": "A", "formative": False, "topic": "Angular Motion"},
    {"id": "4.3.1", "text": "Define centripetal force and centripetal acceleration", "cognitive": "*", "formative": False, "topic": "Centripetal Force and Centripetal Acceleration"},
    {"id": "4.3.2", "text": "Derive centripetal acceleration when speed is uniform", "cognitive": "A", "formative": False, "topic": "Centripetal Force and Centripetal Acceleration"},
    {"id": "4.3.3", "text": "Justify that a centrifuge is used to separate materials using centripetal force", "cognitive": "E", "formative": False, "topic": "Centripetal Force and Centripetal Acceleration"},
    {"id": "4.3.4", "text": "Explain that the objects in orbiting satellites appear to be weightless", "cognitive": "*", "formative": False, "topic": "Centripetal Force and Centripetal Acceleration"},
    {"id": "4.3.5", "text": "Describe that artificial gravity is created to counter weightlessness", "cognitive": "*", "formative": False, "topic": "Centripetal Force and Centripetal Acceleration"},
    {"id": "4.4.1", "text": "Explain moment of inertia and its SI unit with dimension", "cognitive": "*", "formative": False, "topic": "Moment of Inertia"},
    {"id": "4.4.2", "text": "Compare the moment of inertia in rod, ring, disc and sphere", "cognitive": "*", "formative": False, "topic": "Moment of Inertia"},
    {"id": "4.4.3", "text": "Derive relationship between torque, moment of inertia and angular acceleration", "cognitive": "A", "formative": False, "topic": "Moment of Inertia"},
    {"id": "4.4.4", "text": "Solve word problems related to the given relationships", "cognitive": "A", "formative": False, "topic": "Moment of Inertia"},
    {"id": "4.5.1", "text": "Explain angular momentum and its SI unit with dimension", "cognitive": "*", "formative": False, "topic": "Angular Momentum"},
    {"id": "4.5.2", "text": "Solve word problems related to angular momentum", "cognitive": "A", "formative": False, "topic": "Angular Momentum"},
    {"id": "4.5.3", "text": "Explain the law of conservation of angular momentum", "cognitive": "*", "formative": False, "topic": "Angular Momentum"},
    {"id": "4.5.4", "text": "Illustrate the applications of conservation of angular momentum in: a. flywheels to store rotational energy, b. gyroscopes in navigation system, c. ice skaters to adjust their angular velocity. A 5. Deformation in Solids Students should be able to:", "cognitive": "*", "formative": False, "topic": "Angular Momentum"},
    {"id": "5.1.1", "text": "Distinguish between the structures of crystalline, amorphous and polymeric solids", "cognitive": "*", "formative": False, "topic": "Types of Solids"},
    {"id": "5.2.1", "text": "Describe the deformation of solids in one dimension", "cognitive": "*", "formative": False, "topic": "Deformation in Solids"},
    {"id": "5.3.1", "text": "Describe terms elastic deformation, plastic deformation and elastic limit", "cognitive": "*", "formative": False, "topic": "Tensile and Plastic Deformation"},
    {"id": "5.4.1", "text": "Define stress, strain and Young modulus", "cognitive": "*", "formative": False, "topic": "Stress, Strain and Young Modulus"},
    {"id": "5.4.2", "text": "Interpret force extension graph for a deformed material", "cognitive": "E", "formative": False, "topic": "Stress, Strain and Young Modulus"},
    {"id": "5.4.3", "text": "Interpret force extension graph for a deformed material; solve word problems related to Young modulus; E", "cognitive": "A", "formative": False, "topic": "Stress, Strain and Young Modulus"},
    {"id": "5.4.4", "text": "Use daily life objects to explain stress, strain and Young modulus; FA2", "cognitive": "*", "formative": False, "topic": "Stress, Strain and Young Modulus"},
    {"id": "5.5.1", "text": "Determine the elastic potential energy of a material by using . A 6. Fluids Dynamics Students should be able to:", "cognitive": "*", "formative": False, "topic": "Elastic Potential Energy of Materials"},
    {"id": "6.1.1", "text": "Describe upthrust", "cognitive": "*", "formative": False, "topic": "Floating Objects"},
    {"id": "6.1.2", "text": "Solve word problems using W = rho g V", "cognitive": "A", "formative": False, "topic": "Floating Objects"},
    {"id": "6.1.3", "text": "State the principle of floatation in terms of upthrust", "cognitive": "*", "formative": False, "topic": "Floating Objects"},
    {"id": "6.1.4", "text": "Solve word problems using the law of floatation for a floating body", "cognitive": "A", "formative": False, "topic": "Floating Objects"},
    {"id": "6.1.5", "text": "Justify that ships are engineered to float in the sea", "cognitive": "E", "formative": False, "topic": "Floating Objects"},
    {"id": "6.2.1", "text": "Define the following terms: a. streamline flow laminar flow, b. turbulent flow, c. incompressible flow", "cognitive": "*", "formative": False, "topic": "Streamline and Turbulent Flow"},
    {"id": "6.2.2", "text": "State the conditions required for turbulent flow", "cognitive": "*", "formative": False, "topic": "Streamline and Turbulent Flow"},
    {"id": "6.3.1", "text": "Derive the equation of continuity", "cognitive": "A", "formative": False, "topic": "Equation of Continuity"},
    {"id": "6.3.2", "text": "Explain that squeezing one end of a rubber pipe results in increase in flow velocity at the other end", "cognitive": "*", "formative": False, "topic": "Equation of Continuity"},
    {"id": "6.3.3", "text": "Solve word problems related to the equation of continuity", "cognitive": "A", "formative": False, "topic": "Equation of Continuity"},
    {"id": "6.4.1", "text": "State Bernoulli's equation, P + (1/2) rho v^2 + rho g h = constant", "cognitive": "A", "formative": False, "topic": "Bernoullis Equation"},
    {"id": "6.4.2", "text": "Justify that the difference in pressure can arise from different rates of flow of a fluid", "cognitive": "E", "formative": False, "topic": "Bernoullis Equation"},
    {"id": "6.4.3", "text": "Explain Bernoulli effect in the following cases: a. atomizer, b. swing of ball, c. the lift of golf ball the magnus effect, d. venturi duct", "cognitive": "*", "formative": False, "topic": "Bernoullis Equation"},
    {"id": "6.5.1", "text": "Define the following terms: a. viscous fluids, b. non-viscous fluids", "cognitive": "*", "formative": False, "topic": "Viscous Fluids and Fluid Friction"},
    {"id": "6.5.2", "text": "Describe that viscous force in a fluid causes a retarding force on an object moving through it", "cognitive": "*", "formative": False, "topic": "Viscous Fluids and Fluid Friction"},
    {"id": "6.5.3", "text": "Explain that real fluids are viscous fluids", "cognitive": "*", "formative": False, "topic": "Viscous Fluids and Fluid Friction"},
    {"id": "6.5.4", "text": "Describe the following terms: a. fluid friction, b. super fluidity", "cognitive": "*", "formative": False, "topic": "Viscous Fluids and Fluid Friction"},
    {"id": "6.5.5", "text": "Use different liquids in the surroundings to explain fluid friction and super fluidity. FA 7. Oscillations Students should be able to:", "cognitive": "*", "formative": True, "topic": "Viscous Fluids and Fluid Friction"},
    {"id": "7.1.1", "text": "Define periodic and non-periodic oscillation", "cognitive": "*", "formative": False, "topic": "Simple Harmonic Motion S.H.M."},
    {"id": "7.1.2", "text": "Describe Simple Harmonic Motion S.H.M.", "cognitive": "*", "formative": False, "topic": "Simple Harmonic Motion S.H.M."},
    {"id": "7.2.1", "text": "Define the following terms in the context of oscillations: a. displacement, b. amplitude, c. period, d. frequency, e. angular frequency, f. phase difference", "cognitive": "*", "formative": False, "topic": "Uniform Circular Motion and S.H.M."},
    {"id": "7.2.2", "text": "Relate S.H.M. with uniform circular motion", "cognitive": "*", "formative": False, "topic": "Uniform Circular Motion and S.H.M."},
    {"id": "7.2.3", "text": "Derive expression for instantaneous displacement, velocity and acceleration in terms of angular frequency", "cognitive": "A", "formative": False, "topic": "Uniform Circular Motion and S.H.M."},
    {"id": "7.2.4", "text": "Solve word problems related to the SLO #", "cognitive": "*", "formative": False, "topic": "Uniform Circular Motion and S.H.M."},
    {"id": "7.2.5", "text": "Analyse graphical representations of the variations of displacement, velocity and acceleration with time for simple harmonic motion", "cognitive": "An", "formative": False, "topic": "Uniform Circular Motion and S.H.M."},
    {"id": "7.3.1", "text": "Explain that the motion of a body under elastic restoring force is S.H.M.", "cognitive": "*", "formative": False, "topic": "Mass-Spring System"},
    {"id": "7.3.2", "text": "Derive an expression for the time period of a mass-spring system", "cognitive": "A", "formative": False, "topic": "Mass-Spring System"},
    {"id": "7.3.3", "text": "Solve word problems using the expression for the time period of a mass-spring system", "cognitive": "A", "formative": False, "topic": "Mass-Spring System"},
    {"id": "7.4.1", "text": "Explain that the motion of a simple pendulum is S.H.M.", "cognitive": "*", "formative": False, "topic": "Simple Pendulum"},
    {"id": "7.4.2", "text": "Derive an expression for the time period of a simple pendulum", "cognitive": "A", "formative": False, "topic": "Simple Pendulum"},
    {"id": "7.4.3", "text": "Solve word problems using the expression for the time period of a simple pendulum", "cognitive": "A", "formative": False, "topic": "Simple Pendulum"},
    {"id": "7.5.1", "text": "Derive an expression to show that energy is conserved in mass-spring system executing S.H.M.", "cognitive": "A", "formative": False, "topic": "Energy Conservation in S.H.M."},
    {"id": "7.5.2", "text": "Solve word problems related to given expression", "cognitive": "A", "formative": False, "topic": "Energy Conservation in S.H.M."},
    {"id": "7.5.3", "text": "Analyse the interchange between kinetic and potential energy during simple harmonic motion", "cognitive": "An", "formative": False, "topic": "Energy Conservation in S.H.M."},
    {"id": "7.6.1", "text": "Exemplify free and forced oscillation", "cognitive": "*", "formative": False, "topic": "Free and Forced Oscillation"},
    {"id": "7.7.1", "text": "Define resonance", "cognitive": "*", "formative": False, "topic": "Resonance"},
    {"id": "7.7.2", "text": "Describe applications and consequences of resonance in real life", "cognitive": "*", "formative": False, "topic": "Resonance"},
    {"id": "7.8.1", "text": "Explain damped oscillation", "cognitive": "*", "formative": False, "topic": "Damped Oscillations"},
    {"id": "7.8.2", "text": "List different applications of damped oscillation", "cognitive": "*", "formative": False, "topic": "Damped Oscillations"},
    {"id": "7.8.3", "text": "Illustrate displacement-time graphs to show light, critical and heavy damping. A 8. Waves Students should be able to:", "cognitive": "*", "formative": False, "topic": "Damped Oscillations"},
    {"id": "8.1.1", "text": "Define progressive waves", "cognitive": "*", "formative": False, "topic": "Wave Motion"},
    {"id": "8.1.2", "text": "Explain energy transfer through a progressive wave", "cognitive": "*", "formative": False, "topic": "Wave Motion"},
    {"id": "8.1.3", "text": "Solve word problems using intensity = power/ area and intensity amplitude2 for a progressive wave", "cognitive": "A", "formative": False, "topic": "Wave Motion"},
    {"id": "8.1.4", "text": "Solve word problems using ; FA", "cognitive": "*", "formative": True, "topic": "Wave Motion"},
    {"id": "8.2.1", "text": "Differentiate between transverse and longitudinal waves; FA", "cognitive": "*", "formative": True, "topic": "Transverse and Longitudinal Waves"},
    {"id": "8.2.2", "text": "Analyse graphical representations of transverse and longitudinal waves; FA", "cognitive": "*", "formative": True, "topic": "Transverse and Longitudinal Waves"},
    {"id": "8.3.1", "text": "State the principle of superposition of two waves", "cognitive": "*", "formative": False, "topic": "Superposition of Waves"},
    {"id": "8.3.2", "text": "Describe the phenomenon of interference of sound waves", "cognitive": "*", "formative": False, "topic": "Superposition of Waves"},
    {"id": "8.3.3", "text": "Calculate the phase difference between two waves", "cognitive": "A", "formative": False, "topic": "Superposition of Waves"},
    {"id": "8.3.4", "text": "Explain the formation of beats using diagrams", "cognitive": "*", "formative": False, "topic": "Superposition of Waves"},
    {"id": "8.4.1", "text": "Define the terms nodes and antinodes", "cognitive": "*", "formative": False, "topic": "Stationary Waves"},
    {"id": "8.4.2", "text": "Describe the formation of stationary waves in a string and air column", "cognitive": "*", "formative": False, "topic": "Stationary Waves"},
    {"id": "8.4.3", "text": "Solve word problems related to stationary waves", "cognitive": "A", "formative": False, "topic": "Stationary Waves"},
    {"id": "8.5.1", "text": "Describe the Doppler effect", "cognitive": "*", "formative": False, "topic": "Dopplers Effect"},
    {"id": "8.5.2", "text": "Derive the relation between the original frequency of a source of sound and the apparent frequency detected by the listener when: a. the source moves toward a stationary listener, b. the listener moves toward a stationary source, c. both move toward each other", "cognitive": "A", "formative": False, "topic": "Dopplers Effect"},
    {"id": "8.5.3", "text": "Solve word problems using the above relations mentioned in the SLO #", "cognitive": "*", "formative": False, "topic": "Dopplers Effect"},
    {"id": "8.5.4", "text": "Describe the change in frequency and wavelength of light waves due to relative motion (red and blue shifts)", "cognitive": "*", "formative": False, "topic": "Dopplers Effect"},
    {"id": "8.5.5", "text": "Understand the working of radar, sonar, satellites and red and blue shifts", "cognitive": "A", "formative": False, "topic": "Dopplers Effect"},
    {"id": "8.6.1", "text": "Use of waves in modern world for: a. medical purposes, b. digital transmission, c. storage of information, d. monitoring earthquake and tsunami. FA 9. Physical Optics Students should be able to:", "cognitive": "*", "formative": True, "topic": "Waves in Modern World"},
    {"id": "9.1.1", "text": "Discuss different points of view about nature of light", "cognitive": "E", "formative": False, "topic": "Nature of Light"},
    {"id": "9.1.2", "text": "Discuss the concept of wave-front", "cognitive": "E", "formative": False, "topic": "Nature of Light"},
    {"id": "9.1.3", "text": "Describe Huygens principle", "cognitive": "*", "formative": False, "topic": "Nature of Light"},
    {"id": "9.2.1", "text": "Define coherent and monochromatic sources of light", "cognitive": "*", "formative": False, "topic": "Interference of Light"},
    {"id": "9.2.2", "text": "Define interference of light", "cognitive": "*", "formative": False, "topic": "Interference of Light"},
    {"id": "9.2.3", "text": "State conditions necessary for the interference of light", "cognitive": "*", "formative": False, "topic": "Interference of Light"},
    {"id": "9.2.4", "text": "Explain Youngs double slit experiment", "cognitive": "*", "formative": False, "topic": "Interference of Light"},
    {"id": "9.2.5", "text": "Derive relation for fringe spacing", "cognitive": "A", "formative": False, "topic": "Interference of Light"},
    {"id": "9.2.6", "text": "Solve word problems related to the fringe spacing", "cognitive": "A", "formative": False, "topic": "Interference of Light"},
    {"id": "9.3.1", "text": "Describe the construction and working of Michelsons interferometer", "cognitive": "*", "formative": False, "topic": "Michelsons Interferometer"},
    {"id": "9.3.2", "text": "Describe qualitatively about gravitational waves", "cognitive": "*", "formative": False, "topic": "Michelsons Interferometer"},
    {"id": "9.3.3", "text": "State that a gravitational wave passes a body of mass creates a distortion in spacetime", "cognitive": "*", "formative": False, "topic": "Michelsons Interferometer"},
    {"id": "9.3.4", "text": "Describe the use of interferometers in detecting gravitational waves", "cognitive": "*", "formative": False, "topic": "Michelsons Interferometer"},
    {"id": "9.4.1", "text": "Define diffraction of light", "cognitive": "*", "formative": False, "topic": "Diffraction of Light"},
    {"id": "9.4.2", "text": "Describe diffraction of light by diffraction grating", "cognitive": "*", "formative": False, "topic": "Diffraction of Light"},
    {"id": "9.4.3", "text": "Describe the diffraction pattern produced by a diffraction grating and the role of the number of lines in resolving close wavelengths", "cognitive": "*", "formative": False, "topic": "Diffraction of Light"},
    {"id": "9.4.4", "text": "Describe diffraction in a narrow slit; solve word problems related to diffraction of light", "cognitive": "A", "formative": False, "topic": "Diffraction of Light"},
    {"id": "9.5.1", "text": "State Braggs law", "cognitive": "*", "formative": False, "topic": "Braggs Law"},
    {"id": "9.5.2", "text": "Describe diffraction of X-rays through crystals", "cognitive": "*", "formative": False, "topic": "Braggs Law"},
    {"id": "9.5.3", "text": "Derive the equation", "cognitive": "A", "formative": False, "topic": "Braggs Law"},
    {"id": "9.5.4", "text": "Solve word problems related to the given equation", "cognitive": "A", "formative": False, "topic": "Braggs Law"},
    {"id": "9.6.1", "text": "Describe unpolarised and polarised light", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.2", "text": "Explain polarisation with reference to transverse waves", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.3", "text": "Explain polarisation by reflection", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.4", "text": "Explain polarisation by a polaroid", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.5", "text": "State Malus's law, I = I0 cos^2 theta", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.6", "text": "Solve word problems", "cognitive": "A", "formative": False, "topic": "Polarisation"},
    {"id": "9.6.7", "text": "Describe the applications of polarisation in daily life. 10. Thermodynamics Students should be able to:", "cognitive": "*", "formative": False, "topic": "Polarisation"},
    {"id": "10.1.1", "text": "Distinguish between heat and temperature", "cognitive": "*", "formative": False, "topic": "Heat and Temperature"},
    {"id": "10.1.2", "text": "Describe heat as a form of transit energy", "cognitive": "*", "formative": False, "topic": "Heat and Temperature"},
    {"id": "10.1.3", "text": "Identify that regions of equal temperature are in thermal equilibrium", "cognitive": "*", "formative": False, "topic": "Heat and Temperature"},
    {"id": "10.1.4", "text": "Investigate to provide evidence for the transfer of thermal energy between two bodies at different temperatures in a closed system; FA", "cognitive": "*", "formative": True, "topic": "Heat and Temperature"},
    {"id": "10.2.1", "text": "S law and Charless law", "cognitive": "*", "formative": False, "topic": "Fundamentals of the Ideal Gas"},
    {"id": "10.2.2", "text": "Describe that a gas obeying PV T is an ideal gas", "cognitive": "*", "formative": False, "topic": "Fundamentals of the Ideal Gas"},
    {"id": "10.3.1", "text": "State basic postulates of kinetic molecular theory of gases", "cognitive": "*", "formative": False, "topic": "Kinetic Molecular Theory of Gases"},
    {"id": "10.3.2", "text": "Derive relation PV = Nm < v2 >", "cognitive": "A", "formative": False, "topic": "Kinetic Molecular Theory of Gases"},
    {"id": "10.3.3", "text": "Calculate the root-mean-square speed of an ideal gas", "cognitive": "A", "formative": False, "topic": "Kinetic Molecular Theory of Gases"},
    {"id": "10.3.4", "text": "Derive the formula for the average translational kinetic energy of a gas", "cognitive": "A", "formative": False, "topic": "Kinetic Molecular Theory of Gases"},
    {"id": "10.3.5", "text": "Solve word problems related to given average translational kinetic energy of a gas", "cognitive": "A", "formative": False, "topic": "Kinetic Molecular Theory of Gases"},
    {"id": "10.4.1", "text": "Describe internal energy of an ideal gas as the sum of their kinetic energy of molecules only", "cognitive": "*", "formative": False, "topic": "Internal Energy and Work"},
    {"id": "10.4.2", "text": "Independent of paths", "cognitive": "*", "formative": False, "topic": "Internal Energy and Work"},
    {"id": "10.4.3", "text": "Explain work done in thermodynamics", "cognitive": "*", "formative": False, "topic": "Internal Energy and Work"},
    {"id": "10.4.4", "text": "Differentiate between the work done by a gas and the work done on a gas", "cognitive": "*", "formative": False, "topic": "Internal Energy and Work"},
    {"id": "10.5.1", "text": "Explain the first law of thermodynamics", "cognitive": "*", "formative": False, "topic": "First Law of Thermodynamics"},
    {"id": "10.5.2", "text": "Apply the first law of thermodynamics in: a. isothermal, b. adiabatic, c. isobaric, d. isochoric processes", "cognitive": "A", "formative": False, "topic": "First Law of Thermodynamics"},
    {"id": "10.5.3", "text": "Calculate the following on the basis of the first law of thermodynamics: a. change in internal energy, b. work done, c. change in heat", "cognitive": "A", "formative": False, "topic": "First Law of Thermodynamics"},
    {"id": "10.6.1", "text": "Define the terms: a. specific heat, b. molar specific heat", "cognitive": "*", "formative": False, "topic": "Molar Specific Heat of Gases"},
    {"id": "10.6.2", "text": "Explain the molar specific heat of a gas at constant volume and at constant pressure, Cv and Cp", "cognitive": "*", "formative": False, "topic": "Molar Specific Heat of Gases"},
    {"id": "10.6.3", "text": "Show that by using first law of thermodynamics", "cognitive": "A", "formative": False, "topic": "Molar Specific Heat of Gases"},
    {"id": "10.7.1", "text": "Describe the concept of reversible and irreversible processes", "cognitive": "*", "formative": False, "topic": "Reversible and Irreversible Process"},
    {"id": "10.8.1", "text": "Explain the second law of thermodynamics using schematic diagram", "cognitive": "*", "formative": False, "topic": "Second Law of Thermodynamics"},
    {"id": "10.9.1", "text": "Describe heat engine with reference to the second law of thermodynamics", "cognitive": "*", "formative": False, "topic": "Carnot Engine"},
    {"id": "10.9.2", "text": "Explain the working principle of Carnot engine and its four processes with pressure-volume PV diagram", "cognitive": "*", "formative": False, "topic": "Carnot Engine"},
    {"id": "10.9.3", "text": "Derive the formula for efficiency of Carnot engine", "cognitive": "A", "formative": False, "topic": "Carnot Engine"},
    {"id": "10.9.4", "text": "Solve word problems related to efficiency of Carnot engine", "cognitive": "A", "formative": False, "topic": "Carnot Engine"},
    {"id": "10.9.5", "text": "Design an energy efficient device for daily life use; FA", "cognitive": "*", "formative": True, "topic": "Carnot Engine"},
    {"id": "10.10.1", "text": "Describe refrigerator as a reverse of heat engine", "cognitive": "*", "formative": False, "topic": "Refrigerator"},
    {"id": "10.10.2", "text": "Derive expression for the coefficient of performance of a refrigerator", "cognitive": "A", "formative": False, "topic": "Refrigerator"},
    {"id": "10.11.1", "text": "Explain entropy as a measure of the number of microscopic arrangements (microstates) corresponding to a macroscopic state", "cognitive": "E", "formative": False, "topic": "Entropy"},
    {"id": "10.11.2", "text": "Describe positive and negative entropy", "cognitive": "*", "formative": False, "topic": "Entropy"},
    {"id": "10.11.3", "text": "Explain that increase in entropy is the evidence of increase in temperature of a system", "cognitive": "*", "formative": False, "topic": "Entropy"},
    {"id": "10.11.4", "text": "Explain that energy is degraded during all natural processes", "cognitive": "*", "formative": False, "topic": "Entropy"},
    {"id": "10.11.5", "text": "Discuss environmental crisis as an entropy crisis.", "cognitive": "E", "formative": False, "topic": "Entropy"},
]
import re as _re


#: Sub-topics that carry outcomes of their own are covered above. The
#: remainder are listed here so a chapter can name all its sections.
EXTRA_TOPICS = {"1.4": "Significant Figures and Uncertainty"}


def _clean(text):
    """Tidy one extracted outcome.

    The PDF extraction runs neighbouring text together, so an outcome can arrive
    with the next sub-topic heading, the next chapter title, or a stray cognitive
    marker welded onto its end. Those are stripped here rather than in the
    generated table, so a re-extraction cannot reintroduce them.
    """
    text = _re.split(r"\s+\d{1,2}\.\d{1,2}\s+[A-Z]|\s+\d{1,2}\.\s+[A-Z]|\s+\*\s+[A-Z]", text)[0]
    text = _re.sub(r"[;,]?\s*\bFA\d*\s*$", "", text)
    # a cognitive-level marker welded on by the column extraction
    text = _re.sub(r"[;,]?\s+(?:An|E|C|R|U|A)\s*$", "", text)
    if text and not text.endswith((".", "?", "!")):
        text += "."
    text = _re.sub(r"\s*[;*]\s*$", "", text)
    return text.strip(" ;,")


for _row in OUTCOMES:
    _row["text"] = _clean(_row["text"])
    if not _row["topic"]:
        _row["topic"] = EXTRA_TOPICS.get(_row["id"].rsplit(".", 1)[0], "")

# ``REVIEWED`` is authoritative: where an outcome had to be reconstructed, the
# reconstruction overrides whatever the PDF extraction produced.
_BY_ID = {row["id"]: row for row in OUTCOMES}
for _sid, (_text, _cog) in REVIEWED.items():
    _BY_ID[_sid]["text"] = _text
    _BY_ID[_sid]["cognitive"] = _cog


#: chapter number -> (ordered outcome ids, first sub-topic title)
CHAPTERS = {
    1: (["1.1.1", "1.1.2", "1.1.3", "1.1.4", "1.1.5", "1.2.1", "1.2.2", "1.2.3", "1.2.4", "1.3.1", "1.3.2", "1.4.1", "1.4.2"], "Physical Quantities"),
    2: (["2.1.1", "2.2.1", "2.2.2", "2.2.3", "2.3.1", "2.3.2", "2.3.3", "2.4.1", "2.4.2", "2.4.3"], "Introduction to Vectors"),
    3: (["3.1.1", "3.1.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.5", "3.3.1", "3.3.2", "3.4.1", "3.5.1", "3.5.2"], "Equations of Motion"),
    4: (["4.1.1", "4.1.2", "4.1.3", "4.1.4", "4.2.1", "4.2.2", "4.2.3", "4.3.1", "4.3.2", "4.3.3", "4.3.4", "4.3.5", "4.4.1", "4.4.2", "4.4.3", "4.4.4", "4.5.1", "4.5.2", "4.5.3", "4.5.4"], "Projectile"),
    5: (["5.1.1", "5.2.1", "5.3.1", "5.4.1", "5.4.2", "5.4.3", "5.4.4", "5.5.1"], "Types of Solids"),
    6: (["6.1.1", "6.1.2", "6.1.3", "6.1.4", "6.1.5", "6.2.1", "6.2.2", "6.3.1", "6.3.2", "6.3.3", "6.4.1", "6.4.2", "6.4.3", "6.5.1", "6.5.2", "6.5.3", "6.5.4", "6.5.5"], "Floating Objects"),
    7: (["7.1.1", "7.1.2", "7.2.1", "7.2.2", "7.2.3", "7.2.4", "7.2.5", "7.3.1", "7.3.2", "7.3.3", "7.4.1", "7.4.2", "7.4.3", "7.5.1", "7.5.2", "7.5.3", "7.6.1", "7.7.1", "7.7.2", "7.8.1", "7.8.2", "7.8.3"], "Simple Harmonic Motion S.H.M."),
    8: (["8.1.1", "8.1.2", "8.1.3", "8.1.4", "8.2.1", "8.2.2", "8.3.1", "8.3.2", "8.3.3", "8.3.4", "8.4.1", "8.4.2", "8.4.3", "8.5.1", "8.5.2", "8.5.3", "8.5.4", "8.5.5", "8.6.1"], "Wave Motion"),
    9: (["9.1.1", "9.1.2", "9.1.3", "9.2.1", "9.2.2", "9.2.3", "9.2.4", "9.2.5", "9.2.6", "9.3.1", "9.3.2", "9.3.3", "9.3.4", "9.4.1", "9.4.2", "9.4.3", "9.4.4", "9.5.1", "9.5.2", "9.5.3", "9.5.4", "9.6.1", "9.6.2", "9.6.3", "9.6.4", "9.6.5", "9.6.6", "9.6.7"], "Nature of Light"),
    10: (["10.1.1", "10.1.2", "10.1.3", "10.1.4", "10.2.1", "10.2.2", "10.3.1", "10.3.2", "10.3.3", "10.3.4", "10.3.5", "10.4.1", "10.4.2", "10.4.3", "10.4.4", "10.5.1", "10.5.2", "10.5.3", "10.6.1", "10.6.2", "10.6.3", "10.7.1", "10.8.1", "10.9.1", "10.9.2", "10.9.3", "10.9.4", "10.9.5", "10.10.1", "10.10.2", "10.11.1", "10.11.2", "10.11.3", "10.11.4", "10.11.5"], "Heat and Temperature"),
}


def topics(number):
    """The sub-topics of one chapter, as ``{"1.1": "Physical Quantities", ...}``."""
    found = {row["id"].rsplit(".", 1)[0]: row["topic"] for row in OUTCOMES
             if row["id"].startswith(f"{number}.")}
    for key, title in EXTRA_TOPICS.items():
        if key.startswith(f"{number}."):
            found.setdefault(key, title)
    return found


def outcome(sid):
    """One outcome record by identifier, e.g. ``outcome("9.4.2")``."""
    for row in OUTCOMES:
        if row['id'] == sid:
            return row
    raise KeyError(f'the Grade XI syllabus has no outcome {sid!r}')


def chapter_ids(number):
    """Every outcome identifier in one chapter, in syllabus order."""
    return CHAPTERS[number][0]
