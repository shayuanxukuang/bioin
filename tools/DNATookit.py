from structure import *
from collections import Counter
import random
def validateseq(dna_seq):
    tmpseq=dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tmpFreDict={"A":0,"C":0,"G":0,"T":0}
    for nuc in seq:
        tmpFreDict[nuc]+=1
    return tmpFreDict


def transcription(seq):
    return seq.replace("T","U")

def translate_seq(seq,init_pos=0):
    return[DNA_Codons[seq[pos:pos+3]] for pos in range (init_pos,len(seq)-2,3)]


def reversecomplement(seq):
    return ''.join([DNA_reversecomplement[nuc] for nuc in seq])[::-1]


def gc_content(seq):
    """GC content in dna or rna"""
    return round((seq.count('C')+seq.count('G'))/len(seq)*100,6)


def gc_content_subsec(seq,k=20):
    res=[]
    for i in range(0,len(seq)-k+1,k):
        subseq=seq[i:i+k]
        res.append(gc_content(subseq))
    return res



def condon_usage(seq, aminoacid):
    """
    计算给定DNA序列中特定氨基酸的密码子使用频率。

    参数:
        seq (str): DNA序列。
        aminoacid (str): 要查找的氨基酸。

    返回:
        dict: 包含每个密码子及其使用频率的字典。
    """
    tmplist = []
    # 确保循环能够正确处理序列末尾，即使长度不是3的倍数
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i + 3]
        if codon in DNA_Codons and DNA_Codons[codon] == aminoacid:
            tmplist.append(codon)

    fredict = dict(Counter(tmplist))
    totalweight = sum(fredict.values())
    # 使用字典推导式来简化代码并更新频率
    fredict = {seq: round(count / totalweight, 2) for seq, count in fredict.items()}
    return fredict

#读文件
def readFile(filepath):
    with open (filepath,'r')as f:
        return[l.strip()for l in f.readlines()]

#读码框
def gen_read_frames(seq):
    frames=[]
    frames.append(translate_seq(seq,0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reversecomplement(seq), 0))
    frames.append(translate_seq(reversecomplement(seq), 1))
    frames.append(translate_seq(reversecomplement(seq), 2))
    return  frames


def protein_start(seq):
    currentprot=[]
    proteins=[]
    for aa in seq:
        if aa=="_":
            if currentprot:
                for p in currentprot:
                    proteins.append(p)
                currentprot=[]
        else:
            if aa=="M":
                currentprot.append("")
            for i in range(len(currentprot)):
                currentprot[i]+=aa
    return  proteins


def allproteinsorf(seq,startreadpos=0,endpos=0,ordered=False):
    if endpos>startreadpos:
        rfs=gen_read_frames(seq[startreadpos:endpos])
    else:
        rfs=gen_read_frames(seq)

    res=[]
    for rf in rfs:
        prots=protein_start(rf)
        for p in prots:
            res.append(p)

    if ordered:
        return sorted(res,key=len,reverse=True)
    return res