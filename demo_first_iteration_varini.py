import asyncio
from HsgSqually import HsgSqually

        
async def main():
    
    x_pos_varini = 0.4
    y_pos_varini = 0
    rotation_varini = 90
    
    async with HsgSqually() as robot:
        movement_task = asyncio.create_task(robot.move_to_target_position_straight_line(x_pos_target=x_pos_varini,
                                                                                        y_pos_target=y_pos_varini,
                                                                                        angle_target=rotation_varini))
        chat_task = asyncio.create_task(robot.chat())

        await asyncio.gather(movement_task, chat_task)

if __name__ == "__main__":
    asyncio.run(main())
