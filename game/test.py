import gymnasium as gym
from gymnasium.envs.classic_control.cartpole import CartPoleEnv
import numpy as np
import pygame
from pygame.locals import *
import time

# カスタムCartPole（90度まで許容）
class CustomCartPoleEnv(CartPoleEnv):
    def __init__(self, render_mode="human"):
        super().__init__(render_mode=render_mode)
        self.theta_threshold_radians = np.pi  # 90度
        self.x_threshold = 5  # デフォルトのまま

    def step(self, action):
        obs, reward, terminated, truncated, info = super().step(action)

        # カスタム終了条件（±90度で倒れるまでOK）
        x, x_dot, theta, theta_dot = self.state
        terminated = (
            x < -self.x_threshold
            or x > self.x_threshold
            or theta < -self.theta_threshold_radians
            or theta > self.theta_threshold_radians
        )
        terminated=False

        return obs, reward, terminated, truncated, info


# ===============================
# 人間操作部分（←→で制御）
# ===============================
def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Custom CartPole Manual Control")

    env = CustomCartPoleEnv(render_mode="human")
    obs, info = env.reset(seed=42)

    clock = pygame.time.Clock()
    running = True

    play_time_sec = 60
    start_time = time.time()

    while running:
        if time.time() - start_time > play_time_sec:
            print("Time's up!")
            break

        # キーの押下状態確認（連続入力対応）
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            action = 0
        elif keys[K_RIGHT]:
            action = 1
        else:
            action = 0  # 何も押さないときは左（任意）

        # イベント処理（終了操作用）
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

        # 環境ステップ
        obs, reward, terminated, truncated, info = env.step(action)

        # リセット処理（倒れたとき）
        if terminated or truncated:
            print("Resetting...")
            obs, info = env.reset()

        # フレーム制御
        clock.tick(60)

    env.close()
    pygame.quit()

if __name__ == "__main__":
    main()
