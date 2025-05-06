(set-option :produce-models true)

(define-const red Int 2)
(define-const orange Int 7)
(define-const yellow Int 3)

(declare-const g00 Int)
(declare-const g01 Int)
(declare-const g02 Int)
(declare-const g10 Int)
(declare-const g11 Int)
(declare-const g12 Int)
(declare-const g20 Int)
(declare-const g21 Int)
(declare-const g22 Int)

; row and col
(assert (and
    (distinct g00 g01 g02)
    (distinct g10 g11 g12)
    (distinct g20 g21 g22)

    (distinct g00 g10 g20)
    (distinct g01 g11 g21)
    (distinct g02 g12 g22)
))

; Cages
(assert (= 12 (+ g00 g10 g20)))
(assert (= 42 (* g01 g11 g21)))
(assert (= 5 (+ g21 g22)))

; Inequality
(assert (> g10 g00))

; Lock
(assert (= orange g02))


(define-fun valid ((x Int)) Bool (
    or (= x yellow) (= x orange) (= x red)
))
; Tile
(assert (and
    (valid g00)
    (valid g01)
    (valid g02)
    (valid g10)
    (valid g11)
    (valid g12)
    (valid g20)
    (valid g21)
    (valid g22)
))


(check-sat)
(get-model)
