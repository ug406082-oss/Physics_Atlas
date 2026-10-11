"""A full lesson for every published learning outcome.

The rest of the app teaches by topic: a station covers several outcomes and
runs through them. This module is organised the other way round - one entry per
outcome - so that a learner can be certain about any single thing the board
asks for without having to remember which station it belonged to.

Every entry has the same five parts:

``meaning``   what the outcome actually says, in ordinary words
``why``       why it is true, or where it comes from
``example``   a worked example, or a concrete case
``pitfall``   the mistake people actually make
``check``     a question the learner can answer without looking
``answer``    the answer to that question

`tests/test_teaching_depth.py` fails the build if any of the 185 published
outcomes is missing from here or is missing one of those parts.
"""

from __future__ import annotations

__all__ = ["LESSONS", "lesson", "depth_of", "MINIMUM_WORDS"]

#: No outcome gets less teaching than this, measured over meaning + why + example.
MINIMUM_WORDS = 45

LESSONS = {}


# --------------------------------------------------------------------------
# Chapter 1 · Physical Quantities and Measurement
# --------------------------------------------------------------------------

LESSONS.update({
 "1.1.1": {
  "meaning": "Every physical quantity is a number and a unit together. The number alone is "
             "meaningless: 5 what? A length of 5 m and a mass of 5 kg are both '5' and share "
             "nothing. The unit is not a label attached afterwards; it is part of the "
             "measurement itself.",
  "why": "Because a unit is defined as the standard reference against which a quantity is "
         "compared. The metre is not the length of anything you can hold - it is a "
         "convention agreed internationally, and the number only means something because of "
         "the convention behind it.",
  "example": "Write the mass of a body as 3.2 kg. Writing 3.2 on its own is incomplete; the "
             "same number with kg is a mass, and with m would be a length.",
  "pitfall": "Treating the unit as separate from the number, and then dividing quantities "
             "whose units do not match.",
  "check": "Which of these is a complete physical quantity: 9.8, 9.8 N, or 9.8 metres per "
           "second per second?",
  "answer": "Both 9.8 N and 9.8 m s⁻² are complete. 9.8 on its own is not a physical "
            "quantity at all."},

 "1.1.2": {
  "meaning": "A sensible value is one in which the number is small and readable. You choose "
             "the unit so that the number suits the size of the thing measured.",
  "why": "Because the unit is arbitrary once you have a reference. The length of a pencil is "
         "the same whether you write 0.00015 km or 15 cm, but one is awkward to work with "
         "and the other is not. Scientists agree on conventions so that numbers can be "
         "compared between laboratories.",
  "example": "The length of a pencil is 15 cm, not 0.00015 km and not 15000000 µm. All "
             "three are correct; only one is usable.",
  "pitfall": "Choosing a unit that makes the number huge or tiny, which hides the size of the "
             "uncertainty that goes with it.",
  "check": "Which is the sensible way to report the mass of a car: 0.0015 tonnes or 1500 kg?",
  "answer": "1500 kg. Both are correct, but the number should be of order one to a thousand "
            "if the reference is the everyday unit."},

 "1.1.3": {
  "meaning": "Seven quantities are fundamental: length, mass, time, electric current, "
             "temperature, amount of substance and luminous intensity. Each has exactly one "
             "base unit, and every other unit in physics is built from them.",
  "why": "Because the SI defines the base units independently of one another. That "
         "independence is what makes the system consistent: you cannot define the metre "
         "using the second and the metre, because that would be circular. Since 2019 the "
         "metre is defined through the speed of light and the second through an atomic "
         "transition, so the whole system rests on constants that cannot drift.",
  "example": "The newton is defined as kg m s⁻², the joule as kg m² s⁻², and the watt as "
             "kg m² s⁻³. None of them is fundamental.",
  "pitfall": "Treating the base units as the most important ones, or assuming a derived "
             "unit is somehow less valid.",
  "check": "Is the pascal a base quantity or a derived one?",
  "answer": "Derived: 1 Pa = 1 N m⁻² = 1 kg m⁻¹ s⁻². It is built from the base units of "
            "mass, length and time."},

 "1.1.4": {
  "meaning": "A derived unit is any unit obtained by multiplying or dividing base units. "
             "Every measurement in mechanics reduces to kg, m and s.",
  "why": "Because the base units are independent, so anything made from them is also "
         "independent. That is the whole reason for having only seven: the dimensional "
         "method, which is outcome 1.2, depends on it.",
  "example": "Work is force times distance, force is mass times acceleration, and "
             "acceleration is velocity per time, so work comes out as kg m² s⁻² and is "
             "measured in joules.",
  "pitfall": "Assuming the unit must be a symbol you have to look up, rather than working "
             "it out from the quantities involved.",
  "check": "Express the unit of pressure in base units.",
  "answer": "Pressure is force per area, so N m⁻² = (kg m s⁻²) m⁻² = kg m⁻¹ s⁻²."},

 "1.1.5": {
  "meaning": "An equation is homogeneous if both sides reduce to the same base units. This "
             "is a check on an equation you have not seen before.",
  "why": "Because adding, subtracting and equating quantities only makes sense if they are "
         "the same kind of thing. If the units disagree, the equation cannot be true "
         "whatever the numbers are.",
  "example": "Check F = ma: left side kg m s⁻², right side kg × m s⁻². They agree, so the "
             "equation is dimensionally sound.",
  "pitfall": "Treating dimensional homogeneity as proof that an equation is correct. It is "
             "necessary but not sufficient: E = mc² is homogeneous and could still have the "
             "wrong constant.",
  "check": "Is v = at homogeneous, given [v] = L T⁻¹ and [a] = L T⁻²?",
  "answer": "Yes: a × t gives L T⁻² × T = L T⁻¹, which is the unit of velocity."},

 "1.2.1": {
  "meaning": "A dimension tells you the kind of quantity, using the letters M, L and T for "
             "mass, length and time. It is not a unit and it is not a size.",
  "why": "Because the same dimension can carry different units. Speed is L T⁻¹ whether you "
         "write it in m s⁻¹, km h⁻¹ or miles per hour. The dimension survives the change of "
         "unit; the unit does not.",
  "example": "[F] = MLT⁻². Force, weight and thrust all share this dimension while being "
             "quite different physical ideas.",
  "pitfall": "Confusing a dimension with a unit, or expecting a dimension to carry "
             "information about magnitude.",
  "check": "What is the dimension of area, and what is its unit?",
  "answer": "Dimension L², unit m². The dimension says what kind of thing it is; the unit is "
            "one particular choice of scale."},

 "1.2.2": {
  "meaning": "Every quantity in mechanics can be written in terms of M, L and T, and that "
             "expression is its dimensional formula.",
  "why": "Because the base quantities are independent. If you know how a quantity behaves "
         "under scaling you know its dimensions, which is enough to check its unit.",
  "example": "Speed is L T⁻¹, acceleration L T⁻², momentum ML T⁻¹, and weight ML T⁻².",
  "pitfall": "Using dimensions to predict the *form* of a relation, which only works when "
             "one side is dimensionless.",
  "check": "Write the dimensional formula for kinetic energy.",
  "answer": "Energy is ML² T⁻². Half of mv² gives the same thing: M × (L T⁻¹)² = ML² T⁻²."},

 "1.2.3": {
  "meaning": "To show an equation is homogeneous, reduce both sides to base units and "
             "compare. If they match, the equation is dimensionally sound.",
  "why": "Because an equation equates quantities, so the quantities must be of the same "
         "kind. The method is quick, needs no numbers, and catches the commonest "
         "algebraic slips.",
  "example": "For s = ut + ½at²: the right side is LT⁻¹ × T plus LT⁻² × T², which is L in "
             "both terms, matching the left side.",
  "pitfall": "Cancelling L or T as though they were variables rather than symbols for "
             "dimensions.",
  "check": "Is v² = u² + 2as homogeneous?",
  "answer": "Yes. v² gives L² T⁻² and u² + 2as gives L² T⁻² + (L T⁻²)(L) = L² T⁻²."},

 "1.2.4": {
  "meaning": "If you know the dimensions of a quantity, you can find its form - but only "
             "when the relation is between one quantity and its power. s = ut + ½at² "
             "cannot be found this way.",
  "why": "Because dimensions give you the powers but nothing about the numerical "
         "coefficient. For F = ma they tell you F must be MLT⁻², but they cannot tell you "
         "the factor is 1.",
  "example": "Energy E = k m v² has dimensions ML² T⁻², which fixes the form. Since "
             "physics gives E = ½mv², k = ½.",
  "pitfall": "Trying to apply the method to sums of terms, where the dimensions no longer "
             "determine the answer.",
  "check": "Can dimensional analysis find the speed of a wave on a stretched string, "
           "v = sqrt(T/µ)?",
  "answer": "Yes, because there is one quantity T with dimensions MLT⁻² and one µ with "
            "dimensions ML⁻¹, and their ratio has dimensions L² T⁻²."},

 "1.3.1": {
  "meaning": "Precision is how close repeated measurements are to one another. Accuracy is "
             "how close they are to the true value. They are independent.",
  "why": "Because random error scatters readings without moving their centre, while "
         "systematic error moves the centre. Precision detects the first; only comparison "
         "with a known standard detects the second.",
  "example": "Five readings all near 9.8 are precise. If the true value is 9.81 they are "
             "also accurate; if it is 10.2 they are precise but not accurate.",
  "pitfall": "Assuming a precise set of measurements is automatically an accurate one.",
  "check": "A set of readings clustered tightly around a value that is definitely wrong - "
           "precise, accurate, or both?",
  "answer": "Precise but not accurate. The scatter is small; the centre is wrong, which "
            "means a systematic error is present."},

 "1.3.2": {
  "meaning": "A vernier callipers beats a metre rule, which beats a ruler. Each instrument "
             "has a least count, and the finer it is the tighter the cluster of readings.",
  "why": "Because the least count is the smallest division the instrument can resolve. "
         "Errors of one least count are expected and irreducible, so the instrument sets "
         "the floor on your precision.",
  "example": "A metre rule has a least count of 1 mm, a vernier callipers 0.01 cm, and a "
             "screw gauge 0.01 mm. A reading from a metre rule cannot be more precise than "
             "about half a millimetre whatever you do.",
  "pitfall": "Writing down more figures than the instrument can support, which is false "
             "precision and is marked wrong.",
  "check": "What is the largest number of significant figures a metre rule reading can "
           "support?",
  "answer": "Two. A metre rule reads to the millimetre, so 25.4 cm and 25.43 cm are the "
            "same reading wearing different clothes."},

 "1.4.1": {
  "meaning": "When quantities multiply, their fractional uncertainties add. When they add "
             "or subtract, the absolute uncertainties add. Then round the result to the "
             "correct number of significant figures.",
  "why": "Because the uncertainty in a product comes from every factor's own uncertainty. "
         "A quantity built from several measurements can never be more certain than its "
         "least certain part.",
  "example": "For a = F/m with F = 10.0 ± 0.5 N and m = 2.00 ± 0.01 kg, the fractional "
             "uncertainties are 0.05 and 0.005, giving 0.055 or 5.5 %, so a = 5.00 ± 0.28 m "
             "s⁻², which rounds to 5.0 ± 0.3 m s⁻².",
  "pitfall": "Adding absolute uncertainties when the quantities multiply, or quoting more "
             "significant figures than the largest uncertainty allows.",
  "check": "Two lengths are added: 12.3 ± 0.1 cm and 8.4 ± 0.2 cm. What is the uncertainty "
           "of the sum?",
  "answer": "0.1 + 0.2 = 0.3 cm, added in quadrature only if the errors are random: "
            "√(0.1² + 0.2²) = 0.22 cm. For a school answer, 0.3 cm is expected."},

 "1.4.2": {
  "meaning": "Every measurement has uncertainty. There is no such thing as an exact "
             "reading, because the instrument, the observer and the quantity itself are all "
             "imperfect.",
  "why": "Because a physical quantity is a limiting idea. You can refine the instrument "
         "indefinitely and never reach the value, and at some point the uncertainty becomes "
         "the size of the quantity itself, as with the speed of light.",
  "example": "A metre rule reads 25.4 cm, but the true length lies within about half a "
             "millimetre of that. The uncertainty is not a failure; it is the honest shape "
             "of the claim.",
  "pitfall": "Reporting a long string of digits with no uncertainty, which claims a "
             "precision you cannot possibly have.",
  "check": "Why is it wrong to write the length of a room as 4.832156 m?",
  "answer": "Because no ruler can support that many figures. The extra digits are invented, "
            "and they make the answer less trustworthy rather than more."},
})


# --------------------------------------------------------------------------
# Chapter 2 · Scalars and Vectors
# --------------------------------------------------------------------------

LESSONS.update({
 "2.1.1": {
  "meaning": "A scalar has size only. A vector has size and direction, and obeys a "
             "different rule for addition.",
  "why": "Because they are different kinds of thing. Adding 5 N and 3 N gives 8 N, but "
         "adding 5 N east and 3 N north does not give 8 N - it gives something smaller, "
         "because the two are at right angles.",
  "example": "Mass, time, temperature, work and energy are scalars. Displacement, velocity, "
             "force, momentum and acceleration are vectors.",
  "pitfall": "Calling speed a vector because it has a direction. The *speed* is a scalar; "
             "the *velocity* is the vector that contains it.",
  "check": "Is 20 °C a scalar or a vector?",
  "answer": "Scalar. Temperature change is a difference, and differences are scalars even "
            "though temperature is measured along an axis."},

 "2.2.1": {
  "meaning": "Any vector can be split into two perpendicular parts called its rectangular "
             "components. The pair is unique for any chosen pair of axes.",
  "why": "Because a vector is an ordered pair of perpendicular steps. Once you know how far "
         "it reaches along each axis, you have fully described it.",
  "example": "A force of 10 N at 37 degrees above the x axis has components F cos 37° = "
             "8.0 N and F sin 37° = 6.0 N. That is a 6-8-10 triangle.",
  "pitfall": "Using sin where cos belongs, or forgetting to state which axis each component "
             "belongs to.",
  "check": "A boat travels 3 km east and then 4 km north. What are the components of its "
           "total displacement?",
  "answer": "3 km in x and 4 km in y. You do not need an angle: the components are just "
            "the two legs of the journey."},

 "2.2.2": {
  "meaning": "To add vectors by components, add all the x components together and all the y "
             "components together. The two totals are the components of the sum.",
  "why": "Because the axes are independent. Horizontal movement does not affect vertical "
         "movement, so each can be totalled separately and then recombined.",
  "example": "A is 6 N at 0° and B is 8 N at 90°. Rx = 6 + 0 = 6, Ry = 0 + 8 = 8, so the "
             "sum is 10 N at 53° above the x axis.",
  "pitfall": "Adding the magnitudes and the angles. 6 + 8 = 14 is wrong here; the result is "
             "smaller because the two point in different directions.",
  "check": "Two equal forces at 120° to each other have a resultant of...",
  "answer": "One force of the same magnitude, directed along the bisector. This is the "
            "shape of the bonds in graphene and of the legs of a tripod."},

 "2.2.3": {
  "meaning": "Magnitude of the resultant is √(Rx² + Ry²); direction is atan2(Ry, Rx), which "
             "keeps the correct quadrant.",
  "why": "Because the resultant is a right-angled triangle with Rx and Ry as its legs, and "
         "the direction is the angle that triangle makes with the x axis.",
  "example": "Rx = 6, Ry = 8 gives a magnitude of 10 and an angle of atan2(8, 6) = 53.1°.",
  "pitfall": "Using atan(Ry/Rx) instead of atan2. With Rx negative the ordinary tangent "
             "loses the quadrant and can report an angle in the wrong place entirely.",
  "check": "Rx = −3, Ry = 4. What is the direction of the resultant?",
  "answer": "127°, the second quadrant. A calculator set to atan(4/−3) would say 53°, which "
            "points down and to the right instead of up and to the left."},

 "2.3.1": {
  "meaning": "The scalar product, written A·B, multiplies the magnitudes and multiplies in "
             "the cosine of the angle between them. The result is a number.",
  "why": "Because it measures the component of B that lies along A. Only that part of B can "
         "act through A, so the product is a projection and a projection has length only.",
  "example": "A·B = |A||B| cos θ. In components it is AxBx + AyBy, and the two always agree.",
  "pitfall": "Expecting a direction for the answer, or using sin instead of cos.",
  "check": "What is the dot product of a 5 N force and a 3 m displacement at 90°?",
  "answer": "0 J, because cos 90° = 0. The force is perpendicular to the motion and does no "
            "work at all."},

 "2.3.2": {
  "meaning": "The dot product can be evaluated as |A||B| cos θ or as AxBx + AyBy, and the "
             "two routes are equal for any pair of vectors.",
  "why": "Because expanding (Ax i + Ay j)·(Bx i + By j) gives AxBx + AyBy, and substituting "
         "the trig definitions of the components reproduces |A||B| cos θ.",
  "example": "A = 3 i + 4 j and B = 4 i − 3 j. In components, 3×4 + 4×(−3) = 0. As "
             "magnitudes, 5 × 5 × cos 90° = 0. The vectors are perpendicular.",
  "pitfall": "Assuming the two routes are different formulas when they are one result.",
  "check": "A = 3 i + 4 j, B = 4 i − 3 j. What is A·B?",
  "answer": "0. They are perpendicular, so the dot product vanishes."},

 "2.3.3": {
  "meaning": "The dot product is commutative, so A·B = B·A. It is not associative, because "
             "A·(B·C) is a scalar while (A·B)·C is a vector. It is zero when the vectors "
             "are perpendicular and negative when they are opposite.",
  "why": "Commutativity follows from ordinary multiplication of numbers. Associativity fails "
         "because a scalar and a vector are different kinds of quantity and cannot be "
         "combined.",
  "example": "A·B for A at 180° to B is −|A||B|. That negative sign is what distinguishes "
             "pushing from pulling.",
  "pitfall": "Assuming symmetry of the dot product extends to the cross product. It does "
             "not: A × B = −(B × A).",
  "check": "Is A·(B·C) ever equal to (A·B)·C?",
  "answer": "No. The left side is a scalar, the right side is a vector. They are different "
            "quantities and can never be equal."},

 "2.4.1": {
  "meaning": "The vector product, written A × B, multiplies the magnitudes by the sine of "
             "the angle and gives a direction perpendicular to both.",
  "why": "Because sin measures how much of B lies *across* A rather than along it, and the "
         "direction follows from the right-hand rule.",
  "example": "A × B = |A||B| sin θ n̂, where n̂ is the unit vector along the right-hand "
             "normal.",
  "pitfall": "Using cos, or forgetting the direction entirely and giving only a magnitude.",
  "check": "Two parallel vectors of 5 N and 3 N: what is the magnitude of their cross "
           "product?",
  "answer": "0. sin 0° = 0, and parallel vectors span no parallelogram. This is the exact "
            "opposite of the dot product, which is maximal when they are perpendicular."},

 "2.4.2": {
  "meaning": "The magnitude is |A||B| sin θ, which is also the area of the parallelogram the "
             "two vectors span. The direction comes from the right-hand rule.",
  "why": "The parallelogram's base is A and its height is the component of B perpendicular "
         "to A, so its area is exactly the cross product.",
  "example": "Two forces of 10 N and 20 N at 30° give a cross product of 200 × 0.5 = 100 N, "
             "directed normal to the plane they lie in.",
  "pitfall": "Reporting the area without the axis, which is half the answer and always "
             "costs a mark.",
  "check": "The cross product of A and B is 30 N. What happens to it if A is doubled?",
  "answer": "It becomes 60 N. The cross product is linear in each vector, just like the "
            "dot product."},

 "2.4.3": {
  "meaning": "The cross product is not commutative: swapping the vectors reverses its "
             "direction. It is zero for parallel vectors, and its magnitude is the "
             "parallelogram area.",
  "why": "Because reversing the order reverses the sense of the right-hand rule while "
         "leaving the parallelogram, and therefore the area, unchanged.",
  "example": "A × B = −(B × A). In orbital mechanics, L = r × p changes sign if you swap "
             "the order, which is why angular momentum is written in that order "
             "deliberately.",
  "pitfall": "Swapping the vectors for convenience during algebra and forgetting to flip "
             "the sign at the end.",
  "check": "Which is larger, A × B or B × A?",
  "answer": "They have the same magnitude. They point in exactly opposite directions."},
})


