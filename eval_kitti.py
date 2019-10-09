from evaluate_ate_scale_kitti import exec_main
import numpy as np
import matplotlib.pyplot as plt

import argparse



class Eval_Kitti(object):
    def __init__(self):
        return 
    def run(self):
        parser = argparse.ArgumentParser(description='''
        This script computes the absolute trajectory error from the ground truth trajectory and the estimated trajectory. 
        ''')
        parser.add_argument('seq', help='sequence number of kitti dataset, like 04')
        parser.add_argument('--offset', help='time offset added to the timestamps of the second file (default: 0.0)',default=0.0)
        parser.add_argument('--scale', help='scaling factor for the second trajectory (default: 1.0)',default=1.0)
        parser.add_argument('--max_difference', help='maximally allowed time difference for matching entries (default: 0.02)',default=0.02)
        parser.add_argument('--save', help='save aligned second trajectory to disk (format: stamp2 x2 y2 z2)')
        parser.add_argument('--save_associations', help='save associated first and aligned second trajectory to disk (format: stamp1 x1 y1 z1 stamp2 x2 y2 z2)')
        args = parser.parse_args()
        
        seq = args.seq
        args.first_file_time = '/home/levin/workspace/data/kitti/sequences/{}/times.txt'.format(seq)  
        args.first_file_data = '/home/levin/workspace/data/kitti/data_odometry_poses/dataset/poses/{}.txt'.format(seq)    
        args.second_file = '/home/levin/workspace/ORB_SLAM2/temp/slam_result/data/{}/KeyFrameTrajectory.txt'.format(seq)  
        args.verbose = True
        exec_main(args)
        return



if __name__ == '__main__':
    obj = Eval_Kitti()
    obj.run()
    
    
