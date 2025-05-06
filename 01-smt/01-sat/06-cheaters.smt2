(set-option :produce-models true)

; Means it cheated
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)

; B-> not C
(assert (or (not B) (not C)))

; A-> C
(assert (or (not A) C))

; not C-> A or B
(assert (or C A B))

; for finding other
(assert (not (or B)))
(assert A)

; A,C    B     C
(check-sat)
(get-model)
