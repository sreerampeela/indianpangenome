# Converting gene_presence_absence to fasta format
import pandas as pd

df = pd.read_csv("gene_presence_absence.Rtab", sep="\t", header=0)
fout = open("gene_presence_absence_binary.fasta","a", encoding="utf-8", newline="\n")

sampleNames = list(df.columns)
print(sampleNames)
for sample in sampleNames[1:]:
    sampleSeq = "".join([str(x) for x in df[sample]])
    # print(sampleSeq)
    id = ">" + sample.split(".")[0]
    seqobject = id + "\n" + sampleSeq + "\n"
    # print(seqobject)
    fout.write(seqobject)

fout.close()

