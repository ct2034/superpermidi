#!/usr/bin/env python3
import argparse
import enum
import sys

import aubio
from midiutil.MidiFile import MAJOR, SHARPS, MIDIFile


def write_file(fname, mf):
    with open(fname, 'wb') as outf:
        mf.writeFile(outf)


def start_midifile(track, time, fname_no_ext, channel, volume, bpm):
    mf = MIDIFile(1)
    mf.addTrackName(track, time, fname_no_ext)
    mf.addTempo(track, time, bpm)
    mf.addKeySignature(track, time, 0, SHARPS, MAJOR)
    return mf


def write_notes(fname, mf, lookup, track, channel, volume):
    # source / writing midi file:
    # https://stackoverflow.com/questions/11059801/how-can-i-write-a-midi-file-with-python
    with open(fname, 'r') as f:
        for l in f:
            if not l.startswith("#"):
                for i, n in enumerate(l):
                    try:
                        pitch = lookup[n]
                        time = i/4              # 4 per beat
                        duration = 1./4         # quater note
                        mf.addNote(track, channel, pitch,
                                   time, duration, volume)
                    except KeyError:
                        if n != '\n':
                            print("KeyError: " + n)
                        pass
    return mf


def get_lookup():
    # ref note numbers: https://newt.phys.unsw.edu.au/jw/notes.html
    lookup = {
        '1': 60,  # C4
        '2': 62,  # D
        '3': 64,  # E
        '4': 65,  # F
        '5': 67,  # G
        '6': 69,  # A
        '7': 71   # B
    }
    return lookup


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse superperm txt file into midi file.')
    parser.add_argument('fname', type=open)
    parser.add_argument('--bpm', dest='bpm', type=int, default=120,
                        help='Speed fo the file (bpm)')
    args = parser.parse_args()
    fname = args.fname.name
    fname_no_ext = fname.split('.')[0]

    track = 0
    time = 0
    channel = 0
    volume = 100
    lookup = get_lookup()

    mf = start_midifile(track, time, fname_no_ext, channel, volume, args.bpm)
    mf = write_notes(fname, mf, lookup, track, channel, volume)
    write_file(fname_no_ext+".mid", mf)
