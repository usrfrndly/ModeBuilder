class Interval:
    note_names = {528.00: "c", 594.00: "d", 668.25: "e", 704.00: "f", 792.00: "g", 891.00: "a", 1002.38: "b",
                  1056.00: "c"}

    def __init__(self, base_fq):
        self.base_freq = base_fq
        self.note_number = 0
        self.final_frequency = 0
        self.note_name = 0

    def __repr__(self):
        return '{}: Note Name: {}, Scale Degree: {}, Final Frequency:{} '.format(self.__class__.__name__,

                                                                                 self.note_name, self.note_number,
                                                                                 self.final_frequency)

    def to_array(self):
        return [self.note_name, self.note_number, self.final_frequency]

    def get_final_frequency_interval(self):
        return self.final_frequency

    def set_final_frequency_interval(self, freq):
        if freq != 0:
            self.final_frequency = round(float(freq), 3)
        else:
            return 0



    def set_note_name(self):
        if self.final_frequency is not 0:
            if self.final_frequency in self.note_names.keys():
                name = self.note_names[self.final_frequency]
                self.note_name = name
            elif self.get_final_frequency_interval() / 2 in self.note_names.keys():
                name = self.note_names[self.final_frequency / 2]
                self.note_name = name
        else:
            return

