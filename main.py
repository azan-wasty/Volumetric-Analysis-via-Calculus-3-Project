from volumeCalculate import compute_volume
from sympy import symbols, integrate, sqrt, pi, sin, sympify

# Define all symbolic variables used across coordinate systems
x, y, z, r, theta, phi, rho = symbols('x y z r theta phi rho')




# User Input Interface

def user_input_volume():
    print("\n Volume Calculator — Coordinate Transformation")
    print("Supported systems: rectangular | cylindrical | spherical\n")

    # Ask user to choose coordinate system
    method = input("Enter method: ").strip().lower()
    bounds = {}

    # Based on method, ask for specific bounds
    if method == "rectangular":
        print("\nEnter bounds for x, y, z (e.g. -2, 2, sqrt(4 - x**2))")
        bounds["z"] = (input("z lower: "), input("z upper: "))
        bounds["y"] = (input("y lower: "), input("y upper: "))
        bounds["x"] = (input("x lower: "), input("x upper: "))

    elif method == "cylindrical":
        print("\nEnter bounds for r, θ, z (e.g. 0, 2*pi, sqrt(9 - r**2))")
        bounds["z"] = (input("z lower: "), input("z upper: "))
        bounds["r"] = (input("r lower: "), input("r upper: "))
        bounds["theta"] = (input("theta lower: "), input("theta upper: "))

    elif method == "spherical":
        print("\nEnter bounds for ρ, θ, φ (e.g. 0, pi, pi/2)")
        bounds["rho"] = (input("rho lower: "), input("rho upper: "))
        bounds["theta"] = (input("theta lower: "), input("theta upper: "))
        bounds["phi"] = (input("phi lower: "), input("phi upper: "))

    else:
        print("Unsupported method selected.")
        return

    # Compute and display result
    result = compute_volume(method, bounds)
    print("\n Calculated Volume:", result)


# Entry Point

if __name__ == "__main__":
    user_input_volume()
