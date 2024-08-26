from structure import *
class Bio_seq:


    def __init__(self,seq="ATCG",seq_type="DNA",label="no label"):
        self.seq=seq.upper()
        self.label=label
        self.seq_type=seq_type



    def __validate(self):
        return set(Nucleotides).issuperset(self.seq)

    def get_seq_info(self):
        """Returns 4 strings. Full sequence information"""
        return f"[Label]: {self.label}\n[Sequence]: {self.seq}\n[Biotype]: {self.seq_type}\n[Length]: {len(self.seq)}"

    def generate_rnd_seq(self, length=10, seq_type="DNA"):
        """Generate a random DNA sequence, provided the length"""
        seq = ''.join([random.choice(NUCLEOTIDE_BASE[seq_type])
                       for x in range(length)])
        self.__init__(seq, seq_type, "Randomly generated sequence")

    def transcription(self):
        return self.seq.replace("T", "U")

