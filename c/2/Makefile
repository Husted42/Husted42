compiler?=cc
arguments?=-std=c11 -Wall -Werror -Wextra -pedantic -g

mynameis: mynameis.c
	$(compiler) mynameis.c -o mynameis $(arguments)

roll: roll.c
	$(compiler) roll.c -o roll $(arguments)

test_bits: test_bits.c bits.h
	$(compiler) -o test_bits test_bits.c $(arguments)

noAs: noAs.c bits.h
	$(compiler) -o noAs noAs.c $(arguments)
