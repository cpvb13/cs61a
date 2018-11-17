;; Scheme ;;

(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
        	;why does this need two parenthesis?????
            ((y (repeatedly-cube (- n 1) x)))
            (* y y y))
        ))