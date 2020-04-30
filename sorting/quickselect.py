from .quicksort import __partition3way__

def findKthLargest(nums, k, order='asc'):
    if order=='asc':
        val = helperKthsmallest(nums, 0, len(nums) - 1, k)
    elif order=='desc':
        # kth largest -> (N-k)th smallest with 0 based index
        val = helperKthsmallest(nums, 0, len(nums) - 1, len(nums) - k)
    else:
        raise ValueError('order arg must be asc or desc')
    return val


def helperKthsmallest(nums, lo, hi, k):
    lt, gt = __partition3way__(nums, lo, hi)
    if lt <= k <= gt:
        return nums[lt]
    elif k < lt:
        return helperKthsmallest(nums, lo, lt - 1, k)
    elif k > gt:
        return helperKthsmallest(nums, gt + 1, hi, k)
