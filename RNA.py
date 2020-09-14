seqs = ["UUCGCCACUGA", "AUGCCUUGA", "AUGCGGUGAUAA"]

for seq in seqs: #loop through each entry in list
    print(seq)
    if seq.startswith("AUG"): #test if the sequence starts with AUG
        print("Has start codon")
    if seq.count("UGA") > 0:
        if not seq.endswith("UGA"):
            print("Has selenocysteine")
        if seq.endswith("UGA") and seq.count("UGA") > 1:
            print("Has selenocysteine")
