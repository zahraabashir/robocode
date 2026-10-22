from probe_samp_8 import trial
for tgt in [(0.25,-1.82),(0.25,-1.84),(0.25,-1.86),(0.25,-1.88),(1.6,-1.8),(1.6,-1.6),(1.6,-1.7),(2.2,-1.6),(2.2,-1.5)]:
  p,r=trial(tgt); cy=p[1]+(-2.0-p[1])*(p[0]-0)/(p[0]+1.9); print(tgt,p,r,'cross_y',round(cy,3))
