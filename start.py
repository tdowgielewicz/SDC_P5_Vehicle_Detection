import cv2





cap = cv2.VideoCapture('project_video.mp4')
# cap = cv2.VideoCapture('part1.mp4')
# cap = cv2.VideoCapture('harder_challenge_video.mp4')
#cap = cv2.VideoCapture('challenge_video.mp4')


frame_id = 0
while(cap.isOpened()):


    ret, out = cap.read()
    in_img = out
    if ret==True:


        cv2.imshow('result', out )


        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("report/sample_pre.png", in_img)
            cv2.imwrite("report/sample_out.png", out)
            break
    else:
        break

cap.release()
#cv2.destroyAllWindows()