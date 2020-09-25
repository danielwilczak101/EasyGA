# Imported library
import random

def check_values(low,high):
    #Check to make sure its not less then zero
    assert low > 0 , "The random gene low can not be less then zero"
    # Check to make sure the high value is not
    # lower than or equal to low and not 0.
    assert high > low, "High value can not be smaller then low value"
    assert high != 0, "High value can not be zero"

def random_gene(gene_input, gene_input_type, gene_index):
    created_gene = None
    #Determining if single range/domain or index-dependent
    if gene_input_type[gene_index] == "range":
        created_gene = random.randint(gene_input[gene_index][0], gene_input[gene_index][1])
    elif gene_input_type[gene_index] == "domain":
        created_gene = random.choice(gene_input[gene_index])
    elif gene_input_type[gene_index] == "float-range":
        created_gene = random.uniform(gene_input[gene_index][0], gene_input[gene_index][1])

    return created_gene