# --------------------------------------------------------------------------
# Chapter 3 · Motion in One Dimension
# --------------------------------------------------------------------------

LESSONS.update({
 "3.1.1": {
  "meaning": "For a body moving with constant acceleration along a straight line, the "
             "quantities are linked by five equations, and they are consequences of each "
             "other rather than independent facts.",
  "why": "They all come from two ideas: velocity is the rate of change of displacement, "
         "and acceleration is the rate of change of velocity. Integrating those with "
         "constant acceleration gives the set.",
  "example": "v = u + at; s = ut + ½at²; v² = u² + 2as; s = ½(u+v)t; a = 2(s−ut)/t².",
  "pitfall": "Using the equation that does not contain the quantity you are given. Pick by "
             "what you know, not by what looks familiar.",
  "check": "You know u, a and s but not v or t. Which equation do you use?",
  "answer": "v² = u² + 2as. It is the only one of the five with no t in it."},

 "3.1.2": {
  "meaning": "The same equations solve any uniformly accelerated motion, and free fall is "
             "the important special case with a = g.",
  "why": "Because free fall is just uniform acceleration. Gravity gives every body the same "
         "acceleration near the Earth's surface, whatever its mass, because the force grows "
         "in proportion to the mass.",
  "example": "A ball dropped from rest for 3 s falls s = ½ × 9.8 × 9 = 44.1 m and reaches "
             "v = 29.4 m s⁻¹.",
  "pitfall": "Adding the initial velocity when a body is dropped from rest. u = 0 is the "
             "single most common omission.",
  "check": "A ball is thrown downward at 20 m s⁻¹ and falls for 2 s. What is its speed?",
  "answer": "v = 20 + 9.8 × 2 = 39.6 m s⁻¹. The initial velocity adds; it does not replace "
            "g."},

 "3.2.1": {
  "meaning": "When no external force acts, the total momentum of the system does not change. "
             "Momentum is mass times velocity, and it is a vector.",
  "why": "Because the impulse on a body equals the change in its momentum, and internal "
         "forces in any collision are equal and opposite, so they cancel.",
  "example": "A rifle of mass 4 kg fires a bullet of 0.01 kg at 800 m s⁻¹. The bullet goes "
             "forward, the rifle back, and the two momenta are equal at 8 N s each.",
  "pitfall": "Confusing momentum with kinetic energy. Momentum is conserved in every "
             "collision; kinetic energy only in elastic ones.",
  "check": "Why is a heavy ship harder to stop than a light one, even at low speed?",
  "answer": "Its momentum is much larger, because momentum scales with mass at the same "
            "speed. The impulse needed to stop it scales with that momentum."},

 "3.2.2": {
  "meaning": "The same law shows up in a karate chop, a car crash, a bat meeting a ball, and "
             "a rocket in straight flight.",
  "why": "In each case the internal forces between the parts are equal and opposite and "
         "cancel. What remains is whatever the parts do to one another.",
  "example": "A karate chop breaks bricks because the hand stops suddenly and the momentum "
             "must go somewhere - into the bricks. A rocket works because it throws mass "
             "backwards, so it must go forwards.",
  "pitfall": "Thinking the conservation needs the collision to be elastic. It never does: "
             "momentum is conserved in every collision, elastic or not.",
  "check": "In a car crash, why does the car crumple instead of stopping instantly?",
  "answer": "Crumpling increases the time over which the same change in momentum happens, "
            "so the force is smaller. Momentum is still conserved; the car-plus-other-car "
            "system has the same total momentum throughout."},

 "3.2.3": {
  "meaning": "An elastic collision returns all the kinetic energy. An inelastic one does not; "
             "the rest becomes heat, sound and deformation.",
  "why": "Because momentum must be conserved always, but kinetic energy only when no energy "
         "has been converted to anything else.",
  "example": "A steel ball bouncing on a steel floor is nearly elastic. Two lumps of plastic "
             "clay meeting stick together and are perfectly inelastic.",
  "pitfall": "Assuming perfectly inelastic means the objects stick. They may still bounce, "
             "just with less kinetic energy than before.",
  "check": "A ball hits the floor and rebounds at 80 % of its impact speed. Is it elastic?",
  "answer": "No. Kinetic energy depends on speed squared, so it retains 0.8² = 64 % of its "
            "kinetic energy. The missing 36 % became heat and sound."},

 "3.2.4": {
  "meaning": "In a one-dimensional elastic collision between two smooth spheres, the "
             "faster ball keeps its identity and the two exchange velocities.",
  "why": "Because momentum and kinetic energy are both conserved, and the two equations "
         "together have exactly one physical solution: v₁ = u₂ and v₂ = u₁.",
  "example": "A 2 kg ball at 3 m s⁻¹ hits a stationary 1 kg ball. The 2 kg ball stops and "
             "the 1 kg ball leaves at 6 m s⁻¹. Total momentum is unchanged at 6 kg m s⁻¹.",
  "pitfall": "Applying the exchange rule when the balls have equal masses but one is already "
             "moving, or when the collision is not perfectly elastic.",
  "check": "An equal-mass ball hits a stationary equal-mass ball elastically. Does the "
           "striker bounce back?",
  "answer": "No. It stops dead and the target takes all its velocity. That is why Newton's "
            "cradle swings one ball at a time."},

 "3.2.5": {
  "meaning": "In one and two dimensions, conservation of momentum holds in every collision "
             "whether or not energy is conserved.",
  "why": "Because the cancelling forces are internal, whatever directions the bodies move "
         "in. Direction only changes how you resolve the vectors.",
  "example": "A moving ball strikes a stationary one off-centre: the striker deflects and "
             "the target leaves at an angle, and the vector sum of the momenta is unchanged.",
  "pitfall": "Writing the conservation in one dimension when the collision is oblique, and "
             "getting an answer that fails energy or momentum checks.",
  "check": "An oblique elastic collision conserves...",
  "answer": "Momentum and kinetic energy both, in every dimension. Only kinetic energy is "
            "lost in a non-elastic collision, and never momentum."},

 "3.3.1": {
  "meaning": "Work done is the dot product of force and displacement: W = F·d = Fd cos θ.",
  "why": "Because only the component of force along the displacement does anything. A "
         "force perpendicular to the motion is unchanged in direction and magnitude, so it "
         "does no work.",
  "example": "Pushing a lawnmower at 30° to the direction of travel, with a force of 100 N "
             "over 10 m, does 100 × 10 × cos 30° = 866 J.",
  "pitfall": "Using Fd without the angle when the force is not along the displacement.",
  "check": "A force is applied perpendicular to the motion. What work does it do?",
  "answer": "Zero. cos 90° = 0, which is why a body moving in a circle at constant speed "
            "needs no net work."},

 "3.3.2": {
  "meaning": "Work done by a constant force is the area under the force-displacement graph.",
  "why": "Because work accumulates as the body moves, so a graph of force against distance "
         "accumulates area. Below the axis the force opposes the motion and the area counts "
         "negative.",
  "example": "A constant 50 N over 4 m gives a rectangle of area 200 J. A force rising "
             "linearly from 0 to 50 N over 4 m gives a triangle of area 100 J.",
  "pitfall": "Using the final force value times the distance when the force was changing, "
             "which is only right if it was constant.",
  "check": "A spring returns from a 0.4 m compression to rest with a force falling "
           "linearly from 200 N to 0. What work is done by the spring?",
  "answer": "Negative ½ × 200 × 0.4 = −40 J, because the force acts along the direction the "
            "body travels. The negative sign matters."},

 "3.4.1": {
  "meaning": "A conservative force returns all the work done in it to a closed path. A "
             "non-conservative force does not.",
  "why": "Because for a conservative force the work depends only on the endpoints, which "
         "means it is a state function like internal energy and has a potential.",
  "example": "Gravity and the spring force are conservative; friction and air resistance are "
             "not. Push a block round a loop against friction and it does not coast back.",
  "pitfall": "Assuming friction is conservative because you can calculate work done against "
             "it. You can, but it does not return.",
  "check": "A ball rolls once round a horizontal circle and returns to its start at a lower "
           "speed. Which force is non-conservative?",
  "answer": "Rolling friction. Gravity and the normal force both do zero net work on a "
            "closed horizontal path, so the energy loss is friction."},

 "3.5.1": {
  "meaning": "The work done on a body equals its change in kinetic energy. That is the "
             "work-energy theorem, and it holds in every medium, with or without friction.",
  "why": "Because integrate Newton's second law, F = ma, along the path: the integral of F "
         "ds is exactly the change in ½mv².",
  "example": "A 2 kg body pushed by a constant 5 N over 3 m from rest reaches "
             "½mv² = 15 J, so v = √15 = 3.87 m s⁻¹.",
  "pitfall": "Expecting it to fail when friction acts. It does not: the friction force is "
             "included on the left, and the theorem stays exact.",
  "check": "A 5 kg block slides down a smooth 4 m slope from rest. How much work is done on "
           "it?",
  "answer": "It depends on the slope. The work equals the change in kinetic energy, so you "
            "need the height fallen, not the distance along the slope."},

 "3.5.2": {
  "meaning": "The theorem turns every dynamics problem into an energy one: find the work "
             "done, then find the speed.",
  "why": "Because energy is a scalar. You do not need directions, angles or intermediate "
         "velocities - only the starting and ending states.",
  "example": "A 0.5 kg ball is thrown upward at 20 m s⁻¹. At what height does it stop? "
             "½mv² = mgh gives h = v²/2g = 20.4 m.",
  "pitfall": "Forgetting that on the way down the ball regains the kinetic energy it lost, "
             "so the height is v²/2g rather than v²/4g.",
  "check": "Why does a ball thrown upward reach the same height regardless of whether you "
           "throw it with a push or place it and let it fall?",
  "answer": "Because energy is conserved on the way out and conserved again on the way "
            "down. The path taken does not matter, which is the theorem's whole content."},
})


# --------------------------------------------------------------------------
# Chapter 4 · Motion in Two Dimensions
# --------------------------------------------------------------------------

LESSONS.update({
 "4.1.1": {
  "meaning": "A projectile is a body thrown and then left to move under gravity alone. Its "
             "horizontal and vertical motions are completely independent.",
  "why": "Because there is no horizontal force once it leaves the hand, and gravity acts "
         "purely vertically. The two motions share only the same clock.",
  "example": "A ball thrown at 45 degrees travels along a parabola. Throw two balls at "
             "different angles at the same speed and they land at the same time.",
  "pitfall": "Adding the two velocities to find the direction of travel, or assuming the "
             "velocity is constant because the speed on the way up equals the speed on the "
             "way down.",
  "check": "Two balls thrown horizontally from the same height, one at 10 m s⁻¹ and one at "
           "20 m s⁻¹. Which lands first?",
  "answer": "Both, at the same time. Vertical motion is identical for both; the horizontal "
            "speed only changes how far they travel."},

 "4.1.2": {
  "meaning": "For a launch speed u at angle θ, time of flight is 2u sin θ/g, maximum height "
             "is u² sin²θ/2g, and range is u² sin 2θ/g.",
  "why": "All three come from splitting into components. The vertical part has to climb and "
         "fall back, which fixes the time; everything else follows from that.",
  "example": "At 45° the range is u²/g, since sin 90° = 1. That is the maximum.",
  "pitfall": "Forgetting that the time of flight depends on the angle but not the speed, "
             "which is the most surprising of the three results.",
  "check": "What is the time of flight for a ball thrown straight up at 20 m s⁻¹?",
  "answer": "2 × 20 × sin 90° / 9.8 = 4.08 s. It rises for 2.04 s and falls for the same."},

 "4.1.3": {
  "meaning": "These four relations solve any projectile problem once you have decomposed the "
             "motion.",
  "why": "Because the vertical motion is uniformly accelerated with a = −g and the "
         "horizontal motion is uniform, so each half uses the equations of one-dimensional "
         "motion.",
  "example": "Maximum range occurs at 45° because sin 2θ is largest there, at exactly 1.",
  "pitfall": "Using g in the horizontal equations by mistake, or forgetting that the "
             "acceleration is −g once the sign is fixed.",
  "check": "A projectile launched at 30° and one at 60° with the same speed: which is "
           "higher?",
  "answer": "The 60° launch, because height depends on sin²θ and sin 60° > sin 30°. Both "
            "reach the same range, since sin 60° = sin 120°."},

 "4.1.4": {
  "meaning": "Air resistance makes a projectile fall short and land lower. It is largest at "
             "the top, where the body is moving fastest.",
  "why": "Because drag acts opposite to the velocity, so it opposes the horizontal motion "
         "most when the horizontal speed is greatest.",
  "example": "A cricket ball travels about 5 % less far than an ideal projectile, which is "
             "why the ball is bounced before the second batsman and why range estimates "
             "allow for air.",
  "pitfall": "Expecting the effect to shorten the flight time, or to be greatest at launch.",
  "check": "A model rocket with a parachute slows dramatically at the top. Why is that "
           "where the drag is largest?",
  "answer": "Because drag depends on speed, and at the top the vertical speed is zero while "
            "the horizontal speed is at its maximum."},

 "4.2.1": {
  "meaning": "Angular displacement, angular velocity and angular acceleration describe "
             "rotation exactly as distance, speed and acceleration describe motion in a "
             "straight line.",
  "why": "Because circular motion at constant radius has the same structure in one "
         "dimension of space: only the label changes from linear to angular.",
  "example": "A wheel turning at 60 rpm makes one revolution per second, so ω = 2π rad s⁻¹.",
  "pitfall": "Writing rpm as though it were rad s⁻¹. One revolution is 2π radians, not 1.",
  "check": "A wheel turns at 5 rev s⁻¹. What is its angular velocity in rad s⁻¹?",
  "answer": "2π × 5 = 31.4 rad s⁻¹. Mixing revolutions and radians is the standard error."},

 "4.2.2": {
  "meaning": "For motion at radius r, s = rθ, v = rω and a_t = rα.",
  "why": "Because a small angle turns into an arc length by the geometry of the circle, and "
         "differentiating that with respect to time gives the velocity and acceleration "
         "relations.",
  "example": "At 2 rad s⁻¹ on a 0.5 m radius, v = 1.0 m s⁻¹. Doubling the radius doubles "
             "the linear speed at the same angular speed.",
  "pitfall": "Applying these at a point other than the radius you used, or forgetting that "
             "they hold for a rigid body about a fixed axis.",
  "check": "A 1 m wheel turns at 1 rad s⁻¹. What is the speed of a point on the rim?",
  "answer": "1 m s⁻¹, from v = rω. At the centre the same formula gives zero, which is "
            "correct."},

 "4.2.3": {
  "meaning": "Rotational problems convert angles to lengths first, then are identical to "
             "linear ones.",
  "why": "Because s = rθ maps angular onto linear, so the same equations of motion apply "
         "with θ replacing s and r playing the role of conversion.",
  "example": "A wheel of radius 0.2 m turns through 5 rad. The belt around it moves "
             "s = 0.2 × 5 = 1.0 m.",
  "pitfall": "Mixing radii in one problem, or forgetting that angular acceleration is in "
             "rad s⁻² even when time is in seconds.",
  "check": "A disc of radius 0.3 m has angular speed 4 rad s⁻¹. What is the speed at 0.2 m?",
  "answer": "0.8 m s⁻¹. Every point of a rigid body shares one angular speed, so use the "
            "radius of the point you care about."},

 "4.3.1": {
  "meaning": "Centripetal acceleration points towards the centre of the circle and has "
             "magnitude v²/r. Centripetal force is the force producing it.",
  "why": "Because the acceleration in uniform circular motion is entirely due to the change "
         "in direction of velocity. The speed never changes; the velocity does.",
  "example": "A car at 20 m s⁻¹ on a 100 m radius bend has a = 4 m s⁻², needing a force of "
             "800 N on a 1000 kg car.",
  "pitfall": "Describing centripetal force as a separate force pushing inwards. It is "
             "whatever real force - friction, tension, gravity - happens to point that way.",
  "check": "Is the centripetal force an extra force, or a name for an existing one?",
  "answer": "A name. Gravity provides it for satellites, tension for a ball on a string, "
            "friction for a car on a road. None of them is a new force."},

 "4.3.2": {
  "meaning": "a = v²/r follows from the change of direction in a small time interval.",
  "why": "Draw the velocity vector at the start and end of a small arc. The change in "
         "velocity has magnitude v²Δt/r and points at the centre.",
  "example": "The centripetal acceleration of the Earth around the Sun is 6 × 10⁻³ m s⁻², "
             "which is why it falls each year very slightly further away.",
  "pitfall": "Adding the radial acceleration to the tangential one without checking which "
             "kind of motion you have.",
  "check": "Why is the acceleration not v²/2r when using the average velocity over the "
           "interval?",
  "answer": "Because the instantaneous velocity is needed, not the average. The chord of "
            "the arc is shorter than the arc itself, which is exactly why the centripetal "
            "formula is an instantaneous result."},

 "4.3.3": {
  "meaning": "A centrifuge spins a sample so that dense particles move outwards faster than "
             "the liquid.",
  "why": "Because in the rotating frame the apparent force is proportional to mass. Dense "
         "particles experience proportionally more, so they separate from the liquid.",
  "example": "In a clinical centrifuge at 3000 g, particles settle in minutes that would "
             "take hours under gravity.",
  "pitfall": "Thinking the particles are pushed outwards by a real outward force. The real "
             "force is inward; the separation is in the rotating frame.",
  "check": "Why do red blood cells sediment faster than white ones in a centrifuge?",
  "answer": "Their density differs from the plasma's. The sedimentation depends on density "
            "difference, not on absolute mass."},

 "4.3.4": {
  "meaning": "Astronauts in orbit float because both they and the spacecraft are falling "
             "together, so no support force acts on them.",
  "why": "Because a body is weightless whenever it is in free fall. The Earth's gravity is "
         "still acting on the astronaut in orbit; what is missing is the floor pushing back.",
  "example": "At the ISS altitude the orbital speed is 7.7 km s⁻¹ and the gravity is still "
             "about 90 % of surface value.",
  "pitfall": "Saying there is no gravity in orbit. There is plenty; there is no normal "
             "force.",
  "check": "Why does an orbiting astronaut see the spacecraft rotating once per orbit?",
  "answer": "Because the spacecraft is not rotating. The astronaut and everything in the "
            "frame keep a constant orientation relative to the stars while the orbital path "
            "turns under them."},

 "4.3.5": {
  "meaning": "Artificial gravity is created by rotating a spacecraft so the floor pushes "
             "outwards against the centrifugal tendency.",
  "why": "Because rotation produces an apparent outward force proportional to mass, which "
         "behaves in every respect like gravity.",
  "example": "A 5 m radius centrifuge spinning at 2 rad s⁻¹ gives a = rω² = 20 m s⁻², about "
             "twice Earth's gravity.",
  "pitfall": "Confusing the artificial gravity with a real outward force, or ignoring the "
             "Coriolis effect that makes moving objects appear to curve.",
  "check": "Why is artificial gravity easier than artificial weightlessness?",
  "answer": "Weightlessness is the default in orbit and cannot be undone without gravity. "
            "Artificial gravity can simply be switched on."},
})

