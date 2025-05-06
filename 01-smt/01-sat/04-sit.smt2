(set-option :produce-models true)

(declare-const A1 Bool)
(declare-const A2 Bool)
(declare-const A3 Bool)

(declare-const B1 Bool)
(declare-const B2 Bool)
(declare-const B3 Bool)

(declare-const C1 Bool)
(declare-const C2 Bool)
(declare-const C3 Bool)

; not close
(assert (not (or
    (and A1 C2) (and A2 C1) (and A2 C3) (and A3 C2)
)))

; not first
(assert (not A1))

; not C -> B
(assert (not (or
    (and C1 B2) (and C2 B3)
)))

; all sit
(assert (and
    (or A1 A2 A3) (or B1 B2 B3) (or C1 C2 C3)
))

; not in same place
(assert (not (or
    (and A1 B1) (and A1 C1) (and B1 C1)
    (and A2 B2) (and A2 C2) (and B2 C2)
    (and A3 B3) (and A3 C3) (and B3 C3)
)))

(check-sat)
(get-model)
