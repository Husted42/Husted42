# Define a tesor
import torch

# 1. Define a tensor with requires_grad=True
x = torch.tensor(2.0, requires_grad=True)

# 3. Multiply by 2, assign to a new variable
y = torch.mul(x, 2)
y.retain_grad()  # y is non-leaf; grad is discarded after backward unless retained

# 4. Sum the variable's elements, assign to a new variable
sum_y = torch.sum(y)
sum_y.retain_grad()  # also non-leaf, retain to inspect its grad later

# 5. Print gradients of all variables before the backward pass
print("Before backward:")
print("x.grad:", x.grad)
print("y.grad:", y.grad)
print("sum_y.grad:", sum_y.grad)

# 6. Backward pass on the last variable
sum_y.backward()

# 7. Print gradients again
print("\nAfter backward:")
print("x.grad:", x.grad)
print("y.grad:", y.grad)
print("sum_y.grad:", sum_y.grad)

