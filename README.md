# bassBooster
# Audio Bass Boosting Presets with FFmpeg

This project applies a bass boost effect to an audio file using FFmpeg with customizable presets. The script allows you to choose from several refined bass boost presets, then processes your chosen audio file by applying multi-band equalization, a lowpass filter, compression, and echo reverb effects.

> **Disclaimer:** This script is provided for educational and personal use only. Please ensure you have the right to modify and process the audio files you work with.

## Features

- **Preset Selection:**  
  Choose from four bass boost presets ("light", "moderate", "strong", "extreme") that adjust parameters such as bass gain, bass frequency, mid-bass settings, lowpass frequency, and reverb delay.

- **Custom Audio Processing:**  
  Utilizes FFmpeg with multiple audio filters:
  - **Equalizer:** Fine-tunes the bass and mid-bass frequencies.
  - **Lowpass Filter:** Reduces high-frequency content for a smoother sound.
  - **Compressor & Echo:** Applies dynamic range compression and reverb to enhance the audio effect.

- **Input/Output Management:**  
  Processes audio files placed in an `input` folder and saves the processed output to an `output` folder.

## Prerequisites

- **Python 3.x**  
- **FFmpeg:** Make sure FFmpeg is installed and accessible from the command line.
- **Operating System:** The script is platform-independent but requires FFmpeg to be properly installed.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/audio-bass-boosting.git
   cd audio-bass-boosting
