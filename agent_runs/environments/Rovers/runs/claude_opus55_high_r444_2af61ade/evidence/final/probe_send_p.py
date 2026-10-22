from probe_send_lib import *
for s in range(40):
    e=E(s)
    ob=[(e.g(n,'x'),e.g(n,'y')) for n in e.objs('objective')]
    if all(x<0 for x,y in ob):
        sm=[(n,round(e.g(n,'x'),2),round(e.g(n,'y'),2),e.g(n,'is_soil')) for n in e.objs('sample')]
        print(s,ob,sm)
    e.env.close()
