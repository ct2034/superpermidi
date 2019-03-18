from midiutil.MidiFile import MIDIFile, SHARPS, MAJOR
import sys

fname = sys.argv[1]
fname_no_ext = fname.split('.')[0]

# source / writing midi file:
# https://stackoverflow.com/questions/11059801/how-can-i-write-a-midi-file-with-python
mf = MIDIFile(1)
track = 0
time = 0
mf.addTrackName(track, time, fname_no_ext)
mf.addTempo(track, time, 120)
mf.addKeySignature(track, time, 0, SHARPS, MAJOR)
channel = 0
volume = 100

lookup = {  # ref note numbers: https://newt.phys.unsw.edu.au/jw/notes.html
    '1': 60,  # C4
    '2': 62,  # D
    '3': 64,  # E
    '4': 65,  # F
    '5': 67,  # G
    '6': 69,  # A
    '7': 71   # B
}

with open(fname, 'r') as f:
    for l in f:
        if not l.startswith("#"):
            for i, n in enumerate(l):
                try:
                    pitch = lookup[n]
                    time = i/2           # two per beat
                    duration = .5        # half note
                    mf.addNote(track, channel, pitch, time, duration, volume)
                except KeyError:
                    if n != '\n':
                        print("KeyError: " + n)
                    pass

with open(fname_no_ext+".mid", 'wb') as outf:
    mf.writeFile(outf)
