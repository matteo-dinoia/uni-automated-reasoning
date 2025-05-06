(set-option :produce-models true)

; Distance from G
(declare-const A Int)
(declare-const B Int)
(declare-const C Int)
(declare-const D Int)
(declare-const E Int)
(declare-const F Int)
(declare-const G Int)
(declare-const H Int)

(assert (= G 0)) ; it is same

(assert (or  (= A (+ B 4))  (= A (+ D 2))  ))
(assert (or  (= B (+ A 4))  (= B (+ E 6))  (= B (+ C 4))  ))
(assert (or  (= C (+ B 4))  (= C (+ E 7))  ))
(assert (or  (= D (+ A 2))  (= D (+ E 3))  (= D (+ F 5))  ))
(assert (or  (= E (+ B 6))  (= E (+ D 3))  (= E (+ C 7))  (= E (+ H 8))  ))
(assert (or  (= F (+ D 5))  (= F (+ G 9))  ))
(assert (or  (= H (+ E 8))  (= H (+ G 3))  ))

(minimize B)

(check-sat)
(get-model)
(get-objectives)
