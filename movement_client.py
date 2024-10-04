import pygame
import socket

pygame.init()
pygame.joystick.init()

joystick = pygame.joystick.Joystick(0)
joystick.init()

robot_ip = "localhost"
robot_port = 8083
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((robot_ip, robot_port))


def send_command_to_robot(directions: list):
    command = f"{directions[0]},{directions[1]}"
    client_socket.send(command.encode())
    print(f"Sent: {command} to robot")


running = True
prev_movement = None
current_movement = None
prev_rotation = None
current_rotation = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            left_joystick_y = joystick.get_axis(1)
            right_joystick_x = joystick.get_axis(2)

            if left_joystick_y < -0.5:
                current_movement = "forward"
            elif left_joystick_y > 0.5:
                current_movement = "backward"
            else:
                current_movement = "stop"

            if right_joystick_x < -0.5:
                current_rotation = "left"
            elif right_joystick_x > 0.5:
                current_rotation = "right"
            else:
                current_rotation = "stop"

            if current_movement != prev_movement or current_rotation != prev_rotation:
                send_command_to_robot([current_movement, current_rotation])
                prev_movement = current_movement
                prev_rotation = current_rotation

        else:
            if joystick.get_button(0):  # 'X' button pressed
                send_command_to_robot(["stop", "stop"])
            elif joystick.get_button(3):  # 'Triangle' button pressed
                send_command_to_robot(["exit", "exit"])
                prev_movement = None
                current_movement = None
                prev_rotation = None
                current_rotation = None
                running = False


pygame.quit()
client_socket.close()
