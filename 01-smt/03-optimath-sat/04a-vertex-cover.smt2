(set-option :produce-models true)

; Is inside
(declare-const A Bool)
(declare-const B Bool)
(declare-const C Bool)
(declare-const D Bool)
(declare-const E Bool)
(declare-const F Bool)
(declare-const G Bool)

(assert (or A B))
(assert (or B C))
(assert (or C D))
(assert (or C E))
(assert (or D E))
(assert (or D F))
(assert (or D G))
(assert (or E F))


(minimize (+ (ite A 1 0) (ite B 1 0) (ite C 1 0) (ite D 1 0)
    (ite E 1 0) (ite F 1 0) (ite G 1 0)))

(check-sat)
(get-model)
(get-objectives)
