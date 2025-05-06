(set-option :produce-models true)

(declare-const A1 Bool)
(declare-const A2 Bool)
(declare-const A3 Bool)
(declare-const A4 Bool)

(declare-const B1 Bool)
(declare-const B2 Bool)
(declare-const B3 Bool)
(declare-const B4 Bool)

; 12 has one correct
(assert (xor A1 B2))
; 14 nothing is correct
(assert (not (or A1 B4 A4 B1)))
; 43 one correct but wrongly
(assert (or
    (and A4 (not B4) (not B3) (not A3))
    (and A3 (not B4) (not B3) (not A4))
    (and B4 (not A4) (not B3) (not A3))
    (and B3 (not B4) (not A4) (not A3))
))


; all sit
(assert (and
    (or A1 A2 A3 A4)
    (or B1 B2 B3 B4)
))

; not two sit
(assert (not (or
    (and A1 A2)
    (and A1 A3)
    (and A1 A4)
    (and A2 A3)
    (and A2 A4)
    (and A3 A4)

    (and B1 B2)
    (and B1 B3)
    (and B1 B4)
    (and B2 B3)
    (and B2 B4)
    (and B3 B4)
)))

; different
(assert (or (not A3) (not B2)))

; SOL 32
(check-sat)
(get-model)
