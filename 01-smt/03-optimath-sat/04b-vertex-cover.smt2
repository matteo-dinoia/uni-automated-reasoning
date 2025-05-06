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

(assert-soft (not A) :weight 1 :id penality)
(assert-soft (not B) :weight 1 :id penality)
(assert-soft (not C) :weight 1 :id penality)
(assert-soft (not D) :weight 1 :id penality)
(assert-soft (not E) :weight 1 :id penality)
(assert-soft (not F) :weight 1 :id penality)
(assert-soft (not G) :weight 1 :id penality)


(minimize penality)

(check-sat)
(get-model)
(get-objectives)
