from pD_lib import *
S=(0.4,-0.6,np.pi)
print('baseline',trial((S,None)))
print('on line mid',trial((S,pos_on_line(S,0.6,0.0))))
print(pos_on_line(S,0.6,0.0))
