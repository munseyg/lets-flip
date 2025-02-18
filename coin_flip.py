import random

def flip_coin():
  """Simulates a coin flip and returns the result (Heads or Tails)."""
  # Use random.choice to pick randomly between "Heads" and "Tails"
  result = random.choice(["Heads", "Tails"])
  return result

# Example usage:
outcome = flip_coin()
print(f"The coin flip resulted in: {outcome}")


# You can also flip multiple times if you want:
num_flips = 10  # Example: flip 10 times
for _ in range(num_flips):
    outcome = flip_coin()
    print(outcome)


# Or keep track of the results:
num_flips = 100
heads_count = 0
tails_count = 0

for _ in range(num_flips):
    outcome = flip_coin()
    if outcome == "Heads":
        heads_count += 1
    else:
        tails_count += 1

print(f"\nAfter {num_flips} flips:")
print(f"Heads: {heads_count}")
print(f"Tails: {tails_count}")

# Calculate and print the percentages:
heads_percentage = (heads_count / num_flips) * 100
tails_percentage = (tails_count / num_flips) * 100

print(f"Heads Percentage: {heads_percentage:.2f}%")
print(f"Tails Percentage: {tails_percentage:.2f}%")