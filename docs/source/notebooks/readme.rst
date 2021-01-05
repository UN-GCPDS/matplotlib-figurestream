Matplotlib-FigureStream
=======================

A backend for serve Matplotlib animations as web streams.

|GitHub top language| |PyPI - License| |PyPI| |PyPI - Status| |PyPI -
Python Version| |GitHub last commit| |CodeFactor Grade| |Documentation
Status|

.. |GitHub top language| image:: https://img.shields.io/github/languages/top/un-gcpds/matplotlib-figurestream?
.. |PyPI - License| image:: https://img.shields.io/pypi/l/figurestream?
.. |PyPI| image:: https://img.shields.io/pypi/v/figurestream?
.. |PyPI - Status| image:: https://img.shields.io/pypi/status/figurestream?
.. |PyPI - Python Version| image:: https://img.shields.io/pypi/pyversions/figurestream?
.. |GitHub last commit| image:: https://img.shields.io/github/last-commit/un-gcpds/matplotlib-figurestream?
.. |CodeFactor Grade| image:: https://img.shields.io/codefactor/grade/github/UN-GCPDS/matplotlib-figurestream?
.. |Documentation Status| image:: https://readthedocs.org/projects/figurestream/badge/?version=latest
   :target: https://figurestream.readthedocs.io/en/latest/?badge=latest

Instalation
-----------

.. code:: ipython3

    pip install figurestream

Bare minimum
------------

By default, the stream serves on http://localhost:5000

.. code:: ipython3

    # FigureStream replace any Figure object 
    from figurestream import FigureStream
    
    import numpy as np
    from datetime import datetime
    
    # FigureStream can be used like any Figure object
    stream = FigureStream()
    sub = stream.add_subplot(111)
    x = np.linspace(0, 3, 1000)
    
    # Update animation loop
    while True:
        sub.clear()  # clear the canvas
    
        # ------------------------------------------------------------------------
        # Any plot operation 
        sub.set_title('FigureStream')
        sub.set_xlabel('Time [s]')
        sub.set_ylabel('Amplitude')
        sub.plot(x, np.sin(2 * np.pi * 2 * (x + datetime.now().timestamp())))
        sub.plot(x, np.sin(2 * np.pi * 0.5 * (x + datetime.now().timestamp())))
        # ------------------------------------------------------------------------
        
        stream.feed()  # push the frame into the server

For fast updates is recommended to use ``set_data``, ``set_ydata`` and
``set_xdata`` instead of clear and draw again in each loop, also
``FigureStream`` can be implemented from a custom class.

.. code:: ipython3

    # FigureStream replace any Figure object
    from figurestream import FigureStream
    
    import numpy as np
    from datetime import datetime
    
    
    class FastAnimation(FigureStream):
    
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
            axis = self.add_subplot(111)
            self.x = np.linspace(0, 3, 1000)
            
            # ------------------------------------------------------------------------
            # Single time plot configuration
            axis.set_title('FigureStream')
            axis.set_xlabel('Time [s]')
            axis.set_ylabel('Amplitude')
    
            axis.set_ylim(-1.2, 1.2)
            axis.set_xlim(0, 3)
            
            # Lines objects
            self.line1, *_ = axis.plot(self.x, np.zeros(self.x.size))
            self.line2, *_ = axis.plot(self.x, np.zeros(self.x.size))
            # ------------------------------------------------------------------------
    
            self.anim()
    
        def anim(self):
            # Update animation loop
            while True:
                # ------------------------------------------------------------------------
                # Update only the data values is faster than update all the plot
                self.line1.set_ydata(np.sin(2 * np.pi * 2 * (self.x + datetime.now().timestamp())))
                self.line2.set_ydata(np.sin(2 * np.pi * 0.5 * (self.x + datetime.now().timestamp())))
                # ------------------------------------------------------------------------
                
                self.feed() # push the frame into the server
    
    
    if __name__ == '__main__':
        FastAnimation()

Change port and endpoint
------------------------

If we want to serve the stream in a different place we can use the
parameters ``port`` and ``endpoint``, for example:

.. code:: ipython3

    FigureStream(port='5500', endpoint='figure.jpeg')

now the stream will serve on http://localhost:5500/figure.jpeg
