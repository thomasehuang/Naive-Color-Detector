# import the necessary packages
import numpy as np
import argparse
import cv2


def callback(value):
	pass


def setup_trackbars(range_filter):
  cv2.namedWindow("Trackbars", 0)

  for i in ["MIN", "MAX"]:
    v = 0 if i == "MIN" else 255

    for j in range_filter:
      cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, callback)


def get_trackbar_values(range_filter):
  values = []

  for i in ["MIN", "MAX"]:
    for j in range_filter:
      v = cv2.getTrackbarPos("%s_%s" % (j, i), "Trackbars")
      values.append(v)

  return values


def reset_trackbar_values(range_filter):
  for i in ["MIN", "MAX"]:
  	v = 0 if i == "MIN" else 255
   	for j in range_filter:
			cv2.setTrackbarPos("%s_%s" % (j, i), "Trackbars", v)


def handle_arguments():
	args = argparse.ArgumentParser()
	args.add_argument("-i", "--image", help = "path to the image", required=True)
	return vars(args.parse_args())


def main():
	# parse arguments
	args = handle_arguments()

	range_filter = 'BGR'

	setup_trackbars(range_filter)

	# load the image
	image = cv2.imread(args["image"])

	while True:
		frame_to_thresh = image.copy()

		v1_min, v2_min, v3_min, v1_max, v2_max, v3_max = get_trackbar_values(range_filter)

		thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

		preview = cv2.bitwise_and(image, image, mask=thresh)
		cv2.imshow("Preview", preview)
		cv2.imshow("Thresh", thresh)

		# if q is pressed, reset and print the values
		if cv2.waitKey(1) & 0xFF == ord('q'):
			print(v1_min, v2_min, v3_min, v1_max, v2_max, v3_max)
			reset_trackbar_values(range_filter)

		# if esc is pressed, quit
		if cv2.waitKey(33) == 27:
			break


if __name__ == '__main__':
	main()
