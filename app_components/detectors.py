import math

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

LEFT_CHEEK = 234
RIGHT_CHEEK = 454


def dist(a, b):
    return math.hypot(a.x - b.x, a.y - b.y)


def eye_blink(lm, eye):
    v1 = dist(lm[eye[1]], lm[eye[5]])
    v2 = dist(lm[eye[2]], lm[eye[4]])
    h = dist(lm[eye[0]], lm[eye[3]])
    return (v1 + v2) / (2 * h) < 0.20


def is_thumb_up(hand):
    return hand[4].y < hand[0].y




def is_palm_open(hand):
    # Index, middle, ring, pinky
    fingers = [(8, 6), (12, 10), (16, 14), (20, 18)]

    extended = 0
    for tip, pip in fingers:
        if hand[tip].y < hand[pip].y:
            extended += 1

    # Thumb: check distance from palm center
    palm_center_x = hand[0].x
    thumb_tip_x = hand[4].x

    thumb_extended = abs(thumb_tip_x - palm_center_x) > 0.08

    return extended == 4 and thumb_extended



def count_fingers(hand):
    # Index, Middle, Ring, Pinky
    fingers = [(8, 6), (12, 10), (16, 14), (20, 18)]
    count = 0

    for tip, pip in fingers:
        if hand[tip].y < hand[pip].y:
            count += 1

    # Thumb
    if abs(hand[4].x - hand[0].x) > 0.08:
        count += 1

    return count
