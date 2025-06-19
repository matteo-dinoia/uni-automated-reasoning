(set-option :produce-models true)

(declare-const xa Int)
(declare-const xb Int)
(declare-const xc Int)

(assert (>= (+ xa xb xc) 100))
(assert (>= 150 (+ xa xb xc)))
(assert (>= xa 0))
(assert (>= xb 0))
(assert (>= xc 0))

(define-const cost-norm Int   (+ (* xa 10) (* xb 15) (* xc 20)))
(define-const  cost-heavy Int (+ (* xa 21) (* xb 18) (* xc 15)))

(minmax cost-norm cost-heavy)
(check-sat)
(get-model)
(get-value (cost-norm))
(get-value (cost-heavy))
