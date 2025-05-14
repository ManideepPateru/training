def trap(height):
    if not height:
        return 0
    l=0
    r =len(height) - 1
    left_max=0
    right_max = 0
    water_trapped = 0
    while l < r:
        if height[l] < height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                water_trapped += left_max - height[l]
            l += 1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water_trapped += right_max - height[r]
            r -= 1
    return water_trapped
# Example usage
h = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(h))  # Output: 6