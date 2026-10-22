p='candidate_assignment.py'
s=open(p).read()
start=s.index('        for i,r in enumerate(self.rovers):\n            p=pos[i]; start=self.nearest(p)')
end=s.index('            target,task,o,j=best',start)
s=s[:start]+'''        routes=[dijkstra(self.graph,indices=self.nearest(pos[i]),return_predecessors=True) for i in range(2)]
        options=[[],[]]
        for i,r in enumerate(self.rovers):
            dist=routes[i][0]
            candidates=[]
            for k in [0,1]:
                if not acquired[k] and not s.get(r,'store_full'):
                    for oi,o in enumerate(self.samples):
                        if int(s.get(o,'is_soil'))==k:
                            candidates.append((self.sample_masks[oi],'sample',o,k))
            for j,o in enumerate(self.objs):
                if not s.get(o,'received_image') and not any(s.get(o,'have_image_rover'+str(a)) for a in [0,1]):
                    candidates.append((self.image_masks[j]&~self.bad[i,:,j],'image',o,j))
            if self.pending_count(s,i):
                candidates.append((self.radio_mask&~self.send_bad[i],'send',None,None))
            for mask,task,o,j in candidates:
                dd=dist+.05*np.minimum(self.home_dist[i],1e4);dd[~mask]=np.inf
                target=int(np.argmin(dd));cost=dd[target]
                if not np.isfinite(cost):continue
                cost+= .15*self.home_dist[i][target]
                if task=='send':cost+=5 if any(c[1]!='send' for c in candidates) else 0
                if hasattr(self,'last_tasks') and self.last_tasks[i]==(task,j):cost-=1.5
                options[i].append((cost,(target,task,o,j)))
            h=self.nearest(self.homes[i])
            options[i].append((12+.2*dist[h],(h,'home',None,None)))
        best_pair=None;best_score=np.inf
        anywork=any(len(o)>1 for o in options)
        for c0,b0 in options[0]:
            for c1,b1 in options[1]:
                if b0[1]==b1[1] and b0[1] in ['sample','image'] and b0[3]==b1[3]:continue
                if anywork and b0[1]==b1[1]=='home':continue
                score=max(c0,c1)+.3*(c0+c1)
                if score<best_score:best_score=score;best_pair=(b0,b1)
        if best_pair is None:best_pair=(options[0][-1][1],options[1][-1][1])
        self.last_tasks=[(b[1],b[3]) for b in best_pair]
        for i,r in enumerate(self.rovers):
            p=pos[i];start=self.nearest(p);dist,pred=routes[i]
            pending=any(s.get(o,'have_image_rover'+str(i)) and not s.get(o,'received_image') for o in self.objs) or any(s.get(o,'analyzed_rover'+str(i)) and not received[int(s.get(o,'is_soil'))] for o in self.samples)
            best=best_pair[i]
''' + s[end:]
open(p,'w').write(s)
