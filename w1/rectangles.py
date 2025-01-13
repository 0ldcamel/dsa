def overlap(rec1, rec2):
    topleft_x1, topleft_y1, bottomright_x1, bottomright_y1 = rec1
    topleft_x2, topleft_y2, bottomright_x2, bottomright_y2 = rec2
    if bottomright_x1 < topleft_x2 or bottomright_x2 < topleft_x1:
        return False
    if topleft_y1 < bottomright_y2 or topleft_y2 < bottomright_y1:
        return False
    return True

rec1 = (-1,1,1,-1)
rec2 = (0,3,2,0)
rec3 = (0,2,3,-2)
rec4 = (2, -1, 4, -4)

print(overlap(rec1, rec2))
print(overlap(rec1, rec3))
print(overlap(rec3, rec2))
print(overlap(rec1, rec4))
print(overlap(rec2, rec4))
print(overlap(rec3, rec4))