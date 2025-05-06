(set-option :produce-models true)
(declare-const A (_ BitVec 32))
(declare-const B (_ BitVec 32))
(declare-const C (_ BitVec 32))

(define-fun isMultiple ((x (_ BitVec 32)) (y Int)) Bool 
	(= (_ bv0 32) (bvsrem x ((_ to_bv 32) y)))
)
(define-fun isAverage ((average (_ BitVec 32)) (n1 (_ BitVec 32)) (n2 (_ BitVec 32))) Bool 
	(= C (bvsdiv (bvadd n1 n2) (_ bv2 32)))
)

(assert (isMultiple A 5))
(assert (= (bvor A B) (_ bv2022 32)))
(assert (bvsgt (bvsub A B) (_ bv1000 32)))
(assert (isAverage C A B))
(assert (bvsle (bvmul A C) #x0017c1cc))

(check-sat)
(get-model)

; Check is unique
(push 1)
(assert (not (= B (_ bv482 32))))
(check-sat)
