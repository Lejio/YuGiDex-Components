from PySide6.QtGui import QColor

"""
    Styling Class:
    At the core, it is an encapsulated css string. Based on the methods you call, you could customize this output.
"""
class Styler:
    
    def __init__(self) -> None:
        
        self.styler = ""
        
    def setBorder(self, size: int, linetype, color: QColor) -> None:
        
        self.styler += f"border: {size} {linetype} {self.__QColorConverter(color)};"
    
    
    def setBackgroundColor(self, color: QColor) -> None:
        
        self.styler += f"background-color: {self.__QColorConverter(color)};"
        
    
    def setColor(self, color: QColor) -> None:
        
        self.styler += f"color: {self.__QColorConverter(color)}"
    
    
    def __QColorConverter(color: QColor) -> str:
        
        return f"({color.red()}, {color.green()}, {color.blue()}, {color.alpha()})"
    
    
    def __str__(self) -> str:
        
        return self.styler
    