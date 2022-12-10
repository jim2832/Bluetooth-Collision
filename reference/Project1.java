package Project_1;

import java.util.ArrayList;
import java.util.Random;


public class first {
		
		static int[] arrNum;
		//頻道數量
		static int channelNum = 79;
		//測試裝置數量序列
		static int[] deviceNum = {2};
		//儲存裝置測試陣列
		static ArrayList<Integer> deviceSeq = new ArrayList(); 
		//碰撞測試序列
		static ArrayList<Integer> collisionSeq = new ArrayList(); 
		//碰撞次數
		static int collisionNum =0;
		//總次數數量
		static ArrayList<Integer> allTimes = new ArrayList(); 	
		//測試結果機率
		static ArrayList<Double> testProbability = new ArrayList();
		//建立隨機選擇器
		static Random rand_channel=new Random();
		
		
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int count=0; 
		while(count <= deviceNum.length) {
			for(int i =0; i < deviceNum.length;i++) {
				arrNum = new int[deviceNum[i]];
				System.out.println(arrNum.length); //裝置的數量
				count +=1;
	
				//總共模擬次數100次
				for(int SimNum =0; SimNum < 100 ; SimNum ++) {
				//每次模擬跳頻次數1600次
					for(int HopFreq =0; HopFreq < 1600 ; HopFreq++) {
						//看有幾個裝置
						for(int dev=0; dev < arrNum.length ; dev++ ) {
							int randomNum = 0;
							randomNum = rand_channel.nextInt(channelNum)+1;
							deviceSeq.add(randomNum);
							System.out.println(deviceSeq.get(dev));
							if(dev > 0) {
								if(deviceSeq.get(dev-1)== deviceSeq.get(dev)) {
									collisionNum ++;
								}
								deviceSeq.clear();
							}
						}
					}
				}
				System.out.printf("有 2 個裝置的碰撞次數為 %d \n",collisionNum);
				collisionSeq.add(collisionNum);
				allTimes.add(100 * 1600 * deviceNum[i]);
				testProbability.add((double)collisionSeq.get(i) / (double)allTimes.get(i)) ;
			}
		}
		
		for(int p = 0; p < deviceNum.length;p++ ) {
			System.out.printf("有 %d 個裝置的碰撞機率為 %f",deviceNum[p],testProbability.get(p));
		}

	}

}
