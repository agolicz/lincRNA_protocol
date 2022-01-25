import sys
gc_d={}
go_d={}
gch_d={}
gn_d={}
for l in open(sys.argv[1]):
    if(l.startswith("#")):
        continue
    l_arr=l.rstrip().split("\t")
    if(l_arr[2]!="transcript"):
        continue
    for i in l_arr[8].split(";"):
        if(i.startswith("gene_id")):
            gid=i.split(" ")[1]
    s=int(l_arr[3])
    e=int(l_arr[4])
    o=l_arr[6]
    chro=l_arr[0]
    if(gid in gc_d):
        gc_d[gid].append(s)
        gc_d[gid].append(e)
        go_d[gid].add(o)
    else:
        gc_d[gid]=[]
        go_d[gid]=set()
        gch_d[gid]=chro
        gc_d[gid].append(s)
        gc_d[gid].append(e)
        go_d[gid].add(o)

for x in gc_d:
    sl=sorted(gc_d[x])
    orie="".join(go_d[x])
    print(gch_d[x]+"\t"+str(sl[0]-1)+"\t"+str(sl[-1])+"\t"+x[1:-1]+"\t0\t"+orie) 
