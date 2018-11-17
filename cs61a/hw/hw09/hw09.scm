(define-macro (list-of map-expr for var in lst if filter-expr)
	;Bind <name> to the element.
	;If <conditional-expression> evaluates to a truth-y value, 
		;evaluate <map-expression> 
			; add it to the result list.
	;(map <proc> <lst>)
		;Returns a well-formed list constructed by calling 
			;proc (a one-argument procedure) 
			;on each item in lst (a well-formed list).
	`(map 
		(lambda (,var) ,map-expr) 
		;(filter <pred> <lst>)
		(filter 
			(lambda (,var) ,filter-expr) 
			,lst)))
