from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

all_positive = set()
all_negative = set()

def plot_correlations(df, title, target_gene, gene_list_file, ax, xlim=(-0.5, 0.5), alpha=0.05):
    global all_positive
    global all_negative
    print('=============================================================================')
    genes = open(gene_list_file, 'r').read().strip().split(', ')
    print(f'{gene_list_file} genes in total: ', len(genes))
    genes = list(filter(lambda gene: gene in df.columns, genes))
    print(f'{gene_list_file} genes in our data: ', len(genes))
    corrs = np.array([stats.pearsonr(df[target_gene], df[gene])[0] for gene in genes])
    ps = np.array([stats.pearsonr(df[target_gene], df[gene])[1] for gene in genes])
    neg_log_ps = np.array([-np.log10(p) for p in ps])
    neg_log_ps = np.nan_to_num(neg_log_ps, posinf=10)
    neg_log_ps = np.minimum(neg_log_ps, 10)

    neg_corrs = (corrs < 0) & (ps < alpha)
    pos_corrs = (corrs > 0) & (ps < alpha)
    neg_genes = [genes[i] for i in range(len(genes)) if neg_corrs[i]]
    pos_genes = [genes[i] for i in range(len(genes)) if pos_corrs[i]]
    print('Negative genes: ', ', '.join(neg_genes))
    print('Positive genes: ', ', '.join(pos_genes))
    for x in neg_genes:
        all_negative.add(x)
    for x in pos_genes:
        all_positive.add(x)
    print('=============================================================================')

    plt.figure(figsize=(16, 9))

    sns.scatterplot(x=corrs, y=neg_log_ps, ax=ax)
    for i, gene in enumerate(genes):
        ax.text(corrs[i] + 0.01, neg_log_ps[i] + 0.01, gene, fontsize=12)

    ax.plot([xlim[0], xlim[1]], [-np.log10(alpha), -np.log10(alpha)], label=f'p={alpha}')
    ax.legend()

    ax.set_xticks(np.linspace(xlim[0], xlim[1], 21))

    ax.set_title(title)
    ax.set_xlabel('Pearson correlation')
    ax.set_ylabel('-log10 P-value')
