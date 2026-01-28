# import random
# import time
# from collections import deque
# import mediapipe as mp

# from .tasks import TASKS
# from .detectors import *

# mp_face = mp.solutions.face_mesh
# mp_hands = mp.solutions.hands

# face_mesh = mp_face.FaceMesh(refine_landmarks=True)
# hands = mp_hands.Hands(max_num_hands=1)

# SUCCESS_REQUIRED = 3
# MAX_MISTAKES = 3
# STABLE_FRAMES_REQUIRED = 5




# def full_circle_completed(nose_path):
#         xs = [p[0] for p in nose_path]
#         ys = [p[1] for p in nose_path]

#         return (
#             max(xs) - min(xs) > 0.12 and   # left-right coverage
#             max(ys) - min(ys) > 0.12       # up-down coverage
#     )

# class LivenessEngine:
#     def __init__(self):
#         self.success = 0
#         self.mistakes = 0
#         self.time_limit = 15

#         self.task = random.choice(TASKS)
#         self.task_start = time.time()

#         self.stable_frames = 0
#         self.nose_path = deque(maxlen=60)
#         self.direction_score = 0
#         self.head_stage = 0
#         self.neck_start = None
#         self.quadrants = set()

#     def reset_task(self):
#         self.task = random.choice(TASKS)
#         self.time_limit = 15
#         self.task_start = time.time()
#         self.stable_frames = 0
#         self.nose_path.clear()
#         self.direction_score = 0
#         self.head_stage = 0
#         self.neck_start = None
#         self.quadrants.clear()



    


#     def update(self, face_res, hand_res):
#         elapsed = int(time.time() - self.task_start)
#         remaining = max(0, self.time_limit - elapsed)

#         if remaining == 0:
#             self.mistakes += 1
#             if self.mistakes >= MAX_MISTAKES:
#                 return "SPOOF"
#             self.time_limit += 10
#             self.task_start = time.time()
#             self.stable_frames = 0

#         task_ok = False

#         if face_res.multi_face_landmarks:
#             lm = face_res.multi_face_landmarks[0].landmark
#             nose = lm[1]
#             self.nose_path.append((nose.x, nose.y))

#             if self.task == "LEFT_EYE_BLINK":
#                 task_ok = eye_blink(lm, LEFT_EYE)

#             elif self.task == "RIGHT_EYE_BLINK":
#                 task_ok = eye_blink(lm, RIGHT_EYE)

#             elif self.task == "HEAD_MOVE_UP":
#                 # task_ok = nose.y < 0.40
#                 if nose.y < 0.45:
#                     task_ok = True

#             elif self.task == "HEAD_MOVE_DOWN":
#                 # task_ok = nose.y > 0.60
#                  if nose.y > 0.55:
#                     task_ok = True

#             elif self.task == "HEAD_LEFT_RIGHT_CENTER":
#                 if nose.x < 0.40:
#                     self.head_stage = 1
#                 elif nose.x > 0.60 and self.head_stage == 1:
#                     self.head_stage = 2
#                 elif 0.45 < nose.x < 0.55 and self.head_stage == 2:
#                     task_ok = True

#             elif self.task == "HEAD_RIGHT_LEFT_CENTER":
#                 if nose.x > 0.60:
#                     self.head_stage = 1
#                 elif nose.x < 0.40 and self.head_stage == 1:
#                     self.head_stage = 2
#                 elif 0.45 < nose.x < 0.55 and self.head_stage == 2:
#                     task_ok = True

#             elif self.task == "HEAD_UP_DOWN_CENTER":
#                 if nose.y < 0.40:
#                     self.head_stage = 1
#                 elif nose.y > 0.60 and self.head_stage == 1:
#                     self.head_stage = 2
#                 elif 0.45 < nose.y < 0.55 and self.head_stage == 2:
#                     task_ok = True

