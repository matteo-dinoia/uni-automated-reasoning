(set-option :produce-models true)

(declare-const A1 Bool)
(declare-const A2 Bool)
(declare-const A3 Bool)
(declare-const A4 Bool)

(declare-const B1 Bool)
(declare-const B2 Bool)
(declare-const B3 Bool)
(declare-const B4 Bool)

(declare-const C1 Bool)
(declare-const C2 Bool)
(declare-const C3 Bool)
(declare-const C4 Bool)

; even
(assert (or C2 C4))

; at least one differet (useless)

; Not adiacent
(assert (not (or
    (and A1 B1)
    (and B1 C1)

    (and A2 B2)
    (and B2 C2)

    (and A3 B3)
    (and B3 C3)

    (and A4 B4)
    (and B4 C4)
)))

; all sit
(assert (and
    (or A1 A2 A3 A4)
    (or B1 B2 B3 B4)
    (or C1 C2 C3 C4)
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

    (and C1 C2)
    (and C1 C3)
    (and C1 C4)
    (and C2 C3)
    (and C2 C4)
    (and C3 C4)
)))

(assert (not A2))

; 212 312 ...
(check-sat)
(get-model)
