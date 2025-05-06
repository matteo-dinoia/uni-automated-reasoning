(set-option :produce-models true)
(declare-const A Int) 
(declare-const B Int) 
(declare-const C Int)
(declare-const D Int)
(declare-const E Int) 
(declare-const N Int)

(declare-const S1 Bool) 
(declare-const S2 Bool)
(declare-const S3 Bool)
(declare-const S4 Bool) 

; Are digits (10000 <= x <= 99999)
(assert (and (<= A 9) (>= A 1)))
(assert (and (<= B 9) (>= B 0)))
(assert (and (<= C 9) (>= C 0)))
(assert (and (<= D 9) (>= D 0)))
(assert (and (<= E 9) (>= E 0)))

; The number
(assert (= N (+ (* A 10000) (* B 1000) (* C 100) (* D 10) E)))

(assert (= S1 (xor (= (mod N 5) 0) (= (mod N 3) 0))))
(assert (= S2 (= (mod (+ A B C D E) 10) 0)))
(assert (= S3 (and (= A E) (= B D))))
(assert (= S4 (and (<= A B) (<= B C) (<= C D) (<= D E))))

(assert  (= 2 (+ (ite S1 1 0) (ite S2 1 0) (ite S3 1 0) (ite S4 1 0))))

(check-sat)
(get-model)