LESSONS.update({
 "4.4.1": {
  "meaning": "Moment of inertia measures how hard a body resists being turned. Its SI unit "
             "is kg m², and it depends on where the axis is, not just on the mass.",
  "why": "Because angular acceleration is torque divided by it, by analogy with F = ma. A "
         "long thin rod about its centre has I = ML²/12, while the same rod about one end "
         "has ML²/3 - four times as much.",
  "example": "A solid disc has I = ½MR² and a ring has I = MR². The ring is twice as hard "
             "to spin because all its mass is further out.",
  "pitfall": "Treating I as a property of the body alone. The same body's I doubles between "
             "its centre and its end.",
  "check": "Why is a wheel built with a rim rather than a solid disc?",
  "answer": "Because the rim puts the mass further from the axis, doubling I for the same "
            "mass and making the wheel harder to accelerate."},

 "4.4.2": {
  "meaning": "For a rod, ring, disc and sphere about their central axes, the factors are "
             "ML²/12, MR², ½MR² and 2/5 MR² respectively.",
  "why": "Because each is an integral of the mass times the square of its distance from the "
         "axis, and the shapes differ in how far their mass lies from the centre.",
  "example": "For the same M and R the order is sphere, disc, rod, ring. The ring is "
             "hardest to start rotating.",
  "pitfall": "Comparing moments of inertia of bodies with different masses or radii without "
             "normalising for them.",
  "check": "Which has the larger moment of inertia, a disc or an annulus of the same mass "
           "and outer radius?",
  "answer": "The annulus, by a factor of two. Its mass sits on average further from the "
            "axis."},

 "4.4.3": {
  "meaning": "τ = Iα. Angular acceleration is proportional to torque, with the moment of "
             "inertia playing the part of mass.",
  "why": "Because it is Newton's second law written for rotation, and it comes from the "
         "same argument about impulses and momentum.",
  "example": "A torque of 20 N m on a disc with I = 0.5 kg m² gives α = 40 rad s⁻².",
  "pitfall": "Using a body's central I for a torque applied about a different axis.",
  "check": "The same torque is applied to a rod about its centre and about its end. What "
           "happens to the angular acceleration?",
  "answer": "It is four times smaller about the end, because I is four times larger: "
            "ML²/3 against ML²/12."},

 "4.4.4": {
  "meaning": "These relationships solve any problem about a body being started, slowed or "
             "held in steady rotation.",
  "why": "Because the moment of inertia is the only place the body's shape enters, so "
         "reducing a complicated object to its I makes the arithmetic short.",
  "example": "A flywheel of I = 2 kg m² needs a torque of 6 N m to reach 3 rad s⁻²: "
             "α = τ/I.",
  "pitfall": "Forgetting that torque depends on the angle between the force and the lever "
             "arm, exactly as the cross product does.",
  "check": "Why does a revolving mass top an upright bottle?",
  "answer": "It adds to the moment of inertia about the tipping axis. A larger I resists "
            "angular acceleration, so the toppling torque produces less tipping."},

 "4.5.1": {
  "meaning": "Angular momentum is L = Iω, measured in kg m² s⁻¹.",
  "why": "Because it is the rotational counterpart of momentum: the product of the inertia "
         "and the rate of rotation, with the same conservation law behind it.",
  "example": "A figure skater at 2 rev s⁻¹ with I = 1 kg m² has L = 4π kg m² s⁻¹.",
  "pitfall": "Confusing it with linear momentum. L uses I rather than m, and is a vector "
             "along the axis of rotation.",
  "check": "Is angular momentum conserved when a spinning skater pulls in her arms?",
  "answer": "Yes. She does no external torque, so Iω stays constant - and since I falls, ω "
            "rises."},

 "4.5.2": {
  "meaning": "Worked angular-momentum problems are linear-momentum problems with I for m "
             "and ω for v.",
  "why": "Because the two are structurally identical, and the same conservation arguments "
         "apply in each.",
  "example": "A disc with I = 0.5 spins at 4 rad s⁻¹. A torque of 3 N m for 2 s changes L "
             "by 6 kg m² s⁻¹.",
  "pitfall": "Treating angular momentum as though it depended on mass alone, which drops the "
             "shape of the body from the answer.",
  "check": "How does L change if the radius of a spinning disc doubles?",
  "answer": "It quadruples, since I scales as R² while ω is unchanged."},

 "4.5.3": {
  "meaning": "With no external torque, the total angular momentum of a system is constant.",
  "why": "Because torque is the rate of change of angular momentum, exactly as force is the "
         "rate of change of linear momentum.",
  "example": "A diver's angular momentum is fixed as he tucks, so his spin rate increases "
             "to keep Iω constant.",
  "pitfall": "Applying it when there is an external torque - anything touching the system, "
             "including friction at an axle.",
  "check": "A spinning ice skater slows down when she puts her arms out. Is angular "
           "momentum conserved?",
  "answer": "Approximately, ignoring friction. I increases, so ω decreases to keep the "
            "product constant."},

 "4.5.4": {
  "meaning": "Flywheels store rotational energy, gyroscopes hold a direction, and skaters "
             "adjust their spin - all by changing I while Iω stays fixed.",
  "why": "Because conserving L means that anything reducing I must increase ω, and "
         "anything increasing I must reduce it.",
  "example": "A flywheel absorbs energy from a fluctuating engine torque by speeding up and "
             "slowing slightly, which smooths the rotation.",
  "pitfall": "Confusing angular momentum with energy. L is conserved when torque is zero; "
             "rotational energy is not.",
  "check": "Why does a gyroscope in an aircraft keep a steady attitude in a turn?",
  "answer": "Its angular momentum resists any change in orientation. The gyroscopic effect "
            "is the practical use of conservation of L."},
})


# --------------------------------------------------------------------------
# Chapter 5 · Deformation in Solids
# --------------------------------------------------------------------------

LESSONS.update({
 "5.1.1": {
  "meaning": "Crystalline solids have a long-range ordered lattice, amorphous ones a short-"
             "range order only, and polymeric ones long chains of repeating units.",
  "why": "Because the type of order sets the behaviour. A crystal melts at one sharp "
         "temperature because every bond breaks together; an amorphous solid has a range of "
         "bonds and softens gradually.",
  "example": "Quartz and sugar are crystalline; glass and plastic are amorphous; nylon and "
             "PVC are polymeric.",
  "pitfall": "Calling glass a crystal because it is solid. Solidity says nothing about order.",
  "check": "Why does glass soften gradually rather than melting at one temperature?",
  "answer": "Because its bonds are all different strengths. Heat breaks the weakest first, "
            "so there is no single melting point."},

 "5.2.1": {
  "meaning": "A solid deforms when a force is applied, and recovers when the force is "
             "removed, as long as it is not taken past its elastic limit.",
  "why": "Because atoms in a solid sit in potential wells. A small force lifts them out of "
         "the well's side; remove it and they fall back.",
  "example": "Stretching a rubber band by 10 % and releasing it returns it to its original "
             "size, provided it is not stretched beyond its elastic limit.",
  "pitfall": "Expecting a solid to be perfectly rigid. Real solids deform measurably under "
             "any load.",
  "check": "Does a solid deform more when the same force is applied over a smaller area?",
  "answer": "The same deformation for the same stress. The area changes the stress and the "
            "strain together, in the same proportion."},

 "5.3.1": {
  "meaning": "Elastic deformation is fully recoverable, plastic deformation is permanent, "
             "and the elastic limit is the boundary between them.",
  "why": "Because below the limit the atoms return to the bottom of their potential wells; "
         "above it they slip into new wells.",
  "example": "A copper wire stretches elastically then plastically, and does not recover "
             "once past the elastic limit.",
  "pitfall": "Treating the yield point and the elastic limit as the same thing. The elastic "
             "limit is where recovery stops; the yield point is where large plastic strain "
             "begins.",
  "check": "A spring returns to its original length after being stretched. Was the elastic "
           "limit exceeded?",
  "answer": "No. Full recovery means the deformation stayed inside the elastic region."},

 "5.4.1": {
  "meaning": "Stress is force per area, strain is extension per original length, and Young's "
             "modulus is stress divided by strain.",
  "why": "Because they are the dimensionless and dimensional forms of the same measure: how "
         "hard a material is being pulled, how much it gives, and the ratio of one to the "
         "other.",
  "example": "A 100 N load on a 2 mm² wire gives a stress of 50 MPa. A 0.1 % extension "
             "gives a strain of 10⁻³, so Y = 50 MPa / 10⁻³ = 50 GPa.",
  "pitfall": "Using the extended length instead of the original length in the strain "
             "formula.",
  "check": "What is the strain when a 2 m wire stretches by 4 mm?",
  "answer": "0.004 / 2 = 0.002. Convert the millimetres to metres first, or the answer is "
            "1000 times too small."},

 "5.4.2": {
  "meaning": "The force-extension curve has a straight region where extension is "
             "proportional to load, then bends, then yields, then fractures.",
  "why": "Because each region is a different regime of atomic response: elastic, "
         "yielding, plastic flow.",
  "example": "The gradient of the straight section is the stiffness in N m⁻¹; the gradient "
             "of the stress-strain version is Young's modulus.",
  "pitfall": "Reading Young's modulus from the curved part, where the gradient no longer "
             "represents an elastic constant.",
  "check": "What does the area under the force-extension curve measure?",
  "answer": "The work done, which is the energy absorbed before failure. That is a measure "
            "of toughness."},

 "5.4.3": {
  "meaning": "Y = (F/A)/(ΔL/L), and the graph's straight gradient gives it directly.",
  "why": "Because in the elastic region stress is proportional to strain, so the ratio is "
         "constant for a given material and the curve is straight.",
  "example": "F = 120 N, A = 4 mm², ΔL = 0.5 mm over L = 2 m gives Y = 1.2 × 10¹¹ Pa.",
  "pitfall": "Using cross-sectional area in cm² or mm² without converting to m², which "
             "gives an answer 10⁶ too small.",
  "check": "Steel has Y = 2 × 10¹¹ Pa. What stress produces a strain of 10⁻³?",
  "answer": "2 × 10¹¹ × 10⁻³ = 2 × 10⁸ Pa, which is 200 MPa. Strain is one part in a "
            "thousand, and steel is stiff."},

 "5.4.4": {
  "meaning": "Steel bars in concrete, glass fibres in cables, rubber in tyres and steel "
             "guitar strings each exploit a different part of the stress-strain curve.",
  "why": "Because engineers choose a material for the property they need: strength, "
         "stiffness, resilience or toughness.",
  "example": "A reinforcing bar is strong and has enough strain to absorb load before "
             "failing, so a crack appears in the concrete first.",
  "pitfall": "Asking which material is 'best' without naming the property being optimised. "
             "Diamond is stiffest and strongest; rubber is the most resilient.",
  "check": "Why is a guitar string made of steel rather than rubber?",
  "answer": "A string must have a high elastic limit so that bending it does not take a "
            "permanent set, and low damping so that it rings."},

 "5.5.1": {
  "meaning": "The elastic potential energy stored is E = Fx = ½kx².",
  "why": "Because work is the area under the force-extension graph, and for a linear "
         "spring that area is a triangle.",
  "example": "A spring of k = 200 N m⁻¹ stretched 0.04 m stores ½ × 200 × 0.0016 = 0.16 J.",
  "pitfall": "Using Fx instead of ½Fx for a spring that starts unstretched, which doubles "
             "the answer.",
  "check": "Why is the energy ½Fx rather than Fx for a spring stretched from rest?",
  "answer": "Because the force grows from 0 to F during the stretch, so the average force is "
            "F/2 and the work is the product of the average force and the distance."},
})

