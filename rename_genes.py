import sys
g_d={}
t_d={}
for l in open(sys.argv[1]):
    l_arr=l.rstrip().split("\t")
    g_d[l_arr[0]]=l_arr[2]
    t_d[l_arr[1]]=l_arr[3]

for l in open(sys.argv[2]):
    if(l.startswith("#")):
        print(l.rstrip())
        continue
    l_arr=l.rstrip().split("\t")
    d=l_arr[8].split(";")
    da=[]
    for i in d:
        i=i.strip()
        if(i.startswith("gene_id")):
            gid=g_d[i.split()[1]]
            da.append("gene_id "+gid)
        if(i.startswith("transcript_id")):
            tid=t_d[i.split()[1]]
            da.append("transcript_id "+tid)
        if(i.startswith("exon_number")):
            da.append(i)
    print("\t".join(l_arr[0:-1])+"\t"+"; ".join(da)+";")
