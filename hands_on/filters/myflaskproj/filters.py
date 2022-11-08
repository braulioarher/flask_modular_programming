# Define custom filters

def evenFilter(sequence):
    even = []
    for item in sequence:
      if item % 2 == 0:
        even.append(item)
    return even
