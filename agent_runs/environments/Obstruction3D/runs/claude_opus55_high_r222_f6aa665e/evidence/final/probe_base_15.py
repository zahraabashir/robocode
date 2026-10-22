import numpy as np
exec(open('probe_base_11.py').read().split("for seed in")[0])
seed=1
obs,_=env.reset(seed=seed); R=obs.get_object_from_name("robot")
base=np.array([obs.get(R,"pos_base_x"),obs.get(R,"pos_base_y")])
TB=obs.get_object_from_name("target_block"); tb0=np.array(obs.data[TB][:7],float)
rel=tb0[:2]-base; q=np.array([0,0.26,np.pi,-2.27,0,0.96,np.pi/2]); obs,rj=goto(obs,R,q); print("home rej",rj)
for zr in np.arange(0.40,0.125,-0.01):
    q,_=ik(np.array([rel[0]-0.12,rel[1],zr]),q); obs,rj=goto(obs,R,q)
    if rj: print("rej descending",zr)
for dx in np.arange(-0.12,0.121,0.01):
    q,_=ik(np.array([rel[0]+dx,rel[1],0.125]),q); obs,rj=goto(obs,R,q)
    tb=np.array(obs.data[TB][:7],float)
    print(f"dx={dx:+.2f} rej={rj} tb_delta={np.round(tb-tb0,4)} fs={obs.get(R,'finger_state'):.3f}")
    if rj: break
env.close()
