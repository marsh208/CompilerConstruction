Files that already pass:
-do_nothing.cc
-void_return_empty.cc

Already Implemented Typechecking Rules:
-Stm
  -SExp
  -SDecls
  -SReturn
-Exp
  -EInt
  -ETimes
  -EAss
  -ETyped

Rule Implemented for easy_add.cc:
-EPlus

Rule Implemented for ass_easy.cc:
-SInit


Still to be Implemented...
-Stm
  -SWhile
  -SBlock
  -SIfElse
-Exp
  -ETrue
  -EFalse
  -EId
  -EApp
  -EPIncr-- postincrement
  -EPDecr
  -EIncr -- preincrement
  -EDecr
  -ELt
  -EGt
  -ELtEq
  -EGtEq
  -EEq
  -ENEq
  -EAnd
  -EOr
