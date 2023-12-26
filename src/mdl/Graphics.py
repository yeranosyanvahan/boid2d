import os
import math
import pygame
from moviepy.editor import VideoClip, ImageSequenceClip
import numpy as np
        
class Graphics:
           
    def save_on_quit(self, filename, fps=30):
        self.save = True

        def save_recording(self):
            with VideoClip(lambda t: self.frames[int(t*fps)], duration=len(self.frames) // fps) as clip:
                if filename.endswith('.gif'):
                    clip.write_gif(filename, fps=30)
                else:
                    clip.write_videofile(filename, fps=fps)
        
        self.save_recording = save_recording
        self.frames = []


    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.save = False
        os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

    def __del__(self):
        self.quit()
        
    @property
    def event(self):
        return pygame.event
    
    @property
    def QUIT(self):
        return pygame.QUIT
    
    @property
    def KEYDOWN(self):
        return pygame.KEYDOWN   
     
    @property
    def K_SPACE(self):
        return pygame.K_SPACE
    
    def init(self, title = "Boid Simulation"):
                
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()

    def blank(self):
        self.screen.fill((255, 255, 255))

    def draw_boid(self, position, angle, size = 25, color = (0, 0, 255)):
        angle = -angle
        
        # Convert boid's position from meters to pixels
        pixel_x = position[0]
        pixel_y = self.screen.get_height() - position[1]

        # Calculate the points of the triangle
        point1 = (pixel_x, pixel_y)
        point2 = (pixel_x + size * math.cos(angle + 2.8), pixel_y + size * math.sin(angle + 2.8))
        point3 = (pixel_x + size * math.cos(angle - 2.8), pixel_y + size * math.sin(angle - 2.8))

        # Draw the triangle with a red front and black back
        pygame.draw.polygon(self.screen, color, [point1, point2, point3])

    def display(self):
        pygame.display.flip()
        if self.save:
            frame = pygame.surfarray.array3d(self.screen)
            frame = np.rot90(frame)
            self.frames.append(np.flipud(frame))
    
    def quit(self):
        if self.save:
            self.save_recording(self)
        pygame.quit()        
    
    def get_frame(self):
        return pygame.surfarray.array3d(self.screen)


    def draw_vector(self, position, vector, color = (255, 0, 0)):
        # Define the length of0 the velocity vector and the arrowhead size
        velocity_scale = 5
        arrowhead_scale = 0.75
        arrowhead_angle = math.pi / 6  # Angle for the arrowhead wings

        # Calculate the magnitude of the velocity
        velocity_magnitude = math.sqrt(vector[0]**2+vector[1]**2)

        # Calculate the length of the velocity vector
        vector_length = velocity_magnitude * velocity_scale
        arrowhead_length = velocity_magnitude * arrowhead_scale

        # Calculate the angle of the boid's velocity
        angle = -math.atan2(vector[1], vector[0])

        # Convert boid's position from meters to pixels
        pixel_x = position[0]
        pixel_y = self.screen.get_height() - position[1]

        vector_length_x = vector_length * math.cos(angle)
        vector_length_y = vector_length * math.sin(angle)
        # Calculate the end point of the velocity vector
        end_x = pixel_x + vector_length_x
        end_y = pixel_y + vector_length_y

        # Draw the velocity vector
        pygame.draw.line(self.screen, color, (pixel_x, pixel_y), (end_x, end_y), 2)

        # Calculate arrowhead points
        left_wing_x = end_x + arrowhead_length * math.cos(angle - math.pi + arrowhead_angle)
        left_wing_y = end_y + arrowhead_length * math.sin(angle - math.pi + arrowhead_angle)
        right_wing_x = end_x + arrowhead_length * math.cos(angle - math.pi - arrowhead_angle)
        right_wing_y = end_y + arrowhead_length * math.sin(angle - math.pi - arrowhead_angle)

        # Draw the arrowhead
        pygame.draw.polygon(self.screen, color, [
            (end_x + 0.2*vector_length_x, end_y+0.2*vector_length_y),
            (left_wing_x, left_wing_y),
            (right_wing_x, right_wing_y)
        ])

    StatTextColor = (0, 0, 0)
    StatFontSize = 35
    def draw_stats(self, stats):
        font = pygame.font.SysFont(None, Graphics.StatFontSize)  # You can choose a different font and size


        y_offset = Graphics.StatFontSize // 2
        for text in stats:
            img = font.render(text, True, Graphics.StatTextColor)
            self.screen.blit(img, (Graphics.StatFontSize // 2, y_offset))
            y_offset += Graphics.StatFontSize * 0.9

