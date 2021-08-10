#List Comprehensions
print([[n_x, n_y, n_z] for n_x in range(x+1) for n_y in range(y+1) for n_z in range(z+1) if n_x+n_y+n_z != n ])
