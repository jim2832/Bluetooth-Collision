package Project_3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Project3_d {
	
	static int[] arrNum;
	//頻道數量
	static int channelNum = 80;
	//測試裝置數量序列
	static int[] deviceNum = {40,80};
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
	//各個頻道陣列(記錄頻道機率)
	static int[][] channelArray = new int[81][2];
	//壞頻道陣列
	static ArrayList<Integer> badChannel = new ArrayList();
	//正常頻道陣列
	static ArrayList<Integer> normalChannel = new ArrayList(); 
	//用來比較裝置隨機到的頻道參數
	static int number = 0;
	//存取壞頻道得佇列
	static int[] badChannel_Array = new int [81];
	//存取是每個頻道是壞頻道的機率
	static double[] Bad_Channel_Probability = new double[81];
	//換測試別的裝置數量時，讓計算頻道出現次數的陣列回歸初始值的變數
	static int turnDeviceNum = deviceNum[0];
	//頻道號碼
	static int channelNumber = 0;
	//測試門檻
	static double threshold = 0.1;
	//即時的好頻道
	static ArrayList<Integer> NowGood_channel_status = new ArrayList();
	//時即的壞頻道
	static ArrayList<Integer> NowBad_channel_status = new ArrayList();
	//最大差值
	static int max = 0;

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Arrays.fill(badChannel_Array, 0);
			// TODO Auto-generated method stub
			int i = 0;
			while(i < 2) {
				arrNum = new int[deviceNum[i]];
				//System.out.printf("sss:%d \n",arrNum.length);	
				//總共模擬次數100次
				for(int SimNum =0; SimNum < 100 ; SimNum ++) {
				//每次模擬跳頻次數1600次
					for(int HopFreq =0; HopFreq < 1600 ; HopFreq++) {
						//依題目的裝置數，有幾個裝置，隨機跑亂數，跑裝置次數
						for(int dev=0; dev < arrNum.length ; dev++ ) {
							int randomNum = 0;
							randomNum = rand_channel.nextInt(channelNum)+1;
							deviceSeq.add(randomNum); 
							//System.out.println(deviceSeq.get(dev));
						}
						//交換從小排到大(方便比較碰撞次數用)
						for (int k = 0; k < arrNum.length-1; k++) {
							 for (int j = 0; j < arrNum.length- 1; j++) {
							     if (deviceSeq.get(j) > deviceSeq.get(j+1)) {
							     int tmp = deviceSeq.get(j);
							     deviceSeq.set(j,deviceSeq.get(j+1));
							     deviceSeq.set(j+1,tmp);
							     }
							}
						}
						//將排序由小到大的結果印出
						for(int k=0;k<arrNum.length;k++) {
							//System.out.printf("%d:---%d \n",k,deviceSeq.get(k));
						}
						//依裝置次數來跑，主要計算裝置碰撞次數、計算每個頻道在100*1600的各裝置中被占用的次數
						if(arrNum.length != turnDeviceNum) {
							for(int k = 1; k < 81; k++) {
								channelArray[k][0] = 0;
								channelArray[k][1] = 0;
							}
							turnDeviceNum = arrNum.length;
							//System.out.println("Clean-----------------Clean");
						}
						if(arrNum.length == turnDeviceNum) {
							for (int j = 0; j < arrNum.length; j++) {
								//計算裝置碰撞次數
								if(j != 0) {
									if (deviceSeq.get(j-1) == deviceSeq.get(j)) {
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
							//計算每個頻道在100*1600的測試次數當中，各裝置數量被占用的次數
								for(int k = 1; k < 81; k++) {
										if(deviceSeq.get(j) == k) {
											if(channelNumber != deviceSeq.get(j)) {
												channelNumber = deviceSeq.get(j);
												 channelArray[k][0] = channelNumber;
												 //System.out.printf("頻道為 %d  \n",channelArray[k][0]);
												 channelArray[k][1] = channelArray[k][1] + 1;
												 //System.out.printf("頻道次數為 %d  \n",channelArray[k][1]);
												}
											Bad_Channel_Probability[k] =(double)channelArray[k][1] / (double)1600;
											 if(Bad_Channel_Probability[k] > threshold) {
												 badChannel.add(channelArray[k][0]);
												 //System.out.printf("壞頻道為 %d , 門檻為%.1f, 次數:%d ,機率:%.4f \n",channelArray[k][0],threshold,channelArray[k][1],Bad_Channel_Probability[k]);
											 }
											 else {					 
												 normalChannel.add(channelArray[k][0]);
												 //System.out.printf("正常頻道為 %d , 門檻為%.1f, 次數:%d ,機率:%.4f \n",channelArray[k][0],threshold,channelArray[k][1],Bad_Channel_Probability[k]);
											 }
											 
											 if(normalChannel.size() == 0) {
												 break;
											 }
											 else {
												for(int dev=0; dev < arrNum.length ; dev++ ) {
													for(int u=0; u < badChannel.size(); u++) {
														 if(deviceSeq.get(dev) == badChannel.get(u)) {
															 //System.out.printf("BadChannel new---%d----%d \n",u,badChannel.get(u));

																//System.out.printf("BadChannel new---%d----%d \n",u,badChannel.get(u));
															 if(normalChannel.size() != 0) {
																 int normalNum = 0;
																	normalNum = rand_channel.nextInt(normalChannel.size());
																	deviceSeq.set(dev,normalChannel.get(normalNum));
															 }
															 else
															 {
																 int normalNum = 0;
																	normalNum = rand_channel.nextInt(badChannel.size());
																	deviceSeq.set(dev,badChannel.get(normalNum));
															 }
																
																//System.out.printf("Final decive new---%d----%d \n",dev,deviceSeq.get(dev));
																//System.out.printf("Init max new---%d----%d \n",m,max);
																//int value = Math.abs(deviceSeq.get(dev)- normalChannel.get(m));
																//System.out.printf("Decive new---%d----%d \n",dev,deviceSeq.get(dev));
																//System.out.printf("NormalChannel new---%d----%d \n",m,normalChannel.get(m));
																//System.out.printf("Value new---%d----%d \n",m,value);
						
															
															//System.out.printf("Final decive new---%d----%d \n",dev,deviceSeq.get(dev));
														 
													 }
												} 									 
											 } 
										} 
								}
							}
						}
						//清除裝置陣列(方便存取下次不同的裝置數量)
						deviceSeq.clear();
						NowBad_channel_status.clear();
						NowGood_channel_status.clear();
						badChannel.clear();
						normalChannel.clear();
						max = 0;
					}
			
				}
				
				
			}
				//System.out.println("");
				collisionSeq.add(collisionNum);
				allTimes.add(100 * 1600 * deviceNum[i]);
				testProbability.add((double)collisionSeq.get(i) / (double)allTimes.get(i)) ;
				System.out.printf("有 %d 個裝置的碰撞次數為 %d \n",deviceNum[i],collisionSeq.get(i));
				System.out.printf("有 %d 個裝置的碰撞機率為 %f \n",deviceNum[i],testProbability.get(i));
				collisionNum =0;
				i++;
			
	}
			System.out.println("printf");
	}
}


