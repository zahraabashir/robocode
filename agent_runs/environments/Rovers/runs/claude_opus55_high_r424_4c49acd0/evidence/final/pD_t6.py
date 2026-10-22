from pB_lib import *
s=Sim(44); s.goto(1,-1.0,-0.3)
def st(): return [[objf(s,k,'have_image_rover0'),objf(s,k,'received_image')] for k in range(3)]
for p in [(0.4,0.2),(0.7,0.3),(1.0,0.3)]:
    gp(s,0,[p],th=np.pi)
    s.act(a0=(0,0,0,'cal')); s.act(a0=(0,0,0,'img')); print(p,'img',st(),flush=True)
    s.act(a0=(0,0,0,'send')); print('send',st())
