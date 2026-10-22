exec(open('probe_send_7.py').read().split('# rover1 blocker')[0])
for sd in range(30):
    reset(sd); s=dump('sample'); 
    c=[(k,v[:2]) for k,v in s.items() if v[0]<-0.4]
    if c: print(sd,c, {k:v[:2] for k,v in dump('obstacle').items() if v[3]<0.1}); 
