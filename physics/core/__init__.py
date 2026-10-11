"""Pure scientific helpers for Physics Atlas.

One module per chapter. Nothing in this package imports Streamlit, pandas,
NumPy or Plotly, so every formula here can be unit-tested under a bare Python
interpreter and re-used by the data files, the tutor and the tests.

Modules
-------
measurement   Chapter 1 - dimensions, significant figures, uncertainty
vectors       Chapter 2 - components, scalar and vector products
motion1d      Chapter 3 - equations of motion, collisions, work and energy
motion2d      Chapter 4 - projectiles, circular motion, rotation
solids        Chapter 5 - stress, strain and elasticity
fluids        Chapter 6 - upthrust, continuity and Bernoulli
oscillations  Chapter 7 - SHM, mass-spring and simple pendulum
waves         Chapter 8 - wave motion, beats, stationary waves and Doppler
optics        Chapter 9 - interference, diffraction and polarisation
thermo        Chapter 10 - ideal gases, the laws and entropy
"""

from . import (fluids, measurement, motion1d, motion2d, optics, oscillations,
               solids, thermo, vectors, waves)

__all__ = ["measurement", "vectors", "motion1d", "motion2d", "solids",
           "fluids", "oscillations", "waves", "optics", "thermo"]
