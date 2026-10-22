from probe_col_lib import R
from probe_col_bounds import approach
r=R(2)
r.goto(0,0.5,-1.75); r.goto(1,-0.5,-1.75)
print(approach(r,0,(-1,-1.75)), approach(r,1,(1,-1.75)))
