class Settings():
    def __init__(self):
        self.screen_width = 1500
        self.screen_height = 850
        # self.bg_color = (230, 230, 230)
        self.bg_color = (255, 255, 255)
        self.ship_speed = 1.5

        self.bullet_speed = 2  # 子弹速度
        self.bullet_width = 10  # 子弹宽度
        self.bullet_height = 20  # 高度
        self.bullet_color = (60, 60, 60)

        self.alien_speed = 0.5
        self.fleet_direction = 1  # 1: 右, -1: 左
