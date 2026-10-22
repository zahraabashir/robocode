from calib_u import *
import sys
e=R(); e.reset(1)
yaw=float(sys.argv[1]); p=[float(v) for v in sys.argv[2:5]]
qt,ok=kin.ik(e.base(),e.q(),np.array(p),kin.down_R(yaw)); print(ok, np.round(qt,3))
o=e.obs.copy()
for i,f in enumerate(F): o.set(e.r,f,qt[i])
M=kin.fk(e.base(),qt)
def put(name,pos,h=0.015):
    b=o.get_object_from_name(name)
    for k,v in zip(['pose_x','pose_y','pose_z'],pos): o.set(b,k,v)
    for k in ['half_extent_x','half_extent_y','half_extent_z']: o.set(b,k,h)
put('target_block',M[:3,3]); put('obstruction0',M[:3,3]+M[:3,2]*0.157)
put('target_region',[p[0],p[1],0.08],0.01)
import shutil; pth=e.env.render_state(state=o); shutil.copy(pth,'dbg/r_'+sys.argv[5]+'.png'); print(pth)
