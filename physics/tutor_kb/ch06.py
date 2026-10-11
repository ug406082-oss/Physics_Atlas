"""Chapter 6 tutor: upthrust, continuity, Bernoulli and viscosity."""

from __future__ import annotations

from ..core import fluids as F

__all__ = ["KB", "CALCULATORS"]

KB = [
    {"keys": ["upthrust", "what is upthrust", "upward force in a fluid"],
     "title": "Upthrust",
     "answer": (
         "**U = ρ_f g V_d** — the weight of the fluid displaced.\n\n"
         "It points upwards because pressure increases with depth, so the underside of a "
         "submerged body is pushed harder than the top. The net force is up.\n\n"
         "In air the upthrust is small but not zero — it is why a helium balloon rises."),
     "slo": "6.1.1"},
    {"keys": ["archimedes", "archimedes principle", "principle of archimedes",
              "eureka"],
     "title": "Archimedes' principle",
     "answer": (
         "**The upthrust on a fully submerged body equals the weight of the fluid it "
         "displaces.**\n\n"
         "That is all Archimedes claimed, and it is why a body feels lighter in water. A "
         "body of exactly the fluid's density displaces its own weight of fluid and so feels "
         "no net force at all, whatever the depth."),
     "slo": "6.1.4"},
    {"keys": ["principle of floatation", "when does something float", "floating condition"],
     "title": "The principle of floatation",
     "answer": (
         "A body floats only if **its weight does not exceed the maximum upthrust** "
         "(ρ_f g V).\n\n"
         "Setting them equal for a floating body, ρ_f g V_d = ρ_b g V, so:\n\n"
         "**V_d / V = ρ_b / ρ_f**\n\n"
         "Notice that **g cancels** — so the submerged fraction depends only on the ratio of "
         "the densities, and a block floats the same fraction of its depth on the Moon as on "
         "Earth."),
     "slo": "6.1.3"},
    {"keys": ["why do ships float", "why does a ship float", "ship float",
              "why steel ship floats"],
     "title": "Why ships float",
     "answer": (
         "Steel is about 7.8 times denser than water, so a solid block of it sinks. A ship's "
         "hull is **hollow**: it excludes an enormous volume of water while being made of "
         "only a modest mass of steel.\n\n"
         "A 2 × 10⁷ kg ship in sea water displaces about 1.95 × 10⁴ m³ — some 19 500 tonnes of "
         "water — and that is exactly the upthrust needed to support it."),
     "slo": "6.1.5"},
    {"keys": ["streamline flow", "laminar flow", "turbulent flow", "incompressible",
              "types of flow"],
     "title": "Types of flow",
     "answer": (
         "**Streamline (laminar):** the fluid moves in smooth parallel layers that never "
         "mix. Different-coloured layers stay distinct.\n"
         "**Turbulent:** chaotic swirls and eddies; the layers mix almost at once.\n"
         "**Incompressible:** the density stays essentially constant, which is what lets "
         "continuity reduce to A₁v₁ = A₂v₂."),
     "slo": "6.2.1"},
    {"keys": ["conditions for turbulent flow", "when is flow turbulent", "reynolds number",
              "re number"],
     "title": "When does a flow go turbulent?",
     "answer": (
         "**Re = ρvL/η**, dimensionless, comparing inertia against viscosity.\n\n"
         "* Re below about **2000** → laminar\n"
         "* Re above about **4000** → turbulent\n"
         "* in between → transitional\n\n"
         "Turbulence is promoted by **higher speed**, **larger diameter** and **lower "
         "viscosity**; it is suppressed by thicker fluids and smoother pipes."),
     "slo": "6.2.2"},
    {"keys": ["equation of continuity", "continuity equation", "a1v1",
              "conservation of volume"],
     "title": "The equation of continuity",
     "answer": (
         "**A₁v₁ = A₂v₂**\n\n"
         "In one second the same volume must pass every cross-section, so A × v — the "
         "volume flow rate — is constant. Where the pipe narrows, the fluid speeds up.\n\n"
         "**Remember:** area goes as the *square* of the diameter, so halving the diameter "
         "quadruples the speed. Halving the diameter does not double the speed."),
     "slo": "6.3.1"},
    {"keys": ["squeeze a pipe", "squeezing the pipe", "rubber pipe", "hose nozzle",
              "why speed increases"],
     "title": "Why squeezing a pipe speeds the flow up",
     "answer": (
         "Squeezing reduces the cross-sectional area. The same volume per second must still "
         "get through, so the fluid at the squeezed end must move faster — **A₁v₁ = A₂v₂**.\n\n"
         "The overall flow rate out of the open end does not change. Only the speed at the "
         "narrow point does. This is exactly how a fire-hose nozzle works."),
     "slo": "6.3.2"},
    {"keys": ["bernoulli", "bernoulli equation", "p plus half rho", "energy per unit volume"],
     "title": "Bernoulli's equation",
     "answer": (
         "**P + ½ρv² + ρgh = constant** along a streamline.\n\n"
         "It is energy conservation for a fluid, written per unit volume. There are three "
         "stores — pressure, motion and height — and their total never changes.\n\n"
         "**Assumptions:** steady, incompressible, non-viscous flow. Real pipe flow loses "
         "energy to friction, so Bernoulli gives the ideal answer and the right direction of "
         "the error."),
     "slo": "6.4.1"},
    {"keys": ["pressure and flow rate", "why is pressure lower", "fast flow lower pressure",
              "pressure difference"],
     "title": "Speed and pressure trade against each other",
     "answer": (
         "At constant height, Bernoulli reduces to **P + ½ρv² = constant**. So:\n\n"
         "* **faster flow → lower pressure**\n"
         "* slower flow → higher pressure\n\n"
         "That is the whole of the Bernoulli effect, and every application in the syllabus "
         "is one of its consequences."),
     "slo": "6.4.2"},
    {"keys": ["atomizer", "atomiser", "perfume sprayer", "spray", "venturi",
              "magnus effect", "curve ball", "swing of ball", "bernoulli application"],
     "title": "Bernoulli in the real world",
     "answer": (
         "**Atomizer:** air is forced through a narrow jet; it speeds up, its pressure drops "
         "below atmospheric, and the outside air pushes liquid up into that low-pressure "
         "region to be carried out as spray.\n"
         "**Curve ball / Magnus effect:** the spin drags air round with it, making it move "
         "faster on one side. That side is at lower pressure and pushes the ball towards it.\n"
         "**Venturi:** a deliberate constriction speeds the flow up and lowers the pressure; "
         "the difference between the wide and narrow ends is what actually measures the flow "
         "rate."),
     "slo": "6.4.3"},
    {"keys": ["viscosity", "viscous fluid", "non viscous", "what is viscosity",
              "ideal fluid"],
     "title": "Viscosity",
     "answer": (
         "**Viscosity** is a fluid's resistance to internal shear — to one layer sliding "
         "past another.\n\n"
         "**Viscous:** honey, glycerine, engine oil, syrup. **Non-viscous (ideal):** an "
         "idealisation. Water and air are *treated* as non-viscous in school problems, but "
         "every real fluid has some viscosity."),
     "slo": "6.5.1"},
    {"keys": ["fluid friction", "retarding force", "drag force", "air resistance in fluid"],
     "title": "Fluid friction and drag",
     "answer": (
         "A viscous fluid exerts a **retarding force that always opposes motion**. For a "
         "small sphere moving slowly it is **F = 6πηrv**, so it is proportional to the "
         "viscosity and to the speed.\n\n"
         "At higher speeds the drag grows faster than linearly, because the wake behind the "
         "body grows. A falling object eventually reaches a terminal speed where drag exactly "
         "balances its weight."),
     "slo": "6.5.2"},
    {"keys": ["superfluidity", "superfluid", "superfluid helium", "zero viscosity",
              "fountain effect"],
     "title": "Superfluidity",
     "answer": (
         "Below about **2.2 K**, liquid helium enters a superfluid phase with a viscosity of "
         "**exactly zero** — not merely small.\n\n"
         "* a stirred bath never slows down\n"
         "* it creeps up the walls of its container\n"
         "* heating a point inside makes a fountain jet upward\n"
         "* a spun bucket keeps spinning forever, because its circulation is locked to a "
         "quantum\n\n"
         "It is a genuinely quantum effect, not just 'a very runny liquid'."),
     "slo": "6.5.4"},
]


