(set-option :produce-models true)

(declare-const a18 Bool)
(declare-const a19 Bool)
(declare-const a20 Bool)
(declare-const a21 Bool)
(declare-const a22 Bool)
(declare-const a23 Bool)

(declare-const r18 Bool)
(declare-const r19 Bool)
(declare-const r20 Bool)
(declare-const r21 Bool)
(declare-const r22 Bool)
(declare-const r23 Bool)

(declare-const b18 Bool)
(declare-const b19 Bool)
(declare-const b20 Bool)
(declare-const b21 Bool)
(declare-const b22 Bool)
(declare-const b23 Bool)

(declare-const k18 Bool)
(declare-const k19 Bool)
(declare-const k20 Bool)
(declare-const k21 Bool)
(declare-const k22 Bool)
(declare-const k23 Bool)

(assert (not (or (and a18 b18) (and a18 r18) (and a18 k18) (and b18 r18)
    (and b18 k18) (and r18 k18))))
(assert (not (or (and a19 b19) (and a19 r19) (and a19 k19) (and b19 r19)
    (and b19 k19) (and r19 k19))))
(assert (not (or (and a20 b20) (and a20 r20) (and a20 k20) (and b20 r20)
    (and b20 k20) (and r20 k20))))
(assert (not (or (and a21 b21) (and a21 r21) (and a21 k21) (and b21 r21)
    (and b21 k21) (and r21 k21))))
(assert (not (or (and a22 b22) (and a22 r22) (and a22 k22) (and b22 r22)
    (and b22 k22) (and r22 k22))))
(assert (not (or (and a23 b23) (and a23 r23) (and a23 k23) (and b23 r23)
    (and b23 k23) (and r23 k23))))

; ACDC
(assert (or (and a18 a19 a20) (and a21 a19 a20) (and a21 a22 a20) (and a21 a22 a23)))

(assert-soft (or (and b19 b20) (and b22 b23)) :weight 1 :id pen)

(assert-soft (or r18 r23) :weight 1 :id pen)

(assert-soft (or k19 k20 k21 k22) :weight 1 :id pen)

(minimize pen)
(check-sat)
(get-model)
(get-objectives)
