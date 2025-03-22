import os

# Paths for input and output folders
input_folder = "input"
output_folder = "output"

# Define refined presets with balanced values to reduce mid-bass distortion
presets = {
    "light": {"bass_gain": 3, "bass_freq": 50, "midbass_freq": 120, "midbass_gain": -2, "lowpass_freq": 200, "reverb_delay": 5},
    "moderate": {"bass_gain": 5, "bass_freq": 45, "midbass_freq": 110, "midbass_gain": -3, "lowpass_freq": 180, "reverb_delay": 10},
    "strong": {"bass_gain": 7, "bass_freq": 40, "midbass_freq": 100, "midbass_gain": -4, "lowpass_freq": 150, "reverb_delay": 15},
    "extreme": {"bass_gain": 9, "bass_freq": 35, "midbass_freq": 90, "midbass_gain": -5, "lowpass_freq": 120, "reverb_delay": 20}
}

# Display preset options to the user
print("Choose a bass boost preset:")
for key in presets.keys():
    print(f"- {key}")

# Get user selection
preset_choice = input("Enter your preset choice: ").strip().lower()
if preset_choice not in presets:
    print("Invalid preset choice. Please choose a valid option.")
    exit()

# Retrieve parameters based on user choice
selected_preset = presets[preset_choice]
bass_gain = selected_preset["bass_gain"]
bass_freq = selected_preset["bass_freq"]
midbass_freq = selected_preset["midbass_freq"]
midbass_gain = selected_preset["midbass_gain"]
lowpass_freq = selected_preset["lowpass_freq"]
reverb_delay = selected_preset["reverb_delay"]

# Take user input for the song name
song_name = input("Enter the song filename (e.g., hard.mp3): ").strip()

# Remove spaces from the filename for consistency
formatted_song_name = song_name

# Full path to the input file and output file
input_file = os.path.join(input_folder, formatted_song_name)
output_file = os.path.join(output_folder, f"{formatted_song_name.rsplit('.', 1)[0]}BassBoosted_{preset_choice}.mp3")

# Check if the input file exists
if not os.path.exists(input_file):
    print(f"Error: {input_file} does not exist. Please check the filename and try again.")
else:
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Notify if the output file already exists
    if os.path.exists(output_file):
        print(f"Notice: A file with the name {output_file} already exists and will be replaced.")

    # FFmpeg command with multi-band equalizer for fine-tuned bass
    ffmpeg_command = f"""ffmpeg -i "{input_file}" -af \
"equalizer=f={bass_freq}:width_type=h:width=50:g={bass_gain}, \
equalizer=f={midbass_freq}:width_type=h:width=50:g={midbass_gain}, \
lowpass=f={lowpass_freq}, acompressor=threshold=-10dB:ratio=3:attack=5:release=50, \
aecho=0.8:0.9:{reverb_delay}:0.2" "{output_file}" """

    # Run the FFmpeg command
    os.system(ffmpeg_command)
    print(f"Processed audio saved as {output_file}")
