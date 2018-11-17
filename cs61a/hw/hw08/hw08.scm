(define (reverse lst)
    (cond
      ;empty list returns ()
      ( (null? lst) nil)
      ;if second item is empty, return list (#)
      ( (null? (cdr lst)) lst)
      ;append ____recursive call to rest of list to first of list
      ;make sure it is well formed!
      (else (append (reverse (cdr lst)) (list (car lst))))))


(define (longest-increasing-subsequence lst)
    (if (or (null? lst) (null? (cdr lst)) ) 
        lst
        (begin
            ;include the first number
            (define with (filter 
              ;predicate
              (lambda (x)) (< (car x) (cadr x))) 
              ;list
              (list (car lst) (longest-increasing-subsequence (cdr lst))))
            
            ;skip the first number
            (define without (longest-increasing-subsequence (cdr lst)))
            ;check for greater
            (if (> (length with) (length without))
                with
                without))))

; (define (longest-increasing-subsequence lst)
;   ;first check               (< (car lst) (cdr lst))) 

;   (if (or (null? lst) (null? (cdr lst)) ) lst
;     ;take in current lst (will be reduced with each call)
;     ;inc-lst which will be either skipping the next num or includings
;     ((define (track-n lst inc-lst m)
;       (cond 
;         ((null? lst) 
;           (if (eq? (length (cdr inc-lst)) (m))
;             (cdr inc-lst)))
;         (( < (car lst) (cadr lst)) ;
;           (track-n (cdr lst) (cons inc-lst (car lst)) (+ 1 m)))
          
;         ))
;     (track-n lst '() 0))))

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s)) ;2nd
(define (augend s) (caddr s)) ;3rd

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (addend expr) var) (derive (augend expr) var)))


(define (derive-product expr var)
  (make-sum 
    (make-product (derive (addend expr) var)  (augend expr) )
    (make-product (addend expr) (derive (augend expr) var))))

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  (cond ( (= 1 exponent ) base)
        ( (= 0 exponent ) 1)
        ( (and (number? base) (number? exponent)) (expt base exponent))
        (else (list '^ base exponent)
)))

(define (base exp)
  (addend exp)
)

(define (exponent exp)
  (augend exp)
)

(define (exp? exp)
  (cond
  ( (pair? exp) 
    (if (eq? (car exp) '^) #t))
  (else #f)))

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (cond
    ((exp? exp) 
      (make-product 
        (exponent exp) 
        (make-exp (base exp) (- (exponent exp) 1)))
    )
))