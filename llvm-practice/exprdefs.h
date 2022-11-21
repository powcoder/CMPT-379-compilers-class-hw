https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

#ifndef _DECAF_DEFS
#define _DECAF_DEFS

#include <string>

using namespace std;

extern int lineno;
extern int tokenpos;

extern "C"
{
  extern int yyerror(const char *);
  int yyparse(void);
  int yylex(void);  
  int yywrap(void);
}

#endif

