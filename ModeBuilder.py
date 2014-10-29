import struct
import math
import pyaudio
from Scale import Scale
from PythagSeries import PythagSeries
import ModeBuilderTests
from Interval import  Interval
class ModeBuilder(object):

    def __init__(self, base_frequency):
        self.base_frequency = base_frequency
        self.mode_names = ('Ionian','Dorian','Phrygian','Lydian','Mixolydian','Aeolian','Locrian','Ionian')
        self.initial_scale = PythagSeries(self.base_frequency)


# Builds the scale by adjusting shifting the scale, and computing the octave.
    def build_scale_from_octave_adjustment(self):
        octave_scale = Scale(self.base_frequency)
        octave_scale.scale_intervals = self.initial_scale.scale_intervals
        octave_scale.scale_intervals = octave_scale.sort_by_final_frequency()
        for i in self.mode_names:
            print(i)
            self.play_scale(octave_scale.scale_intervals)
            octave_scale.get_next_mode()

# Builds the scale by instantiating a new pythag scale object and with the previous scales 2nd object
    def build_scale_from_pythag_class(self):
        base_fq = self.base_frequency
        for i in self.mode_names:
            print(i)
            pythag_scale = PythagSeries(base_fq)
            pythag_scale_intervals_sorted = pythag_scale.sort_by_final_frequency()
            self.play_scale(pythag_scale_intervals_sorted)
            base_fq = pythag_scale_intervals_sorted[1].final_frequency

            # Plays the sorted pythag scale

    def play_scale(self, scale):

        fs = 48000
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=fs,
            output=True)
        for interval in scale:
            print(interval.final_frequency)
            self.play_tone(interval.final_frequency, .5 , 1, fs, stream)
        stream.close()
        p.terminate()

    def play_tone(self, frequency, amplitude, duration, fs, stream):
        N = int(fs / frequency)
        T = int(frequency * duration)  # repeat for T cycles
        dt = 1.0 / fs
        # 1 cycle
        tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
                for n in range(N))
        # =todo: get the format from the stream; this assumes Float32
        data = b''.join(struct.pack('f', samp) for samp in tone)
        for n in range(T):
            stream.write(data)


def main():
    base = 528.00
    mode_builder = ModeBuilder(base)
    # Unpure Octave
    mode_builder.build_scale_from_octave_adjustment()
    #Pure Octave
    mode_builder.build_scale_from_pythag_class()
    pythag_series = PythagSeries(base)
    scale  = Scale(base)
    scale.scale_intervals = pythag_series.scale_intervals
    ModeBuilderTests.test_natural_scale(pythag_series)
    ModeBuilderTests.test_octave_scale(scale)
if __name__ == '__main__':
    main()