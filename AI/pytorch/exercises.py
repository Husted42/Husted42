import torch

print(" Making tensors ")

x_1 = torch.rand(2, 17)
x_2 = torch.rand(3, 1)
x_3 = torch.rand(5, 2, 1)

print("x_1:", x_1)
print("x_2:", x_2)
print("x_3:", x_3)

x_1[0:2, 0:17] = 7

print("x_1 after modification:", x_1)

# Make a byte tensor
x_byte = torch.ByteTensor(5,)
print("x_byte:", x_byte)

# Make a float tensor
x_byte[1:4] = 1
print("x_byte after modification:", x_byte)

print("\n Addition ")

a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print("a + b:", a + b)
print("torch.add(a, b):", torch.add(a, b))
c = torch.zeros(3)
torch.add(a, b, out=c)
print("out= result:", c)
a.add_(b)  # in-place addition
print("a after in-place add_:", a)

print("\n Subtraction ")

print("b - a:", b - a)
print("torch.sub(b, a):", torch.sub(b, a))

print("\n Multiplication ")

print("element-wise a * b:", a * b)
print("torch.mul(a, b):", torch.mul(a, b))

m_1 = torch.rand(2, 3)
m_2 = torch.rand(3, 4)
print("matrix multiply (matmul):", torch.matmul(m_1, m_2))
print("matrix multiply (@ operator):", m_1 @ m_2)

print("\n Division ")

print("a / b:", a / b)
print("torch.div(a, b):", torch.div(a, b))

print("\n Broadcasting ")

row = torch.tensor([1.0, 2.0, 3.0])
col = torch.tensor([[1.0], [2.0], [3.0]])
print("row + col (broadcasted):", row + col)

print("\n Reshaping / view ")

r = torch.arange(12)
print("original:", r)
print("view(3, 4):", r.view(3, 4))
print("reshape(4, 3):", r.reshape(4, 3))
print("flatten again:", r.view(3, 4).flatten())

print("\n Indexing and slicing ")

grid = torch.arange(16).reshape(4, 4)
print("grid:", grid)
print("first row:", grid[0])
print("last column:", grid[:, -1])
print("submatrix:", grid[1:3, 1:3])

print("\n Aggregations ")

nums = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0])
print("sum:", nums.sum())
print("mean:", nums.mean())
print("max:", nums.max())
print("min:", nums.min())
print("argmax:", nums.argmax())
print("std:", nums.std())

print("\n Device check ")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("using device:", device)
d = nums.to(device)
print("tensor on device:", d)

print("\n Autograd basics ")

w = torch.tensor(2.0, requires_grad=True)
y = w ** 2 + 3 * w + 1
y.backward()
print("y:", y)
print("dy/dw:", w.grad)

print("\n NumPy interop ")

np_arr = nums.numpy()
print("as numpy array:", np_arr)
back_to_tensor = torch.from_numpy(np_arr)
print("back to tensor:", back_to_tensor)

