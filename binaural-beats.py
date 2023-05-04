import numpy as np
import os
from scipy.io import wavfile

# Get user input
freq = float(input("Enter base frequency (in Hz): "))
binaural_freq = float(input("Enter binaural frequency (in Hz): "))
duration_min = float(input("Enter length of .wav file (in minutes): "))

# Convert duration to seconds
duration_sec = duration_min * 60

# Set sampling frequency
sampling_freq = 44100  # in Hz

# Generate time array
time_array = np.arange(0, duration_sec, 1/sampling_freq)

# Generate first sine wave
sine_wave_1 = np.sin(2 * np.pi * freq * time_array)

# Generate second sine wave
sine_wave_2 = np.sin(2 * np.pi * (freq + binaural_freq) * time_array)

# Combine both sine waves
combined_wave = np.array([sine_wave_1, sine_wave_2]).T

# Scale to 16-bit range
combined_wave *= 32767 / np.max(np.abs(combined_wave))

# Convert to 16-bit integers
combined_wave = combined_wave.astype(np.int16)

# Get the path to your Downloads folder
downloads_path = os.path.expanduser("~/Downloads")

# Save to stereo .wav file
wavfile.write(f"{downloads_path}/{int(freq)}hz+{int(binaural_freq)}hz-{int(duration_min)}min.wav", sampling_freq, combined_wave)

# Print completion message
print("Done!")
