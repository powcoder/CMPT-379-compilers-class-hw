https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

/* example that illustrates using C++ code and flex/bison */

#ifndef _USINGCPP_DEFS
#define _USINGCPP_DEFS

#include <string>

using namespace std;

extern "C"
{
  int yyerror(const char *);
  int yyparse(void);
  int yylex(void);  
  int yywrap(void);
}

#endif

