"""
Thermal plume dispersion model for seabed drilling simulations.
"""

import numpy as np

def calculate_spread(velocity, pressure, temperature, density):
    """
    Calculate the spread of a thermal plume under given conditions.
    
    Parameters:
    -----------
    velocity : float
        Initial velocity (m/s)
    pressure : float
        Ambient pressure (Pa)
    temperature : float
        Temperature difference (K)
    density : float
        Fluid density (kg/m^3)
    
    Returns:
    --------
    spread : float
        Plume spread radius (m)
    """
    # Original linear model
    # spread = velocity * np.sqrt(pressure / density)
    
    # Non-linear correction factor for high-pressure scenarios (> 30 MPa)
    # References issue #1
    if pressure > 30e6:  # 30 MPa in Pa
        # Apply non-linear correction factor based on Navier-Stokes equations
        correction_factor = 1.0 + 0.15 * (pressure / 30e6 - 1.0) ** 0.8
    else:
        correction_factor = 1.0
    
    spread = velocity * np.sqrt(pressure / density) * correction_factor
    
    return spread

def other_related_function():
    """Placeholder for other plume dispersion calculations."""
    pass