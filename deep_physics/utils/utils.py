import numpy as np
import matplotlib.pyplot as plt




def generate_linear_data(time=20, speed=10, num_pixels=80, num_balls=1, sf=800, max_period=10, noise_level=0.0):
    """
    Generates a [num_pixels, time * sf] array simulating num_balls going up and down.
    The balls bounce up and down from the 
    The period of the ball is some number between 1 and max_period + 1 generated randomly
    We show the movement of the ball from time t to time ``t + time`` where t is selected uniformly form 
    [0, time]. 
    """
    t = np.linspace(0,time,time * sf) 
    period = (np.random.rand(num_balls) * max_period) + 1
    samples = []
    for i in range(num_balls):
        start = np.random.rand() * time
        y = np.abs(((t + start)  % period[i]*2) - period[i])
        y = y/np.max(y)
        samples.append(y)

    # This first line is so as not to ahve issues with a number being 1. 
    samples = np.array(samples) * 0.999
    samples = np.floor(num_pixels * samples).astype(int)
    time_index = np.arange(sf * time).astype(int)
    pixels = np.zeros((num_pixels, sf * time))

    for i in range(num_balls):

        pixels[samples[i],time_index] = 1

    pixels = pixels + np.random.rand(pixels.shape[0], pixels.shape[1])*noise_level
    pixels = pixels/np.max(pixels)
    return pixels
