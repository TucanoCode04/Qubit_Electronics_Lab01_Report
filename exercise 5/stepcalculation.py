import numpy as np

# Constants
C = 50e-15  # Capacitance in Farads (50 fF)
f_start = 6e9  # Start frequency in Hz (6 GHz)
f_end = 11e9  # End frequency in Hz (11 GHz)
f_step = 250e6  # Frequency step in Hz (250 MHz)

# Generate frequency array
frequencies = np.arange(f_start, f_end + f_step, f_step)

# Calculate Lr1 using resonant frequency formula: f = 1/(2*pi*sqrt(L*C))
# Rearranging: L = 1/(4*pi^2*f^2*C)
lr1_values = 1 / (4 * np.pi**2 * frequencies**2 * C)

# Display results
print("Frequency (GHz) | Lr1 (H)")
print("-" * 35)
for freq, lr1 in zip(frequencies, lr1_values):
    print(f"{freq/1e9:14.3f} | {lr1:.6e}")