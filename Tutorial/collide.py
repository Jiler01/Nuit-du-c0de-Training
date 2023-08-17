class collide:
    def __init__(self, obj1, obj2, type: str):
        if type == "rectangle":
            self.rectangle(obj1, obj2)
        elif type == "circle":
            self.circle(obj1, obj2)

    def rectangle(self, me, other_rect):
        left = me.x
        right = me.x + me.w
        top = me.y
        bottom = me.y + me.h

        other_left = other_rect.x
        other_right = other_rect.x + other_rect.w
        other_top = other_rect.y
        other_bottom = other_rect.y + other_rect.h

        overX = (left <= other_right) and (right >= other_left)
        overY = (top <= other_bottom) and (bottom >= other_top)

        if overX and overY:
            if other_left < left:
                Xposition = 'right'
            elif other_right > right:
                Xposition = 'left'
            else:
                Xposition = 'center'

            if other_top < top:
                Yposition = 'bottom'
            elif other_bottom > bottom:
                Yposition = 'top'
            else:
                Yposition = 'middle'

            self.happens = True
            self.Xposition = Xposition
            self.Yposition = Yposition
        else:
            self.happens = False

    def circle(self, me, other_circle):
        distance = ((me.x - other_circle.x) ** 2 + (me.y - other_circle.y) ** 2) ** 0.5
        if distance <= me.r + other_circle.r:
            if me.x < other_circle.x:
                Xposition = 'right'
            elif me.x > other_circle.x:
                Xposition = 'left'
            else:
                Xposition = 'center'

            if me.y < other_circle.y:
                Yposition = 'bottom'
            elif me.y > other_circle.y:
                Yposition = 'top'
            else:
                Yposition = 'middle'

            self.happens = True
            self.Xposition = Xposition
            self.Yposition = Yposition
        else:
            self.happens = False