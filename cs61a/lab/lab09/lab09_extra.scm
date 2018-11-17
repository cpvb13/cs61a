;; Extra Scheme Questions ;;


; Q5
(define lst
  (cons (cons 1 nil) (cons 2 (cons (cons 3 4) (cons 5 nil))))
     )

; Q6
(define (composed f g)
  (lambda (x) (f (g x)))
)

; Q7
(define (remove item lst)
  (cond
  	( (null? lst)
  		nil)
  	( (= (car lst) item)
  		(remove item (cdr lst)))
  	(else
  		(cons (car lst) (remove item (cdr lst))))
  	)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (contains? s v)
    (cond
    	((null? s)
    		#f)
    	((> (car s) v)
    		#f)
    	((= v (car s))
    		#t)
    	(else (contains? (cdr s) v))

    	)
    )

; Q8
(define (no-repeats s)
  (cond
  	( (null? s)
  		s)
  	(else
  		(cons (car s) 
  			(no-repeats (filter (lambda (x) (not (= (car s) x))) (cdr s) ) ))		)))
;(define (filter f lst)
; if the first s is contained in the rest of s
; remove item from cdr s
; Q9
(define (substitute s old new)
  (cond
  	( (null? s)
  		s)
  	( (pair? (car s))
  		(cons (substitute (car s)) old new) (substitute (cdr s) old new)))
  	( (equal? (car s) old)
  		(cons new (substitute (cdr s) old new)))
  	(else
  		(cons (car s) (substitute (cdr s) old new)))
  	)


; Q10
(define (sub-all s olds news)
  'YOUR-CODE-HERE
)