// 2045. Second Minimum Time to Reach Destination

class Solution {
    public int secondMinimum(int numberOfNodes, int[][] edges, int travelTime, int trafficLightChangeTime) {
      List<Integer>[] graph = new List[numberOfNodes + 1];
      Queue<int[]> queue = new ArrayDeque<>(Arrays.asList(new int[] {1, 0})); 
      int[][] minTime = new int[numberOfNodes + 1][2];
      Arrays.stream(minTime).forEach(times -> Arrays.fill(times, Integer.MAX_VALUE));
      minTime[1][0] = 0;
  
      for (int i = 1; i <= numberOfNodes; ++i)
        graph[i] = new ArrayList<>();
  
      for (int[] edge : edges) {
        final int nodeA = edge[0];
        final int nodeB = edge[1];
        graph[nodeA].add(nodeB);
        graph[nodeB].add(nodeA);
      }
  
      while (!queue.isEmpty()) {
        final int currentNode = queue.peek()[0];
        final int previousTime = queue.poll()[1];
        
        final int numTrafficLightChanges = previousTime / trafficLightChangeTime;
        final int waitTime = numTrafficLightChanges % 2 == 0 ? 0 : trafficLightChangeTime - previousTime % trafficLightChangeTime;
        final int newTime = previousTime + waitTime + travelTime;
        
        for (final int neighbor : graph[currentNode])
          if (newTime < minTime[neighbor][0]) {
            minTime[neighbor][0] = newTime;
            queue.offer(new int[] {neighbor, newTime});
          } 
          else if (minTime[neighbor][0] < newTime && newTime < minTime[neighbor][1]) {
            if (neighbor == numberOfNodes)
              return newTime;
            minTime[neighbor][1] = newTime;
            queue.offer(new int[] {neighbor, newTime});
          }
      }
  
      throw new IllegalArgumentException();
    }
  }