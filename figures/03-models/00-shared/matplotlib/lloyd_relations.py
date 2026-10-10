"""Deterministic teaching samples from original sources; exact Lloyd SSE checks."""
from numeric_relations import *
from matplotlib.patches import Rectangle

def draw():
 points=np.array([[0,0],[0,1],[1,0],[4,2],[4,3],[5,2]],float);initial=np.array([[0,0],[1,0]],float);assigned=np.argmin(np.sum((points[:,None]-initial[None])**2,axis=2),axis=1);updated=np.array([points[assigned==j].mean(axis=0) for j in [0,1]]);reassigned=np.argmin(np.sum((points[:,None]-updated[None])**2,axis=2),axis=1)
 losses=[np.sum((points-initial[assigned])**2),np.sum((points-updated[assigned])**2),np.sum((points-updated[reassigned])**2)];assert np.allclose(losses,[52,14.25,6.1875]);f,aa=fig(169,75,ncols=3)
 for i,a in enumerate(aa):
  labels=assigned if i<2 else reassigned;centers=initial if i==0 else updated;axes(a,(-.5,5.8),(-.5,3.8),'$x_1$','$x_2$',[0,2,4],[0,1,2,3]);a.set_aspect('equal');a.set_title(['分配到最近中心','固定标签更新均值','再次分配'][i]);
  for j,c,m in [(0,YELLOW,'o'),(1,BLUE,'s')]:q=points[labels==j];a.scatter(q[:,0],q[:,1],c=c,ec=INK if j==0 else c,s=23,marker=m)
  a.scatter(centers[:,0],centers[:,1],c=INK,marker='+',s=90,lw=1.2);a.text(.5,-.49,'$J='+f'{losses[i]:g}'+'$',transform=a.transAxes,ha='center')
  if i==0:a.axvline(.5,c=MUTED,ls='--',lw=.7)
  if i==1:
   for old,new in zip(initial,updated):a.annotate('',new,old,arrowprops={'arrowstyle':'->','color':INK,'lw':.8})
  if i==2:a.plot([2.2232,.9018],[-.2,3.5],c=MUTED,ls='--',lw=.7)
 save(f,'clustering-lloyd-steps','01-classic-models',{'samples':points,'initial_centers':initial,'updated_centers':updated,'initial_assignment':assigned,'reassignment':reassigned,'SSE':losses},{'K':2,'ties':'first center via argmin','boundary_reassignment':'original rounded boundary endpoints','teaching_construction':True},[C/'clustering-lloyd-steps.tex'])
 f,aa=fig(169,80,ncols=2);t=np.arange(16)*2*np.pi/16;inner=np.c_[np.cos(t),np.sin(t)];outer=2*inner;a,b=aa;axes(a,(-2.6,2.6),(-2.6,2.6),'$x_1$','$x_2$',[-2,0,2],[-2,0,2]);a.set_aspect('equal');a.scatter(inner[:,0],inner[:,1],c=BLUE,s=18);a.scatter(outer[:,0],outer[:,1],c=RED,marker='s',s=18);a.set_title('二维输入：两个同心圆');axes(b,(-2.3,2.3),(-.4,.4),'一维核 PCA 坐标 $z$','',[-1.5,0,1.5],[]);b.spines['left'].set_visible(False);b.scatter([-1.5],[0],c=BLUE,s=30);b.scatter([1.5],[0],c=RED,s=30,marker='s');b.axhline(0,c=GRID,lw=.7);b.text(-1.5,.12,'$r=1$\n16 点重合',ha='center');b.text(1.5,.12,'$r=2$\n16 点重合',ha='center');b.set_title('$z=\\phi(x)-2.5$');b.text(.5,-.27,'$\\phi(x)=\\|x\\|_2^2$',transform=b.transAxes,ha='center')
 save(f,'dim-kernel-radial','01-classic-models',{'inner_ring':inner,'outer_ring':outer,'kernel_coordinate':[-1.5]*16+[1.5]*16},{'kernel':'f*f^T, f=||x||2^2','mean_feature':2.5,'centered_rank':1,'eigenvalue':72,'eigenvector_sign':'inner negative, outer positive','teaching_construction':True},[C/'dim-kernel-radial.tex'])
 f,aa=fig(112,108,nrows=2,gridspec_kw={'height_ratios':[3,1]});a,b=aa;inside=np.array([[1.25,1.25],[1.7,1.4],[1.4,1.8]]);outside=np.array([[1.2,.45],[1.8,2.55],[.4,1.3],[3.1,2.3]]);axes(a,(0,4.2),(0,3.2),'$x_1$','$x_2$',range(5),range(4),True);a.add_patch(Rectangle((1,1),1,1,fc=YELLOW_FILL,ec=INK,lw=.7));a.scatter(inside[:,0],inside[:,1],c=YELLOW,ec=INK,s=20);a.scatter(outside[:,0],outside[:,1],fc='white',ec=BLUE,s=20);a.set_title('二维单元：计数 3');axes(b,(0,4.2),(-.5,.5),'$x_1$','',range(5),[]);b.spines['left'].set_visible(False);b.axvspan(1,2,color=YELLOW_FILL);b.scatter([1.2,1.25,1.4,1.7,1.8],np.zeros(5),c=INK,s=17);b.set_title('去掉 $x_2$ 限制：一维投影计数 5')
 save(f,'clustering-subspace','01-classic-models',{'inside':inside,'outside':outside,'projected_x':[1.2,1.25,1.4,1.7,1.8]},{'cell':[[1,2],[1,2]],'threshold':3,'teaching_construction':True},[C/'clustering-subspace.tex'])