def _upthrust(rho, volume):
    return (f"**U = {F.upthrust(float(rho), float(volume)):.4g} N**\n\n"
            f"U = ρ g V = {float(rho):g} × 9.8 × {float(volume):g} = "
            f"{F.upthrust(float(rho), float(volume)):.4g} N\n\n"
            f"That is the weight of {float(volume) * 1000:.4g} litres of that fluid.")


def _float(object_density, fluid_density, volume=1.0):
    result = F.floatation_verdict(float(object_density), float(volume), float(fluid_density))
    return (f"**{result['verdict']}**\n\n"
            f"ρ body {float(object_density):g}, ρ fluid {float(fluid_density):g}\n"
            f"* weight = {result['weight']:.4g} N\n"
            f"* maximum upthrust = {result['maximum_upthrust']:.4g} N\n"
            f"* submerged fraction = {result['submerged_fraction'] * 100:.1f} %\n\n"
            f"{result['reason']}")


def _continuity(a1, v1, a2):
    return (f"**v₂ = {F.continuity_velocity(float(a1), float(v1), float(a2)):.4g}**\n\n"
            f"A₁v₁ = A₂v₂ → v₂ = ({float(a1):g} × {float(v1):g}) / {float(a2):g} = "
            f"{F.continuity_velocity(float(a1), float(v1), float(a2)):.4g}\n\n"
            f"The area ratio is {float(a1) / float(a2):.4g}, so the speed changes by that "
            f"factor. The volume flow rate stays at "
            f"{F.continuity_area(float(a1), float(v1)):.4g}.")


