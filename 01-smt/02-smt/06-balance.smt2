(set-option :produce-models true)
(declare-const Y Int) ; yellow
(declare-const G Int) ; green
(declare-const R Int) ; red
(declare-const P Int) ; purple
(declare-const BT Int) 
(declare-const BL Int) 
(declare-const BR Int) 

(assert (and
	(>= Y 0)
	(>= G 0)
	(>= R 0)
	(>= P 0)

))

(assert (= (* BT 2) 56))

(assert (= BT (+ Y Y (* BL 2))))
(assert (= BT (* BR 2)))

(assert (= BL (+ R R)))
(assert (= BL (+ G P)))

(assert (= BR (+ Y Y Y G)))
(assert (= BR (+ R G)))

; TODO
(check-sat)
(get-model)