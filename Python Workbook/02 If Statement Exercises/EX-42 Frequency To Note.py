"""
In the previous question, you converted from note name to frequency. In this question,
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question, then report the name of the note. Otherwise, report that the
frequency does not correspond to a known note. In this exercise, you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.
"""

note_frequencies = {
    'C4': 261.63,
    'D4': 293.66,
    'E4': 329.63,
    'F4': 349.23,
    'G4': 392.00,
    'A4': 440.00,
    'B4': 493.88
}

frequency = float(input("Enter the frequency (Hz): "))

note = ""
for note_, freq in note_frequencies.items():
    if abs(frequency - freq) <= 1:
        note = note_

if note:
    print(f"The frequency {frequency} Hz corresponds to the note {note}.")
else:
    print(f"The frequency {frequency} Hz does not correspond to a known note.")