def _bernoulli(p1, v1, v2):
    result = F.bernoulli(p1=float(p1), v1=float(v1), h1=0, p2=None, v2=float(v2),
                         h2=0, density=1000.0)
    if "error" in result:
        return f"That will not work: {result['error']}"
    return (f"**P₂ = {result['p2']:.4g} Pa**\n\n"
            f"P₁ + ½ρv₁² = P₂ + ½ρv₂² (same height)\n"
            f"P₂ = {float(p1):g} + ½(1000)({float(v1):g}² − {float(v2):g}²) = "
            f"{result['p2']:.4g} Pa\n\n"
            f"The fluid {'slowed down, so the pressure rose' if result['p2'] > float(p1) else 'sped up, so the pressure fell'} "
            f"by {abs(result['p2'] - float(p1)):.4g} Pa.")


def _reynolds(rho, speed, length, eta):
    result = F.reynolds_flow(float(rho), float(speed), float(length), float(eta))
    return (f"**Re = {result['re']:.4g}** → **{result['regime']}**\n\n"
            f"Re = ρvL/η = ({float(rho):g} × {float(speed):g} × {float(length):g}) / "
            f"{float(eta):g} = {result['re']:.4g}\n\n"
            f"{result['note']}")


CALCULATORS = [
    {"pattern": r"upthrust\s*=\s*([\d.]+)\s*(?:and|×|\*|,)\s*([\d.]+)", "reply": _upthrust},
    {"pattern": r"(?:will it|does it)\s*([\d.]+)\s*(?:kg m-?3|kg/m3)?\s*(?:float|sink|float or sink)"
                r"\D*?([\d.]+)", "reply": _float},
    {"pattern": r"continuity\D*?([\d.]+)\s*([\d.]+)\s*([\d.]+)", "reply": _continuity},
    {"pattern": r"bernoulli\D*?([\d.]+)\s*([\d.]+)\s*([\d.]+)", "reply": _bernoulli},
    {"pattern": r"reynolds\D*?([\d.]+)\s*(?:,|and)\s*([\d.]+)\s*(?:,|and)\s*([\d.]+)\s*"
                r"(?:,|and)\s*([\d.]+)", "reply": _reynolds},
]
