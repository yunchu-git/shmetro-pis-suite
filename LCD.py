import pygame
class LCD:
    def __init__(self):
        self.station = None
        self.current = None
        self.station_int = 0
        self.open = False
    def start(self,station):
        if self.open:
            raise RuntimeError("2*000003")
        self.station = station
        self.current = self.station[self.station_int]
        self.open = True
        pygame.init()
        pygame.display.set_mode((800,300))
        pygame.display.set_caption("LCD屏幕")
        while self.open:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    self.open = False
        pygame.quit()
        self.open = False
    def stop(self):
        if self.open:
            pygame.quit()
            self.open = False
        else:
            raise RuntimeError("2*000002")
    def info(self,info_type = "all"):
        if self.open:
            if info_type == "all":
                return [self.station,self.current,self.station_int,self.open]
            else:
                raise ValueError("2*000001")
        else:
            raise RuntimeError("2*000002")
lcd_screen = LCD()
