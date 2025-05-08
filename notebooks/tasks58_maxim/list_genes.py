import os

while os.getcwd()[-len('mcrc-cetuximab-analysis'):] != 'mcrc-cetuximab-analysis':
    os.chdir('..')
os.getcwd()

with open('data/raw_counts_hgnc_unfiltered.csv') as f:
    s = f.readline()
    print(s)
    genes = s.strip().split()[1:]
    print('\n'.join(genes))