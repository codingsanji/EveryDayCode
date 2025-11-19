DSA 1: Logic Building



Process of creating clear, step-by-step methods to solve problems using simple rules and principles.



Mathematical Concepts:

1\. Number Theory

 	a) Decimal      (Base 10 -> 0-9)

 	b) Binary       (Base 2 -> 0,1)

 	c) Octal        (Base 8 -> 0-7)

 	d) Hexadecimal	(Base 16 -> 0-9, A-F)



Conversions:

1. Decimal

 	a) Binary = Repeated Division by 2. Read remainders from bottom up.

 	b) Octal = Repeated Division by 8. Read remainders from bottom up.

 	c) Hexadecimal = Repeated Division by 16. Read remainders from bottom up.

2\. Binary

 	a) Decimal = Positional Notation (sum of powers of 2).

 		eg: (1 \* 2^3) + (1 \* 2^2) + (0 \* 2^1) + (1 \* 2^0)

 			= (1 \* 8) + (1 \* 4) + (0 \* 2) + (1 \* 1)

 			= 8 + 4 + 0 + 1

 			= 13

 	b) Octal = Group binary digits in sets of three from right.

 		eg: Group into 3s:

 			110 101

 			110\_2 = 6\_8

 			101\_2 = 5\_8

 			=65

 	c) Hexadecimal = Group binary digits in sets of four from right. (similar to Octal conversion)

3\. Octal

 	a) Decimal = Positional Notation (sum of powers of 8). (just like Binary to Decimal but 8 instead of 2)

 	b) Binary = Convert each octal digit to its 3-bit binary equivalent. ( reverse of Binary to Octal )

 	c) Hexadecimal = Convert Octal to Binary first, then Binary to Hexadecimal.

4\. Hexadecimal

 	a) Decimal = Positional Notation (sum of powers of 16). (just like Binary to Decimal but 16 instead of 2)

 	b) Binary = Convert each hex digit to its 4-bit binary equivalent.

 		eg:

 			D\_16 = 1101\_2

 			6\_16 = 0110\_2

 	c) Octal = Convert Hexadecimal to Binary first, then Binary to Octal.

 



2\. Arithmetic Operations and Properties

| Property              | Addition                               | Subtraction                           | Multiplication                         | Division                                |

|-----------------------|----------------------------------------|---------------------------------------|----------------------------------------|-----------------------------------------|

| \*\*Closure Property\*\*  | a + b ∈ ℤ                              | a - b ∈ ℤ                             | a × b ∈ ℤ                              | a / b ∉ ℤ                               |

| \*\*Commutative Property\*\* | (a + b) = (b + a)                     | (a - b) ≠ (b - a)                     | (a × b) = (b × a)                      | (a / b) ≠ (b / a)                       |

| \*\*Associative Property\*\* | a + (b + c) = (a + b) + c             | a - (b - c) ≠ (a - b) - c             | a × (b × c) = (a × b) × c              | a / (b / c) ≠ (a / b) / c               |

| \*\*Distributive Property\*\* | a × (b + c) = a × b + a × c           | a × (b - c) = a × b - a × c           | Not applicable                         | Not applicable                          |

| \*\*Identity\*\*          | a + 0 = 0 + a = a                      | Not applicable                        | 1 × a = a × 1 = a                      | Not applicable                          |

| \*\*Inverse\*\*           | a + (-a) = 0                           | Not applicable                        | a × 1 / a = 1                          | Not applicable                          |





3\. Modular Arithmetic

Modulus is the remainder obtained from a division operation. It is basically the number that is "wrapped around" after reaching a certain value and thus is often referred to as "clock arithmetic".

Operations:

1. Modular Addition ->

 		 (a + b) mod m = ((a mod m) + (b mod m)) mod m

 	2) Modular Subtraction ->

 		 (a - b) mod m = ((a mod m) - (b mod m)+m) mod m

 	3) Modular Multiplication ->

 		(a x b) mod m = ((a mod m) x (b mod m)) mod m

 	4) Modular Division ->

 		(a / b) mod m = (a x (inverse of b if exists)) mod m

 	5) Modular Inverse (b modulo m is a number b^-1 such that (b\* b^-1) mod m = 1)

 

