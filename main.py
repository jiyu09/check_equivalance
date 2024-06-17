# A = {1, 2, 3, 4}
# R = {(1, 1), (1, 3), (2, 2), (3, 3),(3, 1), (3, 4), (4, 4), (4, 3)}

def cheak_reflexive(R, A) :
  reflex = set([(x, x) for x in list(A)])
  return reflex.issubset(R)

def cheak_symmetric(R) :
  symmetric = set([(y, x) for (x, y) in list(R)])
  return symmetric.issubset(R)

def cheak_transitive(R) :
  R_list = list(R)
  transitive_list = []
  for (a, b) in R_list :
    for (c, d) in R_list :
      if b == c :
        transitive_list.append((a, d))
  transitive = set(transitive_list)
  return transitive.issubset(R)

def check_equivalance(R, A) :
  return cheak_reflexive(R, A) and cheak_symmetric(R) and cheak_transitive(R)

check_equivalance(R, A)
