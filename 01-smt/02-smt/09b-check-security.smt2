(set-option :produce-models true)
(set-option :produce-unsat-cores true)
(declare-const d1 Int)
(declare-const d2 Int)
(declare-const d3 Int)
(declare-const d4 Int)
(declare-const d5 Int)

(define-fun even ((a Int)) Bool (= (mod a 2) 0))

(assert (and
    (>= d1 0) (<= d1 9)
    (>= d2 0) (<= d2 9)
    (>= d3 0) (<= d3 9)
    (>= d4 0) (<= d4 9)
    (>= d5 0) (<= d5 9)
))


(assert (not (or (= d1 d5) (= d2 d3))))

(assert (and (= (* d1 2) d2) (= (+ d4 1) d5)))

(assert (not (or (= d3 d2 d1) (= d4 d2 d1) (= d4 d3 d1) (= d4 d3 d2)
    (= d5 d2 d1) (= d5 d3 d1) (= d5 d3 d2) (= d5 d4 d1) (= d5 d4 d2) (= d5 d4 d3)
)))


(assert (or (> d1 d2) (> d2 d3) (> d3 d4) (> d4 d5)))
(assert (or (> d1 d2) (> d2 d3) (> d3 d4) (> d4 d5)))

(assert (and (even d2) (even d3) (even d4) (not (even d1)) (not (even d5))))

(assert (= (+ d1 d2 d3 d5) (* d3 2)))

(check-sat)
(get-model)

(push 1)
(assert (not (or (= d1 1) (= d2 2) (= d3 8) (= d4 4) (= d5 5))))

(check-sat)
