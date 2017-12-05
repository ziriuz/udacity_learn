def complement(p_A):
    # complement of P(A), which is the probability that the event did not happen.
    # The complement function takes in the probability of an event, P(A).
    return 1 - p_A


def joint(p_A, p_B):
    # calculates the joint probability of p_A, p_B, WHEN THOSE PROBABILITIES
    # ARE INDEPENDENT (this code wouldn't work for probabilities that depend on each other).
    return (p_A * p_B)


def bayes(p_A, p_B_given_A, p_notB_given_notA):
    # TODO: Calculate the posterior probabilit
    p_BA = joint(p_B_given_A, p_A)
    p_BnotA = joint(complement(p_notB_given_notA), complement(p_A))
    p_B = p_BA + p_BnotA
    posterior = p_A * p_B_given_A / p_B
    
    return posterior


print(bayes(p_A=0.3, p_B_given_A=0.7, p_notB_given_notA=0.9))



p=[0.2, 0.2, 0.2, 0.2, 0.2]
world = ['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
motions = [1,1]
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1


def sense(p, Z):
    q = []
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1 - hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q


def move(p, U):
    # Modify the move function to accommodate the added
    # probabilities of overshooting or undershooting
    # the intended destination.
    q = []
    n = len(p)
    for i in range(len(p)):
        p_cell = p[(i - U + 1) % n] * pUndershoot + p[(i - U - 1) % n] * pOvershoot + p[(i - U) % n] * pExact
        q.append(p_cell)
    return q

for i in range(len(motions)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])

print(p)
