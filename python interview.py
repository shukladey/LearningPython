# Meta interview (Feb 2026)
'''(DE | DS)

Given the below list of tuples, write a code that output the top 3 categories by score.

list1 = [ ("Adventure", 500),
          ("Adventure", 300),
          ("Sports", 600),
          ("TBD", 200),
          ...
        ]
'''

# SOLUTION1:

def top3cat(list1):
  scores = {}
  
  for category, score in list1:
      if category not in scores:
          scores[category] = 0
      scores[category] += score

  sorted_pairs = sorted(
        [(score, category) for category, score in scores.items()],
        reverse=True
    )
  
  # Flip back to (category, score)
    return [(category, score) for score, category in sorted_pairs[:3]]


# SOLUTION2:

def top3cat(list1):
  scores = {}

  # Aggregate scores by category - Pythonic way
  for category, score in data:
      scores[category] = scores.get(category, 0) + score

  sorted_pairs = sorted(
        [(score, category) for category, score in scores.items()],
        reverse=True
    )
  
  # Flip back to (category, score)
    return [(category, score) for score, category in sorted_pairs[:3]]
