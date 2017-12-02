# import the necessary packages
import numpy as np
import argparse
import cv2


def parse_ranges(ranges):
	ranges = ranges[1:-1] # get rid of parenthesis
	return [int(x) for x in ranges.split(', ')]


def handle_arguments():
	args = argparse.ArgumentParser()
	args.add_argument("-i", "--image", help = "path to the image", required=True)
	args.add_argument("-r", "--range", help = "color ranges (blue min, green min, red min, blue max, green max, red max)", required=True)
	return vars(args.parse_args())


def main():
	# parse arguments
	args = handle_arguments()

	# load the image
	image = cv2.imread(args["image"])

	v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = parse_ranges(args['range'])

	frame_to_thresh = image.copy()
	thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))
	score = np.sum(thresh / 255)
	confidence = score / np.size(thresh)

	print(confidence)


if __name__ == '__main__':
	main()