from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QRect, Property, QPropertyAnimation, QEasingCurve, Qt, QPoint, QEvent, QObject
from PySide6.QtGui import QPainter, QColor, QEnterEvent

class SideBar(QWidget):
    
    def __init__(self,
                 width = 50,
                 height = 0,
                 color = QColor("lightgray"),
                 setCurve = QEasingCurve.Type.Linear):
        
        super(SideBar, self).__init__()
        self.currWidth = width
        self.currHeight = height
        
        self.color = color

        self.setFixedWidth(width)
        self.setCurve = setCurve
        self.maxSize = self.currWidth * 5
        self.minimumSize = width
        
        
        # This here sets up the animation
        self.anim = QPropertyAnimation(self, b"changewidth")
        self.anim.setDuration(500)
        self.anim.setStartValue(width)
        self.anim.setEasingCurve(self.setCurve)
        self.setMouseTracking(True)
        
        # This is used to "connect" a widget to an event filter. So now ever single event 
        # (related to this widget) will be passed to the eventfilter.
        # Here, I am installing an event filter for this current widget (which is just a rectangle)
        self.installEventFilter(self)
        
    
    ###############################################################################################
    # Update: I just found out about the QPushButtons built in enter and leave event. This is
    # essentially what the filter event is doing. I think these two are the same. (The app is
    # still running and checking each event).
    ###############################################################################################
    def enterEvent(self, e: QEnterEvent) -> None:        
        # The direction is pretty cool. It would reverse the start and ending values automatically.
        # One annoying thing is that it the easing curve would be reversed too.
        self.anim.setDirection(self.anim.Direction.Forward)
        # State. Detects if the animation is running (boolean). This if not running, run animation.
        # The animation would run fine without this statement. However, it would be really wonky.
        if self.anim.state() == self.anim.State.Stopped:
            
            # Fixing curve type after reversing.
            self.anim.setEasingCurve(QEasingCurve.Type.OutBounce)
            
            # You only really need to set the End Value once. And I put it in the enterEvent so
            # in case the leave Event fires off first, it would not mess up the animation.
            self.anim.setEndValue(self.maxSize)
            
            self.anim.start()
            
        return super().enterEvent(e)
        
    def leaveEvent(self, e: QEvent) -> None:
        
        # Setting the animation to go backwards.
        self.anim.setDirection(self.anim.Direction.Backward)
        
        if self.anim.state() == self.anim.State.Stopped:
            
            self.anim.setEasingCurve(QEasingCurve.Type.InBounce)
            
            self.anim.start()
            
        return super().leaveEvent(e)
        
    
    ###############################################################################################
    # Every widget will call a paintEvent when instantiating and animating. This event basically
    # draws the widget itself. You can customize the widget by drawing your own by using QPainter.
    ###############################################################################################
    def paintEvent(self, e):
        
        self.setFixedWidth(self.currWidth)
        
        p = QPainter(self)
        
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        p.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.currWidth, self.currHeight)
        
        p.setBrush(self.color)
        
        p.drawRect(rect)
        
        p.end()
        
    ###############################################################################################
    # Depricated events. I was experienting with specific mouse move event hoping it would achieve
    # a mouse hover effect I was looking for. Didn't quite work out.
    ###############################################################################################
    
    # def mousePressEvent(self, e):
        
    #     self.anim.setEndValue(self.minimumSize)
    #     self.anim.start()
        
    # def mouseMoveEvent(self, e):
        
    #     self.anim.setEndValue(self.maxSize)
    #     self.anim.start()
        # self.anim.setEndValue(self.minimumSize)

    ###############################################################################################
    # In order to run animations, you need to set up setters and getters for the custom property
    # you want to animate. Here, I want to animate the variable currWidth which is the current
    # width of the widget. Notice, when I create the QPropertyAnimation, I used the setter and 
    # getter's method names and not the currWidth (line 24).
    # The setter must end with a self.update(). Each QObject has this method, and it is used to
    # re-draw the widget (and this is where the paintEvent comes in).
    ###############################################################################################
    @Property(int)
    def changewidth(self):
        
        return self.currWidth
    
    @changewidth.setter
    def changewidth(self, w):
        
        self.currWidth = w
        self.update()