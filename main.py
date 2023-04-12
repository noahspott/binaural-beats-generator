from pydub import AudioSegment


##################
# GET USER INPUT #
##################

# Get the file name
file_name = input("File name: ")

# Get frequency in Hz
frequency = input("Frequency (Hz): ")

# Get binaural frequency in Hz
binaural_frequency = input("Binaural Frequency (Hz): ")

# Get length in minutes
audio_length = input("Length of .wav (minutes): ")



##################
#   FILE EXPORT  #
##################

# Export file
#file_handle = sound.export("~/Downloads")