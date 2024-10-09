"""
The following table lists the sound level in decibels for several common noises.

Noise          |   Decibel level (dB)
Jackhammer     |   130
Gas lawnmowers |   106
Alarm clocks   |   70
Quiet rooms    |   40

Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table, then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed, then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.
"""

sound_level = float(input("Enter the sound level (in decibels): "))

noise_table = {
    130: "Jackhammer",
    106: "Gas lawnmowers",
    70: "Alarm clocks",
    40: "Quiet rooms"
}

if sound_level in noise_table:
    print(f"This is the noise of {noise_table[int(sound_level)]}")
elif 40 < sound_level < 130:
    if 40 < sound_level < 70:
        print(f"This is the noise between {noise_table[40]} and {noise_table[70]}")
    elif 70 < sound_level < 106:
        print(f"This is the noise between {noise_table[70]} and {noise_table[106]}")
    elif 106 < sound_level < 130:
        print(f"This is the noise between {noise_table[106]} and {noise_table[130]}")
elif sound_level > 130:
    print(f"This sound level is larger than the loudest noise in the table.")
else:
    print(f"This sound level is smaller than the quietest noise in the table.")
