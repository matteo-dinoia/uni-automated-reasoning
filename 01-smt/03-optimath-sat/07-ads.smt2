(set-option :produce-models true)
(set-option :opt.priority par)


(declare-const n_ads Int)
(declare-const n_app Int)

(assert (>= n_ads 0))
(assert (>= n_ads 0))

(define-const cost_ads Int (* n_ads 2000))
(define-const cust_ads Int (* n_ads 2))
(define-const rat_ads  Int (* n_ads 1))
(define-const time_ads Int (* n_ads 1))

(define-const cost_app Int (* n_app 500))
(define-const cust_app Int (* n_app 2))
(define-const rat_app  Int (* n_app 5))
(define-const time_app Int (* n_app 2))

(define-const cust_tot Int (+ cust_ads cust_app))
(define-const rat_tot Int (+ rat_ads rat_app))
(define-const cost_tot Int (+ cost_ads cost_app))
(define-const time_tot Int (+ time_ads time_app))

(assert (>= cust_tot 16))
(assert (>= rat_tot 28))

(minimize time_tot)
(minimize cost_tot)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)

(check-sat)
(get-model)
