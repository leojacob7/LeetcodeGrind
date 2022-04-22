var addBinary = function (a, b) {
	let result = '';
	let carry = 0;
	let sum = 0;
	if (a.length > b.length) {
		b = '0'.repeat(a.length - b.length) + b;
	} else {
		a = '0'.repeat(b.length - a.length) + a;
	}

	console.log({ a, b });
	for (let i = a.length - 1; i >= 0; i--) {
		sum = Number(a[i]) ^ Number(b[i]) ^ carry;
		carry =
			(Number(a[i]) & Number(+b[i])) |
			(Number(b[i]) & +carry) |
			(Number(a[i]) & +carry);
		result = sum.toString() + result;
		console.log({ sum, carry, result });
	}

	return carry ? '1' + result : result;
};

const result = addBinary('1', '1');
console.log(result);
