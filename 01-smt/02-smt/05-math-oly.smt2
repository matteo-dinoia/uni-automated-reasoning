(set-option :produce-models true)
(declare-const A Int)
(declare-const B Int)
(declare-const C Int)

(assert (and (<= A 9) (>= A 0)))
(assert (and (<= B 9) (>= B 0)))
(assert (and (<= C 9) (>= C 0)))

(assert (not (= A 0)))
(assert (not (= C 0)))

(assert (= (mod (+ (* C 100) (* B 10) A) 4) 0))
(assert (= (mod (+ (* A 100) (* B 10) C) 4) 0))
(check-sat)
(get-model)