LESSONS.update({
 "6.1.1": {
  "meaning": "Upthrust is the upward force a fluid exerts on a body placed in it. It equals "
             "the weight of the fluid displaced.",
  "why": "The fluid underneath a body is at higher pressure than the fluid above, and when "
         "the pressure differences are integrated over the surface the horizontal parts "
         "cancel and a net upward force remains.",
  "example": "A 1000 kg ship displaces about 1000 kg of sea water and floats; the same "
             "block of steel sinks because it displaces less than its own mass.",
  "pitfall": "Assuming upthrust depends on the body's density. It depends only on the "
             "volume displaced.",
  "check": "What happens to the upthrust if a body is submerged deeper without changing "
           "volume?",
  "answer": "Nothing. Upthrust depends on volume and fluid density, both unchanged. What "
            "increases is the pressure difference between top and bottom."},

 "6.1.2": {
  "meaning": "Upthrust = ρgV, and weight = mg, so a floating body has ρ_fluid V = ρ_body V.",
  "why": "Because a floating body is in equilibrium, so upthrust equals weight. That single "
         "condition gives the ratio of densities directly.",
  "example": "Ice of density 917 kg m⁻³ floats in water of 1000 kg m⁻³, so 91.7 % of its "
             "volume is submerged. That is why icebergs float mostly underwater.",
  "pitfall": "Comparing masses instead of densities when deciding whether something floats.",
  "check": "A 0.5 kg object floats in water. What volume does it displace?",
  "answer": "5 × 10⁻⁴ m³, because a floating body displaces its own weight in water: "
            "ρVg = mg gives V = 0.5/1000."},

 "6.1.3": {
  "meaning": "A body floats if the maximum upthrust, when fully submerged, is at least its "
             "weight. Otherwise it sinks.",
  "why": "Because upthrust grows with the volume submerged and stops at full submersion, so "
         "there is a maximum. If that maximum cannot balance the weight, no amount of "
         "submersion helps.",
  "example": "A steel ship floats because its hollow shape lets it displace a large volume "
             "of water while keeping a small mass.",
  "pitfall": "Expecting a dense body to sink regardless of shape. A steel tanker is less "
             "dense than water overall.",
  "check": "Does a body float if its density equals the fluid's density?",
  "answer": "Yes, exactly neutrally - it will float completely submerged with nothing above "
            "the surface."},

 "6.1.4": {
  "meaning": "Archimedes' principle states that the upthrust on a submerged body equals the "
             "weight of fluid displaced, whatever the shape of the body or the depth.",
  "why": "Because it follows from the pressure difference over the surface, which depends "
         "only on the volume enclosed. It is exact for any shape and any immersion.",
  "example": "A fully submerged 0.004 m³ block in water experiences an upthrust of 39.2 N, "
             "whatever its shape.",
  "pitfall": "Requiring the body to be at the surface. The principle holds at any depth and "
             "for partially submerged bodies too, using just the submerged volume.",
  "check": "Why is Archimedes' principle independent of depth?",
  "answer": "Because the pressure at both the top and the bottom increases with depth by the "
            "same amount ρgh, and that common part cancels, leaving only the part due to "
            "the body's own volume."},

 "6.1.5": {
  "meaning": "Ships float because their average density is less than seawater, achieved by "
             "a hull that encloses a large volume of air.",
  "why": "Because the upthrust depends on displaced volume, not mass. A hollow steel hull "
         "displaces enough water to support a large cargo.",
  "example": "A 100 000 tonne oil tanker typically displaces about the same mass of water "
             "and draws only 10-12 m, since seawater is dense.",
  "pitfall": "Confusing a ship's high mass with a high density. The hull is mostly air.",
  "check": "Why do cargo ships carry cargo low in the hull?",
  "answer": "To keep the centre of gravity low. Stability depends on the metacentric "
            "height, and a low centre of gravity gives a large righting moment."},

 "6.2.1": {
  "meaning": "Streamline or laminar flow has fluid moving in layers that never mix. "
             "Turbulent flow has chaotic mixing. Incompressible flow keeps a constant "
             "density.",
  "why": "Because the flow is laminar at low Reynolds numbers - when inertia is weak "
         "compared with viscosity - and becomes chaotic once inertia wins.",
  "example": "Honey falling in a thin stream is laminar; smoke from a cigarette is "
             "turbulent.",
  "pitfall": "Thinking turbulence is just 'fast' flow. A fast thin layer of syrup is still "
             "laminar.",
  "check": "Is water in a garden hose laminar or turbulent?",
  "answer": "Laminar if the flow is steady and the hose is smooth. Most household pipes "
            "carry laminar flow."},

 "6.2.2": {
  "meaning": "Turbulence appears above a critical Reynolds number, roughly 2000 in a pipe, "
             "and is encouraged by rough surfaces, sudden changes in area and irregular "
             "edges.",
  "why": "Because above that number small disturbances grow instead of being damped out, "
         "and the eddies feed themselves.",
  "example": "A golf ball flies further than a smooth ball of the same speed precisely "
             "because the dimples keep the boundary layer turbulent.",
  "pitfall": "Expecting roughness to reduce turbulence. It increases it.",
  "check": "Why is a boundary layer laminar over a smooth surface but turbulent over a "
           "rough one?",
  "answer": "Roughness provides disturbance centres. Once the Reynolds number is high "
            "enough, those disturbances grow rather than being damped away."},

 "6.3.1": {
  "meaning": "For an incompressible fluid, A₁v₁ = A₂v₂. It comes from the fact that the "
             "volume entering a pipe in a time must equal the volume leaving it.",
  "why": "Because if it did not, fluid would pile up or the pipe would empty. Continuity is "
         "purely a conservation statement.",
  "example": "Squeeze a 1 cm² pipe down to 0.25 cm² and the velocity quadruples, which is "
             "why you cannot get a drink through a pinched straw.",
  "pitfall": "Applying it to a compressible fluid such as gas, where density is not "
             "constant.",
  "check": "Water flows at 2 m s⁻¹ through a 10 cm² pipe. What is the velocity in a 2 cm² "
           "section?",
  "answer": "10 m s⁻¹, from 10 × 2 = 2 × v. The velocity is inversely proportional to the "
            "area."},

 "6.3.2": {
  "meaning": "Squeezing one end of a rubber pipe increases the flow speed at the other end, "
             "even though the flow rate stays the same.",
  "why": "Because continuity ties speed to area. The volume passing per second is the same "
         "everywhere; it is redistributed.",
  "example": "That is why pinching a hose makes the jet faster and narrower rather than "
             "weaker.",
  "pitfall": "Saying more water comes out when you squeeze. The flow rate is constant; the "
             "speed and the shape change.",
  "check": "What happens to the flow rate when you squeeze a hose?",
  "answer": "It stays the same. Continuity guarantees the same volume per second passes "
            "every cross-section; only the velocity and the pressure change."},

 "6.3.3": {
  "meaning": "Continuity problems are solved with two steps: find the flow rate from the "
             "known end, then the velocity at the other end.",
  "why": "Because A₁v₁ = A₂v₂ is one equation with two unknowns in each direction, and the "
         "flow rate is the quantity that carries information between the two ends.",
  "example": "A 4 cm² pipe carries 1.2 × 10⁻³ m³ s⁻¹. At 2 cm² the velocity is 0.6 m s⁻¹.",
  "pitfall": "Converting areas in cm² to m² inconsistently between the two ends.",
  "check": "If the area halves and the flow rate is unchanged, what happens to velocity?",
  "answer": "It doubles, since velocity is inversely proportional to area for a given flow "
            "rate."},

 "6.4.1": {
  "meaning": "Bernoulli's equation states that P + ½ρv² + ρgh is constant along a streamline.",
  "why": "It comes from the work-energy theorem applied to a fluid element, with the "
         "pressure force doing work and gravity doing work, over a distance along the flow.",
  "example": "At the top of a curve the fluid is faster and the pressure lower; that "
             "difference is what makes a curve ball spin.",
  "pitfall": "Applying it across different streamlines, which is not valid, or using it "
             "where viscosity matters.",
  "check": "For a horizontal streamline with constant area, what is constant?",
  "answer": "P + ½ρv². With v constant, the pressure must be constant too."},

 "6.4.2": {
  "meaning": "Where a fluid flows faster, the pressure is lower. That is why pressure "
             "differences arise from different flow rates.",
  "why": "Because the kinetic energy term must trade against the pressure term, and the "
         "sum is fixed. Energy has to come from somewhere.",
  "example": "Air over a fast-moving train drops in pressure, so the train is pushed "
             "inwards.",
  "pitfall": "Assuming fast flow means high pressure because of the pressure gradient. It "
             "is the reverse.",
  "check": "Why does a shower head feel wider than the pipe feeding it, even though the "
           "total flow rate is unchanged?",
  "answer": "Because it is the same rate spread over more area, so the speed is lower and "
            "the pressure is higher at the wide end - the opposite of a constriction."},

 "6.4.3": {
  "meaning": "The atomizer, a swinging ball, the lift on a spinning golf ball and the "
             "venturi duct are all Bernoulli applications.",
  "why": "In each case a faster stream means lower pressure, and something is pushed by "
         "that difference.",
  "example": "In an atomizer, air rushing past the top of the tube drops the pressure above "
             "the liquid and sucks it up, breaking it into droplets.",
  "pitfall": "Applying Bernoulli to a situation where the flow is unsteady or viscous, "
             "such as a pump.",
  "check": "How does a curved football get lift?",
  "answer": "Spin makes the boundary layer turbulent on the curve side, delaying flow "
            "separation. Air moves faster over that side, so the pressure is lower and "
            "the ball is pushed towards it."},

 "6.5.1": {
  "meaning": "A viscous fluid resists relative motion within itself; a non-viscous one "
             "flows without internal friction.",
  "why": "Because molecules in a real fluid interact, and shearing one layer past another "
         "requires work.",
  "example": "Water and air are viscous but only weakly so. Ideal oils and gases are often "
             "treated as non-viscous.",
  "pitfall": "Equating viscosity with density. Honey is viscous and dense, but liquid "
             "mercury is dense and only moderately viscous.",
  "check": "Is air viscous in the sense of this topic?",
  "answer": "Yes, but so slightly that it is usually approximated as non-viscous at "
            "ordinary speeds."},

 "6.5.2": {
  "meaning": "A viscous force opposes the motion of an object through a fluid and is "
             "proportional to speed and to the surface in contact.",
  "why": "Because the fluid immediately around the object has to be dragged along with it, "
         "and it slips back towards rest further away.",
  "example": "Drag on a car rises roughly as the square of speed, which is why aerodynamic "
             "shapes matter at high speed.",
  "pitfall": "Expecting drag to be constant with speed, or to depend on the volume of fluid "
             "the object displaces.",
  "check": "Why does a streamlined shape reduce drag?",
  "answer": "It reduces the area over which the fluid has to be dragged, and delays flow "
            "separation so the wake is smaller."},

 "6.5.3": {
  "meaning": "Every real fluid is viscous. The ideal non-viscous fluid is a mathematical "
             "convenience.",
  "why": "Because viscosity arises from molecular interactions, and every fluid has "
         "molecules that interact.",
  "example": "Water's viscosity of about 1 mPa s at 20 °C is small but measurable, and it "
             "is why a spoon still stirs eventually.",
  "pitfall": "Treating 'non-viscous' as a claim about a real liquid.",
  "check": "Can a real fluid be exactly non-viscous?",
  "answer": "No. Non-viscosity is an idealisation valid for liquids like water where the "
            "viscosity can be neglected in a given calculation."},

 "6.5.4": {
  "meaning": "Fluid friction is the viscous drag within a fluid. Superfluidity is the "
             "complete absence of viscosity, found only in liquid helium below 2.2 K.",
  "why": "Because in superfluidity the atoms form a coherent quantum state that costs no "
         "energy to move, so there is no resistance at all.",
  "example": "Liquid helium II creeps up and over the walls of its container, and flows "
             "through gaps that no ordinary liquid could pass.",
  "pitfall": "Expecting superfluidity to be a matter of temperature alone. It requires both "
             "the low temperature and the correct isotope of helium-4.",
  "check": "Why does a superfluid climb out of a container?",
  "answer": "Because it wets the walls perfectly and experiences no viscosity, so it flows "
            "upwards along the wall under its own momentum."},

 "6.5.5": {
  "meaning": "Water, glycerine, honey and liquid helium show the whole range, from "
             "noticeable drag to none at all.",
  "why": "Because viscosity depends on molecular size, intermolecular forces and "
         "temperature, and those differ enormously between substances.",
  "example": "A marble falls through glycerine at a few cm s⁻¹ and through liquid helium "
             "with no resistance at all.",
  "pitfall": "Ranking liquids by viscosity without noting the temperature, which changes "
             "it by nearly a factor of two over 20 °C.",
  "check": "Which is more viscous, water or honey, and by roughly how much?",
  "answer": "Honey, by roughly 10 000 times at room temperature. The difference is a "
            "consequence of molecular structure and hydrogen bonding."},
})

LESSONS.update({
 "7.1.1": {
  "meaning": "A periodic oscillation repeats itself exactly; a non-periodic one does not, "
             "however gently it is damped.",
  "why": "Because periodicity requires the motion to be a function of time alone, with no "
         "memory of the past. Any loss of energy changes that.",
  "example": "A pendulum in ideal conditions is periodic; a pendulum in air loses amplitude "
             "each swing and is technically non-periodic.",
  "pitfall": "Calling damped motion non-periodic, when the period survives and only the "
             "amplitude falls.",
  "check": "Is a heavily damped oscillator periodic?",
  "answer": "Its period is essentially unchanged; only its amplitude decays. That is what "
            "makes light, critical and heavy damping distinguishable at all."},

 "7.1.2": {
  "meaning": "S.H.M. is the motion for which the restoring force is proportional to "
             "displacement from equilibrium and directed towards it.",
  "why": "Because that proportionality gives an acceleration proportional to -x, which is "
         "the defining feature and the source of the sinusoidal solution.",
  "example": "F = -kx, so a = -(k/m)x. Only this restoring force gives S.H.M.",
  "pitfall": "Thinking motion in a circle is S.H.M. The circle is not; its projection is.",
  "check": "Why is a ball on a string swinging through a vertical circle not S.H.M.?",
  "answer": "Because the restoring force is the tension, which is not proportional to "
            "displacement from the lowest point."},

 "7.2.1": {
  "meaning": "Displacement, amplitude, period, frequency, angular frequency and phase "
             "difference are the six quantities that describe an oscillation.",
  "why": "They fall into pairs: linear against angular, and ordinary frequency against its "
         "angular equivalent, with phase accounting for position in the cycle.",
  "example": "f = 1/T and ω = 2πf, so a 2 Hz oscillation has ω = 12.6 rad s⁻¹.",
  "pitfall": "Mixing f and ω, or treating phase difference as a distance.",
  "check": "A pendulum has period 2 s. What is its angular frequency?",
  "answer": "π rad s⁻¹, since ω = 2π/2. Using 2 directly would be off by a factor of about "
            "6.3."},

 "7.2.2": {
  "meaning": "The projection of a point moving uniformly round a circle performs S.H.M.",
  "why": "Because the horizontal coordinate of a uniform circular motion is A cos ωt, which "
         "is exactly the S.H.M. solution, and its acceleration works out to -ω²x.",
  "example": "The shadow of a point on the rim of a wheel is the standard picture, and it "
             "explains why T = 2π√(L/g) has no dependence on mass.",
  "pitfall": "Saying the circular motion itself is S.H.M. It is the projection only.",
  "check": "Why does the period of a pendulum not depend on the mass of the bob?",
  "answer": "Because it is a projection, where the circle's radius drops out and only the "
            "length survives."},

 "7.2.3": {
  "meaning": "x = A sin(ωt + φ), v = Aω cos(ωt + φ), and a = -Aω² sin(ωt + φ), all from "
             "differentiating the displacement twice.",
  "why": "Because acceleration is the second time-derivative of displacement, and each "
         "differentiation multiplies by ω and shifts the phase by π/2.",
  "example": "Differentiating twice gives a = -ω²x, which is the restoring-force equation "
             "again.",
  "pitfall": "Forgetting the minus sign on the acceleration, or treating the phase as part "
             "of the amplitude.",
  "check": "If x = A sin(ωt), what is a in terms of x?",
  "answer": "a = -ω²x. The acceleration is always opposite to displacement and proportional "
            "to it."},

 "7.2.4": {
  "meaning": "Any problem giving a displacement expression or asking for a phase can be "
             "solved by reading off A, ω and φ and using the derivatives.",
  "why": "Because the three quantities fully determine the motion, and the derivatives give "
         "velocity and acceleration without any further information.",
  "example": "x = 0.05 sin(4t + π/2) gives A = 0.05 m, ω = 4 rad s⁻¹, φ = π/2, and at t = 0 "
             "the particle is at its positive extreme.",
  "pitfall": "Reading φ = π/2 as a time delay rather than a phase offset.",
  "check": "A particle starts at the mean position moving towards the positive extreme. "
           "What is φ in the sine form?",
  "answer": "φ = π/2, because sin(π/2) = 1 gives maximum displacement. For the cosine form "
            "it would be 0."},

 "7.2.5": {
  "meaning": "Displacement, velocity and acceleration graphs are the same sine curve "
             "shifted by a quarter period each, with the acceleration inverted.",
  "why": "Because each is the derivative of the previous one, and differentiation shifts "
         "the phase by a quarter period and multiplies by ω.",
  "example": "When x is at a maximum, v = 0 and a is at its most negative. The three curves "
             "are always a quarter period out of step.",
  "pitfall": "Drawing them in step, which is the single most common error in this topic.",
  "check": "When the displacement is zero, what are v and a?",
  "answer": "v is at its maximum and a is zero. The object passes through equilibrium at "
            "full speed but with no restoring force."},

 "7.3.1": {
  "meaning": "A mass on a spring obeying Hooke's law is exactly S.H.M., because the "
             "restoring force is proportional to displacement.",
  "why": "Because F = -kx and Newton's second law give a = -(k/m)x, which is the defining "
         "equation of S.H.M.",
  "example": "Double the spring constant and the frequency rises by √2, not by 2.",
  "pitfall": "Assuming a stiffer spring oscillates faster in direct proportion.",
  "check": "What happens to the period if the spring constant is quadrupled?",
  "answer": "It is halved, since T = 2π√(m/k). The frequency doubles."},

 "7.3.2": {
  "meaning": "T = 2π√(m/k) for a mass-spring system.",
  "why": "Because comparing the S.H.M. equation a = -ω²x with Newton's second law "
         "a = -(k/m)x gives ω = √(k/m), and then T = 2π/ω = 2π√(m/k). The derivation is "
         "two lines and no assumptions beyond Hooke's law.",
  "example": "m = 0.5 kg and k = 200 N m⁻¹ gives T = 2π√(0.5/200) = 0.314 s, so the "
             "frequency is about 3.2 Hz.",
  "pitfall": "Using g in place of k, or forgetting that mass is under the square root.",
  "check": "Why does the period not depend on gravity at all?",
  "answer": "Because the restoring force is the spring's, not gravity's. Gravity shifts the "
            "equilibrium position but does not change the frequency."},

 "7.3.3": {
  "meaning": "These problems are solved by rearranging T = 2π√(m/k) for whichever quantity "
             "is missing.",
  "why": "Because it is a single equation, and identifying the missing term tells you the "
         "form.",
  "example": "A 0.2 kg mass has period 0.9 s. The constant is k = 4π²m/T² = 9.8 N m⁻¹.",
  "pitfall": "Taking the square root of the wrong side, or dropping the 4π² factor.",
  "check": "How does the period change if the mass is quadrupled?",
  "answer": "It doubles, because mass is under the square root."},
})

