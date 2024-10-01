import asyncio
from HsgSqually import HsgSqually

x_pos_target = 0.3
y_pos_target = 0
rotation_target = 360
        
async def main():
    async with HsgSqually() as robot:
        movement_task = asyncio.create_task(robot.move_to_target_position_straight_line(0.5, 0, 240))
        chat_task = asyncio.create_task(robot.chat())

        await asyncio.gather(movement_task, chat_task)

if __name__ == "__main__":
    asyncio.run(main())
