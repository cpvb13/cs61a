
# def combo(a,b):
#     if a is 0 or b is 0:
#         return a+b
#     elif a%10 == b%10:
#         return (combo(a//10,b//10)*10)+a%10

#     return min(combo(a//10,b)*10+a%10,
#             combo(a,b//10)*10+b%10)







# def tee(iterable):
#     it = iter(iterable)
#     queues = [[],[]]
#     def gen(lst):
#         while True:
#             if not lst:
#                 try:
#                     value = next(it)
#                 except StopIteration:
#                     return
#                 for q in queues:
#                     q.append(value)
#             x = lst.pop
#             print('I just yielded:',x)

#             yield x
#     return [gen(queues[0]), gen(queues[1])]

# yum = ['avo','quin','cream']
# print(yum[0]+' '+yum[-1])*5
# print(print(next(iter(yum))),next(yum))
# next(iter(next(iter(yum))))

# eat = iter(tee(yum))
# neat = next(eat)
# next(neat)


# yum[0] = yum.pop()
# yum.append(next(neat))
# yum[:2]



# next(neat)

# munch = next(iter(tee(yum)))
# next(munch)+' '+next(next(eat))