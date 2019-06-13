import pytest

def rotate_using_tmp_array(arr,d):
	tmp = arr[:d]
	for i in range(d,len(arr)):
		arr[i-d]=arr[i]
	for i in range(len(tmp)):
		arr[len(arr)-d+i] = tmp[i]

def rotate_one_by_one(arr,d):
	for i in range(d):
		tmp = arr[0]
		for m in range(1,len(arr)):
			arr[m-1]=arr[m]
		arr[-1]=tmp

def rotate_juggling_algo(arr,d):
	n = len(arr)
	from math import gcd
	for m in range(gcd(n,d)):
		tmp = arr[m]
		i = m
		while (i+d)%n!=m:
			arr[i] = arr[(i+d)%n]
			i = (i+d)%n
		arr[i]=tmp

def rotate_reverse_algo(arr,d):
	def reverse_arr(array,start,end):
		while start < end:
			tmp = array[start]
			array[start] = array[end]
			array[end]=tmp
			start += 1
			end -= 1
		return

	n = len(arr)-1
	reverse_arr(arr,0,d-1)
	reverse_arr(arr,d,n)
	reverse_arr(arr,0,n)
	return

test_data = [
	([1,2,3,4,5,6,7],3,[4,5,6,7,1,2,3]),
	([1,2,3,4,5,6,7],4,[5,6,7,1,2,3,4]),
	([2,3,4,5,6],5,[2,3,4,5,6]),
	([],0,[])
]

@pytest.mark.parametrize(
	'arr,d,expected_r',test_data)
def test_rotate_using_tmp_array(arr,d,expected_r):
	a = arr.copy()
	rotate_using_tmp_array(a, d)
	assert a ==expected_r

@pytest.mark.parametrize(
	'arr,d,expected_r',test_data)
def test_rotate_one_by_one(arr,d,expected_r):
	a = arr.copy().copy()
	rotate_one_by_one(a, d)
	assert a ==expected_r

@pytest.mark.parametrize(
	'arr,d,expected_r',test_data)
def test_rotate_juggling_algo(arr,d,expected_r):
	a = arr.copy()
	rotate_juggling_algo(a, d)
	assert a ==expected_r

@pytest.mark.parametrize(
	'arr,d,expected_r',test_data)
def test_rotate_reverse_algo(arr,d,expected_r):
	a = arr.copy()
	rotate_reverse_algo(a, d)
	assert a ==expected_r
