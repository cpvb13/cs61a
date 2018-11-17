(define (accumulate combiner start n term)
  (if (= 0 n) start
  	(combiner
  		(term n)
  		(accumulate combiner start (- n 1) term))))

(define (accumulate-tail combiner start n term)
	(if (= 0 n) start
		(accumulate-tail 
			combiner 
			(combiner start (term n))
			(- n 1) 
			term)))

(define (partial-sums stream)
  (define (helper n stream)
  	(if (null? stream) '()
  	(cons-stream 
  		(+ n (car stream)) 
  		(helper (+ n (car stream)) (cdr-stream stream)))))
  (helper 0 stream)
)

(define (rle s)
 (define (helper s n new)
 	(cond 
    ((null? s) new) 
    ((null? (cdr-stream s)) (cons-stream (list (car s) (+ n 1)) nil))
    ;((null? s)  new)
    ;((null? (cdr-stream s)) (list (car s) (+ n 1)))
    ((= (car s) (car (cdr-stream s))) (helper (cdr-stream s) (+ n 1) new)) ;while its the same num
      ;(helper (cdr-stream s) (+ n 1) new))
    ; when its different
    (else (cons-stream (list (car s) (+ n 1)) (helper (cdr-stream s) 0 new)))
      ))
  (helper s 0 '())
)