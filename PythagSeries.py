"""
PythagSeries.py
Jaclyn Horowitz
Music Software Projects 2014
"""

import csv
import math
import struct
import copy
from Scale import Scale
from Interval import Interval
from PythagSeriesInterval import PythagSeriesInterval

'''
PythagSeries class : Represents the pythagorean series and is initialized with a base frequency.
'''


class PythagSeries(Scale):
    def __init__(self,base_fq):
        super(PythagSeries, self).__init__(base_fq)
        self.interval_list = [-1, 0, 1, 2, 3, 4, 5]
        # An array that contains properties for each interval_number_unsorted in the pythag series
        #self.pythag_scale_intervals = [None] * numintervals
        self.generate_pythag_scale()

    # generate_pythag_scale(): adds information for each interval_number_unsorted in the pythagorean series to the pythag_scale_intervals array
    def generate_pythag_scale(self):
        i = 0
        for interval in self.interval_list:
            self.scale_intervals.append(PythagSeriesInterval(interval,self.base_freq))
            self.scale_intervals[-1].set_note_name()
            i += 1
        self.scale_intervals.append(self.get_octave())
        #final_frequencies = [intv.final_frequency for intv in self.pythag_scale_intervals]
        #self.pythag_scale_sorted_final_frequencies = sorted(final_frequencies)

    # show_all_rows(): Prints each row in the pythagorithmic series
    def show_series_columns(self):
        print("[Interval, Numerator, Denominator, Factor,"
              " Interval Frequency, Octave, Octave Denom, Factor (Octave Adjusted), Final Frequency ]")
        for i in range(0, len(self.scale_intervals)):
            self.scale_intervals[i].show_column()

    def get_octave(self):
        octave = Interval(self.base_freq)
        octave_freq = self.base_freq * 2
        octave.final_frequency = octave_freq
        octave.note_number = self.NUM_INTERVALS
        octave.set_note_name()
        return octave

    def get_next_mode(self):
        self.scale_intervals = self.sort_by_final_frequency()
        self.scale_intervals.pop(0)
        octave = self.get_octave()
        self.scale_intervals.append(octave)
        return self.scale_intervals

        



        #print(octave_freq)



