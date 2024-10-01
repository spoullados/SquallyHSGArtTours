import asyncio
from HsgSqually import HsgSqually

x_pos_target = 0.3
y_pos_target = 0
rotation_target = 360
        
async def main():
    async with HsgSqually() as robot:
       await robot.move_to_target_position_straight_line(x_pos_target, y_pos_target, rotation_target)
       await robot.say("Arrived.")

if __name__ == "__main__":
    asyncio.run(main())
