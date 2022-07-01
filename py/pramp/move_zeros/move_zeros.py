# def moveZerosToEnd(arr):
#     """
#     @param arr: int[]
#     @return: int[]
#     """
# result = []
#
# for i in range(0, len(arr)):
#     if i == 0:
#         if pos == None:
#             pos = i
#     elif pos != None:
#         # swap with pos
#         tmp = arr[i]
#         arr[i] = arr[pos]
#         arr[pos] = tmp
#         pos = po s +1


def move_zeroes(self, nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1


if __name__ == "__main__":
    move_zeroes([1, 0, 23, 4, 1, 2, 5, 810, 10, 0])
