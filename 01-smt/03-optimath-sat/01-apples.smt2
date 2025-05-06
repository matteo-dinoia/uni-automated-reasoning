(set-option :produce-models true)

(declare-const n Int)
(declare-const total_trees Int)
(declare-const apples_per_trees Int)

; problem
(assert (= total_trees (+ 50 n)))
(assert (= apples_per_trees (- 800 (* 10 n))))
; (assert (>= n 0))

(maximize (* total_trees apples_per_trees))

(check-sat)
(get-model)
(get-objectives)
