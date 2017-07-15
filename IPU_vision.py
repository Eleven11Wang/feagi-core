
"""
# This file acts as the Input Processing Unit (IPU) for the system.
# Functions in this file will provide methods to pass raw data through basic filters and feed them to the
# processing layers.

# For test purposes only and need to see how it can be eliminated from code for efficiency
"""

import numpy as np
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import matplotlib.pyplot as plt

import settings
import architect


def convert_image_to_coordinates(image):   # Image is currently assumed to be a 28 x 28 numpy array
    """
    Function responsible for reading an image and converting the pixel values to coordinates
    """
    # Note: currently set to function based on Gray scale image

    image_locations = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if image[x, y] >= settings.image_color_intensity_tolerance:
                image_locations.append([x, y, 0])

    # Image location will be fed to another function to identify the Id of neurons to be activated
    return image_locations


def convert_image_locations_to_neuron_ids(image_locations):
    """
    Queries the connectome for each location and provides the list of Neuron Ids matching the location
    :param image_locations:
    :return:
    """
    neuron_id_list = []
    for x in range(len(image_locations)):
            # call the function to find neuron candidates for a given location
            tmp = architect.neuron_finder('vision_v1', image_locations[x], settings.location_tolerance)
            for item in tmp:
                if (item is not None) and (neuron_id_list.count(item) == 0):
                    neuron_id_list.append(item)
    return neuron_id_list


def image_read_by_block(image, kernel_size, seed_coordinates):
    x = seed_coordinates[0]
    y = seed_coordinates[1]
    if divmod(kernel_size, 2)[1] == 0:
        print("Error: Kernel size should only be Odd number!")
        return
    kernel_values = np.zeros((kernel_size, kernel_size))
    scan_length = divmod(kernel_size, 2)[0]
    for a in range(0, kernel_size):
        for b in range(0, kernel_size):
            if ((x-scan_length+a >= 0) and (y-scan_length+b >= 0) and (x-scan_length+a < np.shape(image)[0])
                    and (y-scan_length+b < np.shape(image)[1])):
                kernel_values[a, b] = image[x-scan_length+a, y-scan_length+b]
    return kernel_values


def kernel_direction(kernel_values):
    """
    Apply all filters from the IPU_vision_filters to the kernel and evaluate the best match
    Output is the Type of directional cell which will be activated 
    :param kernel_size: 
    :param kernel_values: 
    :return: 
    
    The following conditions will estimate the line orientation angle into 4 standard options as following:
    1: /        2: \        3: -       4: |       0 : none
    Each if condition will perform a simple statistical analysis on the concentration of the pixels
    """
    # todo: Important >>> Something is wrong with this function returning incorrect values as direction label changes

    np.tmp = kernel_values
    kernel_size = np.shape(np.tmp)
    kernel_size = kernel_size[0]
    if divmod(kernel_size, 2)[1] == 0:
        print("Error: Kernel size should only be Odd number!")
        return

    result = np.zeros((kernel_size, kernel_size))
    end_result = {}
    for filter_entry in settings.genome["IPU_vision_filters"][str(kernel_size)]:
        filter_value = settings.genome["IPU_vision_filters"][str(kernel_size)][filter_entry]
        for i in range(0, kernel_size):
            for ii in range(0, kernel_size):
                result[i][ii] = kernel_values[i][ii] * filter_value[i][ii]
                ii += 1
            i += 1
        end_result[filter_entry] = result
        result = np.zeros((kernel_size, kernel_size))
    tmpArray = []
    # print('this is tmp before all appends', tmpArray)
    for entry in end_result:
        sumation = np.sum(end_result[entry])
        # print("Appending: %s Sum: %d \n End_result: \n %s" % (entry, sumation,end_result[entry]))
        # tmp = np.append(tmp, [entry, np.sum(end_result[entry])], axis=0)
        tmpArray.append([entry, np.sum(end_result[entry])])
        # print('***', tmpArray)
    # print("This is the end result: \n %s" % end_result)
    # print('tmp after appends %s' % tmpArray)
    maxValue = max(zip(*tmpArray)[1])
    maxValueIndex = zip(*tmpArray)[1].index(maxValue)
    direction = tmpArray[maxValueIndex][0]
    # direction = direction.replace('\\', '\')
    # print('max value is %s' % maxValue)
    # print('max index is %s' % maxValueIndex)
    # print('direction is %s' % direction)
    return direction


def create_direction_matrix(image, kernel_size):
    """
    Generates a Matrix where each element outlines the Direction detected by the Kernel filters against each 
    corresponding pixel in the image. 
    :param image: 
    :param kernel_size: 
    :return: 
    """
    if divmod(kernel_size, 2)[1] == 0:
        print("Error: Kernel size should only be Odd number!")
        return
    row_index = 0
    col_index = 0
    direction_matrix = [[] for x in range(np.shape(image)[1])]
    for row in image:
        for row_item in row:
            direction = kernel_direction(image_read_by_block(image, kernel_size, [row_index, col_index]))
            direction_matrix[row_index].append(direction)
            col_index += 1
        col_index = 0
        row_index += 1
    return direction_matrix


"""
todo: Need to add a method to combine multiple IPU layer data into a single one
        -Think how to build a direction agnostic representation of an object
        

"""
def kernel_edge_detector(kernel_values):


    return


def image_processing():
    """
    Function to read an image from a file and have it converted to it's fundamental components
    """
    return


def image_orientation_detector():
    """
    Performs higher level analysis to detect the direction of an image
    """
    # todo: need to figure which processing layer this belongs to. It might need to go thru entire stack
    return


def orientation_matrix():
    """
    Function to produce an orientation matrix based on the raw image data
    """
    # A 27*27 image will produce a 9x9 orientation matrix
    # or we can produce the orientation matrix the same size as the image
    return


def direction_stats(image_block):
    """
    Reads direction Kernel data and returns statistics on the percentage of each direction
    :param kernel: 
    :return: 
    """
    # direction_matrix = (image, kernel_size))
    # print(image)


    direction_matrix = ''
    for row in image_block:
        for item in row:
            direction_matrix = direction_matrix + str(item)

    # generate a list of all unique Characters present in the image block
    unique_chars = []
    for item in direction_matrix:
        if unique_chars.count(item) == 0 and item != ' ':
            unique_chars.append(item)
    # print('list of unique chars = %s' % unique_chars)


    # Count number of occorances of each unique character
    counts = []
    for item in unique_chars:
        counts.append([item, direction_matrix.count(item)])

    # Calculate the percentage of usage of each word
    stats = []
    count_total = direction_matrix.__len__() - direction_matrix.count(' ')
    for key in range(0, counts.__len__()):
        stats.append([counts[key][0], str(counts[key][1] * 100 / float(count_total)) + ' %'])

    return stats






# settings.init()
# print(kernel_direction([
#   [ 1,  1,  1]
#  ,[ 1,  10,  1]
#  ,[ 1,  1,  1]]))
# print(kernel_direction([
#   [ 1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1]]))
# print(kernel_direction([
#   [ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]
#  ,[ 1,  1,  1,  1,  1,  1,  1]]))

#
# print(direction_stats(kernel_direction([
#   [ 1,  1,  1]
#  ,[ 1,  10,  1]
#  ,[ 1,  1,  1]])))

