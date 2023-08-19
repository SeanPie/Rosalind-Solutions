def probability_dominant(k,m,n):
    total_pop = k+m+n
    prob_dom_dom = 1 # Probability of dom allele with two dom parents
    prob_dom_rec = 0.5 # Probability with one dom parent, one rec parent
    prob_dom_hetero = 0.75 # one dom parent, one heterozygous parent

    prob_k = k / total_pop
    prob_m = m / total_pop
    prob_n = n / total_pop

    # Sum of each event where each event is the product of all possible outcomes, allele probability, 1st parent type, 2nd parent type
    prob_dom_allele = (prob_dom_dom * prob_k * prob_k +
                       prob_dom_rec * prob_k * prob_n +
                       prob_dom_rec * prob_n * prob_k +
                       prob_dom_hetero * prob_k * prob_m +
                       prob_dom_hetero * prob_m * prob_k +
                       prob_dom_hetero * prob_n * prob_m +
                       prob_dom_hetero * prob_m * prob_n +
                       prob_dom_hetero * prob_k * prob_n +
                       prob_dom_hetero * prob_n * prob_k)
    
    return prob_dom_allele
print(probability_dominant(2,2,2))