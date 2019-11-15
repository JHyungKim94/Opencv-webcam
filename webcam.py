import cv2

def main(mirror=False):
    # Frame object setting
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Object Information
    if cam.isOpened():
        print("width: {}, height: {}".format(cam.get(3), cam.get(4)))

    while True:
        ret, frame = cam.read()
        if ret:
            if mirror:
                frame = cv2.flip(frame, 1)

            # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imshow('my_webcam', frame)

            if cv2.waitKey(1) == 5:
                break  # esc to quit
        else:
            print('error')

if __name__ == '__main__':
    main()