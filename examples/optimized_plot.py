# FigureStream replace any Figure object
from figurestream import FigureStream

import numpy as np
from datetime import datetime


########################################################################
class FastAnimation(FigureStream):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        axis = self.add_subplot(111)
        self.x = np.linspace(0, 3, 1000)

        axis.set_title('FigureStream')
        axis.set_xlabel('Time [s]')
        axis.set_ylabel('Amplitude')

        axis.set_ylim(-1.2, 1.2)
        axis.set_xlim(0, 3)

        self.line1, *_ = axis.plot(self.x, np.zeros(self.x.size))
        self.line2, *_ = axis.plot(self.x, np.zeros(self.x.size))

        self.anim()

    # ----------------------------------------------------------------------
    def anim(self):
        """"""
        while True:
            self.line1.set_ydata(np.sin(2 * np.pi * 2 * (self.x + datetime.now().timestamp())))
            self.line2.set_ydata(np.sin(2 * np.pi * 0.5 * (self.x + datetime.now().timestamp())))
            self.feed()


if __name__ == '__main__':
    FastAnimation()
