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

(assert-soft (= A 0) :weight 1 :id penality)
(assert-soft (= B 0) :weight 1 :id penality)
(assert-soft (= C 0) :weight 1 :id penality)
(assert-soft (= D 0) :weight 1 :id penality)

(maximize penality)

(check-sat)
(get-model)
