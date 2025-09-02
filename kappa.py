def cohen_kappa(matrix):
    """
    matrix: 2x2 confusion matrix [[a, b], [c, d]]
    """
    a, b = matrix[0]
    c, d = matrix[1]

    N = a + b + c + d

    # Observed agreement
    Po = (a + d) / N

    # Marginal probabilities
    prob_yes_A = (a + b) / N
    prob_no_A = (c + d) / N
    prob_yes_B = (a + c) / N
    prob_no_B = (b + d) / N

    # Expected agreement
    Pe = (prob_yes_A * prob_yes_B) + (prob_no_A * prob_no_B)

    # Kappa
    kappa = (Po - Pe) / (1 - Pe)
    
    return kappa

# Example usage:
# confusion_matrix = [[Both Yes, A Yes / B No], [A No / B Yes, Both No]]
confusion_matrix = #[[A, B], [C, D]]
kappa = cohen_kappa(confusion_matrix)
print(f"Cohen's Kappa: {kappa:.3f}")