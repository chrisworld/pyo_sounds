import numpy as np

from pyo import *

def mic_gain_xy(phi):
  """
  gain of xy microphon, phi in degrees
  """
  return np.array([np.cos((phi + 45) * np.pi / 180), np.cos((phi - 45) * np.pi / 180)])


# start server
s = Server(sr=44100, duplex=1, audio='jack', jackname='pyo').boot().start()

# amplitude of server
s.amp = 0.5

# set source angle
phi = 15

g_xy = mic_gain_xy(phi)

print("g_xy: ", g_xy)

# to loudspeaker
l = Sine(freq=200, mul=float(g_xy[0])).out(0)
r = Sine(freq=200, mul=float(g_xy[1])).out(1)

s.gui(locals())