(set-option :produce-models true)

; node, color #
(declare-const A1 Bool)
(declare-const B1 Bool)
(declare-const C1 Bool)
(declare-const D1 Bool)

(declare-const A2 Bool)
(declare-const B2 Bool)
(declare-const C2 Bool)
(declare-const D2 Bool)

(declare-const A3 Bool)
(declare-const B3 Bool)
(declare-const C3 Bool)
(declare-const D3 Bool)

; Connected not same color
(assert (not (or
    (or (and A1 D1) (and A2 D2) (and A3 D3))
    (or (and A1 B1) (and A2 B2) (and A3 B3))
    (or (and A1 C1) (and A2 C2) (and A3 C3))
    (or (and C1 D1) (and C2 D2) (and C3 D3))
    (or (and C1 B1) (and C2 B2) (and C3 B3))
)))

; all sit
(assert (and
    (or A1 A2 A3)
    (or B1 B2 B3)
    (or C1 C2 C3)
    (or D1 D2 D3)
))

; not two sit
(assert (not (or
    (and A1 A2)
    (and A1 A3)
    (and A2 A3)

    (and B1 B2)
    (and B1 B3)
    (and B2 B3)

    (and C1 C2)
    (and C1 C3)
    (and C2 C3)

    (and D1 D2)
    (and D1 D3)
    (and D2 D3)
)))

; A1 C2 B3 D3
(check-sat)
(get-model)
