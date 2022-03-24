/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
var spiralOrder = function (matrix) {
	const m = matrix.length;
	const n = matrix[0].length;
	let h = 0,
		v = 0;
	let res = [];
	const visited = 'VISITED';
	let direction = 'r';
	//comment
	for (i = 0; i < m * n; i++) {
		res.push(matrix[h][v]);
		matrix[h][v] = visited;
		if (direction === 'r') {
			if (!matrix[h][v + 1] || matrix[h][v + 1] == visited) {
				direction = 'd';
				h = h + 1;
				continue;
			} else {
				v = v + 1;
				continue;
			}
		}
		if (direction == 'd') {
			//
			if (
				!matrix[h + 1] ||
				!matrix[h + 1][v] ||
				matrix[h + 1][v] == visited
			) {
				direction = 'l';
				v = v - 1;
				continue;
			} else {
				h = h + 1;
				continue;
			}
		}
		if (direction == 'l') {
			if (!matrix[h][v - 1] || matrix[h][v - 1] == visited) {
				direction = 'u';
				h = h - 1;
				continue;
			} else {
				v = v - 1;
				continue;
			}
		}
		if (direction == 'u') {
			if (
				!matrix[h - 1] ||
				!matrix[h - 1][v] ||
				matrix[h - 1][v] == visited
			) {
				direction = 'r';
				v = v + 1;
				continue;
			} else {
				h = h - 1;
				continue;
			}
		}
	}
	return res;
};

const result = spiralOrder([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9],
]);

console.log(result);
