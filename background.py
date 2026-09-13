import cv2
import numpy as np


class BackgroundModel:
    """
    Continuously learns the scene background.

    During warm-up, the background is built from incoming frames.
    After warm-up, it adapts slowly only where the cloak mask is false.
    """

    def __init__(self, warmup_frames=75, learning_rate=0.05):
        self.background = None
        self.warmup_frames = warmup_frames
        self.learning_rate = learning_rate
        self.frame_count = 0
        self.ready = False

    def update(self, frame, cloak_mask=None):
        """
        Update the background model.

        frame:
            Current BGR camera frame.

        cloak_mask:
            Binary mask where 255 = cloak.
            During warm-up this can be None.
        """

        # First frame initializes the model.
        if self.background is None:
            self.background = frame.astype(np.float32)
            self.frame_count = 1
            return self.get_background(), False

        # ---------------------------------------
        # Automatic warm-up
        # ---------------------------------------
        if not self.ready:

            self.background = (
                0.90 * self.background
                + 0.10 * frame.astype(np.float32)
            )

            self.frame_count += 1

            if self.frame_count >= self.warmup_frames:
                self.ready = True

            return self.get_background(), self.ready

        # ---------------------------------------
        # Continuous background learning
        # ---------------------------------------

        current = frame.astype(np.float32)

        if cloak_mask is None:
            return self.get_background(), True

        # Only update pixels that are NOT cloak.
        non_cloak = cloak_mask == 0

        self.background[non_cloak] = (
            (1.0 - self.learning_rate)
            * self.background[non_cloak]
            + self.learning_rate
            * current[non_cloak]
        )

        return self.get_background(), True

    def get_background(self):
        """Return the background as an 8-bit image."""

        if self.background is None:
            return None

        return np.clip(
            self.background,
            0,
            255
        ).astype(np.uint8)

    def reset(self):
        """Reset the background model."""

        self.background = None
        self.frame_count = 0
        self.ready = False

    def is_ready(self):
        return self.ready