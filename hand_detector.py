import cv2
import mediapipe as mp

# código de exemplo para ser estudado extraído do vídeo: https://www.youtube.com/watch?v=RbqGPFrWZC8

video = cv2.VideoCapture(2)

hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

while True:
    check, img = video.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hand.process(img_rgb)
    h, w, _ = img.shape
    points_position = []
    if hand_points := results.multi_hand_landmarks:
        for points in hand_points:
            mp_draw.draw_landmarks(img, points, hand.HAND_CONNECTIONS)
            for cord in points.landmark:
                cx, cy = int(cord.x * w), int(cord.y * h)
                points_position.append((cx,cy))
            fingers = [8, 12, 16, 20]
            contador = 0
            if points_position:
                if points_position[4][0] < points_position[3][0]:
                    contador += 1
                for x in fingers:
                   if points_position[x][1] < points_position[x-2][1]:
                       contador +=1
            cv2.rectangle(img, (80, 10), (200,110), (255, 0, 0), -1)
            cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

    cv2.imshow("Imagem", img)
    cv2.waitKey(1)