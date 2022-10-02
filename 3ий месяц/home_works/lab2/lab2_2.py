class Tool():
    def __init__(self):
        self.hp = 100

    def action(self):
        self.hp -= 10

class Saw(Tool):
    def __init__(self):
        super().__init__()

    def action(self):
        print("saw saw saw saw saw saw")
        return super().action()

class Axe(Tool):
    def __init__(self):
        super().__init__()

    def action(self):
        print("AXE")
        return super().action()

class Drill(Tool):
    def __init__(self):
        super().__init__()

    def action(self):
        print("ddddddrrrrriiiiiiilllllllllll")
        return super().action()

class Hammer(Tool):
    def __init__(self):
        super().__init__()

    def action(self):
        print("HAMMER HAMMER HAMMER")
        return super().action()

class Screwdriver(Tool):
    def __init__(self):
        super().__init__()

    def action(self):
        print("Screwdriver")
        return super().action()

class Robot():
    def __init__(self):
        self.robotTool = None
    
    def setup_tool(self, tool):
        self.robotTool = tool
    
    def drop_tool(self):
        self.robotTool = None
    
    def action(self):
        if self.robotTool == None:
            print("Tool not installed")
            return False
        
        if self.robotTool != None and self.robotTool.hp > 9:
            self.robotTool.action()
            print(self.robotTool.hp)
            print("-" * 40)
        elif self.robotTool.hp <= 9:
            print("Tool is broken")

            

saw = Saw()

robot = Robot()
robot.setup_tool(saw)
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.action()
robot.drop_tool()
robot.action()