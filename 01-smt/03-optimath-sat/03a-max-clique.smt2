(set-option :produce-models true)

; Is inside
(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)

(assert (or (= A 1) (= A 0)))
(assert (or (= B 1) (= B 0)))
(assert (or (= C 1) (= C 0)))
(assert (or (= D 1) (= D 0)))

(assert (not (and (= B 1) (= D 1))))

(maximize (+ A B C D))

(check-sat)
(get-model)
(get-objectives)
