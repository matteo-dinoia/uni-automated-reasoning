(set-option :produce-models true)

(declare-const X Int)
(declare-const Y Int)

(define-fun max ((a Int) (b Int)) Int (ite (> a b) a b))
(define-const maximum Int (max (* X Y Y) (* Y X X)))

; Sum is 9 of not negative
(assert (= 9 (+ X Y)))
(assert (and (>= X 0) (>= Y 0)))

; Bound result
(assert (>= maximum 0))
(assert (<= maximum 200))

(maximize maximum)

(check-sat)
(get-model)
(get-objectives)
