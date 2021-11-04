// 동서남북
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];
const n = 5;

const inRange = (x, y) => {
  // 범위 안에 있으면 참
  return 0 <= x && x < n && 0 <= y && y < n;
};
// 맨해튼 거리 계산
const inDistance = (x1, y1, x2, y2) => {
  return Math.abs(x1 - x2) + Math.abs(y1 - y2) <= 2 ? true : false;
};

function bfs(place, visited) {
  let q = [];
  // 완전 탐색
  for (let strY = 0; strY < n; strY++) {
    for (let strX = 0; strX < n; strX++) {
      // push는 기준이 되는 지점에서 함. 일단 P는 무조건 기준지점이 됨
      if (place[strX][strY] === "P") {
        q.push([strX, strY]);

        while (q.length > 0) {
          // 가장 이전에 넣은 애 빼내고, 방문한 곳 true표시
          let [cx, cy] = q.shift();
          visited[cy][cx] = true;

          //기준 지점을 중심으로 동서남북 탐색할 거임
          for (let i = 0; i < 4; i++) {
            const nx = cx + dx[i];
            const ny = cy + dy[i];
            // 기본적으로 범위 내에 있어야 하고, 방문했으면 안됨
            if (
              inRange(nx, ny) &&
              !visited[ny][nx] &&
              inDistance(strX, strY, nx, ny)
            ) {
              // 무조건 거리두기 실패
              if (place[ny][nx] === "P") {
                return 0;
              }
              // X가 아니라면 일단 새로운 기준점이 됨
              else {
                place[ny][nx] !== "X" && q.push([nx, ny]);
              }
            }
          }
        }
      }
    }
  }
  return 1;
}

// 맨해튼 거리 3부터 가능
function solution(places) {
  const answer = [];
  places.map((place) => {
    // 방문 기록 기록할 2차원 리스트 초기화
    let visited = Array.from(Array(5), () => new Array(5).fill(false));
    answer.push(bfs(place, visited));
  });
  return answer;
}

console.log(
  solution([
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
  ])
);
