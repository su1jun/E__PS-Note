import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

        // 큐와 우선순위 큐에 요소 추가
        for (int i = 0; i < priorities.length; i++) {
            queue.add(new int[]{i, priorities[i]});
            priorityQueue.add(priorities[i]);
        }

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            // 현재 프로세스의 우선순위가 가장 높은 우선순위와 같은지 확인
            if (current[1] == priorityQueue.peek()) {
                priorityQueue.poll();
                answer++;
                // 현재 프로세스가 목표 위치에 있는 프로세스인지 확인
                if (current[0] == location) {
                    break;
                }
            } else {
                queue.add(current);
            }
        }

        return answer;
    }
}