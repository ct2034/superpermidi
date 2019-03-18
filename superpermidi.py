from midiutil.MidiFile import MIDIFile, SHARPS, MAJOR
import sys

# source / writing midi file:
# https://stackoverflow.com/questions/11059801/how-can-i-write-a-midi-file-with-python
fname = sys.argv[1]
fname_no_ext = fname.split('.')[0]

# create your MIDI object
mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, fname_no_ext)
mf.addTempo(track, time, 120)
mf.addKeySignature(track, time, 0, SHARPS, MAJOR)

# add some notes
channel = 0
volume = 100

lookup = {  # note numbers: https://newt.phys.unsw.edu.au/jw/notes.html
    '1': 60, # C4
    '2': 62, # D
    '3': 64, # E
    '4': 65, # F
    '5': 67, # G
    '6': 69, # A
    '7': 71  # B
}

with open(fname, 'r') as f:
    for l in f:
        if not l.startswith("#"):
            for i, n in enumerate(l):
                try:
                    pitch = lookup[n]    # C4 (middle C)
                    time = i/2           # start on beat 0
                    duration = .5        # half note
                    mf.addNote(track, channel, pitch, time, duration, volume)
                except KeyError:
                    if n != '\n':
                        print("KeyError: " + n)
                    pass

# write it to disk
with open(fname_no_ext+".mid", 'wb') as outf:
    mf.writeFile(outf)