#             elif self.task == "HEAD_DOWN_UP_CENTER":
#                 if nose.y > 0.60:
#                     self.head_stage = 1
#                 elif nose.y < 0.40 and self.head_stage == 1:
#                     self.head_stage = 2
#                 elif 0.45 < nose.y < 0.55 and self.head_stage == 2:
#                     task_ok = True

           
            

#         if hand_res.multi_hand_landmarks and face_res.multi_face_landmarks:
#             lm = face_res.multi_face_landmarks[0].landmark
#             hand = hand_res.multi_hand_landmarks[0].landmark
#             label = hand_res.multi_handedness[0].classification[0].label

#             if self.task == "LEFT_CHEEK_TOUCH_LEFT_HAND":
#                 task_ok = label == "Left" and abs(hand[8].x - lm[LEFT_CHEEK].x) < 0.05

#             elif self.task == "RIGHT_CHEEK_TOUCH_RIGHT_HAND":
#                 task_ok = label == "Right" and abs(hand[8].x - lm[RIGHT_CHEEK].x) < 0.05

#             elif self.task == "LEFT_THUMB_UP":
#                 task_ok = label == "Left" and is_thumb_up(hand)

#             elif self.task == "RIGHT_THUMB_UP":
#                 task_ok = label == "Right" and is_thumb_up(hand)

#             elif self.task == "LEFT_PALM_OPEN":
#                 task_ok = label == "Left" and is_palm_open(hand)

#             elif self.task == "RIGHT_PALM_OPEN":
#                 task_ok = label == "Right" and is_palm_open(hand)

           


#         # if task_ok:
#         #     self.stable_frames += 1
#         # else:
#         #     self.stable_frames = 0

#         # event based

#         if self.task in ["LEFT_EYE_BLINK", "RIGHT_EYE_BLINK"]:
#             if task_ok:
#                 self.success += 1
#                 if self.success >= SUCCESS_REQUIRED:
#                     return "REAL"
#                 self.reset_task()
#             return remaining


#         if task_ok:
#             self.stable_frames += 1
#         else:
#             self.stable_frames = max(0, self.stable_frames - 1)

#         if self.stable_frames >= STABLE_FRAMES_REQUIRED:
#             self.success += 1
#             if self.success >= SUCCESS_REQUIRED:
#                 return "REAL"
#             self.reset_task()

#         return remaining





import random
import time
from collections import deque
import mediapipe as mp

from .tasks import TASKS
from .detectors import *

mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

face_mesh = mp_face.FaceMesh(refine_landmarks=True)
hands = mp_hands.Hands(max_num_hands=1)

SUCCESS_REQUIRED = 3
MAX_MISTAKES = 3
STABLE_FRAMES_REQUIRED = 5


