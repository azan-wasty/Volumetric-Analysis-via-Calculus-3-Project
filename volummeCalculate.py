from sympy import symbols, integrate, sqrt, pi, sin, sympify

# Define all symbolic variables used across coordinate systems
x, y, z, r, theta, phi, rho = symbols('x y z r theta phi rho')

# ----------------------------
# Rectangular Triple Integral
# ----------------------------
def volume_rectangular(bounds):
    z_bounds = bounds['z']
    y_bounds = bounds['y']
    x_bounds = bounds['x']
    integrand = 1  # ∭ 1 dz dy dx

    return integrate(
        integrate(
            integrate(integrand, (z, *z_bounds)),
            (y, *y_bounds)
        ),
        (x, *x_bounds)
    ).evalf()

# ----------------------------
# Cylindrical Triple Integral
# ----------------------------
def volume_cylindrical(bounds):
    z_bounds = bounds['z']
    r_bounds = bounds['r']
    theta_bounds = bounds['theta']
    integrand = r  # Jacobian for cylindrical ∭ r dz dr dθ

    return integrate(
        integrate(
            integrate(integrand, (z, *z_bounds)),
            (r, *r_bounds)
        ),
        (theta, *theta_bounds)
    ).evalf()


# Spherical Triple Integral

def volume_spherical(bounds):
    rho_bounds = bounds['rho']
    theta_bounds = bounds['theta']
    phi_bounds = bounds['phi']
    integrand = rho**2 * sin(phi)  # Jacobian for spherical ∭ ρ²sin(φ) dρ dφ dθ

    return integrate(
        integrate(
            integrate(integrand, (rho, *rho_bounds)),
            (phi, *phi_bounds)
        ),
        (theta, *theta_bounds)
    ).evalf()


# Main Dispatcher with Bound Checks

def compute_volume(method, raw_bounds):
    """
    Takes:
      method: 'rectangular', 'cylindrical', or 'spherical'
      raw_bounds: dictionary with lower/upper limits as strings

    Returns:
      Evaluated symbolic volume (float)
    """
    try:
        # Convert all string bounds to symbolic expressions
        parsed_bounds = {
            var: (sympify(low), sympify(high))
            for var, (low, high) in raw_bounds.items()
        }

        # Check if lower < upper (where possible)
        for var, (low, high) in parsed_bounds.items():
            try:
                if low.evalf() > high.evalf():
                    return f" Invalid bounds for '{var}': lower limit is greater than upper limit."
            except:
                pass  # Skip comparison if it can't be evaluated numerically

        # Dispatch to appropriate coordinate system
        if method == "rectangular":
            return volume_rectangular(parsed_bounds)
        elif method == "cylindrical":
            return volume_cylindrical(parsed_bounds)
        elif method == "spherical":
            return volume_spherical(parsed_bounds)
        else:
            return "Unsupported method."

    except Exception as e:
        return f"Error: {e}"

