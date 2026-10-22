from pathlib import Path
s=Path('approach.py').read_text()
s=s.replace('rr=self.pts-com\n        torque=', '''rr=self.pts-com
        tangent=np.column_stack((-self.normals[:,1],self.normals[:,0]))
        omega_n=(rr[:,0]*self.normals[:,1]-rr[:,1]*self.normals[:,0])/(inertia+np.sum(rr*rr,axis=1))
        omega_t=(rr[:,0]*tangent[:,1]-rr[:,1]*tangent[:,0])/(inertia+np.sum(rr*rr,axis=1))
        cross=np.column_stack((-self.pts[:,1],self.pts[:,0]))
        jn=np.column_stack((self.normals-omega_n[:,None]*cross,omega_n))
        jt=np.column_stack((tangent-omega_t[:,None]*cross,omega_t))
        weights=np.array([1.,1.,.35]); desired=np.r_[delta,angle]
        dn=(jn*weights)@desired; dt=(jt*weights)@desired
        nn=np.sum(jn*jn*weights,axis=1); nt=np.sum(jn*jt*weights,axis=1); tt=np.sum(jt*jt*weights,axis=1)
        denom=dn*tt-dt*nt
        optimum=np.divide(dt*nn-dn*nt,denom,out=np.zeros(len(dn)),where=np.abs(denom)>1e-10)
        fs=np.column_stack((np.full(len(dn),-.4),np.clip(optimum,-.4,.4),np.full(len(dn),.4)))
        gains=np.maximum(0,dn[:,None]+fs*dt[:,None])**2/(nn[:,None]+2*fs*nt[:,None]+fs*fs*tt[:,None])
        f=fs[np.arange(len(dn)),np.argmax(gains,axis=1)]
        self.dirs=self.normals+f[:,None]*tangent
        self.dirs/=np.linalg.norm(self.dirs,axis=1)[:,None]
        torque=''')
s=s.replace('torque=rr[:,0]*self.normals[:,1]-rr[:,1]*self.normals[:,0]','torque=rr[:,0]*self.dirs[:,1]-rr[:,1]*self.dirs[:,0]')
s=s.replace('vel=self.normals-omega','vel=self.dirs-omega')
s=s.replace('target=p-n*(s[28]-.008)+n*step','target=p-n*(s[28]-.008)+self.dirs[k]*step')
Path('candidate_optimized.py').write_text(s)