class LivenessEngine:
    def __init__(self):
        self.success = 0
        self.mistakes = 0
        self.time_limit = 15

        self.task = random.choice(TASKS)
        self.task_start = time.time()

        self.stable_frames = 0
        self.nose_path = deque(maxlen=60)
        self.direction_score = 0
        self.head_stage = 0
        self.neck_start = None
        self.quadrants = set()

    def reset_task(self):
        self.task = random.choice(TASKS)
        self.time_limit = 15
        self.task_start = time.time()
        self.stable_frames = 0
        self.nose_path.clear()
        self.direction_score = 0
        self.head_stage = 0
        self.neck_start = None
        self.quadrants.clear()

    def update(self, face_res, hand_res):
        elapsed = int(time.time() - self.task_start)
        remaining = max(0, self.time_limit - elapsed)

        if remaining == 0:
            self.mistakes += 1
            if self.mistakes >= MAX_MISTAKES:
                return "SPOOF"
            self.time_limit += 10
            self.task_start = time.time()
            self.stable_frames = 0

        task_ok = False

        # ---------------- FACE TASKS ----------------
        if face_res.multi_face_landmarks:
            lm = face_res.multi_face_landmarks[0].landmark
            nose = lm[1]
            self.nose_path.append((nose.x, nose.y))

            if self.task == "LEFT_EYE_BLINK":
                task_ok = eye_blink(lm, LEFT_EYE)

            elif self.task == "RIGHT_EYE_BLINK":
                task_ok = eye_blink(lm, RIGHT_EYE)

            elif self.task == "HEAD_MOVE_UP":
                task_ok = nose.y < 0.45

            elif self.task == "HEAD_MOVE_DOWN":
                task_ok = nose.y > 0.55

            elif self.task == "HEAD_LEFT_RIGHT_CENTER":
                if nose.x < 0.40:
                    self.head_stage = 1
                elif nose.x > 0.60 and self.head_stage == 1:
                    self.head_stage = 2
                elif 0.45 < nose.x < 0.55 and self.head_stage == 2:
                    task_ok = True

            elif self.task == "HEAD_RIGHT_LEFT_CENTER":
                if nose.x > 0.60:
                    self.head_stage = 1
                elif nose.x < 0.40 and self.head_stage == 1:
                    self.head_stage = 2
                elif 0.45 < nose.x < 0.55 and self.head_stage == 2:
                    task_ok = True

            elif self.task == "HEAD_UP_DOWN_CENTER":
                if nose.y < 0.40:
                    self.head_stage = 1
                elif nose.y > 0.60 and self.head_stage == 1:
                    self.head_stage = 2
                elif 0.45 < nose.y < 0.55 and self.head_stage == 2:
                    task_ok = True

            elif self.task == "HEAD_DOWN_UP_CENTER":
                if nose.y > 0.60:
                    self.head_stage = 1
                elif nose.y < 0.40 and self.head_stage == 1:
                    self.head_stage = 2
                elif 0.45 < nose.y < 0.55 and self.head_stage == 2:
                    task_ok = True

        # ---------------- HAND TASKS ----------------
        if hand_res.multi_hand_landmarks and face_res.multi_face_landmarks:
            lm = face_res.multi_face_landmarks[0].landmark
            hand = hand_res.multi_hand_landmarks[0].landmark
            label = hand_res.multi_handedness[0].classification[0].label

            if self.task == "LEFT_CHEEK_TOUCH_LEFT_HAND":
                task_ok = label == "Left" and abs(hand[8].x - lm[LEFT_CHEEK].x) < 0.05

            elif self.task == "RIGHT_CHEEK_TOUCH_RIGHT_HAND":
                task_ok = label == "Right" and abs(hand[8].x - lm[RIGHT_CHEEK].x) < 0.05

            elif self.task == "LEFT_THUMB_UP":
                task_ok = label == "Left" and is_thumb_up(hand)

            elif self.task == "RIGHT_THUMB_UP":
                task_ok = label == "Right" and is_thumb_up(hand)

            elif self.task == "LEFT_PALM_OPEN":
                task_ok = label == "Left" and is_palm_open(hand)

            elif self.task == "RIGHT_PALM_OPEN":
                task_ok = label == "Right" and is_palm_open(hand)

            # ✅ FINGER COUNT TASKS (ADDED)
            elif "FINGER" in self.task:
                side, _, count = self.task.split("_")
                count = int(count)

                if label.upper() == side:
                    task_ok = count_fingers(hand) == count

        # ---------------- EVENT-BASED EYE BLINK ----------------
        if self.task in ["LEFT_EYE_BLINK", "RIGHT_EYE_BLINK"]:
            if task_ok:
                self.success += 1
                if self.success >= SUCCESS_REQUIRED:
                    return "REAL"
                self.reset_task()
            return remaining

        # ---------------- STABILITY-BASED TASKS ----------------
        if task_ok:
            self.stable_frames += 1
        else:
            self.stable_frames = max(0, self.stable_frames - 1)

        if self.stable_frames >= STABLE_FRAMES_REQUIRED:
            self.success += 1
            if self.success >= SUCCESS_REQUIRED:
                return "REAL"
            self.reset_task()

        return remaining
