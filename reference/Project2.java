package Project_2;

import java.util.ArrayList;
import java.util.Random;

public class second {
	
	static int[] arrNum;
	//頻道數量
	static int channelNum = 80;
	//測試裝置數量序列
	static int[] deviceNum = {2,10,20,30,40,50,60,70,80};
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
			//while(count <= deviceNum.length) {
			//for(int i =0; i < deviceNum.length;i++) {
			int i =0;	
			while(i < 9) {
					arrNum = new int[deviceNum[i]];
					System.out.printf("sss:%d \n",arrNum.length);
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
							}
							for (int k = 0; k < arrNum.length-1; k++) {
							      for (int j = 0; j < arrNum.length- 1; j++) {
							        if (deviceSeq.get(j) > deviceSeq.get(j+1)) {
							          int tmp = deviceSeq.get(j);
							          deviceSeq.set(j,deviceSeq.get(j+1));
							          deviceSeq.set(j+1,tmp);
							        }
							      }
							}
							//排序隨機數字的大小(由小到大)
							for(int k=0;k<arrNum.length;k++) {
								System.out.printf("%d:---%d \n",k,deviceSeq.get(k));
							}
							int number =0;
							for (int j = 1; j < arrNum.length; j++) {
							    if (deviceSeq.get(j) == deviceSeq.get(j-1)) {
							    	if(number != deviceSeq.get(j)) {
							    		number = deviceSeq.get(j);
								        collisionNum++;
								        collisionNum++;
							    	}
							    	else {
							    		collisionNum++;
							    	}
							    }
							}
							deviceSeq.clear();
						}
					}
					collisionSeq.add(collisionNum);
					allTimes.add(100 * 1600 * deviceNum[i]);
					testProbability.add((double)collisionSeq.get(i) / (double)allTimes.get(i)) ;
					collisionNum =0;
					i++;
				}
			 		
				//}
			//}	
			for(int p = 0; p < deviceNum.length;p++ ) {
				System.out.printf("有 %d 個裝置的碰撞次數為 %d \n",deviceNum[p],collisionSeq.get(p));
				System.out.printf("有 %d 個裝置的碰撞機率為 %f \n",deviceNum[p],testProbability.get(p));
			}

		}

}
