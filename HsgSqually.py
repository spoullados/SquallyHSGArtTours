import navel
from calculate_distance import calculate_distance
from calculate_angle import calculate_angle
from HsgAIModule import HsgAIModule

class HsgSqually:
    def __init__(self):
        self.robot = None
        
        self.current_x_pos = 0
        self.current_y_pos = 0
        self.current_rotation = 0
        
        self.AI_module = HsgAIModule()
        

    async def __aenter__(self):
        self.robot = await navel.Robot().__aenter__()
        return self
    

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.robot:
            await self.robot.__aexit__(exc_type, exc_val, exc_tb)
            

    async def move(self, distance, speed):
        await self.robot.move_base(distance, speed)
        

    async def rotate_to(self, target_angle):
        await self.robot.rotate_base(target_angle)
        self.current_rotation = target_angle
        
        
    async def move_to_target_position_straight_line(self, x_pos_target, y_pos_target, angle_target):
        distance = calculate_distance(self.current_x_pos, self.current_y_pos, x_pos_target, y_pos_target)
        angle_to_target = calculate_angle(self.current_x_pos, self.current_y_pos, x_pos_target, y_pos_target)
        await self.rotate_to(angle_to_target)
        await self.move(distance, 0.2)
        await self.rotate_to(angle_target)
        
       
    async def say(self, message={"role": "failure", "content": "An error occured."}, say=True):
        print(f"{message['role']} said: {message['content']}")
        if say:
            await self.robot.say(message["content"])
        

    async def chat(self):
        while True:
            user_speech = await self.AI_module.get_user_speech()

            if not user_speech["content"]:
                continue
            
            await self.say(user_speech, False)

            response = self.AI_module.get_response()
            await self.say(response)
