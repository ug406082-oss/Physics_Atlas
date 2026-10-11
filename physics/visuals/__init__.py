"""The diagram library.

One module per chapter, so each chapter draws its own figures and nothing else
has to know about them. :mod:`physics.visuals` re-exports everything, which is
what the rest of the app imports.
"""

from __future__ import annotations

from .common import freeze, GOLDEN_ANGLE, _svg, defs, wrap
from . import ch01, ch02, ch04, ch05, ch06, ch07, ch08, ch09, ch10
from .ch01 import (ambiguity_bars, balance, error_target, progress_ring,
                   reading_ruler, si_wheel, sigfig_highlight,
                   uncertainty_number_line, unit_blocks)
from .ch02 import (component_resultant, cross_parallelogram,
                   dot_projection, right_hand_rule,angle_arc, component_rectangle, cross_plane, project_shadow,
                   resultant_parallelogram, scalar_vector_strip, shadow_dial,
                   torque_arc, vector_arrow)
from .ch04 import (angular_dials, centripetal_circle, centrifuge_tube,
                   component_split, inertia_shapes, rotation_disc,
                   skater_spin, trajectory_family, weightless_orbit)
from .ch05 import (deformation_kinds, load_extension_curve, energy_triangle, load_unload_trace,
                   solid_types, stress_strain_curve, wire_comparison)
from .ch10 import (carnot_cycle_plot, derivation_ladder, energy_lines,
                   engine_blocks, entropy_room, equilibrium_contact,
                   gas_law_grid, heat_capacity_bars, molecular_box,
                   pressure_collisions, process_quadrant, pv_area,
                   refrigerator_blocks, reversible_split, speed_distribution,
                   temperature_scales, thermometer_cutaway)
from .ch09 import (bragg_layers, brewster_diagram, coherence_panel,
                   diffraction_pattern, grating_panel, huygens_construction,
                   interference_explorer, malus_curve, michelson_layout,
                   polarisation_types, polaroid_chain, sensitivity_scale,
                   spacetime_ring, wavefront_growth, youngs_arrangement)
from .ch08 import (beat_panel, doppler_explorer, interference_map,
                   particle_motion, pipe_bench, progressive_trace,
                   round_trip, spectrum_shift, stationary_bench, two_wave_bench,
                   wave_graph_annotated)
from .ch07 import (circle_projection, energy_bars, pendulum_rig, period_comparison,
                   phase_dial, shm_scope, spring_rig)
from .ch06 import (archimedes_bench, atomizer_diagram, bernoulli_profile,
                   flow_regime_strip, hull_diagram, pipe_continuity,
                   superfluidity_panel, viscosity_ladder)

__all__ = [
    "GOLDEN_ANGLE", "_svg", "defs", "wrap",
    "ambiguity_bars", "balance", "error_target", "progress_ring",
    "reading_ruler", "si_wheel", "sigfig_highlight",
    "uncertainty_number_line", "unit_blocks",
    "ch01", "ch02", "ch04", "ch05", "ch06", "ch07", "ch08", "ch09",
    "angle_arc", "component_rectangle", "cross_plane", "project_shadow",
    "resultant_parallelogram", "scalar_vector_strip", "component_resultant", "dot_projection",
           "cross_parallelogram", "right_hand_rule", "shadow_dial",
    "torque_arc", "vector_arrow",
    "deformation_kinds", "load_extension_curve", "energy_triangle", "load_unload_trace",
    "solid_types", "stress_strain_curve", "wire_comparison",
    "archimedes_bench", "atomizer_diagram", "bernoulli_profile",
    "flow_regime_strip", "hull_diagram", "pipe_continuity",
    "superfluidity_panel", "viscosity_ladder",
    "angular_dials", "centripetal_circle", "centrifuge_tube", "component_split",
    "inertia_shapes", "rotation_disc", "skater_spin", "trajectory_family",
    "weightless_orbit",
    "circle_projection", "energy_bars", "pendulum_rig", "period_comparison",
    "phase_dial", "shm_scope", "spring_rig",
    "beat_panel", "doppler_explorer", "interference_map", "particle_motion",
    "pipe_bench", "progressive_trace", "round_trip", "spectrum_shift",
    "stationary_bench", "two_wave_bench", "wave_graph_annotated",
    "bragg_layers", "brewster_diagram", "coherence_panel", "diffraction_pattern",
    "grating_panel", "huygens_construction", "interference_explorer",
    "malus_curve", "michelson_layout", "polarisation_types", "polaroid_chain",
    "sensitivity_scale", "spacetime_ring", "wavefront_growth",
    "youngs_arrangement",
    "carnot_cycle_plot", "derivation_ladder", "energy_lines", "engine_blocks",
    "entropy_room", "equilibrium_contact", "gas_law_grid",
    "heat_capacity_bars", "molecular_box", "pressure_collisions",
    "process_quadrant", "pv_area", "refrigerator_blocks",
    "reversible_split", "speed_distribution", "temperature_scales",
    "thermometer_cutaway",
]
