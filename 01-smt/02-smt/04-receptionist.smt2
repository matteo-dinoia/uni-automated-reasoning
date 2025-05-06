(set-option :produce-models true)
(set-option :produce-unsat-cores true)
(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)
(declare-const E Int)

(assert (distinct A B C D E))
(assert (and
	(and (>= A 1) (<= A 5))
	(and (>= B 1) (<= B 5))
	(and (>= C 1) (<= C 5))
	(and (>= D 1) (<= D 5))
	(and (>= E 1) (<= E 5))
))

; AAAAAAAAAA
(push 1)
(assert (! (<= A 2) :named gA))
(check-sat)
(get-model)

; BBBBBBBBBBB
(push 1)
(assert (! (= (mod B 2) 0) :named gB))
(check-sat)
(get-model)

; CCCCCCCCCC
(push 1)
(assert (! (= C 1)  :named gC))
(check-sat)
(get-model)

; DDDDDDDDDDDD
(push 1)
(assert (! (= (mod D 2) 0) :named gD))
(check-sat)
(get-unsat-core)

; EEEEEEEEEEEE
(push 1)
(assert (! (or (= E 1) (= E 5)) :named gE))
(check-sat)
(get-unsat-core)