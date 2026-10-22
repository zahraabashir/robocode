from pathlib import Path
s=Path('approach.py').read_text()
s=s.replace('self.pts=np.array(points); self.normals=np.array(normals)', '''self.pts=np.repeat(np.array(points),3,axis=0); self.normals=np.repeat(np.array(normals),3,axis=0)
        tangent=np.column_stack((-self.normals[:,1],self.normals[:,0]))
        self.dirs=self.normals+np.tile(np.array([-.3,0.,.3]),len(points))[:,None]*tangent
        self.dirs/=np.linalg.norm(self.dirs,axis=1)[:,None]''')
s=s.replace('torque=rr[:,0]*self.normals[:,1]-rr[:,1]*self.normals[:,0]','torque=rr[:,0]*self.dirs[:,1]-rr[:,1]*self.dirs[:,0]')
s=s.replace('vel=self.normals-omega','vel=self.dirs-omega')
s=s.replace('target=p-n*(s[28]-.008)+n*step','target=robot+self.dirs[k]*step+n*(-s[28]+.008-along)')
Path('candidate_angles.py').write_text(s)
