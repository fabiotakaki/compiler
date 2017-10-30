# Compiler


# Steps to run

Clone the repository and using your virtualenv, run the following steps on terminal:

1. pip install -r requirements.txt
2. export FLASK_APP=flask_compiler/flask_compiler.py
3. export FLASK_DEBUG=true
4. flask run

# First da linguagem LALG:

1. ```<programa> = {program};```
2. ```<bloco> = {int, boolean, procedure, begin};```
3. ```<parte de declaração de variáveis> = {int, boolean}; 4<declaração de variáveis> = {int, boolean};```
5. ```<lista de identificadores> = {_,a - z,A - Z};```
6. ```<parte de declaração de subrotina> = {procedure}; 7<declaração de procedimento> = {procedure}; 8<parâmetros formais> = {var, _,a - z,A - Z};```
9. ```<seção de parâmetros formais> = {var, _,a - z,A - Z}; 10<comando composto> = {begin};```
11. ```<comando> = {_,a - z,A – Z, if, while, begin}; 12<atribuição> = {_,a - z,A – Z };```
13. ```<chamada de procedimento> = {_,a - z,A – Z }; 14<comando condifional 1> = {begin};```
15. ```<comando repetitivo 1> = {while};```
16. ```<expressão> = {+,-,_,a - z,A – Z, 1-9, (, not}; 17<relação> = {=, <>, <, <=, >=,>};```
18. ```<expressão simples> = {+,-, _,a - z,A – Z, 1-9, (, not}; 19<termo> = {_,a - z,A – Z , 1-9, (, not};```
20. ```<fator> = {_,a - z,A – Z , 1-9, (, not};```
21. ```<variável> = {_,a - z,A – Z };```
22. ```<lista de expressões> = {+,-,_,a - z,A – Z, 1-9, (, not }; 23<número> = {0-9};```
24. ```<dígito> = {0-9}```
25. ```<identificador> = {_,a - z,A – Z };```
26. ```<letra> = {_,a - z,A – Z};```

# Follow da Linguagem LALG

1. ```<programa> = {$};```
2. ```<bloco> = {.};```
3. ```<parte de declaração de variável> = {procedure, begin}; ```
4. ```<declaração de variáveis> = {;};```
5. ```<lista de identificadores> = {:};```
6. ```<parte de declaração de subrotinas> = {begin}; 7<declaração de procedimento> = {;};```
8. ```<parâmetros formais> = {;};```
9. ```<seção de parâmetros formais> = {;, )};```
10. ```<comando composto> = {.};```
11. ```<comando> = {;, end, else};```
12. ```<atribuição> = {;, end, else};```
13. ```<chamada de procedimento> = {;, end, else };```
14. ```<comando condicional 1> = {;, end, else};```
15. ```<comando repetitivo 1> = {;, end, else};```
16. ```<expressão> = {end, do, then, ;};```
17. ```<relação> = {+, -, end, do, then, ;, (, not};```
18. ```<expressão simples> = {+, -, end, do, then, ;, (, not }; 19<termo> = {+, -, end, do, then, ;, (, not };```
20. ```<fator> = {+, -, end, do, then, ;, (, not };```
21. ```<variável> = {+, -, end, do, then, ;, (, not , :=};```
22. ```<lista de expressão> = {)};```
23. ```<número> = {+, -, end, do, then, ;, (, not};```
24. ```<dígito> = {+, -, end, do, then, ;, (, not};```
25. ```<identificador> = {end, do, then, ;};```
26. ```<letra> = { end, do, then, ;, 1-9, a-z, A-Z};```

# Gramática

## Declarações
program : RES_PROGRAM IDENTIFICADOR SE_DELIMITADOR block

block : part_declare_variables compound_command
      | part_declare_subroutines compound_command
      | compound_command

part_declare_variables : declare_variables SE_DELIMITADOR
                       | part_declare_variables

declare_variables : type list_ids

list_ids : IDENTIFICADOR
         | SE_VIRGULA list_ids


part_declare_subroutines : declare_procedure
                         | part_declare_subroutines

declare_procedure : RES_PROCEDURE IDENTIFICADOR formal_parameters block
                  | RES_PROCEDURE IDENTIFICADOR block

formal_parameters : AP section_formal_parameters FP

section_formal_parameters : RES_VAR list_ids SE_DOIS_PONTOS IDENTIFICADOR
                          | list_ids SE_DOIS_PONTOS IDENTIFICADOR

## Comandos

compound_command : RES_BEGIN commands RES_END

commands : command
         | commands

command : assignment
        | calling_procedure
        | compound_command
        | command_conditional_1
        | command_loop_1

assignment : variable
           | expression

calling_procedure : IDENTIFICADOR
                  | IDENTIFICADOR AP list_expressions FP

command_conditional_1 : RES_IF expression RES_THEN command
                      | RES_IF expression RES_THEN command RES_ELSE command

command_loop_1 : RES_WHILE expression RES_DO command


## Expressões

expression : simple_expression
           | simple_expression relation simple_expression

relation : RES_IGUAL
         | RES_DIFERENTE                      
         | RES_MENOR                      
         | RES_MENOR_IGUAL                      
         | RES_MAIOR_IGUAL                      
         | RES_MAIOR

simple_expression : OPSOMA term simple_expression_1
                  | OPSUB term simple_expression_1
                  | OPSOMA term
                  | OPSUB term

simple_expression_1 : OPSOMA term
                    | OPSUB term
                    | RES_OR term
                    | simple_expression_1

term : factor term_1
     | factor

term_1 : OPMUL factor
       | RES_DIV factor
       | RES_AND factor 
       | term_1       

factor : variable
       | NUMERO
       | AP expression FP
       | RES_NOT factor

variable : IDENTIFICADOR
         | IDENTIFICADOR expression

list_expression : expression
                | expression expression_1

expression_1 : SE_VIRGULA expression
             | expression_1

   


