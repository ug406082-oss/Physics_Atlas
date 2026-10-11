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