LESSONS.update({
 "7.4.1": {
  "meaning": "A pendulum's motion is S.H.M. only for small angles. Beyond about 10 degrees "
             "the approximation starts to fail and the period grows.",
  "why": "The restoring force is -mg sin θ, which is only proportional to -θ when θ is "
         "small. The equation of motion is therefore only exactly linear in the limit.",
  "example": "At 5 degrees the error is 0.05 %; at 30 degrees it is 1.7 %; at 90 degrees "
             "the period is 17.6 % longer than the small-angle formula predicts.",
  "pitfall": "Treating 'small angle' loosely, and using 20 or 30 degrees when measuring a "
             "pendulum.",
  "check": "Why do physics pendulums use a small bob and a long string?",
  "answer": "A longer string reduces the angular excursion for a given sideways motion, so "
            "the angle stays small. A small bob keeps the period measurable with a stopwatch."},

 "7.4.2": {
  "meaning": "T = 2π√(L/g), where L is the distance from the pivot to the centre of the "
             "bob.",
  "why": "Because applying mL²θ'' = -mgθ to a small-angle oscillation and comparing with "
         "ω² = k/m gives the result. Note that the mass cancels entirely.",
  "example": "A 1 m pendulum has T = 2.01 s, giving g = 4π²L/T² = 9.80 m s⁻² when timed "
             "at the laboratory.",
  "pitfall": "Measuring to the bottom of the bob instead of its centre, which lengthens L "
             "and lengthens the measured period.",
  "check": "A pendulum is 1.5 times as long. How does the period change?",
  "answer": "By √1.5 = 1.22. Length is under the square root, so lengthening a pendulum by "
            "half only lengthens its period by about a fifth."},

 "7.4.3": {
  "meaning": "These problems are solved by rearranging T = 2π√(L/g) for the missing "
             "quantity, and by plotting T² against L to find g from the gradient.",
  "why": "Because squaring removes the square root and gives a straight line with gradient "
         "4π²/g, which uses every measurement rather than just one.",
  "example": "With L = 0.9 m and T = 1.93 s, g = 4π² × 0.9/1.93² = 9.52 m s⁻².",
  "pitfall": "Dividing instead of multiplying, or forgetting the 4π².",
  "check": "How would you find g most reliably from a pendulum?",
  "answer": "Time about 20 oscillations for several lengths, then plot T² against L. The "
            "gradient is 4π²/g, so g = 4π²/gradient."},

 "7.5.1": {
  "meaning": "For a mass-spring system the total energy is ½kA² and it is the same at every "
             "point of the motion.",
  "why": "Because integrating the restoring force gives ½kx², and adding the kinetic energy "
         "cancels the x-dependence exactly, leaving a constant.",
  "example": "A 0.5 kg mass on a 200 N m⁻¹ spring with amplitude 0.04 m has a total energy "
             "of 0.16 J, whatever its position.",
  "pitfall": "Expecting the energy to change between the extremes and the mean position. "
             "Only its division between forms changes.",
  "check": "How much kinetic energy is there at the extreme position?",
  "answer": "None. The speed is zero there, so all 0.16 J is potential."},

 "7.5.2": {
  "meaning": "Energy problems use E = ½kA² for the total, and the position only decides how "
             "it is divided.",
  "why": "Because the total is fixed by the amplitude alone, which makes the energy "
         "independent of the mass - a surprisingly useful result.",
  "example": "At x = A/2 the potential is ½k(A/2)² = ⅛kA² and the kinetic is ⅜kA², so the "
             "ratio is 1:3.",
  "pitfall": "Using ½mv² for the total energy instead of ½kA²; they are equal but only at "
             "the amplitude.",
  "check": "At what position is the kinetic energy half the total?",
  "answer": "At x = A/√2, because the kinetic energy is ½k(A² − x²) and that equals ¼kA² "
            "when x² = A²/2."},

 "7.5.3": {
  "meaning": "Kinetic and potential energy exchange continuously, crossing twice per period, "
             "with the sum unchanging.",
  "why": "Because the energy is stored in whichever form the motion currently allows: "
         "potential when the force is fighting the displacement, kinetic when the spring "
         "is relaxed.",
  "example": "Over one full oscillation the energy is entirely kinetic, entirely potential, "
             "entirely kinetic and entirely potential in turn.",
  "pitfall": "Plotting both curves rising together, or claiming energy is destroyed at the "
             "extreme.",
  "check": "How many times per cycle do the kinetic and potential energies exchange?",
  "answer": "Twice. Once near each extreme and once near each passage through the mean "
            "position."},

 "7.6.1": {
  "meaning": "A free oscillation runs on its own stored energy with no external driver. A "
             "forced one is driven at a chosen frequency.",
  "why": "Because the response to a driving force depends on the relation between the "
         "driving frequency and the natural frequency.",
  "example": "A tuning fork is a free oscillator; a singer shaking a glass is driving it "
             "forced.",
  "pitfall": "Assuming a free oscillation continues forever. Real ones damp away.",
  "check": "Is a pendulum swinging in still air free or forced?",
  "answer": "Free. Nothing external is driving it; it slows only because of damping."},

 "7.7.1": {
  "meaning": "Resonance is the large amplitude produced when the driving frequency equals "
             "the natural frequency.",
  "why": "Because each push then lands just as the system returns to the same phase, so "
         "energy is fed in faster than damping removes it.",
  "example": "A glass dropped at the frequency of a note that matches its own vibrates "
             "violently enough to break.",
  "pitfall": "Thinking resonance means a large amplitude only at one exact frequency with "
             "nothing either side. The response is a curve with a peak.",
  "check": "What happens to the amplitude if the driving frequency is changed by only one "
           "per cent away from resonance?",
  "answer": "It falls sharply. The resonance peak is narrow for a lightly damped system and "
            "broad for a heavily damped one."},

 "7.7.2": {
  "meaning": "Resonance is useful for selecting a frequency and dangerous when it is "
             "unnoticed.",
  "why": "Because any system driven at its natural frequency accumulates energy, and how "
         "much depends on how lightly it is damped.",
  "example": "Soldiers break step on bridges; aircraft are tuned to avoid structural modes; "
             "radio receivers use resonance to select one station.",
  "pitfall": "Believing only the dangerous examples. Selecting a radio station is resonance "
             "used deliberately.",
  "check": "Why is a tall building given a tuned mass damper?",
  "answer": "To stop wind-driven resonance. The damper is tuned to the building's natural "
            "frequency so it moves out of phase with the wind's driving force."},

 "7.8.1": {
  "meaning": "A damped oscillator loses energy steadily to friction, air resistance and "
             "sound, so its amplitude falls while the frequency is nearly unchanged.",
  "why": "Because the energy leaks away as heat and sound in the surroundings rather than "
         "staying in the motion, and the restoring force that sets the frequency is "
         "unaffected.",
  "example": "A pendulum amplitude falls off roughly as exp(-bt/2m), but its period changes "
             "very little.",
  "pitfall": "Expecting damping to change the frequency noticeably. That only happens for "
             "heavy damping.",
  "check": "Does a damped oscillator still oscillate forever, in principle?",
  "answer": "No. For any non-zero damping the amplitude decays to zero. With no damping at "
            "all it would persist indefinitely, which is idealised and unphysical."},

 "7.8.2": {
  "meaning": "Shock absorbers, door closers, suspension dampers and compasses in water all "
             "exist to remove energy deliberately.",
  "why": "Because unwanted motion is usually worse than the energy it costs to stop it, and "
         "damping converts that energy harmlessly into heat.",
  "example": "A bicycle's fork damper controls the rebound after a bump so the wheel keeps "
             "contact with the ground.",
  "pitfall": "Confusing damping with resonance. Damping protects; resonance destroys.",
  "check": "Why is a car more comfortable with shock absorbers?",
  "answer": "Without them the body would keep oscillating after every bump, because the "
            "springs alone store and return the energy."},

 "7.8.3": {
  "meaning": "Light damping oscillates many times before settling, critical damping returns "
             "fastest without overshoot, and heavy damping does not oscillate at all.",
  "why": "Because damping sets how much of the energy survives each cycle, and the return to "
         "equilibrium can happen either smoothly, on the first swing, or not at all.",
  "example": "A pendulum in air is lightly damped; a car shock absorber is tuned close to "
             "critical.",
  "pitfall": "Calling critical damping 'no damping'. It is the most damping that still "
             "returns without overshooting.",
  "check": "Which kind of damping would you want in a lift to stop it at the floor "
           "without a bounce?",
  "answer": "Critical, or very close to it. It gives the fastest return to equilibrium with "
            "no overshoot."},
})

LESSONS.update({
 "8.1.1": {
  "meaning": "A progressive wave carries energy from one place to another without the "
             "medium itself travelling.",
  "why": "Because the disturbance is a pattern of displacement, and the pattern moves while "
         "each particle stays where it is.",
  "example": "A stone's ripple reaches the far shore while the water at this shore is back "
             "where it started.",
  "pitfall": "Saying the medium moves along with the wave.",
  "check": "Does a sound wave carry air from the singer to the listener?",
  "answer": "No. Each air molecule oscillates about its own position; the energy is what "
            "travels, about 340 m each second."},

 "8.1.2": {
  "meaning": "Energy is transferred through the medium; the medium itself only oscillates.",
  "why": "Because work is done by the restoring force as each element of the medium is "
         "displaced, and that work becomes the energy of the pulse.",
  "example": "In a stretched string the pulse carries both kinetic energy, in the moving "
             "mass, and potential energy, in the deformation.",
  "pitfall": "Expecting energy to be conserved only in one of those forms at any instant.",
  "check": "Where is the energy of a transverse pulse at maximum displacement?",
  "answer": "Entirely potential. The string is deformed but momentarily stationary, so all "
            "the energy is stored in the deformation."},

 "8.1.3": {
  "meaning": "Intensity is power per area, and it varies as the square of the amplitude.",
  "why": "Because energy is carried at the rate that mass is set moving, and the work done "
         "in moving an element scales with the square of how far it is displaced. Two "
         "effects therefore compound: twice the amplitude moves twice the mass and twice "
         "as far per cycle, which is a factor of four, and doubles the energy each element "
         "carries, a further factor of four.",
  "example": "Quadrupling the amplitude multiplies the intensity by sixteen. This is a very "
             "unfriendly law for a loudspeaker, which is why they are built to work at small "
             "excursions.",
  "pitfall": "Saying intensity varies directly with amplitude, or ignoring the area in "
             "intensity = power/area.",
  "check": "How much louder is a sound if the amplitude doubles?",
  "answer": "Four times the intensity. This is why small amplitude increases are "
            "perceptually large."},

 "8.1.4": {
  "meaning": "V = fλ connects speed, frequency and wavelength for every wave.",
  "why": "Because in one period, T = 1/f, the wavefront advances by exactly one wavelength. "
         "Those three quantities cannot be varied independently, so any one of them fixes "
         "the product of the other two. That single constraint is what makes the formula so "
         "widely useful.",
  "example": "A 440 Hz sound of wavelength 0.773 m travels at 340 m s⁻¹, since "
             "440 × 0.773 = 340. Double the frequency and you must halve the wavelength "
             "or the speed, and the speed is usually fixed by the medium.",
  "pitfall": "Changing the frequency when a wave crosses from air into water. The frequency "
             "is set by the source and does not change; only the speed and the wavelength "
             "do.",
  "check": "Sound enters water and its speed rises. What happens to the wavelength?",
  "answer": "It rises in proportion, because the frequency is unchanged. If the speed rises "
            "by a factor 4.4, so does the wavelength."},

 "8.2.1": {
  "meaning": "Transverse waves oscillate perpendicular to their direction of travel; "
             "longitudinal waves oscillate along it.",
  "why": "Because the two must be drawn with their motion in different directions: one "
         "perpendicular to travel and one along it, so the longitudinal wave needs sliders "
         "rather than a curve. A transverse wave needs a medium stiff enough to "
         "supply a sideways restoring force, which is why light, which is a changing "
         "electric field, is transverse while a displacement wave in air cannot be.",
  "example": "Light and water ripples are transverse; sound in air is longitudinal, which is "
             "why sound cannot travel through a vacuum and light can.",
  "pitfall": "Thinking the *wave* moves sideways in a transverse wave. The wave moves along "
             "its length; only the particles move across.",
  "check": "Can a longitudinal wave pass through air? Why not through a solid?",
  "answer": "It passes through air, which offers negligible resistance to compression and "
            "rarefaction. In a solid the layers resist being pushed past one another."},

 "8.2.2": {
  "meaning": "A transverse wave is drawn as a wave shape, because the particles move up and "
             "down while the wave travels sideways. A longitudinal wave is drawn as a row "
             "of particles sliding past one another, because they move along the direction "
             "of travel.",
  "why": "Because the two motions are perpendicular, the drawing has to show the motion as "
         "well as the wave itself. A sinusoid only ever describes displacement across "
         "the direction of travel, so drawing a longitudinal wave as one silently "
         "misrepresents the physics. The slinky pushed along its length is the honest "
         "picture: the coils compress and rarefy in turn.",
  "example": "A slinky pushed along shows compressions and rarefactions moving down it.",
  "pitfall": "Drawing a longitudinal wave as a sinusoid, which is the usual mistake.",
  "check": "What do the crowded regions of a longitudinal wave represent?",
  "answer": "Compressions, where the particles are close together and the pressure is "
            "above normal."},

 "8.3.1": {
  "meaning": "When two waves overlap, each carries on unaffected and the resultant is the "
             "sum of their displacements.",
  "why": "Because the equation of motion for the medium is linear: it contains no term in "
         "the square of the displacement, so any set of wave-shaped solutions can be added "
         "and the result is another valid solution. The pulses pass through because nothing "
         "in the physics makes them interact.",
  "example": "Two pulses crossing through each other emerge unchanged in size and shape, "
             "and every joule that disappears from one point of the medium reappears at "
             "another.",
  "pitfall": "Expecting the waves to bounce off each other or pass through weakened.",
  "check": "What happens to two pulses after they have passed through each other?",
  "answer": "Nothing. Each emerges exactly as it entered. That is why you can hear two "
            "people speaking at once and understand both."},

 "8.3.2": {
  "meaning": "Interference occurs where two coherent waves overlap: constructive where they "
             "agree and destructive where they oppose.",
  "why": "Because the resultant displacement is the sum of the two, so amplitudes add or "
         "subtract according to the phase difference, and the energy carried by the result "
         "redistributes into the constructive regions. Nothing is destroyed at a node; it has "
         "gone somewhere else along the wave.",
  "example": "Headphones use interference to cancel noise reaching each ear, and active noise "
             "cancelling depends precisely on the outgoing wave arriving at the ear 180° out "
             "of phase with the noise.",
  "pitfall": "Expecting interference to destroy energy. It only redistributes it; at a node "
             "the energy goes elsewhere.",
  "check": "Why must the two sources be coherent for a steady interference pattern?",
  "answer": "Their phase difference must be constant. If it wanders, the pattern moves too "
            "fast to see and averages to silence."},

 "8.3.3": {
  "meaning": "Phase difference is measured in degrees or radians, with 360° being one full "
             "cycle.",
  "why": "Because each wave repeats every period, so the fraction of a period by which two "
         "waves are offset completely describes their relative state. Once the phase is "
         "known, the amplitudes either add or subtract, and nothing else about the two "
         "waves matters.",
  "example": "A 180° phase difference is total opposition, giving destructive interference; "
             "0° gives constructive. A quarter wavelength of path difference gives a 90° "
             "phase shift.",
  "pitfall": "Equating phase difference with time difference without dividing by the period.",
  "check": "A path difference of λ/2 corresponds to what phase difference?",
  "answer": "π radians or 180°, since a half-wavelength offset is half a cycle."},

 "8.3.4": {
  "meaning": "Two sounds of nearly equal frequency produce beats at the difference of their "
             "frequencies.",
  "why": "Because their superposition gives a carrier wave whose amplitude oscillates at "
         "the difference frequency, and the ear hears that amplitude pulsing as beats.",
  "example": "Two forks at 440 and 444 Hz give four beats per second, and the formula is "
             "|f₁ − f₂|.",
  "pitfall": "Using the sum of the frequencies, or forgetting the absolute value.",
  "check": "How can you measure an unknown frequency with a known one using beats?",
  "answer": "Count the beats per second, and the unknown is the known frequency plus or "
            "minus that count. Raising the pressure makes the beat rate fall, which tells "
            "you whether the unknown fork is higher."},

 "8.4.1": {
  "meaning": "Nodes are points of no permanent vibration; antinodes are points of maximum "
             "vibration.",
  "why": "Because in a stationary wave the two component waves cancel completely at a node "
         "and add completely at an antinode.",
  "example": "The middle of a string fixed at both ends is a node for the fundamental, "
             "which is why the first harmonic has half a wavelength along it.",
  "pitfall": "Thinking nodes are points where nothing happens. They are points where the two "
             "waves continually cancel.",
  "check": "How far apart are adjacent nodes?",
  "answer": "Half a wavelength. The pattern repeats every λ/2, with a node at each end of "
            "each half-wavelength."},

 "8.4.2": {
  "meaning": "Two identical waves travelling in opposite directions produce a wave that "
             "does not travel: nodes and antinodes stay fixed.",
  "why": "Because at every point the two displacements are equal and opposite at a node, "
         "and equal in direction at an antinode, and both of those relationships are "
         "permanent.",
  "example": "A stretched string clamped at both ends, and an air column in a closed pipe, "
             "both support stationary waves.",
  "pitfall": "Using the open-pipe rule for a closed pipe. A closed pipe has a node at the "
             "closed end and supports odd multiples of a quarter wavelength.",
  "check": "A pipe closed at one end resonates at 200 Hz. What is the next resonance?",
  "answer": "600 Hz, not 400. A closed pipe supports 1, 3, 5 … quarter wavelengths, so the "
            "frequencies are in the ratio 1:3:5."},

 "8.4.3": {
  "meaning": "Stationary wave problems use L = nλ/2 for strings and L = (2n−1)λ/4 for "
             "closed pipes, with the boundary condition fixing n.",
  "why": "Because the allowed patterns are exactly those satisfying the boundary conditions "
         "at both ends.",
  "example": "A 1.5 m string at 50 Hz has v = fλ = 50 × 3 = 150 m s⁻¹ if λ = 3 m is the "
             "only mode that fits.",
  "pitfall": "Forgetting that the wavelength is fixed by the length, so changing the "
             "frequency changes the mode rather than fitting more wavelengths.",
  "check": "A 0.60 m pipe, open at both ends, has its first resonance at 140 Hz. What is "
           "the second?",
  "answer": "420 Hz, three times as high. An open pipe supports nλ/2, so the frequencies "
            "are in the ratio 1:2:3."},

 "8.5.1": {
  "meaning": "The Doppler effect is the apparent change in frequency when source and "
             "observer move relative to each other.",
  "why": "Because moving the source changes the spacing of the wavefronts it emits, and "
         "moving the observer changes how often those wavefronts are encountered.",
  "example": "A siren drops in pitch as it passes you, because you move from meeting the "
             "wavefronts head-on to meeting them from behind.",
  "pitfall": "Thinking the frequency of the source actually changes. It does not; only the "
             "apparent frequency does.",
  "check": "Why does a sound become higher as an ambulance approaches you?",
  "answer": "You are moving towards the wavefronts, so you encounter them more often per "
            "second than they are emitted."},

 "8.5.2": {
  "meaning": "If the source moves towards a stationary listener, f' = fv/(v−vs); if the "
             "listener moves towards a stationary source, f' = f(v+vo)/v; both together, "
             "f' = f(v+vo)/(v−vs); and both away, with the signs reversed.",
  "why": "Because the two cases are different mechanisms: a moving source compresses the "
         "spacing of the wavefronts it emits, while a moving observer changes the rate at "
         "which they are met.",
  "example": "A car sounding 500 Hz at 20 m s⁻¹ in air (v = 340) oncoming to a stationary "
             "observer gives 500 × 340/320 = 531 Hz.",
  "pitfall": "Using the moving-source formula for a moving observer, or forgetting to "
             "reverse the signs for a receding body.",
  "check": "A source recedes at half the speed of sound. What fraction of its true frequency "
           "is heard?",
  "answer": "v/(v + vs) = v/(v + v/2) = 2/3, so about 0.67f. Receding always lowers the "
            "pitch."},

 "8.5.3": {
  "meaning": "Doppler problems are solved by identifying which bodies are moving towards "
             "each other, assigning the signs, and substituting.",
  "why": "Because the four cases are one formula with the signs of vs and vo set by the "
         "direction of motion.",
  "example": "Observer at 10 m s⁻¹ towards a source at 20 m s⁻¹ towards them, f = 500, "
             "v = 340: f' = 500 × (340+10)/(340−20) = 547 Hz.",
  "pitfall": "Measuring all speeds as positive magnitudes without deciding the direction of "
             "relative motion first.",
  "check": "When source and observer both approach at the same speed, is the pitch higher or "
           "lower than the true frequency?",
  "answer": "Higher, always. The numerator grows and the denominator shrinks, so the shift is "
            "greater than either case alone."},

 "8.5.4": {
  "meaning": "The Doppler effect applies to light exactly as it does to sound, with the "
             "speed of light in place of the speed of sound.",
  "why": "Because the reasoning about wavefront spacing does not depend on what the wave is, "
         "only on its speed.",
  "example": "Stars are classified by whether their spectra are shifted towards the red or "
             "towards the blue, and that shift gives their radial velocity.",
  "pitfall": "Thinking the effect is negligible for light because the speed of light is so "
             "large. At stellar speeds it is enormous.",
  "check": "Why must astronomers observe light at wavelengths outside the visible range?",
  "answer": "So they can observe the hydrogen lines in the ultraviolet, and the visible "
            "redshift of anything beyond a nearby galaxy then moves them into the visible "
            "band."},

 "8.5.5": {
  "meaning": "Radar, sonar and satellite tracking all work by sending a wave and detecting "
             "the reflected wave, whose frequency shift reveals the relative motion.",
  "why": "Because the returning wave has travelled a path in which both source and target "
         "moved, and the frequency shift on reflection encodes their radial velocity.",
  "example": "Police radar measures the Doppler shift of the reflected microwave to find a "
             "vehicle's speed. Red and blue shifts are the same effect applied to distant "
             "galaxies.",
  "pitfall": "Confusing a radar reflection with an echo of the original frequency. The "
             "moving reflector is what introduces the shift.",
  "check": "Why does a galaxy's light appear redder when it is receding?",
  "answer": "Because its whole spectrum is Doppler-shifted towards longer wavelengths by the "
            "same mechanism as a receding siren."},

 "8.6.1": {
  "meaning": "Waves are used in medicine for imaging and therapy, in digital transmission, "
             "in storing information, and in monitoring earthquakes and tsunamis.",
  "why": "Because a wave carries information reliably through media that would block a "
         "particle or a direct signal.",
  "example": "An ultrasound scan is a reflected sound wave above the audible range; "
             "hard drives read the wave pattern off a spinning disc.",
  "pitfall": "Equating 'modern application' with 'invented recently'. Waves in all four "
             "roles are old, and the physics has not changed.",
  "check": "Why can ultrasound image an unborn baby when light cannot?",
  "answer": "Sound is only weakly attenuated by tissue, while light is scattered within a "
            "few millimetres. The contrast comes from reflecting boundaries, not from "
            "penetration."},
})

