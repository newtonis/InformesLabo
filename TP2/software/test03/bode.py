import numpy as np
import csv
from math import *


def round_sig(x, sig=2):
    return round(x, sig-int(floor(log10(abs(x))))-1)


def convert_freq(value):
    value = round_sig(value,2)
    if value < 1000:
        return "%3d Hz" % value
    if value < 1000 * (10**3):
        return "%.1f KHz" % (value/1000.0)
    return "%.1f MHz" % (value/float(10**6))


class Bode:
    points = []
    current = 0
    amp = 2
    data = dict()
    status = 0

    last_read = dict()
    current_action = "Waiting to start"


    def __init__(self):
        self.last_read["amp"] = 0.1
        self.last_read["pha"] = 0.1

    def set(self, osc, gen):
        self.osc = osc
        self.gen = gen

    def start(self, start_freq, end_freq, points , amp):
        self.points = np.logspace(np.log10(start_freq), np.log10(end_freq), points)
        self.current = 0
        self.amp = amp
        self.status = 1
        self.get_to_freq(self.points[self.current], self.amp)

    def update(self):
        if self.status:
            if self.osc.update():
                print("Taking point ", self.current)
                self.current_action = "Saving data ..."
                self.data[str(self.points[self.current])] = dict()
                self.data[str(self.points[self.current])]["vin"] = self.amp
                self.data[str(self.points[self.current])]["amp"] = self.osc.ratio2to1()
                self.data[str(self.points[self.current])]["pha"] = self.osc.phase2to1()
                self.last_read["amp"] = self.data[str(self.points[self.current])]["amp"]
                self.last_read["pha"] = self.data[str(self.points[self.current])]["pha"]

                print(self.data[str(self.points[self.current])])

                self.current += 1
                if self.current == len(self.points):
                    print("Bode finished")
                    print(self.data)
                    self.status = 0
                    self.current_action = "Finished all tasks"
                    return 1
                self.get_to_freq(self.points[self.current], self.amp)
            else:
                self.current_action = "Finding scale ... "

        return 0

    def get_scale_x(self):
        pass

    def get_scale_y(self):
        pass

    def get_freq(self):
        return self.points[self.current]

    def get_step(self):
        return self.current

    def get_to_freq(self, freq, amp):
        self.osc.set_scale_X(1.0 / freq * 3)
        self.gen.set_sine(freq, amp)

    def get_data(self):
        data = dict()
        data["sample"] = self.current+1
        data["total"] = len(self.points)
        data["amp"] = self.last_read["amp"]
        data["pha"] = self.last_read["pha"]
        if self.current < len(self.points):
            data["freq"] = convert_freq(self.points[self.current])
        else:
            data["freq"] = convert_freq(0.1)

        data["action"] = self.current_action

        return data

    def open_csv(self, filename):

        with open(filename , 'w') as csvfile:
            fieldnames = ["freq","vin", "amp", "pha"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in self.data:
                writer.writerow(float(i), self.data[i]["vin"], self.data[i]["amp"], self.data[i]["pha"])