import argparse
import umbridge
import numpy as np


parser = argparse.ArgumentParser(description="Model output")
parser.add_argument("url",metavar="url",type=str,
                    help= "The URL on which the model is running, e.g. http://localhost:[port_number] if the model is hosted locally")
args = parser.parse_args()
print(f"Connecting to host {args.url}")


model = umbridge.HTTPModel(args.url,"MODEL_NAME")

#Define mean of parameters that shall be varied in a range of +-10%
L_arm = 200e-6 # in henry (H)
L_AC = 320e-3
R_arm = 20e-3 # in Ohms
R_AC = 60e-3

#Define parameters that will be assumed to be ideal and will thus not be varied
L_DC = 5e-3
R_DC = 10e-3
U_AC = 325 # in volts (V): amplitude of the grid
omega_AC = 2*np.pi*50 # assume grid frequency of 50 Hz
U_DC = 700 # assumee ideal, constant DC voltage
I_AC = 15 # in amperes (A): grid current
phi_AC = 0 # in °: Initial phase shift of grid current

#Define time interval
t_step = 125e-6 # in seconds: time resolution
t_stop = 20e-3 #time horizon should be at least one full grid period, i.e. 20ms
t = np.arange(0,t_stop,t_step)