LESSONS.update({
 "9.1.1": {
  "meaning": "Corpuscular, wave, electromagnetic and quantum theories of light each "
             "explained something the previous one could not.",
  "why": "Because each was the best available account of the evidence at the time, and each "
         "failed on a specific experiment. Newton explained straight lines but not "
         "diffraction; Huygens explained diffraction but needed an aether; Maxwell removed "
         "the aether but said nothing about the photoelectric effect.",
  "example": "The wave picture says light interferes; the quantum picture says it arrives in "
             "quanta. Neither contradicts the other, because they are predictions of "
             "different experiments.",
  "pitfall": "Asking which is correct. The question is which theory predicts the result of "
             "the experiment in front of you.",
  "check": "Which theory of light cannot explain why light slows down entering glass?",
  "answer": "Newton's. He predicted light should travel faster in a denser medium, and it "
            "does not."},

 "9.1.2": {
  "meaning": "A wavefront is the surface joining all the points the wave has reached at the "
             "same instant.",
  "why": "Because the wave is a moving surface of constant phase, and that surface travels "
         "normal to itself at every point.",
  "example": "The circular fronts from a dropped pebble, and the nearly straight fronts from "
             "a distant loudspeaker.",
  "pitfall": "Thinking wavefronts move sideways, or that a wavefront is the path of a "
             "particle.",
  "check": "In what direction does a circular wavefront travel?",
  "answer": "Outward from the centre, radially, and always normal to itself."},

 "9.1.3": {
  "meaning": "Every point on a wavefront acts as a source of secondary wavelets, and the "
             "new wavefront is the envelope that just touches them all.",
  "why": "Because each point of the medium at the front of the disturbance begins the same "
         "disturbance as soon as the front arrives. The envelope is the locus of the "
         "earliest wavelets, which is where the medium is first disturbed.",
  "example": "Huygens' construction gives reflection, refraction and diffraction from one "
             "rule, and explains why a shadow has a sharp edge.",
  "pitfall": "Drawing the new wavefront through the centres of the wavelets. It must touch "
             "them, not pass through them.",
  "check": "Why does refraction follow from Huygens' principle?",
  "answer": "Wavelets travel fastest in the less dense medium, so the envelope leans towards "
            "the slow side, bending the ray towards the normal."},

 "9.2.1": {
  "meaning": "Coherent sources keep a constant phase difference; monochromatic sources emit "
             "one wavelength.",
  "why": "Coherence is what makes a pattern stationary rather than a blur, and "
         "monochromaticity is what keeps the fringes clean rather than smeared.",
  "example": "Two sodium lamps emit the same frequency but are not coherent, so any fringes "
             "average away instantly. Two slits cut from one wavefront are perfectly "
             "coherent.",
  "pitfall": "Assuming equal frequency implies coherence. It does not; the phase must also "
             "be constant.",
  "check": "Why must a two-slit experiment use one source rather than two?",
  "answer": "Because two independent sources drift in and out of phase, so the pattern moves "
            "too fast to see and averages to uniform brightness."},

 "9.2.2": {
  "meaning": "Interference of light is the redistribution of intensity where two coherent "
             "waves overlap.",
  "why": "Because the resultant displacement is their sum, so amplitudes add or subtract "
         "according to the phase.",
  "example": "Young's experiment gives bright and dark fringes that can be measured and used "
             "to find a wavelength far too small to measure any other way.",
  "pitfall": "Expecting the dark parts to be regions of destroyed energy. The energy has "
             "gone into the bright parts.",
  "check": "Why does light interference need such precise alignment that it is hard to see "
           "by hand?",
  "answer": "Because the path difference between two points on a wavefront must be constant "
            "to within a small fraction of a wavelength, and a wavelength of 500 nm is a "
            "fifth of a hair's breadth."},

 "9.2.3": {
  "meaning": "The conditions are coherent sources, the same frequency, comparable "
             "amplitudes, and a path difference within the coherence length.",
  "why": "Each condition removes one way the pattern can be destroyed, and all four are "
         "needed.",
  "example": "Washing colours on cloth works only in daylight because daylight has enough "
             "spectral range; in coloured light the fringes from different wavelengths land "
             "on top of each other and wash out.",
  "pitfall": "Forgetting amplitude. Two waves of very unequal amplitude interfere, but the "
             "fringes are faint and the visibility is poor.",
  "check": "Which condition fails when you observe interference in white light?",
  "answer": "Monochromaticity. Each wavelength makes its own fringe system, and the systems "
            "overlap."},

 "9.2.4": {
  "meaning": "Young's apparatus splits one wavefront into two coherent beams, recombines "
             "them, and lets the interference pattern fall on a screen.",
  "why": "Because the two beams must start from the same wavefront to have any chance of a "
         "fixed phase difference.",
  "example": "Light through two slits 0.5 mm apart gives fringes about 1 mm apart on a "
             "screen a metre away.",
  "pitfall": "Using two separate lamps, which can never be coherent.",
  "check": "Why are the slits much narrower than their separation?",
  "answer": "So each slit diffracts into a wide, nearly spherical wave, and the two "
            "overlapping wavefronts interfere across a wide screen instead of only behind "
            "the slits."},

 "9.2.5": {
  "meaning": "Fringe spacing is dy = λL/d, with bright fringes at y = nλL/d and dark ones "
             "at y = (n + ½)λL/d.",
  "why": "Because the path difference from the slits is approximately d sin θ, and with "
         "y/L ≪ 1 that becomes dy ≈ dL. Setting it equal to a whole or half wavelength "
         "gives the positions.",
  "example": "λ = 550 nm, L = 1 m, d = 0.5 mm gives dy = 1.1 mm.",
  "pitfall": "Using the small-angle approximation where it does not hold, or forgetting "
             "that the dark fringes are at half-integer positions.",
  "check": "What happens to the fringe spacing if the slit separation is doubled?",
  "answer": "It is halved, because dy is inversely proportional to d."},

 "9.2.6": {
  "meaning": "Fringe-spacing problems give λ, L, d and dy, and one of them is the unknown.",
  "why": "Because there is one equation, so the missing quantity tells you the form.",
  "example": "L = 1.2 m, d = 0.4 mm and 12 fringes over 22 mm give λ = dy d/L = 7.3 × "
             "10⁻⁷ m.",
  "pitfall": "Counting fringes rather than the gaps between them: n fringes span n−1 gaps.",
  "check": "If 10 fringes occupy 9.0 mm, what is the fringe spacing?",
  "answer": "1.0 mm, because 10 fringes span 9 gaps. This off-by-one is the commonest error "
            "in the topic."},

 "9.3.1": {
  "meaning": "Michelson's interferometer splits a beam at a half-silvered mirror, sends the "
             "two arms down and back, and recombines them into a circular fringe pattern.",
  "why": "Because splitting and recombining keeps the two beams coherent over a very long "
         "path, which is what makes it sensitive enough to detect a shift of a fraction of "
         "a wavelength.",
  "example": "Moving one mirror by λ/2 moves one fringe, which is why the instrument is an "
             "extremely fine length measure.",
  "pitfall": "Halving the distance change. The light makes the round trip, so the path "
             "changes by twice the mirror movement.",
  "check": "A mirror moves 0.5 µm and one fringe passes. What is the wavelength?",
  "answer": "2 µm, because the round trip doubled it: path change = 1 µm = λ."},

 "9.3.2": {
  "meaning": "Gravitational waves are ripples in spacetime caused by accelerating massive "
             "bodies.",
  "why": "Because general relativity says mass curves spacetime and matter in motion drags "
         "it, so anything that accelerates sharply radiates spacetime disturbances.",
  "example": "Neutron stars spiralling into each other radiate enough power in gravitational "
             "waves to outshine whole galaxies, and LIGO detects a change of 10⁻¹⁸ m.",
  "pitfall": "Confusing them with electromagnetic waves. They pass straight through matter "
             "without being scattered.",
  "check": "Why can gravitational waves pass through a galaxy?",
  "answer": "Because they are distortions of spacetime itself, not disturbances of the "
            "electromagnetic field, so ordinary matter is essentially transparent to them."},

 "9.3.3": {
  "meaning": "A passing gravitational wave stretches spacetime in one direction while "
             "squeezing it in the perpendicular direction.",
  "why": "Because the metric tensor is traceless: the wave adds in one direction and removes "
         "in the other, leaving the volume unchanged.",
  "example": "LIGO's two perpendicular arms change length alternately, one going out while "
             "the other comes in.",
  "pitfall": "Expecting the wave to stretch in both directions at once.",
  "check": "How do LIGO's two arms respond to one pass of a wave?",
  "answer": "One lengthens while the other shortens, half a cycle apart. That differential "
            "is what makes an interferometer the right instrument to detect it."},

 "9.3.4": {
  "meaning": "Interferometers detect gravitational waves by measuring arm length changes far "
             "below the size of a proton.",
  "why": "Because the arms are kilometres long, so the strain of 10⁻²¹ becomes a measurable "
         "length of 10⁻¹⁸ m, and no material can be used that would drift.",
  "example": "LIGO suspends each mirror in a four-stage pendulum so it is effectively "
             "decoupled from the ground, and works in a vacuum to remove air currents.",
  "pitfall": "Considering the ordinary optical interference the instrument already "
             "produces. That is a nuisance to be suppressed, not the signal.",
  "check": "Why must LIGO's mirrors be isolated from the ground?",
  "answer": "Ground motion and acoustic noise are far larger than the signal. Without "
            "suspension and vacuum the arms would drown in noise, which is why LIGO uses "
            "four-stage pendulums, seismic isolation and a 1 km vacuum tube."},
})

