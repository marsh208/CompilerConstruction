(module
  (import "env" "printInt" (func $printInt (param i32)))
  (func
    $main
    (result i32)
    (local $ix$0 i32)
    (local $iy$0 i32)
    (i32.const 50)
    (local.set $ix$0)
    (local.get $ix$0)
    (i32.const 1)
    i32.add
    (local.set $ix$0)
    (local.get $ix$0)
    (i32.const 1)
    i32.sub
    (local.get $ix$0)
    i32.add
    (local.set $iy$0)
    (local.get $iy$0)
    return
  )
  (export "main" (func $main))
)
