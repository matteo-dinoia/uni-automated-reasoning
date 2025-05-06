(set-option :produce-models true)

(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const O1 Bool)
(declare-const O2 Bool)

(assert (= O1
    (or
        (and A B)
        (and
            (or B C)
            (and C B)
        )

    )
))

(assert (= O2
    (and
        B
        (or A C)
    )
))

(assert (not (= O1 O2)))

(check-sat)
