class Monitor:

    def __init__(self, frequency: int):
        self.monitor_name = 'Samsung'
        self.monitor_matrix = 'VA'
        self.monitor_res = 'WQHD'
        self.monitor_freq = frequency

    def information(self):
        print(
            f' Monitor 1:\n  Name: {monitor_1.monitor_name}\n  Matrix: {monitor_1.monitor_matrix}\n  Resolution: {monitor_1.monitor_res}\n  Frequency: {monitor_1.monitor_freq}\n')
        print(
            f' Monitor 2:\n  Name: {monitor_2.monitor_name}\n  Matrix: {monitor_2.monitor_matrix}\n  Resolution: {monitor_2.monitor_res}\n  Frequency: {monitor_2.monitor_freq}\n')
        print(
            f' Monitor 3:\n  Name: {monitor_3.monitor_name}\n  Matrix: {monitor_3.monitor_matrix}\n  Resolution: {monitor_3.monitor_res}\n  Frequency: {monitor_3.monitor_freq}\n')
        print(
            f' Monitor 4:\n  Name: {monitor_4.monitor_name}\n  Matrix: {monitor_4.monitor_matrix}\n  Resolution: {monitor_4.monitor_res}\n  Frequency: {monitor_4.monitor_freq}\n\n')


monitor_1 = Monitor(60)
monitor_2 = Monitor(144)
monitor_3 = Monitor(70)
monitor_4 = Monitor(60)
print('MONITORS:\n')
monitor_1.information()


class Headphones:
    def __init__(self, micro: str):
        self.headphones_name = 'Sony'
        self.headphones_sensitivity = 108
        self.headphones_micro = micro

    def information(self):
        print(
            f' Headphones 1:\n  Name: {headphones_1.headphones_name}\n  Sensitivity: {headphones_1.headphones_sensitivity}\n  Microphone: {headphones_1.headphones_micro}\n')
        print(
            f' Headphones 2:\n  Name: {headphones_2.headphones_name}\n  Sensitivity: {headphones_2.headphones_sensitivity}\n  Microphone: {headphones_2.headphones_micro}\n')
        print(
            f' Headphones 3:\n  Name: {headphones_3.headphones_name}\n  Sensitivity: {headphones_3.headphones_sensitivity}\n  Microphone: {headphones_3.headphones_micro}')


headphones_1 = Headphones('False')
headphones_2 = Headphones('True')
headphones_3 = Headphones('True')
print('HEADPHONES:\n')
headphones_1.information()
'''while True:
    print('amelia k is the best<33')'''
