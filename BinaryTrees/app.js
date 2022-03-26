class TreeNode {
	constructor(value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}

	preOrderTraversal = (node) => {
		function recursiveFunction(node, arr = []) {
			if (!node) return null;
			arr.push(node.value);
			recursiveFunction(node.left, arr);
			recursiveFunction(node.right, arr);
			return arr;
		}
		return recursiveFunction(node);
	};

	preorderTraversalIterative = function (root) {
		const values = [];
		const list = [root];
		console.log(list);
		while (list.length) {
			const nd = list.pop();
			if (nd) {
				values.push(nd.value);
				list.push(nd.right, nd.left);
			}
		}
		return values;
	};

	inorderTraversalIterative = function (root) {
		var stack = [];
		var now = root;
		var res = [];

		while (now || stack.length) {
			console.log('now', now);
			while (now) {
				stack.push(now);
				now = now.left;
			}
			now = stack.pop();
			res.push(now.value);
			now = now.right;
		}

		return res;
	};
}

//     1
//    / \
//   2   3
//  / \ / \
//  4   5
const root = new TreeNode(1);
elem2 = new TreeNode(2);
elem3 = new TreeNode(3);
elem4 = new TreeNode(4);
elem5 = new TreeNode(5);

root.left = elem2;
root.right = elem3;
// elem2.left = elem4;
// elem3.right = elem5;
const result = root.inorderTraversalIterative(root);
console.log(result);
