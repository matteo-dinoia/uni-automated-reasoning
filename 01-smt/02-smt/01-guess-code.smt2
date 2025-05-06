(set-option :produce-models true)
(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)

(assert (and (<= A 9) (>= A 0)))
(assert (and (<= B 9) (>= B 0)))
(assert (and (<= C 9) (>= C 0)))
(assert (and (<= D 9) (>= D 0)))

(assert (= (+ A C) D))
(assert (= (* A B) C))
(assert (= (- C B) B))
(assert (= (* A 4) D))

(assert (distinct A B C D))

(check-sat)
(get-model)
