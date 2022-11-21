https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""
    python smash-gcc-lex.py [NUM]

    Generates a C program with an identifier string whose length is equal to NUM.
    Useful to check robustness of the lexical analyzer in various compilers.

    e.g. Run:
    
        python smash-gcc-lex.py | gcc -xc -

    This may not actually produce an a.out file. Works (or not) with gcc or clang.

    Compare to flex by running:

        make smash-gcc-lex
        python smash-gcc-lex.py | ./smash-gcc-lex

"""

import sys
if __name__ == "__main__":
  #n = sys.maxint / 100000000
  n = 10000000000
  if len(sys.argv) > 1:
    n = int(sys.argv[1])
  print("using n = {}\n".format(n), file=sys.stderr)
  sys.stdout.write("#include <stdio.h>\nint main() { int ")
  #for i in xrange(n): sys.stdout.write('x')
  sys.stdout.write('x' * n)
  sys.stdout.write(r' = 1; printf("yes\n"); }')
  print("\nfinished generating C code ...\n", file=sys.stderr)

