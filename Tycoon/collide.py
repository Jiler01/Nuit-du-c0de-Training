class ColiPosition:
    def __init__(self,me,other_rectangle):
        self.me_top = me.x
        self.me_bottom = me.x + me.h
        self.me_left = me.y
        self.me_right = me.y + me.w

        self.other_top = other_rectangle.x
        self.other_bottom = other_rectangle.x + other_rectangle.w
        self.other_left = other_rectangle.y
        self.other_right = other_rectangle.y + other_rectangle.w

        overX = self.other_right >= self.me_left and self.other_left <= self.me_right
        overY = self.other_bottom >= self.me_top and self.other_top <= self.me_bottom

        self.happens = overX and overY

        ############

        if self.me_top > self.other_bottom:
            self.Yposition = "above"
            self.Ydistance = self.me_top - self.other_bottom
        elif self.me_bottom < self.other_top:
            self.Yposition = "under"
            self.Ydistance = self.other_top - self.me_top
        else:
            self.Yposition = "overlapY"
            self.Ydistance = 0

        if self.me_left > self.other_right: 
            self.Xposition = "left"
            self.Xdistance = self.me_left - self.other_right
        elif self.me_right < self.other_left:
            self.Xposition = "right"
            self.Ydistance = self.other_left - self.me_right
        else:
            self.Xposition = "center"
            self.Xdistance = 0