LESSONS.update({
 "9.4.1": {
  "meaning": "Diffraction is the spreading of light past an obstacle or through an opening, "
             "wider for longer wavelengths and narrower openings.",
  "why": "Because it is the spreading of every wave past its edges, and it becomes "
         "significant when the opening is comparable to the wavelength.",
  "example": "You can hear round a doorway because sound diffracts, but you cannot see round "
             "it because visible wavelengths are so much shorter.",
  "pitfall": "Expecting a sharp shadow always. With a small source and a small object the "
             "shadow edges are blurred by diffraction.",
  "check": "Why can you hear a conversation round a corner but not see the speakers?",
  "answer": "Sound wavelengths are of the order of a metre, comparable to the doorway, so "
            "they diffract strongly. Visible light is around 500 nm, five million times "
            "smaller."},

 "9.4.2": {
  "meaning": "A diffraction grating is many equally spaced slits, producing sharp, intense "
             "principal maxima whose brightness grows with the number of lines.",
  "why": "Because the wavelets from all the slits add only at angles where the path "
         "difference is a whole number of wavelengths; elsewhere they mostly cancel.",
  "example": "A grating with 5000 lines per mm separates the sodium D lines, which are 0.6 nm "
             "apart, far beyond the resolving power of a prism.",
  "pitfall": "Expecting the fringes to be broad as in a single slit. More lines means "
             "sharper maxima and the same width regardless of slit spacing.",
  "check": "Why does a grating have far more resolving power than a single slit?",
  "answer": "Because its maxima are extremely sharp - each slit contributes to a very narrow "
            "range of angle - so two close wavelengths land at visibly different angles."},

 "9.4.3": {
  "meaning": "A single slit gives a broad central maximum twice as wide as the rest, with "
             "minima at a sin θ = mλ for m = 1, 2, 3 and no minimum at m = 0.",
  "why": "Because the light from across the whole slit interferes, and the cancellation is "
         "strongest for a wide slit at small angles.",
  "example": "The shadow of a hand is sharp-edged, but the shadow of a finger from a distant "
             "lamp is soft, because the finger is comparable to a wavelength in some "
             "dimension only.",
  "pitfall": "Using the grating formula for a single slit. The two are different: a slit has "
             "mλ = a sin θ for minima and a grating has mλ = d sin θ for maxima.",
  "check": "Why is the central maximum twice as wide as the others?",
  "answer": "Because it is bounded by minima on either side at ±λ/a, whereas the other "
            "maxima are bounded by minima a full λ/a apart. There is no minimum at zero, so "
            "the central band is twice as wide."},

 "9.4.4": {
  "meaning": "Diffraction problems use a sin θ = mλ for slit minima, and give λ, a and θ "
             "with one unknown.",
  "why": "Because the positions of the minima are fixed by the cancellation condition.",
  "example": "With a = 0.1 mm and m = 1, λ = 550 nm gives sin θ = 5.5 × 10⁻³, or θ = 0.32°.",
  "pitfall": "Forgetting that sin θ ≤ 1, so minima exist only up to mλ ≤ a. Beyond that "
             "there are no more minima, and the problem becomes about the maximum order.",
  "check": "How many minima are there for a = 0.1 mm and λ = 550 nm?",
  "answer": "mλ ≤ a gives m ≤ 0.1e-3/550e-9 = 182, so there are 181 minima plus the central "
            "maximum. Most of them are very close to the axis."},

 "9.5.1": {
  "meaning": "Bragg's law is 2d sin θ = mλ, where θ is the glancing angle to the plane.",
  "why": "Because the lower ray travels an extra 2d sin θ on the way down to the next plane "
         "and back up, and for the reflections to add that must be a whole number of "
         "wavelengths.",
  "example": "X-rays reflected from a crystal with d = 0.5 nm at 1° give a first-order "
             "reflection, since 2 × 0.5e-9 × sin 1° = 17 nm.",
  "pitfall": "Measuring θ from the normal instead of from the plane, which halves the "
             "answer and is the classic error in this topic.",
  "check": "Why are X-ray detectors always quoted at 2θ?",
  "answer": "Because 2θ is the angle between the incident and the reflected beam, which is "
            "what the detector arm actually reads."},

 "9.5.2": {
  "meaning": "X-rays diffract from the atomic planes in a crystal, and the angles of the "
             "reflections reveal the arrangement.",
  "why": "Because the spacing of the planes is comparable to the X-ray wavelength, so the "
         "diffraction angles are large enough to measure.",
  "example": "Sodium chloride gives reflections at d, d/2, d/3 with intensities that reveal "
             "the face-centred cubic arrangement.",
  "pitfall": "Using visible light, whose wavelength is far too short to diffract off atomic "
             "planes at all.",
  "check": "Why is the diffraction angle for crystal planes so large?",
  "answer": "Because the plane spacing is only a few ångströms, comparable to the wavelength, "
            "so the angle needed to reach the first order is tens of degrees."},

 "9.5.3": {
  "meaning": "The derivation compares two rays from the same incoming wave: the lower one "
             "reflects off the next plane down and travels an extra 2d sin θ.",
  "why": "Because the two rays must arrive in phase for the reflection to be bright, and the "
         "path difference is exactly that extra distance.",
  "example": "Setting 2d sin θ = mλ gives Bragg's law, and the order m counts how many "
             "wavelengths the extra path represents.",
  "pitfall": "Forgetting that m must be a whole number, so the angles are discrete and not "
             "continuous.",
  "check": "What happens if the angle does not satisfy Bragg's law for any whole m?",
  "answer": "The reflections from successive planes cancel and no X-rays get through. That is "
            "why the crystal is rotated to find the peaks."},

 "9.5.4": {
  "meaning": "Bragg problems give d, λ, θ and m, with one of them unknown.",
  "why": "Because there is one equation with a whole-number constraint on m.",
  "example": "d = 0.28 nm and first order at 17° gives λ = 2 × 0.28e-9 × sin 17° = 1.64 × "
             "10⁻¹⁰ m, which is a soft X-ray.",
  "pitfall": "Using the largest m that appears to work when the correct answer is the "
             "smallest integer.",
  "check": "With λ = 1.54 × 10⁻¹⁰ m and d = 0.23 nm, what is the highest possible order?",
  "answer": "2, because m ≤ 2d/λ = 2.99. The third order would need sin θ > 1."},

 "9.6.1": {
  "meaning": "Unpolarised light vibrates in every plane at once; plane-polarised light "
             "vibrates in one plane only.",
  "why": "Because ordinary light comes from millions of atoms emitting independently, each "
         "with a random direction, and the sum has no preferred plane.",
  "example": "Sunlight and an ordinary bulb are unpolarised; light after a polaroid is "
             "polarised.",
  "pitfall": "Thinking unpolarised light has no direction of vibration. It has every "
             "direction at once.",
  "check": "Is light from a single excited atom polarised or unpolarised?",
  "answer": "Polarised. The unpolarisation comes from the huge number of randomly oriented "
            "atoms in a source, not from the individual emission."},

 "9.6.2": {
  "meaning": "Only transverse waves can be polarised, because polarisation selects a plane "
             "of vibration and a longitudinal wave has none.",
  "why": "Because polarisation means selecting a plane of vibration, and a longitudinal "
         "wave's particles vibrate along the direction of travel rather than across it. "
         "There is no plane there to select, so turning any filter changes nothing at all. "
         "Transverse waves do have such a plane, and rotating a filter relative to it "
         "changes the transmitted amount continuously.",
  "example": "Sound in air cannot be polarised, but light can. This is one of the cleanest "
             "tests separating the two kinds of wave.",
  "pitfall": "Attempting to polarise sound and expecting the same result as with light.",
  "check": "Why can sound in air not be polarised?",
  "answer": "Because its particles vibrate along the direction of travel. Rotating any "
            "filter changes nothing, since there is no plane of vibration to select."},

 "9.6.3": {
  "meaning": "At Brewster's angle, tan θ_B = n₂/n₁, the reflected light is completely "
             "plane-polarised and the reflected and refracted rays are at right angles.",
  "why": "Because only the component of the electric field perpendicular to the plane of "
         "incidence is reflected; at Brewster's angle the other component is transmitted "
         "entirely.",
  "example": "Sunlight reflecting off a wet road at about 57° is polarised, which is why "
             "polarising sunglasses cut glare so effectively.",
  "pitfall": "Expecting the transmitted light to be polarised. It is partly polarised "
             "perpendicular to the reflected direction.",
  "check": "For glass of index 1.5 in air, what is Brewster's angle?",
  "answer": "arctan 1.5 = 56.3°. Note it does not depend on the wavelength, unlike Snell's "
            "law."},

 "9.6.4": {
  "meaning": "A polaroid passes only the component of vibration along its transmission axis, "
             "halving unpolarised light and transmitting I₀ cos²θ thereafter.",
  "why": "Because the molecules inside are aligned, so they absorb the vibration component "
         "across the chain and allow the one along it.",
  "example": "Two crossed polarisers give a black view; inserting a third at 45° lets light "
             "through again.",
  "pitfall": "Expecting the third polariser to reduce the light. Adding a filter can never "
             "increase transmission - but it can, because the middle one re-orients the "
             "vibrations.",
  "check": "Why does a third polariser at 45° brighten the view?",
  "answer": "Because the middle one converts the light into 45° polarised light, and the "
            "final one at 45° then passes half of that rather than none. The middle polariser "
            "re-orients the vibrations rather than merely absorbing them."},

 "9.6.5": {
  "meaning": "Malus's law states I = I₀ cos²θ, where θ is the angle between the transmission "
             "axes.",
  "why": "Because a polaroid passes only the component of the electric field along its "
         "transmission axis, and that component is the amplitude multiplied by the cosine "
         "of the angle. The transmitted intensity is the square of the amplitude, so the "
         "cosine gets squared as well - which is the whole reason the law is a cos squared "
         "and not a cosine.",
  "example": "At 45° exactly half passes; at 60° a quarter passes. The dependence falls away "
             "steeply as the angle grows.",
  "pitfall": "Applying it to the first polaroid, where the half is due to unpolarised input "
             "rather than to any angle.",
  "check": "What fraction of the light passes through a polaroid at 30° to its axis?",
  "answer": "cos²30 = 0.75, so three quarters. Halving the angle does not double the "
            "transmission."},

 "9.6.6": {
  "meaning": "Malus problems give I₀ and θ, or a series of angles, with I the unknown.",
  "why": "Because there is one equation and the square is the only real difficulty. "
         "Reading the angle off the graph first is usually quicker than doing it, and it "
         "removes any chance of taking cos of the wrong quantity.",
  "example": "400 W m⁻² at 60° gives 400 × cos²60 = 400 × 0.25 = 100 W m⁻². At 30° the same "
             "input gives 300 W m⁻².",
  "pitfall": "Forgetting the square, or using the half-value rule for the second polaroid.",
  "check": "Two polaroids are crossed and the first passes 800 W m⁻². What comes through "
           "the second?",
  "answer": "Zero. cos²90 = 0, so nothing gets through and the view is black."},

 "9.6.7": {
  "meaning": "Sunglasses, photography, LCD screens and 3-D films all exploit polarisation, "
             "each using a different part of the same physics.",
  "why": "Because once light is polarised it can be turned by another filter, blocked, or "
         "used to carry one of two images.",
  "example": "In an LCD, each layer can rotate the polarised light by 0° or 90°, switching "
             "the pixel on or off.",
  "pitfall": "Expecting polarising sunglasses to make a scene darker. They cut the reflected "
             "glare, not the general brightness.",
  "check": "Why do 3-D glasses need the two images to be differently polarised?",
  "answer": "So each eye receives only its own image. Without that the two would superimpose "
            "and you would see a blurred double image."},
})

LESSONS.update({
 "10.1.1": {
  "meaning": "Heat is energy transferred because of a temperature difference; temperature "
             "measures the average kinetic energy of the molecules.",
  "why": "Because they are different kinds of thing. A body contains internal energy and a "
         "temperature, but it contains heat only for as long as some of that energy is "
         "actually in transit.",
  "example": "A hot bath holds internal energy and has a temperature. The moment you draw a "
             "bath full of water, energy is in transit and that transit is the heat.",
  "pitfall": "Treating heat as a substance stored inside a body, which is why 'used up heat' "
             "is meaningless.",
  "check": "Which of these contains heat: a warm stone, or a stone warming your hand?",
  "answer": "Neither contains it. Energy is in transit only while the stone warms your hand; "
            "the stone has internal energy and a temperature."},

 "10.1.2": {
  "meaning": "Heat is a form of transit energy, and it always flows from the hotter body to "
             "the colder one without any external agency.",
  "why": "Because spontaneous transfer in the opposite direction would increase the total "
         "entropy, which the second law forbids.",
  "example": "Heat never flows from cold milk to a warm room, even though the milk is the "
             "smaller body and cools the room negligibly.",
  "pitfall": "Assuming a small cold body must cool a large warm one, which confuses size "
             "with temperature.",
  "check": "Can heat flow from cold to hot if work is supplied?",
  "answer": "Yes - a refrigerator does exactly that, but it consumes work. Heat alone never "
            "moves that way spontaneously."},

 "10.1.3": {
  "meaning": "Regions at equal temperature are in thermal equilibrium, and no net heat "
             "passes between them.",
  "why": "Because temperature is the property that decides the direction of heat flow. "
         "Equal temperature means no driving difference at all.",
  "example": "Two thermometers left in the same beaker agree and stay agreed; that shared "
             "reading is a property of the beaker, not of either thermometer.",
  "pitfall": "Thinking equilibrium means the temperatures are equal in time. They are equal "
             "at a given instant and stay equal.",
  "check": "If A = B and B = C in temperature, what can you say about A and C?",
  "answer": "That A = C. This is the zeroth law, and it is what makes a thermometer worth "
            "having."},

 "10.1.4": {
  "meaning": "In a closed system two bodies at different temperatures reach a common "
             "temperature, and the energy one loses equals the energy the other gains.",
  "why": "Because energy is conserved. Nothing is destroyed in the transfer, so the total "
         "internal energy of the two bodies together is unchanged.",
  "example": "Hot water added to cold water in a calorimeter ends at a temperature between "
             "the two, with m₁c₁ΔT₁ = m₂c₂ΔT₂.",
  "pitfall": "Using the final temperature for both bodies, or forgetting the calorimeter's own "
             "heat capacity.",
  "check": "100 g of water at 80 °C is mixed with 100 g at 20 °C. What is the final "
           "temperature?",
  "answer": "50 °C, because the masses and heat capacities are equal. That is the whole of "
            "the experiment - no thermometer precision beyond that is meaningful."},

 "10.2.1": {
  "meaning": "Boyle's law gives P₁V₁ = P₂V₂ at constant temperature; Charles's law gives "
             "V₁/T₁ = V₂/T₂ at constant pressure.",
  "why": "Boyle's from the pressure each molecule's impacts produce; Charles's from the "
         "molecules moving faster when heated, so occupying more space at the same pressure.",
  "example": "Halving the volume doubles the pressure; doubling the kelvin temperature doubles "
             "the volume.",
  "pitfall": "Using Celsius in Charles's law, which makes the law false rather than "
             "approximately true.",
  "check": "A gas at 300 K is warmed to 600 K at constant pressure. By what factor does its "
           "volume change?",
  "answer": "It doubles, since V ∝ T with T in kelvin. The Celsius change of 300 K would give "
            "the wrong answer entirely."},

 "10.2.2": {
  "meaning": "A gas obeying PV proportional to T at fixed n is ideal.",
  "why": "Because that relation says the three properties are linked by a single equation "
         "with no dependence on the identity of the gas, which is exactly what 'ideal' means.",
  "example": "Real gases approximate this well at ordinary pressures and fail near "
             "condensation, where the molecules' own volume and attractions stop being "
             "negligible.",
  "pitfall": "Expecting ideal gases to exist. No gas is exactly ideal; the term is a limit "
             "in which the deviations vanish.",
  "check": "Why does a real gas deviate from PV = nRT at high pressure?",
  "answer": "Because the molecules' own volume stops being negligible beside the container's, "
            "so the volume available for free motion is less than V."},

 "10.3.1": {
  "meaning": "A gas is a very large number of tiny molecules in random motion, colliding "
             "elastically, with negligible attractions, whose average kinetic energy depends "
             "only on temperature.",
  "why": "Because those six assumptions are what allow the macroscopic pressure and "
         "temperature to be calculated from statistics rather than tracked particle by "
         "particle.",
  "example": "Pressure is the rate of momentum transfer to the walls; temperature is the "
             "average kinetic energy, with no reference to which gas it is.",
  "pitfall": "Adding a seventh assumption that all molecules move at the same speed. They do "
             "not, and that assumption would kill the subject.",
  "check": "Which postulate does Boyle's law come from?",
  "answer": "That the collisions with the wall are elastic and that halving the volume "
            "doubles the collision rate at the same speed."},

 "10.3.2": {
  "meaning": "PV = (1/3) N m ⟨v²⟩, which reduces exactly to PV = nRT.",
  "why": "Because summing the momentum changes over every molecule and dividing by area and "
         "time gives the pressure, with the 1/3 arising from motion in three dimensions.",
  "example": "Substituting ⟨v²⟩ = 3RT/M and N = nN_A cancels the mass entirely and leaves "
             "nRT.",
  "pitfall": "Losing the factor of 3, which appears because only a third of the molecules "
             "move in any one direction at a given instant.",
  "check": "Why does PV = (1/3)Nm⟨v²⟩ reduce to PV = nRT rather than something else?",
  "answer": "Because ⟨v²⟩ = 3RT/M, and the 3 cancels the 1/3. Meanwhile Nm with N = nN_A and "
            "M = mass per mole becomes exactly n times R per kelvin."},

 "10.3.3": {
  "meaning": "v_rms = √(3RT/M), the speed of a molecule whose energy is all translational.",
  "why": "Because the rms speed is defined as the square root of the mean square speed, and "
         "the mean square speed follows directly from the average energy (3/2)kT.",
  "example": "Nitrogen at 300 K gives 517 m s⁻¹. The molar mass must be in kg mol⁻¹.",
  "pitfall": "Using g mol⁻¹ instead of kg mol⁻¹, which gives a speed 1000 times too large.",
  "check": "By what factor does v_rms increase when the temperature is quadrupled?",
  "answer": "By a factor of two, since speed scales as the square root of T."},

 "10.3.4": {
  "meaning": "The average translational energy of a molecule is (3/2)kT, and of a mole is "
             "(3/2)RT.",
  "why": "Because one degree of freedom always contributes (1/2)kT, and there are three "
         "translational degrees of freedom, one per axis.",
  "example": "At 300 K it is 6.21 × 10⁻²¹ J per molecule, with no dependence on the gas.",
  "pitfall": "Expecting a heavier gas to have a larger average energy. It has the same, and "
             "is simply slower.",
  "check": "Why does this expression contain no mass?",
  "answer": "Because a heavier molecule is slower in exactly the proportion that keeps its "
            "kinetic energy the same. The mass cancels between ½m⟨v²⟩ and (3/2)kT."},

 "10.3.5": {
  "meaning": "These problems give T and ask for the per-molecule or per-mole energy.",
  "why": "Because the formula is direct once T is in kelvin, and the only real difficulty is "
         "keeping the per-molecule and per-mole answers apart. The two differ by Avogadro's "
         "number, so the same physical energy looks five orders of magnitude different "
         "depending on the unit you quote it in.",
  "example": "At 500 K a molecule carries 1.036 × 10⁻²⁰ J, and a mole carries 5.18 kJ. "
             "Multiply the first by 6.022 × 10²³ and you get the second.",
  "pitfall": "Quoting per-molecule energy in joules and per-mole in kJ, then comparing the "
             "numbers directly.",
  "check": "A mole of any ideal gas at 300 K has how much translational energy?",
  "answer": "1.5 × 8.314 × 300 = 3740 J, about 3.74 kJ, whichever gas it is."},
})

