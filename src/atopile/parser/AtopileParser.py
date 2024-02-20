# Generated from AtopileParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

if "." in __name__:
    from .AtopileParserBase import AtopileParserBase
else:
    from AtopileParserBase import AtopileParserBase

def serializedATN():
    return [
        4,1,80,341,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,1,0,1,0,5,0,97,8,0,10,0,12,0,100,9,0,1,0,1,0,1,1,1,1,3,1,106,
        8,1,1,2,1,2,1,2,5,2,111,8,2,10,2,12,2,114,9,2,1,2,3,2,117,8,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,131,8,3,1,4,1,
        4,1,5,1,5,1,5,1,5,3,5,139,8,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,
        7,4,7,150,8,7,11,7,12,7,151,1,7,1,7,3,7,156,8,7,1,8,1,8,1,8,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,169,8,9,10,9,12,9,172,9,9,1,10,1,
        10,3,10,176,8,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,186,
        8,11,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,
        1,15,1,15,1,15,3,15,203,8,15,1,16,1,16,1,16,1,17,1,17,1,17,3,17,
        211,8,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,4,21,222,8,
        21,11,21,12,21,223,1,22,1,22,1,22,3,22,229,8,22,1,23,1,23,1,23,1,
        24,1,24,1,24,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,246,
        8,26,10,26,12,26,249,9,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,257,
        8,27,10,27,12,27,260,9,27,1,28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,
        269,8,28,1,29,1,29,1,29,3,29,274,8,29,1,30,1,30,1,30,3,30,279,8,
        30,1,31,1,31,1,31,1,31,1,32,1,32,1,32,3,32,288,8,32,1,33,1,33,1,
        33,1,33,1,34,1,34,3,34,296,8,34,1,35,1,35,1,35,1,35,1,36,1,36,3,
        36,304,8,36,1,37,1,37,3,37,308,8,37,1,38,1,38,1,38,3,38,313,8,38,
        1,39,1,39,3,39,317,8,39,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,42,
        1,42,1,42,4,42,329,8,42,11,42,12,42,330,1,43,1,43,1,44,1,44,1,45,
        1,45,1,46,1,46,1,46,0,2,52,54,47,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,90,92,0,4,1,0,6,8,1,0,50,51,4,0,
        32,32,35,35,52,53,64,64,1,0,16,17,340,0,98,1,0,0,0,2,105,1,0,0,0,
        4,107,1,0,0,0,6,130,1,0,0,0,8,132,1,0,0,0,10,134,1,0,0,0,12,143,
        1,0,0,0,14,155,1,0,0,0,16,157,1,0,0,0,18,162,1,0,0,0,20,173,1,0,
        0,0,22,185,1,0,0,0,24,187,1,0,0,0,26,190,1,0,0,0,28,194,1,0,0,0,
        30,202,1,0,0,0,32,204,1,0,0,0,34,207,1,0,0,0,36,212,1,0,0,0,38,215,
        1,0,0,0,40,217,1,0,0,0,42,219,1,0,0,0,44,228,1,0,0,0,46,230,1,0,
        0,0,48,233,1,0,0,0,50,236,1,0,0,0,52,239,1,0,0,0,54,250,1,0,0,0,
        56,268,1,0,0,0,58,270,1,0,0,0,60,278,1,0,0,0,62,280,1,0,0,0,64,287,
        1,0,0,0,66,289,1,0,0,0,68,293,1,0,0,0,70,297,1,0,0,0,72,301,1,0,
        0,0,74,305,1,0,0,0,76,309,1,0,0,0,78,316,1,0,0,0,80,318,1,0,0,0,
        82,321,1,0,0,0,84,325,1,0,0,0,86,332,1,0,0,0,88,334,1,0,0,0,90,336,
        1,0,0,0,92,338,1,0,0,0,94,97,5,19,0,0,95,97,3,2,1,0,96,94,1,0,0,
        0,96,95,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,
        1,0,0,0,100,98,1,0,0,0,101,102,5,0,0,1,102,1,1,0,0,0,103,106,3,4,
        2,0,104,106,3,8,4,0,105,103,1,0,0,0,105,104,1,0,0,0,106,3,1,0,0,
        0,107,112,3,6,3,0,108,109,5,40,0,0,109,111,3,6,3,0,110,108,1,0,0,
        0,111,114,1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,116,1,0,0,
        0,114,112,1,0,0,0,115,117,5,40,0,0,116,115,1,0,0,0,116,117,1,0,0,
        0,117,118,1,0,0,0,118,119,5,19,0,0,119,5,1,0,0,0,120,131,3,18,9,
        0,121,131,3,16,8,0,122,131,3,20,10,0,123,131,3,28,14,0,124,131,3,
        26,13,0,125,131,3,34,17,0,126,131,3,32,16,0,127,131,3,38,19,0,128,
        131,3,40,20,0,129,131,3,24,12,0,130,120,1,0,0,0,130,121,1,0,0,0,
        130,122,1,0,0,0,130,123,1,0,0,0,130,124,1,0,0,0,130,125,1,0,0,0,
        130,126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,0,130,129,1,0,0,0,
        131,7,1,0,0,0,132,133,3,10,5,0,133,9,1,0,0,0,134,135,3,12,6,0,135,
        138,3,88,44,0,136,137,5,12,0,0,137,139,3,78,39,0,138,136,1,0,0,0,
        138,139,1,0,0,0,139,140,1,0,0,0,140,141,5,39,0,0,141,142,3,14,7,
        0,142,11,1,0,0,0,143,144,7,0,0,0,144,13,1,0,0,0,145,156,3,4,2,0,
        146,147,5,19,0,0,147,149,5,1,0,0,148,150,3,2,1,0,149,148,1,0,0,0,
        150,151,1,0,0,0,151,149,1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,
        153,154,5,2,0,0,154,156,1,0,0,0,155,145,1,0,0,0,155,146,1,0,0,0,
        156,15,1,0,0,0,157,158,5,13,0,0,158,159,3,78,39,0,159,160,5,12,0,
        0,160,161,3,90,45,0,161,17,1,0,0,0,162,163,5,12,0,0,163,164,3,90,
        45,0,164,165,5,13,0,0,165,170,3,78,39,0,166,167,5,38,0,0,167,169,
        3,78,39,0,168,166,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,170,171,
        1,0,0,0,171,19,1,0,0,0,172,170,1,0,0,0,173,175,3,78,39,0,174,176,
        3,80,40,0,175,174,1,0,0,0,175,176,1,0,0,0,176,177,1,0,0,0,177,178,
        5,42,0,0,178,179,3,22,11,0,179,21,1,0,0,0,180,186,3,90,45,0,181,
        186,3,36,18,0,182,186,3,64,32,0,183,186,3,78,39,0,184,186,3,52,26,
        0,185,180,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,185,183,1,0,0,
        0,185,184,1,0,0,0,186,23,1,0,0,0,187,188,3,78,39,0,188,189,3,80,
        40,0,189,25,1,0,0,0,190,191,3,78,39,0,191,192,5,65,0,0,192,193,3,
        78,39,0,193,27,1,0,0,0,194,195,3,30,15,0,195,196,5,54,0,0,196,197,
        3,30,15,0,197,29,1,0,0,0,198,203,3,78,39,0,199,203,3,82,41,0,200,
        203,3,32,16,0,201,203,3,34,17,0,202,198,1,0,0,0,202,199,1,0,0,0,
        202,200,1,0,0,0,202,201,1,0,0,0,203,31,1,0,0,0,204,205,5,10,0,0,
        205,206,3,88,44,0,206,33,1,0,0,0,207,210,5,9,0,0,208,211,3,88,44,
        0,209,211,3,86,43,0,210,208,1,0,0,0,210,209,1,0,0,0,211,35,1,0,0,
        0,212,213,5,11,0,0,213,214,3,78,39,0,214,37,1,0,0,0,215,216,3,90,
        45,0,216,39,1,0,0,0,217,218,3,42,21,0,218,41,1,0,0,0,219,221,3,52,
        26,0,220,222,3,44,22,0,221,220,1,0,0,0,222,223,1,0,0,0,223,221,1,
        0,0,0,223,224,1,0,0,0,224,43,1,0,0,0,225,229,3,46,23,0,226,229,3,
        48,24,0,227,229,3,50,25,0,228,225,1,0,0,0,228,226,1,0,0,0,228,227,
        1,0,0,0,229,45,1,0,0,0,230,231,5,57,0,0,231,232,3,52,26,0,232,47,
        1,0,0,0,233,234,5,58,0,0,234,235,3,52,26,0,235,49,1,0,0,0,236,237,
        5,78,0,0,237,238,3,52,26,0,238,51,1,0,0,0,239,240,6,26,-1,0,240,
        241,3,54,27,0,241,247,1,0,0,0,242,243,10,2,0,0,243,244,7,1,0,0,244,
        246,3,54,27,0,245,242,1,0,0,0,246,249,1,0,0,0,247,245,1,0,0,0,247,
        248,1,0,0,0,248,53,1,0,0,0,249,247,1,0,0,0,250,251,6,27,-1,0,251,
        252,3,56,28,0,252,258,1,0,0,0,253,254,10,2,0,0,254,255,7,2,0,0,255,
        257,3,56,28,0,256,253,1,0,0,0,257,260,1,0,0,0,258,256,1,0,0,0,258,
        259,1,0,0,0,259,55,1,0,0,0,260,258,1,0,0,0,261,262,5,50,0,0,262,
        269,3,56,28,0,263,264,5,51,0,0,264,269,3,56,28,0,265,266,5,54,0,
        0,266,269,3,56,28,0,267,269,3,58,29,0,268,261,1,0,0,0,268,263,1,
        0,0,0,268,265,1,0,0,0,268,267,1,0,0,0,269,57,1,0,0,0,270,273,3,60,
        30,0,271,272,5,41,0,0,272,274,3,56,28,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,59,1,0,0,0,275,279,3,78,39,0,276,279,3,64,32,0,277,279,
        3,62,31,0,278,275,1,0,0,0,278,276,1,0,0,0,278,277,1,0,0,0,279,61,
        1,0,0,0,280,281,5,36,0,0,281,282,3,52,26,0,282,283,5,37,0,0,283,
        63,1,0,0,0,284,288,3,66,33,0,285,288,3,70,35,0,286,288,3,72,36,0,
        287,284,1,0,0,0,287,285,1,0,0,0,287,286,1,0,0,0,288,65,1,0,0,0,289,
        290,3,68,34,0,290,291,5,15,0,0,291,292,3,68,34,0,292,67,1,0,0,0,
        293,295,5,4,0,0,294,296,3,88,44,0,295,294,1,0,0,0,295,296,1,0,0,
        0,296,69,1,0,0,0,297,298,3,74,37,0,298,299,5,29,0,0,299,300,3,76,
        38,0,300,71,1,0,0,0,301,303,5,4,0,0,302,304,3,88,44,0,303,302,1,
        0,0,0,303,304,1,0,0,0,304,73,1,0,0,0,305,307,5,4,0,0,306,308,3,88,
        44,0,307,306,1,0,0,0,307,308,1,0,0,0,308,75,1,0,0,0,309,312,5,4,
        0,0,310,313,5,32,0,0,311,313,3,88,44,0,312,310,1,0,0,0,312,311,1,
        0,0,0,312,313,1,0,0,0,313,77,1,0,0,0,314,317,3,84,42,0,315,317,3,
        88,44,0,316,314,1,0,0,0,316,315,1,0,0,0,317,79,1,0,0,0,318,319,5,
        39,0,0,319,320,3,78,39,0,320,81,1,0,0,0,321,322,3,78,39,0,322,323,
        5,33,0,0,323,324,3,86,43,0,324,83,1,0,0,0,325,328,3,88,44,0,326,
        327,5,33,0,0,327,329,3,88,44,0,328,326,1,0,0,0,329,330,1,0,0,0,330,
        328,1,0,0,0,330,331,1,0,0,0,331,85,1,0,0,0,332,333,5,4,0,0,333,87,
        1,0,0,0,334,335,5,20,0,0,335,89,1,0,0,0,336,337,5,3,0,0,337,91,1,
        0,0,0,338,339,7,3,0,0,339,93,1,0,0,0,28,96,98,105,112,116,130,138,
        151,155,170,175,185,202,210,223,228,247,258,268,273,278,287,295,
        303,307,312,316,330
    ]

