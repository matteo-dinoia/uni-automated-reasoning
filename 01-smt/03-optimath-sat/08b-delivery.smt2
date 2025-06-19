(set-option :produce-models true)
(declare-const xa Int)
(declare-const xb Int)
(declare-const xc Int)

(assert (and (>= xa 0) (>= xb 0) (>= xc 0)))
(assert (and (>= (+ xa xb xc) 100) (<= (+ xa xb xc) 150)))

(define-const cost-norm  Int   (+ (* xa 10) (* xb 15) (* xc 20)))
(define-const cost-heavy Int   (+ (* xa 21) (* xb 18) (* xc 15)))


(minmax
    cost-norm
    cost-heavy
)

(check-sat)
(get-model)
(get-value (cost-norm))
(get-value (cost-heavy))
