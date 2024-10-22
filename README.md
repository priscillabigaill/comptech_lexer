# Lexical Analyzer for Custom Programming Language

### Group Members:

- Joseph Ruys (2602116964)
- Priscilla Abigail (2602109883)
- Vania Agnes (2602158531)

### Overview
This repository contains the Lexical Analyzer component of a compiler for a new programming language. The goal is to develop a Lexical Analyzer based on the provided grammar using Python and regular expressions.

### Grammar Specification

The grammar for the new programming language is defined as follows:

1. `program`: 
   - `declaration_list declaration`
   
2. `declaration_list`: 
   - `declaration declaration_list | declaration`

3. `declaration`: 
   - `var_decl | func_decl`
   
4. `var_decl`: 
   - `type ID ;`

5. `func_decl`: 
   - `type ID ( param_list ) compound_stmt`

6. `param_list`: 
   - `param_list, param | param`

7. `param`: 
   - `type ID`

8. `type`: 
   - `INT | FLOAT | CHAR`

9. `compound_stmt`: 
   - `{ statement_list }`

10. `statement_list`: 
    - `statement statement_list | statement`

11. `statement`: 
    - `var_decl | assignment_stmt | if_stmt | while_stmt | return_stmt | compound_stmt`

12. `assignment_stmt`: 
    - `ID = expression ;`

13. `if_stmt`: 
    - `IF ( expression ) statement ELSE statement`

14. `while_stmt`: 
    - `WHILE ( expression ) statement`

15. `return_stmt`: 
    - `RETURN expression ;`

16. `expression`: 
    - `term + term | term - term | term * term | term / term | term`

17. `term`: 
    - `factor * factor | factor / factor | factor`

18. `factor`: 
    - `ID | NUMBER | ( expression )`

### Token Types
The following token types are recognized by the Lexical Analyzer:
- `KEYWORD`: `INT`, `FLOAT`, `CHAR`, `IF`, `WHILE`, `RETURN`, `ELSE`
- `ID`: Identifiers (variable/function names) starting with a letter or underscore, followed by letters, digits, or underscores.
- `NUMBER`: Integer or floating-point numbers.
- `CHAR_LITERAL`: Character literals (e.g., `'A'`).
- `ASSIGN_OP`: Assignment operator (`=`).
- `ARITH_OP`: Arithmetic operators (`+`, `-`, `*`, `/`).
- `LEFT_BRACE`, `RIGHT_BRACE`: `{` and `}`.
- `LEFT_PAREN`, `RIGHT_PAREN`: `(` and `)`.
- `SEMICOLON`: `;`
- `COMMA`: `,`
- `WHITESPACE`: Ignored by the analyzer (spaces, tabs, newlines).
