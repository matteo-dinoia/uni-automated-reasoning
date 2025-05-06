(set-option :produce-models true)

(declare-const m Real)
(declare-const q Real)

(declare-const x Real)
(declare-const y Real)

(define-const Ax Real 1)
(define-const Ay Real (/ 3 2))
(define-const Bx Real (/ 1 2))
(define-const By Real 7)

(define-fun f ((x Real)) Real (+ (* m x) q))

; Line passing in A
(assert (= Ay (f Ax)))
; Line passing in B
(assert (= By (f Bx)))

(assert (= y (f 0)))
(assert (= 0 (f x)))


(check-sat)
(get-model)
