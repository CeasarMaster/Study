class Monitor:

    def __init__(self, frequency: int):
        self.monitor_name = 'Samsung'
        self.monitor_matrix = 'VA'
        self.monitor_res = 'WQHD'
        self.monitor_freq = frequency

    def information(self):
        print(
            f'  Name: {self.monitor_name}\n  Matrix: {self.monitor_matrix}\n  Resolution: {self.monitor_res}\n  Frequency: {self.monitor_freq}\n')


monitor_1 = Monitor(60)
monitor_2 = Monitor(144)
monitor_3 = Monitor(70)
monitor_4 = Monitor(60)
print('MONITORS:\n')
monitor_1.information()
monitor_2.information()
monitor_3.information()
monitor_4.information()


class Headphones:
    def __init__(self, micro: bool):
        self.headphones_name = 'Sony'
        self.headphones_sensitivity = 108
        self.headphones_micro = micro

    def information(self):
        print(
            f'  Name: {self.headphones_name}\n  Sensitivity: {self.headphones_sensitivity}\n  Microphone: {self.headphones_micro}\n')


headphones_1 = Headphones(False)
headphones_2 = Headphones(True)
headphones_3 = Headphones(True)
print('HEADPHONES:\n')
headphones_1.information()
headphones_2.information()
headphones_3.information()

