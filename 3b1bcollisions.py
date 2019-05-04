# this code is to simulate what goes on in this video: https://www.youtube.com/watch?v=jsYwFizhncE
# u1 = speed before collision of big block
# u2 = news speed before collision of small block
# v1 = speed after collision of big block
# v2 = speed after collisoin of small block

# desired digits of pi
ndigits = 3


# masses of the blocks
m1 = 100**(ndigits-1)
m2 = 2

u1 = 1 # result is independentof this value
u2 = 0

#print(u1,u2)
collision_count = 0

while u1 > u2:
	# collision happens, see https://en.wikipedia.org/wiki/Elastic_collision#One-dimensional-Newtonian for math behind this
	frac = m1 + m2
	v1 = (m1-m2)/frac*u1+2*m2/frac*u2
	v2 = (m2-m1)/frac*u2+2*m1/frac*u1

	# after the blocks collide, the small block also collides with the wass, so add 2 collisions
	collision_count += 2

	# the velocity of the big block remains the same. The velocity of the small block gets reversed since it hits the wall
	u1 = v1
	u2 = -v2
	#print(u1,u2)

# if v2 is negative, the small block doesn't reach the wall again so remove a collision
if v2<0:
	collision_count -= 1

print(collision_count)
