import sys
g_s=set()
gbase=sys.argv[1]

g_d={}
gcnt=0
for l in open(sys.argv[2]):
    l_arr=l.rstrip().split("\t")
    g=l_arr[0]
    t=l_arr[1]
    if(g not in g_d):
        gcnt=gcnt+1
        g2=gbase+str(gcnt).zfill(8)
        g_d[g]=g2
tcnt_d={}
for l in open(sys.argv[2]):
    l_arr=l.rstrip().split("\t")
    g=l_arr[0]
    t=l_arr[1]
    gn=g_d[l_arr[0]]
    if(gn not in tcnt_d):
        tcnt_d[gn]=1
        tn=gn+"."+str(tcnt_d[gn])
        print(g+"\t"+t+"\t"+"\""+gn+"\""+"\t"+"\""+tn+"\"")
    else:
        tcnt_d[gn]=tcnt_d[gn]+1
        tn=gn+"."+str(tcnt_d[gn])
        print(g+"\t"+t+"\t"+"\""+gn+"\""+"\t"+"\""+tn+"\"")