LESSONS.update({
 "10.4.1": {
  "meaning": "The internal energy of an ideal gas is the sum of the kinetic energies of its "
             "molecules, U = (f/2)nRT.",
  "why": "Because an ideal gas has no interactions to store energy: nothing in bonds, "
         "nothing in the walls. All the internal energy is molecular motion.",
  "example": "For a monatomic gas U = (3/2)nRT; for a diatomic gas at room temperature "
             "U = (5/2)nRT because two rotational degrees of freedom are active.",
  "pitfall": "Adding the kinetic energy of the container's bulk motion. Internal energy is "
             "about the molecules' own motion, not the system's motion.",
  "check": "Why does a monatomic gas have U = (3/2)nRT?",
  "answer": "Three translational degrees of freedom, each contributing (1/2)RT per mole. A "
            "single atom cannot rotate, so there is nothing else."},

 "10.4.2": {
  "meaning": "The change in internal energy depends only on the two end states, never on "
             "the path taken between them.",
  "why": "Because U = (f/2)nRT depends only on T for an ideal gas, so any change in the gas's "
         "thermal state fixes ΔU regardless of how it got there.",
  "example": "A gas taken from state A to state B by expanding slowly or quickly has the "
             "same ΔU, but does very different amounts of work on the way.",
  "pitfall": "Adding work done to ΔU when the path differs. That is the work done, not the "
             "internal energy change.",
  "check": "Two paths between the same two states give ΔU = 500 J. Can they give different "
           "work?",
  "answer": "Yes, and they do. The work differs because the areas under the two P-V paths "
            "differ, while ΔU is fixed."},

 "10.4.3": {
  "meaning": "Work in thermodynamics is the transfer of energy by a force acting through a "
             "displacement, W = P ΔV for a gas.",
  "why": "Because work is energy transferred by a force, and a gas expanding does work "
         "pushing the surroundings out.",
  "example": "A gas expanding by 0.001 m³ at 10⁵ Pa does 100 J of work on its surroundings.",
  "pitfall": "Using the gas's internal energy, which stays fixed in an isothermal expansion "
             "even though the gas does work.",
  "check": "In which process does a gas do no work at all?",
  "answer": "In an isochoric one. With no change of volume there is no displacement, so no "
            "work is done whatever the temperature does."},

 "10.4.4": {
  "meaning": "Work done by a gas is positive on expansion and negative on compression; work "
             "done on it is the same magnitude with the opposite sign.",
  "why": "Because they are two descriptions of one transfer, and the sign only records which "
         "body did the pushing.",
  "example": "Compression: W(by) is negative and W(on) is positive. That is why compression "
             "raises the internal energy for a given heat input.",
  "pitfall": "Using the phrase 'work done by a gas' without saying whether you mean the gas's "
             "work or the work on it, then forgetting which one the formula wants.",
  "check": "A gas is compressed by 500 J of work. What is W in the convention dU = Q − W?",
  "answer": "W = −500 J, because W is work done by the gas and here the surroundings did the "
            "pushing. Compression therefore lowers dU for a given Q."},

 "10.5.1": {
  "meaning": "The first law states dU = Q − W: the heat added to a gas either raises its "
             "internal energy or is spent pushing the surroundings.",
  "why": "Because it is conservation of energy applied to a gas, with W measured as work done "
         "by the gas.",
  "example": "Heat 500 J into a gas that does 300 J of work and the internal energy rises by "
             "200 J.",
  "pitfall": "Writing dU = Q + W with W as work done by the gas. That is a different "
             "convention, not a different law, and mixing them loses marks.",
  "check": "Does the first law say anything about which processes are possible?",
  "answer": "No. It only balances energy. Whether a particular process is possible at all is "
            "the second law's business."},

 "10.5.2": {
  "meaning": "Apply the first law in isothermal, adiabatic, isobaric and isochoric processes, "
             "each of which fixes one of Q, W or dU.",
  "why": "Because each process's defining constraint forces one of the three terms, and the "
         "first law then gives the other two.",
  "example": "Isothermal: dU = 0, so Q = W. Adiabatic: Q = 0, so dU = −W. Isochoric: W = 0, "
             "so Q = dU.",
  "pitfall": "Forgetting that an isothermal expansion does work even though dU is zero.",
  "check": "Which process gives dU = 0 and Q = W?",
  "answer": "The isothermal one, because an ideal gas's internal energy depends only on "
            "temperature, and the temperature is held constant."},

 "10.5.3": {
  "meaning": "Given two of heat, work and internal energy change, the third follows from "
             "dU = Q − W.",
  "why": "Because the first law is one equation with three quantities and two of them are "
         "always known.",
  "example": "A gas absorbs 2500 J at constant volume, so dU = 2500 J exactly and W = 0.",
  "pitfall": "Taking dU as something to calculate independently. It is fixed by the two end "
             "states, so it must come out the same whichever route you take.",
  "check": "A gas absorbs 1000 J and does 300 J of work. What is its change in internal "
           "energy?",
  "answer": "700 J. If you then compressed it back by 300 J of work instead, it would also "
            "do 300 J, and the same 700 J would be recovered - the work is path-dependent "
            "even though dU is not."},

 "10.6.1": {
  "meaning": "Specific heat capacity is the heat needed to raise one kilogram by one kelvin; "
             "molar specific heat is the same for one mole.",
  "why": "Because materials differ enormously in how much energy it takes to warm them, and "
         "the two units let you use whichever matches your data.",
  "example": "Water has a specific heat of 4200 J kg⁻¹ K⁻¹; copper 390. Copper needs ten "
             "times more energy per kilogram, and rises faster for the same input.",
  "pitfall": "Mixing the two units, which gives an answer off by the molar mass.",
  "check": "What is the specific heat of a substance that needs 8.4 kJ to raise 0.5 kg by "
           "4 K?",
  "answer": "8400 / (0.5 × 4) = 4200 J kg⁻¹ K⁻¹, which is water."},

 "10.6.2": {
  "meaning": "Cp is always greater than Cv, because at constant pressure the gas also does "
             "work as it expands.",
  "why": "Because Cp = Cv + R. The extra R is exactly the work of expansion per kelvin, "
         "found by expanding one mole at constant pressure.",
  "example": "For a diatomic gas Cv = 5R/2 and Cp = 7R/2, so Cp > Cv by R = 8.314.",
  "pitfall": "Using Cp where Cv belongs, or expecting Cv > Cp because the gas is confined. "
             "Being confined costs no energy.",
  "check": "Why does Cv depend on the degrees of freedom but Cp differ by exactly R "
           "whatever the gas?",
  "answer": "Both count the same molecular motions, but Cp adds the expansion work on top. "
            "That extra term is fixed by the ideal gas law and does not depend on the "
            "molecule."},

 "10.6.3": {
  "meaning": "Cp − Cv = R, proved from the first law.",
  "why": "Because heating one mole at constant pressure by dT needs Cp dT, the same rise at "
         "constant volume needs Cv dT, and the difference has gone into P dV = R dT.",
  "example": "For any ideal gas the difference in molar heat capacities is 8.314 J mol⁻¹ K⁻¹, "
             "which is the gas constant.",
  "pitfall": "Applying it to solids or liquids, where the molecules are bound and the "
             "argument does not hold.",
  "check": "A gas has Cp = 29.1 and Cv = 20.8. What is Cv + Cp?",
  "answer": "49.9 J mol⁻¹ K⁻¹, which is (3 + 7)R/2 for a diatomic gas. Cp − Cv = 8.3 "
            "confirms it is ideal."},

 "10.7.1": {
  "meaning": "A reversible process can be undone with no net change anywhere; an irreversible "
             "one cannot.",
  "why": "Because reversibility needs no friction, no finite temperature difference and no "
         "finite pressure difference - all three are unavoidable in practice.",
  "example": "A frictionless piston compressing slowly is reversible. Friction, mixing and "
             "heat flowing between bodies at different temperatures are not.",
  "pitfall": "Expecting any real process to be reversible. None is; Carnot is the limit that "
             "bounds all of them.",
  "check": "Why is a gas expanding into a vacuum irreversible?",
  "answer": "Nothing external changes, so there is no stored work with which to push the gas "
            "back. Restoring it needs work from outside that the gas cannot repay."},

 "10.8.1": {
  "meaning": "The second law says heat will not pass spontaneously from cold to hot, or flow "
             "wholly from a single reservoir into work.",
  "why": "Because both would decrease the entropy of the universe, and the total entropy of "
         "an isolated system never decreases.",
  "example": "The schematic is always the same: a hot reservoir, a cold reservoir, and an "
             "engine between them. Remove the cold reservoir and no engine can exist.",
  "pitfall": "Reading the second law as a restriction on energy. It restricts the conversion "
             "of heat into work, which is a different thing.",
  "check": "What would a 100 % efficient heat engine be, physically?",
  "answer": "A device taking heat from one reservoir and turning all of it into work. It is "
            "precisely what the second law forbids, and no amount of clever engineering "
            "will produce one."},

 "10.9.1": {
  "meaning": "A heat engine takes heat from a hot reservoir, does work and rejects heat to a "
             "cold reservoir; its efficiency is W/Q_h.",
  "why": "Because an engine must reject heat: the second law requires a temperature "
         "difference, so there must be a cold reservoir to receive what is not converted.",
  "example": "A steam engine with 1000 J in and 600 J rejected does 400 J of work, an "
             "efficiency of 0.40.",
  "pitfall": "Calculating efficiency as W/Q_h when Q_h was never measured, or expecting the "
             "waste heat to be optional.",
  "check": "Can an engine operate with only one reservoir?",
  "answer": "No. With no cold reservoir the rejected heat has nowhere to go, so the second "
            "law forces Q_c = 0 and hence efficiency 100 %, which is exactly the forbidden "
            "case."},

 "10.9.2": {
  "meaning": "The Carnot cycle is two isotherms joined by two adiabats on a P-V diagram, "
             "and its enclosed area is the net work.",
  "why": "Because each leg is reversible: isothermal heat exchange at two temperatures and "
         "adiabatic connections that change the volume without changing the entropy.",
  "example": "1→2 expands isothermally at T_h taking in heat; 2→3 expands adiabatically and "
             "cools to T_c; 3→4 compresses isothermally; 4→1 compresses adiabatically.",
  "pitfall": "Expecting the adiabats to be isotherms too. They are steeper by a factor γ, "
             "which is what closes the loop.",
  "check": "What does the enclosed area of the cycle represent?",
  "answer": "The net work done in one cycle, found by adding the area under each leg with its "
            "sign. It is the work the engine delivers per revolution."},

 "10.9.3": {
  "meaning": "The efficiency of a Carnot engine is η = 1 − T_c/T_h, with both temperatures "
             "in kelvin.",
  "why": "Because Q_c/T_c = Q_h/T_h for a reversible cycle, so Q_c/Q_h = T_c/T_h and η = 1 "
         "− Q_c/Q_h becomes 1 − T_c/T_h.",
  "example": "Between 500 K and 300 K the efficiency is 0.40, and no gas property appears in "
             "the result at all.",
  "pitfall": "Using Celsius, which gives a nonsense result because the ratio is not "
             "invariant under a shift.",
  "check": "Why does the Carnot efficiency depend only on the two temperatures?",
  "answer": "Because the derivation uses only Q_c/T_c = Q_h/T_h, which follows from the "
            "second law for any reversible cycle. All the gas properties cancel."},

 "10.9.4": {
  "meaning": "Carnot problems give the two temperatures and ask for η, or give η and ask for "
             "one temperature.",
  "why": "Because there is one equation, and the gas constant, the working substance and the "
         "volume all cancel out of it. That is why a steam engine and a nuclear reactor with "
         "the same reservoir temperatures have the same ideal ceiling.",
  "example": "A 0.50 efficiency between 400 K and 200 K, since 1 − 200/400 = 0.5. The same "
             "ceiling applies whether the working substance is air or mercury.",
  "pitfall": "Quoting an efficiency above the Carnot limit for the same pair of "
             "temperatures. That would mean the second law has been broken.",
  "check": "An engine runs at 0.30 between 500 K and a cold reservoir. What is T_c?",
  "answer": "T_c = 500 × 0.70 = 350 K. If the cold reservoir were warmer than that, the "
            "engine could not run at all."},

 "10.9.5": {
  "meaning": "Designing an efficient daily device means shrinking the temperature gap the "
             "device works against and closing every leak.",
  "why": "Because the Carnot bound is set by the temperature gap alone, and every real "
         "device loses further energy to friction, conduction, radiation and mixing.",
  "example": "A domestic fridge at 4 °C has a Carnot COP of about 10; the same fridge at "
             "−18 °C has about 1.9, and runs for a fraction of the time.",
  "pitfall": "Optimising the compressor while ignoring the insulation. The gap dominates.",
  "check": "What single change most improves a refrigerator's efficiency?",
  "answer": "Raising its internal temperature. The COP is T_c/(T_h − T_c), so every kelvin "
            "you raise it by makes the gap smaller and the coefficient larger."},
})

LESSONS.update({
 "10.10.1": {
  "meaning": "A refrigerator is a heat engine run backwards: it takes heat from a cold space, "
             "rejects heat into the room, and consumes work.",
  "why": "Because the Carnot cycle is a loop, and nothing in the physics says which way round "
         "it must run. Reversing it moves heat from cold to hot at the cost of work.",
  "example": "Q_h = Q_c + W, so a fridge removing 100 J from the cold space with 30 J of "
             "electricity dumps 130 J into the room. That is why a fridge warms a room "
             "slightly.",
  "pitfall": "Thinking it creates cold. It removes heat from one place and puts more than "
             "that somewhere else.",
  "check": "Why does running a refrigerator with its door open warm the room?",
  "answer": "Because it is moving heat from the room back into the room with work added on "
            "top. The net effect is pure heating, which is a useful way of seeing that no "
            "cooling was actually produced."},

 "10.10.2": {
  "meaning": "The coefficient of performance is COP = Q_c/W = T_c/(T_h − T_c) for an ideal "
             "refrigerator.",
  "why": "Because W = Q_h − Q_c and Q_h/T_h = Q_c/T_c for a reversible cycle, which gives "
         "W = Q_c(T_h − T_c)/T_c and hence the formula.",
  "example": "A cold space at 240 K in a 300 K room gives COP = 240/60 = 4.0, meaning 4 J of "
             "heat removed per joule spent.",
  "pitfall": "Calling it an efficiency. It measures heat moved, so it can and usually does "
             "exceed 1.",
  "check": "How does the COP change as the cold reservoir gets colder?",
  "answer": "It falls, because T_h − T_c grows. A fridge at −18 °C in a 30 °C room has a Carnot "
            "COP of 1.9; at 4 °C in the same room it is 10.5."},

 "10.11.1": {
  "meaning": "Entropy measures how many microscopic arrangements are compatible with the "
             "observed macroscopic state.",
  "why": "Because a gas that has spread through a room is compatible with vastly more "
         "arrangements of its molecules than the same gas in a corner, and a statistical "
         "quantity is best described by how many microstates realise it.",
  "example": "A drop of ink spreading through water has far more accessible arrangements "
             "than the same ink in a tight drop, and its entropy rises.",
  "pitfall": "Equating entropy with visible disorder, which is a slogan rather than a "
             "definition and fails when you try to compute with it.",
  "check": "Why does a gas filling a room have a larger entropy than the same gas confined "
           "to one corner?",
  "answer": "Because every molecule has the whole room to be in rather than a fraction of "
            "it. The number of arrangements rises enormously, by roughly the cube of the "
            "volume ratio."},

 "10.11.2": {
  "meaning": "Absorbing heat at positive absolute temperature gives positive entropy; "
             "releasing heat gives negative.",
  "why": "Because dS = Q_rev/T, and T is positive in kelvin, so the sign of dS is the sign "
         "of the heat transferred.",
  "example": "A gas absorbing 2000 J at 400 K gains 5 J K⁻¹; the same gas losing that heat "
             "loses 5 J K⁻¹.",
  "pitfall": "Expecting positive entropy always. It is negative for a system that is losing "
             "heat, and that is not a violation of anything.",
  "check": "Why must the denominator in dS = Q/T be in kelvin?",
  "answer": "Because a change of one Celsius degree is the same size as one kelvin, but at "
            "0 °C the Celsius expression would divide by zero. Absolute zero is the floor "
            "below which no negative temperature exists."},

 "10.11.3": {
  "meaning": "The entropy of a gas rises with temperature even at constant volume, because "
             "faster molecules have far more accessible arrangements.",
  "why": "Because entropy counts microstates, and the number of arrangements grows far "
         "faster than linearly with molecular speed.",
  "example": "Heating a gas at constant volume raises its temperature and its entropy "
             "together, even though no work is done.",
  "pitfall": "Confusing entropy with volume, and expecting a constant-volume gas to have "
             "constant entropy.",
  "check": "If a gas is heated at constant volume, does its entropy change?",
  "answer": "Yes, it increases. Entropy depends on temperature, not on volume; it is the "
            "temperature change that is evidence the gas got hotter."},

 "10.11.4": {
  "meaning": "In every natural process some energy becomes heat too dispersed to do useful "
             "work again.",
  "why": "Because random microscopic motion cannot be lined up again by chance, so the "
         "organised energy cannot be recovered.",
  "example": "A book falling to the floor keeps its energy exactly, but as random motion of "
             "the floor and air it cannot be made to lift the book again.",
  "pitfall": "Saying energy is lost. The first law forbids that; what is degraded is its "
             "quality.",
  "check": "Why can a falling book not bounce back up to its original height?",
  "answer": "Because converting the random motion of the floor and air back into organised "
            "upward motion would require the microscopic motions to line up perfectly, which "
            "is effectively impossible."},

 "10.11.5": {
  "meaning": "Pollution, depletion of resources and the greenhouse effect are all entropy "
             "problems: they take something concentrated and make it spread out.",
  "why": "Because producing local order always costs a larger entropy increase somewhere "
         "else, and there is no free way to re-concentrate a dispersed resource.",
  "example": "A finite ore deposit gets dispersed when mined, and re-concentrating it costs "
             "more energy than the metal is worth.",
  "pitfall": "Treating entropy as a moral argument. It is a bookkeeping statement: it says "
             "energy must go somewhere, and does not say what one ought to do.",
  "check": "Why is extracting metal from seawater more expensive than from an ore?",
  "answer": "Because seawater is a dilute, dispersed arrangement with high entropy. "
            "Concentrating it is the reverse of a natural spreading, so it costs energy."},
})


def lesson(outcome_id):
    """The full teaching block for one outcome, or ``None`` if none is written."""
    return LESSONS.get(outcome_id)


def depth_of(outcome_id):
    """Words of teaching attached to one outcome, for the coverage report."""
    entry = LESSONS.get(outcome_id)
    if not entry:
        return 0
    return len((entry["meaning"] + entry["why"] + entry.get("example", "")).split())
