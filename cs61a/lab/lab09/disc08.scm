(define (factorial x)
	(cond
		((= x 0)
			1)
		(else
			( * x (factorial (- x 1) ) ) )))

(define (factorial x)
	(if
		((= x 0)
			1
			(* x 
				(factorial (- x 1) ) ) )))
; line up operands with indent of operator

(define (fib n))
	(cond
		((= n 1) 1)
		((= n 0) 0) 
		(else
			(+ (fib (- n 1) 
			   (fib (- n 2)))))

(define (concat a b)
	(cond
		((null? a) b)
		((null? b) a)
		(else
			(cons (car a) 
				  (concat (cdr a) b)))
	))

(define (replicate x n)
	(cond
		((= n 1) x)
		(else ( cons x (replicate (x (- n 1))))
		)
	))

(define (uncompress s)
	(cond
		((null? s) nil)
		(else (concat (replicate 
						(car(car s)) 
						((car(cdr(car s)))))
					  (uncompress (cdr s))))


(define (map fn lst)
	(cond
		((null? lst) nil)
		(else (cons (fn (car lst)) 
					(map fn (cdr lst))))))

; (define (deep-map fn lst)
; 	(cond 
; 		((list? (car lst))
; 			(deep-map fn (car lst)))
; 		((null? lst)
; 			nil)
; 		(else (cons
; 			(map fn (car lst)) 
; 			(deep-map fn (cdr lst))))))


(define (deep-map fn lst)
	(cond 
		((list? lst)
			(cons (deep-map fn (car lst)))
				  (deep-map fn (cdr lst)))

		((null? lst) nil)
		(else (fn lst)))) 
			



(define (make-tree label branches) 
	(cons label branches))

(define (label tree) ; (define branches car)
	(car tree))

(define (branches tree) ; (define branches cdr)
	(cdr tree))

(define (tree-sum tree)

