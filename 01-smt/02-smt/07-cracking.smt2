(set-option :produce-models true)
(declare-const A Int) 
(declare-const B Int) 
(declare-const C Int)
(declare-const D Int)
(declare-const E Int) 

; Are digits
(assert (and (<= A 9) (>= A 0)))
(assert (and (<= B 9) (>= B 0)))
(assert (and (<= C 9) (>= C 0)))
(assert (and (<= D 9) (>= D 0)))
(assert (and (<= E 9) (>= E 0)))

; P1 1!=5 2!=3
(assert (and (distinct A E) (distinct B C)))
; P2 B=A*2 E = D+1
(assert (= B (* A 2)))
(assert (= D (- E 1)))

; P3 (no digit appears more than 2)
(assert (and
	(=> (= A B) (not (or (= A C) (= A D) (= A E))))
	(=> (= A C) (not (or (= A B) (= A D) (= A E))))
	(=> (= A D) (not (or (= A C) (= A B) (= A E))))
	(=> (= A E) (not (or (= A C) (= A D) (= A B))))

	(=> (= B C) (not (or (= B A) (= B D) (= B E))))
	(=> (= B D) (not (or (= B A) (= B C) (= B E))))
	(=> (= B E) (not (or (= B A) (= B D) (= B C))))

	(=> (= C D) (not (or (= C A) (= C B) (= C E))))
	(=> (= C E) (not (or (= C A) (= C D) (= C B))))

	(=> (= D E) (not (or (= D A) (= D B) (= B C))))
))

; P4 not sorded
(assert (not
	(and (<= A B ) (<= B C ) (<= C D ) (<= D E ))
))

(assert (not
	(and (>= A B ) (>= B C ) (>= C D ) (>= D E ))
))

; P5 1 and 5 odd and other even
(assert (= (mod A 2) 1))
(assert (= (mod B 2) 0))
(assert (= (mod C 2) 0))
(assert (= (mod D 2) 0))
(assert (= (mod E 2) 1))

; P6
(assert (= (+ A B C D E) (+ D (* 2 C))))


;Uniqueness
;(assert (not (= A 1)))

(check-sat)
(get-model)