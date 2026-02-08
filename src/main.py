import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
p.setTimeStep(1. / 100.)
p.setRealTimeSimulation(True)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 1]

base_rot_id = p.addUserDebugParameter("base_rot",-0.7, 0.7, 0)
top_rot_id = p.addUserDebugParameter("top_rot",-3.14, 3.14, 0)


robotId = p.loadURDF("my.urdf", startPosition, startOrientation)

for i in range(10000):
    base_rot = p.readUserDebugParameter(base_rot_id)
    top_rot = p.readUserDebugParameter(top_rot_id)
    p.setJointMotorControl2(robotId, 0, p.POSITION_CONTROL, targetPosition=base_rot, maxVelocity=0.25)
    p.setJointMotorControl2(robotId, 1, p.POSITION_CONTROL, targetPosition=top_rot)

    p.stepSimulation()
    time.sleep(1. / 100.)

p.disconnect()
