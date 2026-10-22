from probe_col_lib import R
r=R(0)
print(r.pos(0)); print(r.step(0,0.2,0)); print(r.step(0,0,0.2)); print(r.step(0,0,0,0.4)); print(r.step(0,0.2,0))
print(r.pos(1)); print(r.step(1,0.2,0)); print(r.step(1,0.123,-0.077))
print(r.step(1,0.5,0))
