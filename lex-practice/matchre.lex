%{
  /* Compare Lex with Python and Perl

	Lex:
		make matchre
		python3 -c 'print("b"*100000 + "d")' | ./matchre
		python3 -c 'print("b"*100000)' | ./matchre
		
	Python:
		python3 -c 'print("b"*100000 + "d")' | python3 matchre.py 
		python3 -c 'print("b"*100000') | python3 matchre.py 

	Perl:
		perl -e 'print("b"x100000 . "d")' | perl matchre.pl
		perl -e 'print("b"x100000)' | perl matchre.pl

  */
#include <stdio.h>
%}

%%

^((a|b)+(b|c)+)+d$	{ printf("yes\n"); return 0; }
.+ 					{ printf("no\n"); return 0; }

%%