class AtopileParser ( AtopileParserBase ):

    grammarFileName = "AtopileParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'component'", "'module'", 
                     "'interface'", "'pin'", "'signal'", "'new'", "'from'", 
                     "'import'", "'assert'", "'to'", "'True'", "'False'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'+/-'", "'\\u00B1'", "'%'", "'.'", "'...'", "'*'", 
                     "'('", "')'", "','", "':'", "';'", "'**'", "'='", "'['", 
                     "']'", "'|'", "'^'", "'&'", "'<<'", "'>>'", "'+'", 
                     "'-'", "'/'", "'//'", "'~'", "'{'", "'}'", "'<'", "'>'", 
                     "'=='", "'>='", "'<='", "'<>'", "'!='", "'@'", "'->'", 
                     "'+='", "'-='", "'*='", "'@='", "'/='", "'&='", "'|='", 
                     "'^='", "'<<='", "'>>='", "'**='", "'//='", "'within'" ]

    symbolicNames = [ "<INVALID>", "INDENT", "DEDENT", "STRING", "NUMBER", 
                      "INTEGER", "COMPONENT", "MODULE", "INTERFACE", "PIN", 
                      "SIGNAL", "NEW", "FROM", "IMPORT", "ASSERT", "TO", 
                      "TRUE", "FALSE", "ASSERTION_STRING", "NEWLINE", "NAME", 
                      "STRING_LITERAL", "BYTES_LITERAL", "DECIMAL_INTEGER", 
                      "OCT_INTEGER", "HEX_INTEGER", "BIN_INTEGER", "FLOAT_NUMBER", 
                      "IMAG_NUMBER", "PLUS_OR_MINUS", "PLUS_SLASH_MINUS", 
                      "PLUS_MINUS_SIGN", "PERCENT", "DOT", "ELLIPSIS", "STAR", 
                      "OPEN_PAREN", "CLOSE_PAREN", "COMMA", "COLON", "SEMI_COLON", 
                      "POWER", "ASSIGN", "OPEN_BRACK", "CLOSE_BRACK", "OR_OP", 
                      "XOR", "AND_OP", "LEFT_SHIFT", "RIGHT_SHIFT", "ADD", 
                      "MINUS", "DIV", "IDIV", "NOT_OP", "OPEN_BRACE", "CLOSE_BRACE", 
                      "LESS_THAN", "GREATER_THAN", "EQUALS", "GT_EQ", "LT_EQ", 
                      "NOT_EQ_1", "NOT_EQ_2", "AT", "ARROW", "ADD_ASSIGN", 
                      "SUB_ASSIGN", "MULT_ASSIGN", "AT_ASSIGN", "DIV_ASSIGN", 
                      "AND_ASSIGN", "OR_ASSIGN", "XOR_ASSIGN", "LEFT_SHIFT_ASSIGN", 
                      "RIGHT_SHIFT_ASSIGN", "POWER_ASSIGN", "IDIV_ASSIGN", 
                      "WITHIN", "SKIP_", "UNKNOWN_CHAR" ]

    RULE_file_input = 0
    RULE_stmt = 1
    RULE_simple_stmts = 2
    RULE_simple_stmt = 3
    RULE_compound_stmt = 4
    RULE_blockdef = 5
    RULE_blocktype = 6
    RULE_block = 7
    RULE_dep_import_stmt = 8
    RULE_import_stmt = 9
    RULE_assign_stmt = 10
    RULE_assignable = 11
    RULE_declaration_stmt = 12
    RULE_retype_stmt = 13
    RULE_connect_stmt = 14
    RULE_connectable = 15
    RULE_signaldef_stmt = 16
    RULE_pindef_stmt = 17
    RULE_new_stmt = 18
    RULE_string_stmt = 19
    RULE_assert_stmt = 20
    RULE_comparison = 21
    RULE_compare_op_pair = 22
    RULE_lt_arithmetic_or = 23
    RULE_gt_arithmetic_or = 24
    RULE_in_arithmetic_or = 25
    RULE_arithmetic_expression = 26
    RULE_term = 27
    RULE_factor = 28
    RULE_power = 29
    RULE_atom = 30
    RULE_arithmetic_group = 31
    RULE_literal_physical = 32
    RULE_bound_quantity = 33
    RULE_quantity_end = 34
    RULE_bilateral_quantity = 35
    RULE_implicit_quantity = 36
    RULE_bilateral_nominal = 37
    RULE_bilateral_tolerance = 38
    RULE_name_or_attr = 39
    RULE_type_info = 40
    RULE_numerical_pin_ref = 41
    RULE_attr = 42
    RULE_totally_an_integer = 43
    RULE_name = 44
    RULE_string = 45
    RULE_boolean_ = 46

    ruleNames =  [ "file_input", "stmt", "simple_stmts", "simple_stmt", 
                   "compound_stmt", "blockdef", "blocktype", "block", "dep_import_stmt", 
                   "import_stmt", "assign_stmt", "assignable", "declaration_stmt", 
                   "retype_stmt", "connect_stmt", "connectable", "signaldef_stmt", 
                   "pindef_stmt", "new_stmt", "string_stmt", "assert_stmt", 
                   "comparison", "compare_op_pair", "lt_arithmetic_or", 
                   "gt_arithmetic_or", "in_arithmetic_or", "arithmetic_expression", 
                   "term", "factor", "power", "atom", "arithmetic_group", 
                   "literal_physical", "bound_quantity", "quantity_end", 
                   "bilateral_quantity", "implicit_quantity", "bilateral_nominal", 
                   "bilateral_tolerance", "name_or_attr", "type_info", "numerical_pin_ref", 
                   "attr", "totally_an_integer", "name", "string", "boolean_" ]

    EOF = Token.EOF
    INDENT=1
    DEDENT=2
    STRING=3
    NUMBER=4
    INTEGER=5
    COMPONENT=6
    MODULE=7
    INTERFACE=8
    PIN=9
    SIGNAL=10
    NEW=11
    FROM=12
    IMPORT=13
    ASSERT=14
    TO=15
    TRUE=16
    FALSE=17
    ASSERTION_STRING=18
    NEWLINE=19
    NAME=20
    STRING_LITERAL=21
    BYTES_LITERAL=22
    DECIMAL_INTEGER=23
    OCT_INTEGER=24
    HEX_INTEGER=25
    BIN_INTEGER=26
    FLOAT_NUMBER=27
    IMAG_NUMBER=28
    PLUS_OR_MINUS=29
    PLUS_SLASH_MINUS=30
    PLUS_MINUS_SIGN=31
    PERCENT=32
    DOT=33
    ELLIPSIS=34
    STAR=35
    OPEN_PAREN=36
    CLOSE_PAREN=37
    COMMA=38
    COLON=39
    SEMI_COLON=40
    POWER=41
    ASSIGN=42
    OPEN_BRACK=43
    CLOSE_BRACK=44
    OR_OP=45
    XOR=46
    AND_OP=47
    LEFT_SHIFT=48
    RIGHT_SHIFT=49
    ADD=50
    MINUS=51
    DIV=52
    IDIV=53
    NOT_OP=54
    OPEN_BRACE=55
    CLOSE_BRACE=56
    LESS_THAN=57
    GREATER_THAN=58
    EQUALS=59
    GT_EQ=60
    LT_EQ=61
    NOT_EQ_1=62
    NOT_EQ_2=63
    AT=64
    ARROW=65
    ADD_ASSIGN=66
    SUB_ASSIGN=67
    MULT_ASSIGN=68
    AT_ASSIGN=69
    DIV_ASSIGN=70
    AND_ASSIGN=71
    OR_ASSIGN=72
    XOR_ASSIGN=73
    LEFT_SHIFT_ASSIGN=74
    RIGHT_SHIFT_ASSIGN=75
    POWER_ASSIGN=76
    IDIV_ASSIGN=77
    WITHIN=78
    SKIP_=79
    UNKNOWN_CHAR=80

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class File_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(AtopileParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(AtopileParser.NEWLINE)
            else:
                return self.getToken(AtopileParser.NEWLINE, i)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.StmtContext)
            else:
                return self.getTypedRuleContext(AtopileParser.StmtContext,i)


        def getRuleIndex(self):
            return AtopileParser.RULE_file_input

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile_input" ):
                return visitor.visitFile_input(self)
            else:
                return visitor.visitChildren(self)




    def file_input(self):

        localctx = AtopileParser.File_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 21392166951073752) != 0):
                self.state = 96
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [19]:
                    self.state = 94
                    self.match(AtopileParser.NEWLINE)
                    pass
                elif token in [3, 4, 6, 7, 8, 9, 10, 12, 13, 20, 36, 50, 51, 54]:
                    self.state = 95
                    self.stmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 101
            self.match(AtopileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(AtopileParser.Simple_stmtsContext,0)


        def compound_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Compound_stmtContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = AtopileParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 105
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 9, 10, 12, 13, 20, 36, 50, 51, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 103
                self.simple_stmts()
                pass
            elif token in [6, 7, 8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.compound_stmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.Simple_stmtContext)
            else:
                return self.getTypedRuleContext(AtopileParser.Simple_stmtContext,i)


        def NEWLINE(self):
            return self.getToken(AtopileParser.NEWLINE, 0)

        def SEMI_COLON(self, i:int=None):
            if i is None:
                return self.getTokens(AtopileParser.SEMI_COLON)
            else:
                return self.getToken(AtopileParser.SEMI_COLON, i)

        def getRuleIndex(self):
            return AtopileParser.RULE_simple_stmts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmts" ):
                return visitor.visitSimple_stmts(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmts(self):

        localctx = AtopileParser.Simple_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.simple_stmt()
            self.state = 112
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 108
                    self.match(AtopileParser.SEMI_COLON)
                    self.state = 109
                    self.simple_stmt() 
                self.state = 114
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 115
                self.match(AtopileParser.SEMI_COLON)


            self.state = 118
            self.match(AtopileParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def import_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Import_stmtContext,0)


        def dep_import_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Dep_import_stmtContext,0)


        def assign_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Assign_stmtContext,0)


        def connect_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Connect_stmtContext,0)


        def retype_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Retype_stmtContext,0)


        def pindef_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Pindef_stmtContext,0)


        def signaldef_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Signaldef_stmtContext,0)


        def string_stmt(self):
            return self.getTypedRuleContext(AtopileParser.String_stmtContext,0)


        def assert_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Assert_stmtContext,0)


        def declaration_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Declaration_stmtContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_simple_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_stmt" ):
                return visitor.visitSimple_stmt(self)
            else:
                return visitor.visitChildren(self)




    def simple_stmt(self):

        localctx = AtopileParser.Simple_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_stmt)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.import_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 121
                self.dep_import_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 122
                self.assign_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 123
                self.connect_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 124
                self.retype_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 125
                self.pindef_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 126
                self.signaldef_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 127
                self.string_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 128
                self.assert_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 129
                self.declaration_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compound_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockdef(self):
            return self.getTypedRuleContext(AtopileParser.BlockdefContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_compound_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompound_stmt" ):
                return visitor.visitCompound_stmt(self)
            else:
                return visitor.visitChildren(self)




    def compound_stmt(self):

        localctx = AtopileParser.Compound_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_compound_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.blockdef()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockdefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blocktype(self):
            return self.getTypedRuleContext(AtopileParser.BlocktypeContext,0)


        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def COLON(self):
            return self.getToken(AtopileParser.COLON, 0)

        def block(self):
            return self.getTypedRuleContext(AtopileParser.BlockContext,0)


        def FROM(self):
            return self.getToken(AtopileParser.FROM, 0)

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_blockdef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockdef" ):
                return visitor.visitBlockdef(self)
            else:
                return visitor.visitChildren(self)




    def blockdef(self):

        localctx = AtopileParser.BlockdefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_blockdef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.blocktype()
            self.state = 135
            self.name()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 136
                self.match(AtopileParser.FROM)
                self.state = 137
                self.name_or_attr()


            self.state = 140
            self.match(AtopileParser.COLON)
            self.state = 141
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocktypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPONENT(self):
            return self.getToken(AtopileParser.COMPONENT, 0)

        def MODULE(self):
            return self.getToken(AtopileParser.MODULE, 0)

        def INTERFACE(self):
            return self.getToken(AtopileParser.INTERFACE, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_blocktype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlocktype" ):
                return visitor.visitBlocktype(self)
            else:
                return visitor.visitChildren(self)




    def blocktype(self):

        localctx = AtopileParser.BlocktypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_blocktype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 448) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_stmts(self):
            return self.getTypedRuleContext(AtopileParser.Simple_stmtsContext,0)


        def NEWLINE(self):
            return self.getToken(AtopileParser.NEWLINE, 0)

        def INDENT(self):
            return self.getToken(AtopileParser.INDENT, 0)

        def DEDENT(self):
            return self.getToken(AtopileParser.DEDENT, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.StmtContext)
            else:
                return self.getTypedRuleContext(AtopileParser.StmtContext,i)


        def getRuleIndex(self):
            return AtopileParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = AtopileParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4, 9, 10, 12, 13, 20, 36, 50, 51, 54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.simple_stmts()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.match(AtopileParser.NEWLINE)
                self.state = 147
                self.match(AtopileParser.INDENT)
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 148
                    self.stmt()
                    self.state = 151 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 21392166950549464) != 0)):
                        break

                self.state = 153
                self.match(AtopileParser.DEDENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dep_import_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(AtopileParser.IMPORT, 0)

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def FROM(self):
            return self.getToken(AtopileParser.FROM, 0)

        def string(self):
            return self.getTypedRuleContext(AtopileParser.StringContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_dep_import_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDep_import_stmt" ):
                return visitor.visitDep_import_stmt(self)
            else:
                return visitor.visitChildren(self)




    def dep_import_stmt(self):

        localctx = AtopileParser.Dep_import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dep_import_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(AtopileParser.IMPORT)
            self.state = 158
            self.name_or_attr()
            self.state = 159
            self.match(AtopileParser.FROM)
            self.state = 160
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(AtopileParser.FROM, 0)

        def string(self):
            return self.getTypedRuleContext(AtopileParser.StringContext,0)


        def IMPORT(self):
            return self.getToken(AtopileParser.IMPORT, 0)

        def name_or_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.Name_or_attrContext)
            else:
                return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(AtopileParser.COMMA)
            else:
                return self.getToken(AtopileParser.COMMA, i)

        def getRuleIndex(self):
            return AtopileParser.RULE_import_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImport_stmt" ):
                return visitor.visitImport_stmt(self)
            else:
                return visitor.visitChildren(self)




    def import_stmt(self):

        localctx = AtopileParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_import_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(AtopileParser.FROM)
            self.state = 163
            self.string()
            self.state = 164
            self.match(AtopileParser.IMPORT)
            self.state = 165
            self.name_or_attr()
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38:
                self.state = 166
                self.match(AtopileParser.COMMA)
                self.state = 167
                self.name_or_attr()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def ASSIGN(self):
            return self.getToken(AtopileParser.ASSIGN, 0)

        def assignable(self):
            return self.getTypedRuleContext(AtopileParser.AssignableContext,0)


        def type_info(self):
            return self.getTypedRuleContext(AtopileParser.Type_infoContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_assign_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_stmt" ):
                return visitor.visitAssign_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assign_stmt(self):

        localctx = AtopileParser.Assign_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_assign_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.name_or_attr()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 174
                self.type_info()


            self.state = 177
            self.match(AtopileParser.ASSIGN)
            self.state = 178
            self.assignable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(AtopileParser.StringContext,0)


        def new_stmt(self):
            return self.getTypedRuleContext(AtopileParser.New_stmtContext,0)


        def literal_physical(self):
            return self.getTypedRuleContext(AtopileParser.Literal_physicalContext,0)


        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_assignable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignable" ):
                return visitor.visitAssignable(self)
            else:
                return visitor.visitChildren(self)




    def assignable(self):

        localctx = AtopileParser.AssignableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_assignable)
        try:
            self.state = 185
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.string()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.new_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.literal_physical()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.name_or_attr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.arithmetic_expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def type_info(self):
            return self.getTypedRuleContext(AtopileParser.Type_infoContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_declaration_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration_stmt" ):
                return visitor.visitDeclaration_stmt(self)
            else:
                return visitor.visitChildren(self)




    def declaration_stmt(self):

        localctx = AtopileParser.Declaration_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaration_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.name_or_attr()
            self.state = 188
            self.type_info()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Retype_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.Name_or_attrContext)
            else:
                return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,i)


        def ARROW(self):
            return self.getToken(AtopileParser.ARROW, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_retype_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetype_stmt" ):
                return visitor.visitRetype_stmt(self)
            else:
                return visitor.visitChildren(self)




    def retype_stmt(self):

        localctx = AtopileParser.Retype_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_retype_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.name_or_attr()
            self.state = 191
            self.match(AtopileParser.ARROW)
            self.state = 192
            self.name_or_attr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Connect_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connectable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.ConnectableContext)
            else:
                return self.getTypedRuleContext(AtopileParser.ConnectableContext,i)


        def NOT_OP(self):
            return self.getToken(AtopileParser.NOT_OP, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_connect_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnect_stmt" ):
                return visitor.visitConnect_stmt(self)
            else:
                return visitor.visitChildren(self)




    def connect_stmt(self):

        localctx = AtopileParser.Connect_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_connect_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.connectable()
            self.state = 195
            self.match(AtopileParser.NOT_OP)
            self.state = 196
            self.connectable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConnectableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def numerical_pin_ref(self):
            return self.getTypedRuleContext(AtopileParser.Numerical_pin_refContext,0)


        def signaldef_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Signaldef_stmtContext,0)


        def pindef_stmt(self):
            return self.getTypedRuleContext(AtopileParser.Pindef_stmtContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_connectable

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConnectable" ):
                return visitor.visitConnectable(self)
            else:
                return visitor.visitChildren(self)




    def connectable(self):

        localctx = AtopileParser.ConnectableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_connectable)
        try:
            self.state = 202
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.name_or_attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.numerical_pin_ref()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 200
                self.signaldef_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self.pindef_stmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Signaldef_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNAL(self):
            return self.getToken(AtopileParser.SIGNAL, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_signaldef_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignaldef_stmt" ):
                return visitor.visitSignaldef_stmt(self)
            else:
                return visitor.visitChildren(self)




    def signaldef_stmt(self):

        localctx = AtopileParser.Signaldef_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_signaldef_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(AtopileParser.SIGNAL)
            self.state = 205
            self.name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pindef_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIN(self):
            return self.getToken(AtopileParser.PIN, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def totally_an_integer(self):
            return self.getTypedRuleContext(AtopileParser.Totally_an_integerContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_pindef_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPindef_stmt" ):
                return visitor.visitPindef_stmt(self)
            else:
                return visitor.visitChildren(self)




    def pindef_stmt(self):

        localctx = AtopileParser.Pindef_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pindef_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(AtopileParser.PIN)
            self.state = 210
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 208
                self.name()
                pass
            elif token in [4]:
                self.state = 209
                self.totally_an_integer()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class New_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(AtopileParser.NEW, 0)

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_new_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNew_stmt" ):
                return visitor.visitNew_stmt(self)
            else:
                return visitor.visitChildren(self)




    def new_stmt(self):

        localctx = AtopileParser.New_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_new_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(AtopileParser.NEW)
            self.state = 213
            self.name_or_attr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string(self):
            return self.getTypedRuleContext(AtopileParser.StringContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_string_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_stmt" ):
                return visitor.visitString_stmt(self)
            else:
                return visitor.visitChildren(self)




    def string_stmt(self):

        localctx = AtopileParser.String_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_string_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.string()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assert_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self):
            return self.getTypedRuleContext(AtopileParser.ComparisonContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_assert_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssert_stmt" ):
                return visitor.visitAssert_stmt(self)
            else:
                return visitor.visitChildren(self)




    def assert_stmt(self):

        localctx = AtopileParser.Assert_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assert_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.comparison()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def compare_op_pair(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.Compare_op_pairContext)
            else:
                return self.getTypedRuleContext(AtopileParser.Compare_op_pairContext,i)


        def getRuleIndex(self):
            return AtopileParser.RULE_comparison

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = AtopileParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.arithmetic_expression(0)
            self.state = 221 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 220
                self.compare_op_pair()
                self.state = 223 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 57)) & ~0x3f) == 0 and ((1 << (_la - 57)) & 2097155) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compare_op_pairContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lt_arithmetic_or(self):
            return self.getTypedRuleContext(AtopileParser.Lt_arithmetic_orContext,0)


        def gt_arithmetic_or(self):
            return self.getTypedRuleContext(AtopileParser.Gt_arithmetic_orContext,0)


        def in_arithmetic_or(self):
            return self.getTypedRuleContext(AtopileParser.In_arithmetic_orContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_compare_op_pair

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare_op_pair" ):
                return visitor.visitCompare_op_pair(self)
            else:
                return visitor.visitChildren(self)




    def compare_op_pair(self):

        localctx = AtopileParser.Compare_op_pairContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_compare_op_pair)
        try:
            self.state = 228
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [57]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.lt_arithmetic_or()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.gt_arithmetic_or()
                pass
            elif token in [78]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.in_arithmetic_or()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lt_arithmetic_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LESS_THAN(self):
            return self.getToken(AtopileParser.LESS_THAN, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_lt_arithmetic_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLt_arithmetic_or" ):
                return visitor.visitLt_arithmetic_or(self)
            else:
                return visitor.visitChildren(self)




    def lt_arithmetic_or(self):

        localctx = AtopileParser.Lt_arithmetic_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_lt_arithmetic_or)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(AtopileParser.LESS_THAN)
            self.state = 231
            self.arithmetic_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gt_arithmetic_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GREATER_THAN(self):
            return self.getToken(AtopileParser.GREATER_THAN, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_gt_arithmetic_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGt_arithmetic_or" ):
                return visitor.visitGt_arithmetic_or(self)
            else:
                return visitor.visitChildren(self)




    def gt_arithmetic_or(self):

        localctx = AtopileParser.Gt_arithmetic_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_gt_arithmetic_or)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(AtopileParser.GREATER_THAN)
            self.state = 234
            self.arithmetic_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_arithmetic_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITHIN(self):
            return self.getToken(AtopileParser.WITHIN, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_in_arithmetic_or

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIn_arithmetic_or" ):
                return visitor.visitIn_arithmetic_or(self)
            else:
                return visitor.visitChildren(self)




    def in_arithmetic_or(self):

        localctx = AtopileParser.In_arithmetic_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_in_arithmetic_or)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(AtopileParser.WITHIN)
            self.state = 237
            self.arithmetic_expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(AtopileParser.TermContext,0)


        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def ADD(self):
            return self.getToken(AtopileParser.ADD, 0)

        def MINUS(self):
            return self.getToken(AtopileParser.MINUS, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_arithmetic_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression" ):
                return visitor.visitArithmetic_expression(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AtopileParser.Arithmetic_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_arithmetic_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.term(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 247
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AtopileParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                    self.state = 242
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 243
                    _la = self._input.LA(1)
                    if not(_la==50 or _la==51):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 244
                    self.term(0) 
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(AtopileParser.FactorContext,0)


        def term(self):
            return self.getTypedRuleContext(AtopileParser.TermContext,0)


        def STAR(self):
            return self.getToken(AtopileParser.STAR, 0)

        def DIV(self):
            return self.getToken(AtopileParser.DIV, 0)

        def IDIV(self):
            return self.getToken(AtopileParser.IDIV, 0)

        def PERCENT(self):
            return self.getToken(AtopileParser.PERCENT, 0)

        def AT(self):
            return self.getToken(AtopileParser.AT, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)



    def term(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AtopileParser.TermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_term, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.factor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AtopileParser.TermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_term)
                    self.state = 253
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 254
                    _la = self._input.LA(1)
                    if not(((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 4298113033) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 255
                    self.factor() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(AtopileParser.ADD, 0)

        def factor(self):
            return self.getTypedRuleContext(AtopileParser.FactorContext,0)


        def MINUS(self):
            return self.getToken(AtopileParser.MINUS, 0)

        def NOT_OP(self):
            return self.getToken(AtopileParser.NOT_OP, 0)

        def power(self):
            return self.getTypedRuleContext(AtopileParser.PowerContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = AtopileParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_factor)
        try:
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.match(AtopileParser.ADD)
                self.state = 262
                self.factor()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self.match(AtopileParser.MINUS)
                self.state = 264
                self.factor()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(AtopileParser.NOT_OP)
                self.state = 266
                self.factor()
                pass
            elif token in [4, 20, 36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 267
                self.power()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(AtopileParser.AtomContext,0)


        def POWER(self):
            return self.getToken(AtopileParser.POWER, 0)

        def factor(self):
            return self.getTypedRuleContext(AtopileParser.FactorContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_power

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)




    def power(self):

        localctx = AtopileParser.PowerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_power)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.atom()
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(AtopileParser.POWER)
                self.state = 272
                self.factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def literal_physical(self):
            return self.getTypedRuleContext(AtopileParser.Literal_physicalContext,0)


        def arithmetic_group(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_groupContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = AtopileParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_atom)
        try:
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.name_or_attr()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.literal_physical()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.arithmetic_group()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_groupContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_PAREN(self):
            return self.getToken(AtopileParser.OPEN_PAREN, 0)

        def arithmetic_expression(self):
            return self.getTypedRuleContext(AtopileParser.Arithmetic_expressionContext,0)


        def CLOSE_PAREN(self):
            return self.getToken(AtopileParser.CLOSE_PAREN, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_arithmetic_group

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_group" ):
                return visitor.visitArithmetic_group(self)
            else:
                return visitor.visitChildren(self)




    def arithmetic_group(self):

        localctx = AtopileParser.Arithmetic_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arithmetic_group)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(AtopileParser.OPEN_PAREN)
            self.state = 281
            self.arithmetic_expression(0)
            self.state = 282
            self.match(AtopileParser.CLOSE_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Literal_physicalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bound_quantity(self):
            return self.getTypedRuleContext(AtopileParser.Bound_quantityContext,0)


        def bilateral_quantity(self):
            return self.getTypedRuleContext(AtopileParser.Bilateral_quantityContext,0)


        def implicit_quantity(self):
            return self.getTypedRuleContext(AtopileParser.Implicit_quantityContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_literal_physical

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral_physical" ):
                return visitor.visitLiteral_physical(self)
            else:
                return visitor.visitChildren(self)




    def literal_physical(self):

        localctx = AtopileParser.Literal_physicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_literal_physical)
        try:
            self.state = 287
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.bound_quantity()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 285
                self.bilateral_quantity()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 286
                self.implicit_quantity()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bound_quantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def quantity_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.Quantity_endContext)
            else:
                return self.getTypedRuleContext(AtopileParser.Quantity_endContext,i)


        def TO(self):
            return self.getToken(AtopileParser.TO, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_bound_quantity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBound_quantity" ):
                return visitor.visitBound_quantity(self)
            else:
                return visitor.visitChildren(self)




    def bound_quantity(self):

        localctx = AtopileParser.Bound_quantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_bound_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.quantity_end()
            self.state = 290
            self.match(AtopileParser.TO)
            self.state = 291
            self.quantity_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Quantity_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AtopileParser.NUMBER, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_quantity_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuantity_end" ):
                return visitor.visitQuantity_end(self)
            else:
                return visitor.visitChildren(self)




    def quantity_end(self):

        localctx = AtopileParser.Quantity_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_quantity_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(AtopileParser.NUMBER)
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 294
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bilateral_quantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bilateral_nominal(self):
            return self.getTypedRuleContext(AtopileParser.Bilateral_nominalContext,0)


        def PLUS_OR_MINUS(self):
            return self.getToken(AtopileParser.PLUS_OR_MINUS, 0)

        def bilateral_tolerance(self):
            return self.getTypedRuleContext(AtopileParser.Bilateral_toleranceContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_bilateral_quantity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBilateral_quantity" ):
                return visitor.visitBilateral_quantity(self)
            else:
                return visitor.visitChildren(self)




    def bilateral_quantity(self):

        localctx = AtopileParser.Bilateral_quantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_bilateral_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.bilateral_nominal()
            self.state = 298
            self.match(AtopileParser.PLUS_OR_MINUS)
            self.state = 299
            self.bilateral_tolerance()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Implicit_quantityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AtopileParser.NUMBER, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_implicit_quantity

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_quantity" ):
                return visitor.visitImplicit_quantity(self)
            else:
                return visitor.visitChildren(self)




    def implicit_quantity(self):

        localctx = AtopileParser.Implicit_quantityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_implicit_quantity)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(AtopileParser.NUMBER)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 302
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bilateral_nominalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AtopileParser.NUMBER, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_bilateral_nominal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBilateral_nominal" ):
                return visitor.visitBilateral_nominal(self)
            else:
                return visitor.visitChildren(self)




    def bilateral_nominal(self):

        localctx = AtopileParser.Bilateral_nominalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_bilateral_nominal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.match(AtopileParser.NUMBER)
            self.state = 307
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 306
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bilateral_toleranceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AtopileParser.NUMBER, 0)

        def PERCENT(self):
            return self.getToken(AtopileParser.PERCENT, 0)

        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_bilateral_tolerance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBilateral_tolerance" ):
                return visitor.visitBilateral_tolerance(self)
            else:
                return visitor.visitChildren(self)




    def bilateral_tolerance(self):

        localctx = AtopileParser.Bilateral_toleranceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_bilateral_tolerance)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(AtopileParser.NUMBER)
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 310
                self.match(AtopileParser.PERCENT)

            elif la_ == 2:
                self.state = 311
                self.name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_or_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self):
            return self.getTypedRuleContext(AtopileParser.AttrContext,0)


        def name(self):
            return self.getTypedRuleContext(AtopileParser.NameContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_name_or_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_or_attr" ):
                return visitor.visitName_or_attr(self)
            else:
                return visitor.visitChildren(self)




    def name_or_attr(self):

        localctx = AtopileParser.Name_or_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_name_or_attr)
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.attr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.name()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(AtopileParser.COLON, 0)

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_type_info

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_info" ):
                return visitor.visitType_info(self)
            else:
                return visitor.visitChildren(self)




    def type_info(self):

        localctx = AtopileParser.Type_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_type_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(AtopileParser.COLON)
            self.state = 319
            self.name_or_attr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numerical_pin_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_or_attr(self):
            return self.getTypedRuleContext(AtopileParser.Name_or_attrContext,0)


        def DOT(self):
            return self.getToken(AtopileParser.DOT, 0)

        def totally_an_integer(self):
            return self.getTypedRuleContext(AtopileParser.Totally_an_integerContext,0)


        def getRuleIndex(self):
            return AtopileParser.RULE_numerical_pin_ref

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumerical_pin_ref" ):
                return visitor.visitNumerical_pin_ref(self)
            else:
                return visitor.visitChildren(self)




    def numerical_pin_ref(self):

        localctx = AtopileParser.Numerical_pin_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_numerical_pin_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 321
            self.name_or_attr()
            self.state = 322
            self.match(AtopileParser.DOT)
            self.state = 323
            self.totally_an_integer()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AtopileParser.NameContext)
            else:
                return self.getTypedRuleContext(AtopileParser.NameContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(AtopileParser.DOT)
            else:
                return self.getToken(AtopileParser.DOT, i)

        def getRuleIndex(self):
            return AtopileParser.RULE_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = AtopileParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.name()
            self.state = 328 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 326
                    self.match(AtopileParser.DOT)
                    self.state = 327
                    self.name()

                else:
                    raise NoViableAltException(self)
                self.state = 330 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Totally_an_integerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(AtopileParser.NUMBER, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_totally_an_integer

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTotally_an_integer" ):
                return visitor.visitTotally_an_integer(self)
            else:
                return visitor.visitChildren(self)




    def totally_an_integer(self):

        localctx = AtopileParser.Totally_an_integerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_totally_an_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(AtopileParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(AtopileParser.NAME, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName" ):
                return visitor.visitName(self)
            else:
                return visitor.visitChildren(self)




    def name(self):

        localctx = AtopileParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(AtopileParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(AtopileParser.STRING, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_string

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)




    def string(self):

        localctx = AtopileParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(AtopileParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUE(self):
            return self.getToken(AtopileParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(AtopileParser.FALSE, 0)

        def getRuleIndex(self):
            return AtopileParser.RULE_boolean_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolean_" ):
                return visitor.visitBoolean_(self)
            else:
                return visitor.visitChildren(self)




    def boolean_(self):

        localctx = AtopileParser.Boolean_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_boolean_)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[26] = self.arithmetic_expression_sempred
        self._predicates[27] = self.term_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def term_sempred(self, localctx:TermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




